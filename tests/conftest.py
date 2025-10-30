"""
pytest配置文件

提供测试配置和fixtures，包括：
- 测试数据库配置
- 测试Redis配置
- 测试客户端配置
- 测试数据fixtures
"""

import pytest
import asyncio
from typing import AsyncGenerator, Generator
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.main import create_app
from src.config.settings import get_settings
from src.config.database import get_db_session


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """创建事件循环"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def test_settings() -> Generator:
    """测试配置"""
    settings = get_settings()
    settings.database_url = "sqlite:///:memory:"
    settings.redis_url = "redis://localhost:6379/1"
    yield settings


@pytest.fixture
def test_app(test_settings) -> Generator:
    """测试应用"""
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: test_settings
    yield app


@pytest.fixture
def test_client(test_app) -> Generator:
    """测试客户端"""
    with TestClient(test_app) as client:
        yield client


@pytest.fixture
def test_db_session() -> Generator:
    """测试数据库会话"""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    
    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
    
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_user_data() -> dict:
    """测试用户数据"""
    return {
        "username": "test_doctor",
        "email": "doctor@hospital.com",
        "password": "test_password_123",
        "full_name": "测试医生",
        "department": "耳鼻喉科",
        "title": "主治医师"
    }


@pytest.fixture
def test_patient_data() -> dict:
    """测试患者数据"""
    return {
        "name": "测试患者",
        "age": 35,
        "gender": "男",
        "phone": "13800138000",
        "id_card": "110101199001011234",
        "medical_history": "无特殊病史"
    }


@pytest.fixture
def test_consultation_data() -> dict:
    """测试问诊数据"""
    return {
        "chief_complaint": "头痛、鼻塞3天",
        "symptoms": ["头痛", "鼻塞", "流涕"],
        "duration": "3天",
        "severity": "中等",
        "previous_treatment": "自行服用感冒药，效果不佳"
    }


@pytest.fixture
def test_triage_request() -> dict:
    """测试导诊请求数据"""
    return {
        "symptoms": ["头痛", "鼻塞", "流涕"],
        "duration": "3天",
        "severity": "中等",
        "description": "患者3天前出现头痛、鼻塞、流涕症状，伴有轻微发热"
    }


@pytest.fixture
def test_diagnosis_request() -> dict:
    """测试诊断请求数据"""
    return {
        "patient_id": 1,
        "symptoms": ["头痛", "鼻塞", "流涕"],
        "medical_history": "无特殊病史",
        "physical_examination": {
            "temperature": 37.5,
            "blood_pressure": "120/80",
            "heart_rate": 80
        },
        "lab_results": {
            "wbc": 8.5,
            "crp": 5.2
        }
    }


@pytest.fixture
async def test_async_client(test_app) -> AsyncGenerator:
    """异步测试客户端"""
    from httpx import AsyncClient
    async with AsyncClient(app=test_app, base_url="http://test") as client:
        yield client


@pytest.fixture
def mock_redis():
    """模拟Redis客户端"""
    import fakeredis
    return fakeredis.FakeRedis(decode_responses=True)


@pytest.fixture
def mock_ai_model():
    """模拟AI模型"""
    class MockAIModel:
        def predict(self, text):
            return {"prediction": "感冒", "confidence": 0.85}
    
    return MockAIModel()


@pytest.fixture
def mock_external_systems():
    """模拟外部系统"""
    class MockHIS:
        def get_patient_info(self, patient_id):
            return {"name": "测试患者", "age": 35}
    
    class MockLIS:
        def get_lab_results(self, patient_id):
            return {"wbc": 8.5, "crp": 5.2}
    
    return {
        "his": MockHIS(),
        "lis": MockLIS()
    }


# 测试标记
pytest.mark.unit = pytest.mark.unit
pytest.mark.integration = pytest.mark.integration
pytest.mark.e2e = pytest.mark.e2e
pytest.mark.slow = pytest.mark.slow


# 测试配置
def pytest_configure(config):
    """pytest配置"""
    config.addinivalue_line(
        "markers", "unit: 单元测试"
    )
    config.addinivalue_line(
        "markers", "integration: 集成测试"
    )
    config.addinivalue_line(
        "markers", "e2e: 端到端测试"
    )
    config.addinivalue_line(
        "markers", "slow: 慢速测试"
    )


# 测试收集钩子
def pytest_collection_modifyitems(config, items):
    """修改测试收集"""
    for item in items:
        # 为异步测试添加标记
        if asyncio.iscoroutinefunction(item.function):
            item.add_marker(pytest.mark.asyncio)
        
        # 根据测试路径自动添加标记
        if "unit/" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration/" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "e2e/" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
