---
id: PROJ-STRUCT-001
sn: PROJ
status: active
---

# PROJ-STRUCT-001 项目目录结构 ⚡ TDD主场核心

## 项目根目录结构

基于Python+FastAPI+PostgreSQL技术栈和分层架构+微服务设计模式，定义团队协作友好的项目目录结构。

### 根目录组织
```
ent_otorhinolaryngology_agent_system_v2/
├── spec/                           # 📋 SPEC框架文档
│   ├── requirements/               # 需求文档
│   ├── design/                     # 设计文档
│   ├── implementation/             # ⚡ TDD策略文档（本目录）
│   └── task_planning/              # 任务规划文档
├── src/                           # 🔧 源代码目录
│   ├── app/                        # 应用核心代码
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI应用入口
│   │   ├── config/                 # 配置管理
│   │   ├── models/                 # 数据模型
│   │   ├── services/               # 业务服务
│   │   ├── api/                    # API路由
│   │   └── utils/                  # 工具函数
│   ├── tests/                       # 🧪 测试代码目录
│   │   ├── unit/                   # 单元测试
│   │   ├── integration/            # 集成测试
│   │   ├── e2e/                    # 端到端测试
│   │   └── fixtures/               # 测试数据
│   ├── migrations/                  # 数据库迁移
│   ├── scripts/                    # 脚本工具
│   └── requirements.txt             # Python依赖
├── docker/                        # 🐳 Docker配置
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── docker-compose.prod.yml
├── k8s/                          # ☸️ Kubernetes配置
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── docs/                          # 📚 项目文档
├── .github/                       # GitHub Actions CI/CD
└── README.md                      # 项目说明
```

## 源代码目录结构

### 应用代码组织 (src/app/)
```
src/app/
├── __init__.py
├── main.py                        # FastAPI应用入口
├── config/
│   ├── __init__.py
│   ├── settings.py                 # 应用配置
│   ├── database.py                 # 数据库配置
│   └── logging.py                  # 日志配置
├── models/
│   ├── __init__.py
│   ├── patient.py                  # 患者模型
│   ├── consultation.py             # 问诊会话模型
│   ├── diagnosis.py                # 诊断记录模型
│   └── medical_knowledge.py         # 医学知识模型
├── services/
│   ├── __init__.py
│   ├── auth_service.py             # 认证服务
│   ├── triage_service.py           # 智能导诊服务
│   ├── diagnosis_service.py        # 辅助诊断服务
│   ├── nlp_service.py              # 自然语言处理服务
│   └── integration/                # 外部系统集成
│       ├── his_service.py
│       └── lis_service.py
├── api/
│   ├── __init__.py
│   ├── dependencies.py             # FastAPI依赖
│   ├── v1/                        # API版本1
│   │   ├── __init__.py
│   │   ├── auth.py                 # 认证API
│   │   ├── triage.py               # 导诊API
│   │   ├── diagnosis.py            # 诊断API
│   │   └── health.py               # 健康检查API
│   └── middleware/                 # 中间件
│       ├── auth.py
│       ├── cors.py
│       └── logging.py
└── utils/
    ├── __init__.py
    ├── security.py                # 安全工具
    ├── validators.py              # 验证器
    └── helpers.py                 # 辅助函数
```

## 测试代码目录结构

### 测试组织 (src/tests/)
```
src/tests/
├── __init__.py
├── conftest.py                    # pytest配置
├── unit/                          # 单元测试
│   ├── __init__.py
│   ├── test_auth_service.py
│   ├── test_triage_service.py
│   ├── test_diagnosis_service.py
│   └── test_nlp_service.py
├── integration/                   # 集成测试
│   ├── __init__.py
│   ├── test_api_integration.py
│   ├── test_database_integration.py
│   └── test_external_integration.py
├── e2e/                           # 端到端测试
│   ├── __init__.py
│   ├── test_patient_journey.py
│   ├── test_doctor_workflow.py
│   └── test_system_integration.py
└── fixtures/                      # 测试数据
    ├── __init__.py
    ├── patient_data.py
    ├── consultation_data.py
    └── diagnosis_data.py
```

## 配置文件组织

### Docker配置 (docker/)
```
docker/
├── Dockerfile                      # 应用镜像构建
├── docker-compose.yml              # 开发环境
├── docker-compose.prod.yml         # 生产环境
└── .dockerignore                   # Docker忽略文件
```

### Kubernetes配置 (k8s/)
```
k8s/
├── namespace.yaml                  # 命名空间
├── configmap.yaml                 # 配置映射
├── secret.yaml                    # 密钥管理
├── deployment.yaml                 # 部署配置
├── service.yaml                   # 服务配置
├── ingress.yaml                   # 入口配置
└── hpa.yaml                       # 水平扩展配置
```

## 模块间引用关系

### 核心引用网络
```
project_structure.md (基础文档)
├── 被: tdd_strategy.md (引用目录结构)
├── 被: bdd_test_scenarios.md (引用测试位置)
├── 被: test_driven_sequence.md (引用构建顺序)
├── 被: test_data_management.md (引用数据位置)
└── 被: code_quality_gates.md (引用质量标准)
```

### 团队协作边界
- **前端团队**: 负责API接口设计和前端实现
- **后端团队**: 负责业务逻辑和API实现
- **测试团队**: 负责测试策略和质量保证
- **运维团队**: 负责部署和监控配置

## TDD协作约定

### 分支管理策略
- **主分支**: `main` - 生产环境代码
- **开发分支**: `develop` - 开发环境代码
- **功能分支**: `feature/功能名称` - 功能开发
- **修复分支**: `hotfix/问题描述` - 紧急修复

### 代码提交规范
- **提交信息格式**: `type(scope): description`
- **类型**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **示例**: `feat(auth): add JWT token refresh mechanism`

### 测试驱动开发流程
1. **红**: 编写失败的测试用例
2. **绿**: 编写最少代码使测试通过
3. **重构**: 优化代码结构，保持测试通过

> 📝 **文档状态**: TDD策略框架已搭建，等待后续设计完善
