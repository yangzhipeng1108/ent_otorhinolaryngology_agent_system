"""
配置模块

提供应用配置管理功能，包括：
- 应用设置
- 数据库配置
- 环境变量管理
"""

from .settings import get_settings

__all__ = ["get_settings"]
