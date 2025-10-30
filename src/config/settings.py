"""
应用设置配置

管理应用的所有配置项，包括：
- 数据库连接配置
- Redis缓存配置
- API服务配置
- 安全配置
- 日志配置
"""

from functools import lru_cache
from typing import List, Optional
from pydantic import BaseSettings, validator
import os


class Settings(BaseSettings):
    """应用配置类"""
    
    # 应用基础配置
    app_name: str = "三甲医院耳鼻喉科问诊Agent系统"
    app_version: str = "1.0.0"
    environment: str = "development"
    debug: bool = True
    
    # 服务配置
    host: str = "0.0.0.0"
    port: int = 8000
    
    # 数据库配置
    database_url: str = "postgresql://ent_user:ent_password@localhost:5432/ent_agent_db"
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "ent_agent_db"
    database_user: str = "ent_user"
    database_password: str = "ent_password"
    
    # Redis配置
    redis_url: str = "redis://localhost:6379/0"
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: Optional[str] = None
    
    # JWT配置
    jwt_secret_key: str = "your-super-secret-jwt-key-change-in-production"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7
    
    # CORS配置
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080"
    ]
    
    # 可信主机配置
    allowed_hosts: List[str] = ["localhost", "127.0.0.1", "0.0.0.0"]
    
    # 日志配置
    log_level: str = "INFO"
    log_file: str = "logs/app.log"
    
    # 文件上传配置
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    upload_dir: str = "uploads"
    
    # AI模型配置
    ai_model_path: str = "models/"
    ai_model_timeout: int = 30
    
    # 外部系统集成配置
    his_system_url: Optional[str] = None
    lis_system_url: Optional[str] = None
    emr_system_url: Optional[str] = None
    
    # 监控配置
    enable_metrics: bool = True
    metrics_port: int = 9090
    
    @validator("environment", pre=True)
    def validate_environment(cls, v):
        """验证环境配置"""
        valid_environments = ["development", "testing", "staging", "production"]
        if v not in valid_environments:
            raise ValueError(f"environment must be one of {valid_environments}")
        return v
    
    @validator("database_url", pre=True)
    def build_database_url(cls, v, values):
        """构建数据库连接URL"""
        if v:
            return v
        
        host = values.get("database_host", "localhost")
        port = values.get("database_port", 5432)
        name = values.get("database_name", "ent_agent_db")
        user = values.get("database_user", "ent_user")
        password = values.get("database_password", "ent_password")
        
        return f"postgresql://{user}:{password}@{host}:{port}/{name}"
    
    @validator("redis_url", pre=True)
    def build_redis_url(cls, v, values):
        """构建Redis连接URL"""
        if v:
            return v
        
        host = values.get("redis_host", "localhost")
        port = values.get("redis_port", 6379)
        db = values.get("redis_db", 0)
        password = values.get("redis_password")
        
        if password:
            return f"redis://:{password}@{host}:{port}/{db}"
        return f"redis://{host}:{port}/{db}"
    
    @property
    def is_development(self) -> bool:
        """是否为开发环境"""
        return self.environment == "development"
    
    @property
    def is_production(self) -> bool:
        """是否为生产环境"""
        return self.environment == "production"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """
    获取应用配置实例（单例模式）
    
    Returns:
        Settings: 配置实例
    """
    return Settings()


# 数据库配置
DATABASE_CONFIG = {
    "pool_size": 10,
    "max_overflow": 20,
    "pool_timeout": 30,
    "pool_recycle": 3600,
    "echo": False  # 设置为True可以看到SQL语句
}

# Redis配置
REDIS_CONFIG = {
    "decode_responses": True,
    "socket_connect_timeout": 5,
    "socket_timeout": 5,
    "retry_on_timeout": True,
    "health_check_interval": 30,
}

# 日志配置
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "formatter": "detailed",
            "class": "logging.FileHandler",
            "filename": "logs/app.log",
            "mode": "a",
        },
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ["default", "file"],
        },
        "uvicorn": {
            "level": "INFO",
            "handlers": ["default", "file"],
            "propagate": False,
        },
        "sqlalchemy.engine": {
            "level": "WARNING",
            "handlers": ["default", "file"],
            "propagate": False,
        },
    },
}
