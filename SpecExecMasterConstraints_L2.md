---
# SpecExecMasterConstraints_L2.md

> **定位**: L2级别执行约束文档 - 目录结构与命名约定
> **用途**: 定义项目执行的Canonical约束和规范
> **版本**: v1.0.0
> **生成时间**: 2025-10-30T09:15:48Z

## 项目元信息

- **项目名称**: ent_otorhinolaryngology_agent_system_v2
- **约束级别**: L2-BALANCED
- **技术栈**: Python+FastAPI+PostgreSQL+Redis+Docker+Kubernetes
- **架构模式**: 分层架构+微服务设计

## 强约束声明

### 文件位置约束 (I1-CanonicalLocation)
- **Constraints文档**: `./SpecExecMasterConstraints_L2.md` ⭐ 必须第一个生成
- **MasterPlan文档**: `./SpecExecMasterPlan_L2.md`
- **SubPlan文档**: `./SpecExecSubPlan_{序号}_{GOAL或TYPE}_L2.md`
- **Dashboard文档**: `./SpecExecMasterDashboard_L2.md`
- **Lessons文档**: `./SpecExecMasterLessons_L2.md`

### 依赖链约束 (I4-DependencyChain)
```
Constraints → MasterPlan → SubPlan → Dashboard/Lessons
```

## 技术栈识别表

| 类别 | 技术选型 | 版本要求 | 用途 |
|------|----------|----------|------|
| 后端语言 | Python | 3.8+ | 主要开发语言 |
| Web框架 | FastAPI | 0.104+ | API服务框架 |
| 数据库 | PostgreSQL | 13+ | 主数据库 |
| 缓存 | Redis | 6.0+ | 缓存和会话存储 |
| 前端 | React | 18+ | 用户界面 |
| 容器化 | Docker | 20.10+ | 容器化部署 |
| 编排 | Kubernetes | 1.24+ | 容器编排 |
| 测试框架 | pytest | 7.4+ | 单元测试 |
| BDD框架 | behave | 1.2+ | 行为驱动测试 |
| API测试 | httpx | 0.24+ | HTTP客户端测试 |

## 目录结构规范

### 根目录结构
```
ent_otorhinolaryngology_agent_system_v2/
├── src/                          # 源代码目录
│   ├── api/                      # API接口层
│   ├── core/                     # 核心业务逻辑
│   ├── models/                   # 数据模型
│   ├── services/                 # 业务服务层
│   └── utils/                    # 工具函数
├── tests/                        # 测试目录
│   ├── unit/                     # 单元测试
│   ├── integration/              # 集成测试
│   ├── e2e/                      # 端到端测试
│   └── fixtures/                 # 测试数据
├── docs/                         # 文档目录
├── scripts/                      # 脚本目录
├── docker/                       # Docker配置
├── k8s/                          # Kubernetes配置
├── requirements/                 # 依赖文件
└── SpecExec*                     # ProgressPlan文档
```

### 源代码目录结构
```
src/
├── __init__.py
├── main.py                       # FastAPI应用入口
├── config/                       # 配置模块
│   ├── __init__.py
│   ├── settings.py               # 应用配置
│   └── database.py               # 数据库配置
├── api/                          # API接口层
│   ├── __init__.py
│   ├── deps.py                   # 依赖注入
│   ├── middleware.py             # 中间件
│   └── v1/                       # API版本1
│       ├── __init__.py
│       ├── auth.py               # 认证接口
│       ├── triage.py             # 导诊接口
│       ├── diagnosis.py          # 诊断接口
│       └── integration.py        # 集成接口
├── core/                         # 核心业务逻辑
│   ├── __init__.py
│   ├── auth/                     # 认证核心
│   ├── triage/                   # 导诊核心
│   ├── diagnosis/                # 诊断核心
│   └── integration/              # 集成核心
├── models/                       # 数据模型
│   ├── __init__.py
│   ├── base.py                   # 基础模型
│   ├── patient.py                # 患者模型
│   ├── consultation.py           # 问诊模型
│   └── diagnosis.py              # 诊断模型
├── services/                     # 业务服务层
│   ├── __init__.py
│   ├── auth_service.py           # 认证服务
│   ├── triage_service.py         # 导诊服务
│   ├── diagnosis_service.py      # 诊断服务
│   └── integration_service.py    # 集成服务
└── utils/                        # 工具函数
    ├── __init__.py
    ├── security.py               # 安全工具
    ├── validators.py             # 验证工具
    └── helpers.py                # 辅助函数
```

### 测试目录结构
```
tests/
├── __init__.py
├── conftest.py                   # pytest配置
├── unit/                         # 单元测试
│   ├── __init__.py
│   ├── test_auth/                # 认证单元测试
│   ├── test_triage/              # 导诊单元测试
│   ├── test_diagnosis/           # 诊断单元测试
│   └── test_integration/         # 集成单元测试
├── integration/                  # 集成测试
│   ├── __init__.py
│   ├── test_api/                 # API集成测试
│   ├── test_database/            # 数据库集成测试
│   └── test_external/            # 外部系统集成测试
├── e2e/                          # 端到端测试
│   ├── __init__.py
│   ├── test_patient_journey/     # 患者完整旅程测试
│   └── test_doctor_workflow/     # 医生工作流测试
└── fixtures/                     # 测试数据
    ├── __init__.py
    ├── patients.py               # 患者测试数据
    ├── consultations.py          # 问诊测试数据
    └── diagnoses.py              # 诊断测试数据
```

## 命名约定

### 文件命名规范
| 类型 | 命名格式 | 示例 |
|------|----------|------|
| Python模块 | snake_case.py | `auth_service.py` |
| 测试文件 | test_*.py | `test_auth_service.py` |
| 配置文件 | *.config.py | `settings.py` |
| Docker文件 | Dockerfile | `Dockerfile` |
| K8s配置 | *.yaml | `deployment.yaml` |

### 目录命名规范
| 类型 | 命名格式 | 示例 |
|------|----------|------|
| 源码目录 | snake_case | `src/core/` |
| 测试目录 | snake_case | `tests/unit/` |
| 配置目录 | snake_case | `config/` |

### 组件命名规范
| 类型 | 命名格式 | 示例 |
|------|----------|------|
| 类名 | PascalCase | `AuthService` |
| 函数名 | snake_case | `authenticate_user` |
| 变量名 | snake_case | `user_token` |
| 常量名 | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| API端点 | kebab-case | `/api/v1/auth/login` |

### 数据库命名规范
| 类型 | 命名格式 | 示例 |
|------|----------|------|
| 表名 | snake_case | `patients` |
| 字段名 | snake_case | `patient_id` |
| 索引名 | idx_表名_字段名 | `idx_patients_id` |
| 外键名 | fk_表名_字段名 | `fk_consultations_patient_id` |

## 禁止区域

### 禁止提交的文件和目录
```
# 开发工具配置
.vscode/
.idea/
*.swp
*.swo
*~

# Python缓存
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# 测试覆盖率
.coverage
.pytest_cache/
htmlcov/
.tox/
.nox/

# 环境配置
.env
.env.local
.env.*.local
venv/
env/
ENV/

# 日志文件
*.log
logs/

# 数据库文件
*.db
*.sqlite3

# 临时文件
tmp/
temp/
.tmp/

# 操作系统
.DS_Store
Thumbs.db
```

### 禁止的代码实践
- 硬编码的敏感信息（密码、密钥、令牌）
- 直接在生产环境中执行调试代码
- 未经验证的外部依赖
- 跨越安全边界的直接数据库访问
- 忽略输入验证的API端点

## 引用方式

### ProgressPlan文档引用
```markdown
# 引用Constraints
参见 [SpecExecMasterConstraints_L2.md](./SpecExecMasterConstraints_L2.md)

# 引用MasterPlan
参见 [SpecExecMasterPlan_L2.md](./SpecExecMasterPlan_L2.md)

# 引用SubPlan
参见 [SpecExecSubPlan_01_INFRASTRUCTURE_L2.md](./SpecExecSubPlan_01_INFRASTRUCTURE_L2.md)

# 引用Dashboard
参见 [SpecExecMasterDashboard_L2.md](./SpecExecMasterDashboard_L2.md)

# 引用Lessons
参见 [SpecExecMasterLessons_L2.md](./SpecExecMasterLessons_L2.md)
```

### 代码文档引用
```python
"""
模块文档字符串

引用相关ProgressPlan:
- 目标: SpecExecMasterPlan_L2.md#GOAL-XXX
- 约束: SpecExecMasterConstraints_L2.md
- 实现: SpecExecSubPlan_XXX_L2.md
"""
```

## 执行引用方式

### Round执行引用格式
```markdown
## Round X: {Round目标}

**ProgressPlan引用**:
- MasterPlan: SpecExecMasterPlan_L2.md#Phase-X
- SubPlan: SpecExecSubPlan_XX_L2.md#Round-X
- Constraints: SpecExecMasterConstraints_L2.md#命名约定
- Dashboard: SpecExecMasterDashboard_L2.md#SubPlan-XX

**质量门禁**:
- 代码覆盖率: ≥80%
- 集成通过率: ≥95%
- 性能基准: API响应时间≤2秒
```

### Step执行引用格式
```markdown
### Step X: {Step目标}

**依赖文档**:
- 前置Step: Step X-1的产出
- 约束参考: SpecExecMasterConstraints_L2.md
- 目标SubPlan: SpecExecSubPlan_XX_L2.md
- 验收标准: SpecExecMasterDashboard_L2.md
```

## 约定变更日志

| 版本 | 日期 | 变更内容 | 变更原因 |
|------|------|----------|----------|
| v1.0.0 | 2025-10-30 | 初始版本创建 | 基于SPEC脚手架生成 |

---

**约束说明**: 本文档定义了项目执行的Canonical约束，所有ProgressPlan文档必须严格遵循。任何变更需要经过团队讨论和版本控制。
