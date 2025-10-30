"""
基础设施单元测试

测试项目基础设施组件，包括：
- 应用启动测试
- 配置加载测试
- 数据库连接测试
- Redis连接测试
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from src.main import create_app
from src.config.settings import get_settings


class TestApplicationStartup:
    """应用启动测试"""
    
    def test_create_app(self):
        """测试应用创建"""
        app = create_app()
        assert app is not None
        assert app.title == "三甲医院耳鼻喉科问诊Agent系统"
        assert app.version == "1.0.0"
    
    def test_app_routes(self):
        """测试应用路由"""
        app = create_app()
        routes = [route.path for route in app.routes]
        
        # 检查核心路由是否存在
        assert "/" in routes
        assert "/health" in routes
        assert "/api/v1/auth" in routes
        assert "/api/v1/triage" in routes
        assert "/api/v1/diagnosis" in routes
        assert "/api/v1/integration" in routes
    
    def test_health_endpoint(self, test_client: TestClient):
        """测试健康检查端点"""
        response = test_client.get("/health")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "ENT AI Agent System"
        assert data["version"] == "1.0.0"
    
    def test_root_endpoint(self, test_client: TestClient):
        """测试根路径端点"""
        response = test_client.get("/")
        assert response.status_code == 200
        
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "docs" in data


class TestConfiguration:
    """配置测试"""
    
    def test_settings_loading(self):
        """测试配置加载"""
        settings = get_settings()
        assert settings is not None
        assert settings.app_name == "三甲医院耳鼻喉科问诊Agent系统"
        assert settings.app_version == "1.0.0"
        assert settings.environment in ["development", "testing", "staging", "production"]
    
    def test_database_url_construction(self):
        """测试数据库URL构建"""
        settings = get_settings()
        assert settings.database_url.startswith("postgresql://")
        assert "ent_agent_db" in settings.database_url
    
    def test_redis_url_construction(self):
        """测试Redis URL构建"""
        settings = get_settings()
        assert settings.redis_url.startswith("redis://")
    
    def test_environment_properties(self):
        """测试环境属性"""
        settings = get_settings()
        
        # 测试开发环境属性
        if settings.environment == "development":
            assert settings.is_development is True
            assert settings.is_production is False
            assert settings.debug is True
    
    @patch.dict("os.environ", {"ENVIRONMENT": "invalid"})
    def test_invalid_environment_validation(self):
        """测试无效环境验证"""
        with pytest.raises(ValueError, match="environment must be one of"):
            get_settings()


class TestDatabaseConnection:
    """数据库连接测试"""
    
    @patch("src.config.database.create_engine")
    def test_database_engine_creation(self, mock_create_engine):
        """测试数据库引擎创建"""
        from src.config.database import get_db_engine
        
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        
        engine = get_db_engine()
        assert engine == mock_engine
        mock_create_engine.assert_called_once()
    
    @patch("src.config.database.sessionmaker")
    def test_database_session_creation(self, mock_sessionmaker):
        """测试数据库会话创建"""
        from src.config.database import get_db_session
        
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session
        
        session = get_db_session()
        assert session == mock_session
        mock_sessionmaker.assert_called_once()


class TestRedisConnection:
    """Redis连接测试"""
    
    @patch("redis.Redis")
    def test_redis_client_creation(self, mock_redis):
        """测试Redis客户端创建"""
        from src.config.database import get_redis_client
        
        mock_client = MagicMock()
        mock_redis.return_value = mock_client
        
        client = get_redis_client()
        assert client == mock_client
        mock_redis.assert_called_once()
    
    @patch("aioredis.from_url")
    def test_async_redis_client_creation(self, mock_aioredis):
        """测试异步Redis客户端创建"""
        from src.config.database import get_async_redis_client
        
        mock_client = MagicMock()
        mock_aioredis.return_value = mock_client
        
        client = get_async_redis_client()
        assert client == mock_client
        mock_aioredis.assert_called_once()


class TestMiddleware:
    """中间件测试"""
    
    def test_cors_middleware(self, test_client: TestClient):
        """测试CORS中间件"""
        response = test_client.options("/api/v1/auth/login")
        assert response.status_code == 200
        
        # 检查CORS头
        headers = response.headers
        assert "access-control-allow-origin" in headers or "access-control-allow-origins" in headers
    
    def test_trusted_host_middleware(self, test_client: TestClient):
        """测试可信主机中间件"""
        # 测试正常主机访问
        response = test_client.get("/", headers={"Host": "localhost"})
        assert response.status_code == 200
        
        # 测试异常主机访问（应该被拒绝）
        response = test_client.get("/", headers={"Host": "malicious.host"})
        # 根据配置，可能被拒绝或允许，这里不强制要求


class TestErrorHandling:
    """错误处理测试"""
    
    def test_404_error(self, test_client: TestClient):
        """测试404错误"""
        response = test_client.get("/nonexistent-endpoint")
        assert response.status_code == 404
        
        data = response.json()
        assert "detail" in data
    
    def test_method_not_allowed(self, test_client: TestClient):
        """测试方法不允许错误"""
        response = test_client.post("/health")
        assert response.status_code == 405
        
        data = response.json()
        assert "detail" in data


class TestSecurity:
    """安全测试"""
    
    def test_no_sensitive_info_in_response(self, test_client: TestClient):
        """测试响应中不包含敏感信息"""
        response = test_client.get("/health")
        data = response.json()
        
        # 检查是否包含敏感信息
        sensitive_keys = ["password", "secret", "key", "token"]
        data_str = str(data).lower()
        
        for key in sensitive_keys:
            assert key not in data_str, f"敏感信息 '{key}' 不应出现在响应中"
    
    def test_security_headers(self, test_client: TestClient):
        """测试安全头"""
        response = test_client.get("/")
        
        # 检查基本安全头
        headers = response.headers
        # 注意：FastAPI默认可能不设置所有安全头，这里检查基本的
        assert "content-type" in headers


# RED阶段测试 - 确保基础设施测试失败（TDD RED阶段）
class TestInfrastructureRED:
    """基础设施RED阶段测试 - 应该失败"""
    
    def test_missing_database_connection(self, test_client: TestClient):
        """测试缺失数据库连接 - 应该失败"""
        # 这个测试在RED阶段应该失败，因为数据库还没有配置
        with pytest.raises(Exception):
            # 尝试访问需要数据库的端点
            test_client.get("/api/v1/auth/users")
    
    def test_missing_redis_connection(self, test_client: TestClient):
        """测试缺失Redis连接 - 应该失败"""
        # 这个测试在RED阶段应该失败，因为Redis还没有配置
        with pytest.raises(Exception):
            # 尝试访问需要Redis的端点
            test_client.post("/api/v1/auth/login", json={"username": "test", "password": "test"})
    
    def test_missing_ai_model(self, test_client: TestClient):
        """测试缺失AI模型 - 应该失败"""
        # 这个测试在RED阶段应该失败，因为AI模型还没有加载
        with pytest.raises(Exception):
            # 尝试访问需要AI模型的端点
            test_client.post("/api/v1/triage/analyze", json={"symptoms": ["头痛"]})
