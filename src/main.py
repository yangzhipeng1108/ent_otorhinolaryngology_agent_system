"""
三甲医院耳鼻喉科问诊Agent系统 - FastAPI应用入口

这是系统的主要入口点，负责：
- 创建FastAPI应用实例
- 配置中间件和依赖注入
- 注册API路由
- 启动应用服务
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

from src.config.settings import get_settings
from src.api.v1 import auth, triage, diagnosis, integration


def create_app() -> FastAPI:
    """
    创建FastAPI应用实例
    
    Returns:
        FastAPI: 配置好的FastAPI应用实例
    """
    settings = get_settings()
    
    app = FastAPI(
        title="三甲医院耳鼻喉科问诊Agent系统",
        description="为三甲医院耳鼻喉科提供智能问诊、导诊和辅助诊断服务",
        version="1.0.0",
        docs_url="/docs" if settings.environment == "development" else None,
        redoc_url="/redoc" if settings.environment == "development" else None,
    )
    
    # 配置CORS中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # 配置可信主机中间件
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.allowed_hosts
    )
    
    # 注册API路由
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["认证服务"])
    app.include_router(triage.router, prefix="/api/v1/triage", tags=["智能导诊"])
    app.include_router(diagnosis.router, prefix="/api/v1/diagnosis", tags=["辅助诊断"])
    app.include_router(integration.router, prefix="/api/v1/integration", tags=["系统集成"])
    
    # 健康检查端点
    @app.get("/health")
    async def health_check():
        """健康检查端点"""
        return {
            "status": "healthy",
            "service": "ENT AI Agent System",
            "version": "1.0.0",
            "environment": settings.environment
        }
    
    # 根路径
    @app.get("/")
    async def root():
        """根路径信息"""
        return {
            "message": "三甲医院耳鼻喉科问诊Agent系统",
            "version": "1.0.0",
            "docs": "/docs" if settings.environment == "development" else "文档不可用"
        }
    
    return app


app = create_app()


if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info"
    )
