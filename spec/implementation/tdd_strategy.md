---
id: TDD-STRATEGY-001
sn: TDD
status: active
source_proj: PROJ-STRUCT-001
---

# TDD-STRATEGY-001 TDD策略和方法 ⚡ TDD主场核心

## TDD核心理念

### 测试驱动开发原则
- **测试优先**: 先写测试，后写代码
- **红绿重构**: Red-Green-Refactor循环
- **小步前进**: 每个测试驱动一个小功能实现
- **持续集成**: 测试与代码同步开发

### 团队协作TDD策略
基于C2-PARTICIPATE模式，建立团队协作的TDD工作流程：
- **AI提供策略建议**: 基于项目特点提供TDD组织方案
- **团队参与讨论**: 开发团队评估技术可行性
- **共同确定方案**: 平衡理想与现实的TDD实施策略

## 测试金字塔策略

### 三层测试架构
```
                    /\
                   /   \  E2E Tests (10%)
                  /     \
                 /       \  Integration Tests (20%)
                /         \
               /           \  Unit Tests (70%)
```

### 单元测试 (70%)
- **目标**: 验证单个函数/类的正确性
- **范围**: 业务逻辑、数据处理、工具函数
- **工具**: pytest + unittest.mock
- **覆盖率要求**: ≥80%

### 集成测试 (20%)
- **目标**: 验证模块间交互正确性
- **范围**: API接口、数据库操作、外部系统集成
- **工具**: pytest + TestContainers
- **覆盖率要求**: ≥60%

### 端到端测试 (10%)
- **目标**: 验证完整业务流程
- **范围**: 用户旅程、关键业务场景
- **工具**: Playwright + pytest
- **覆盖率要求**: ≥40%

## 技术栈选择

### 测试框架
```python
# 核心测试框架
pytest==7.4.0
pytest-asyncio==0.21.0
pytest-cov==4.1.0

# Mock和Stub
pytest-mock==3.11.1
responses==0.23.3
factory-boy==3.2.1

# 数据库测试
pytest-postgresql==5.0.0
testcontainers==3.7.1

# API测试
httpx==0.24.1
pytest-httpx==0.21.0

# E2E测试
playwright==1.40.0
pytest-playwright==0.4.3
```

### 测试数据库配置
```python
# conftest.py
@pytest.fixture(scope="session")
def test_db():
    """测试数据库fixture"""
    # 使用TestContainers创建临时数据库
    with PostgresContainer("postgres:13") as postgres:
        yield postgres.get_connection_url()
```

## BDD场景策略

### Given-When-Then标准格式
```gherkin
Feature: 智能导诊功能
  作为患者
  我希望通过症状描述获得科室推荐
  以便快速找到合适的就诊科室

  Scenario: 患者描述喉咙症状获得导诊建议
    Given 患者在智能导诊系统页面
    And 患者输入"喉咙干痒，持续3天"
    When 患者点击"开始导诊"按钮
    Then 系统应该分析症状并推荐到耳鼻喉科
    And 系统应该生成预问诊报告
```

### 场景组织策略
- **按功能模块组织**: 每个主要功能模块对应一个Feature文件
- **按用户故事组织**: 每个User Story对应多个Scenario
- **按测试类型组织**: 正常流程、异常处理、边界条件

## 测试数据管理

### 测试数据策略
- **固定数据**: 使用factory-boy创建可重复的测试数据
- **动态数据**: 使用faker生成随机测试数据
- **清理策略**: 每个测试后自动清理测试数据

### Factory模式实现
```python
# tests/factories/patient_factory.py
import factory
from app.models.patient import Patient

class PatientFactory(factory.Factory):
    class Meta:
        model = Patient
    
    id = factory.Sequence(lambda n: f"P{n:03d}")
    name = factory.Faker("name")
    age = factory.Faker("random_int", min=1, max=80)
    gender = factory.Iterator(["MALE", "FEMALE"])
    phone = factory.Faker("phone_number")
    email = factory.Faker("email")
```

## 代码质量标准

### 代码覆盖率要求
- **单元测试覆盖率**: ≥80%
- **集成测试覆盖率**: ≥60%
- **整体覆盖率**: ≥70%

### 代码质量检查
```python
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: black
      - id: isort
      - id: flake8
      - id: mypy
      - id: pytest
```

### 静态分析工具
- **代码格式化**: black
- **导入排序**: isort
- **代码检查**: flake8, mypy
- **类型检查**: mypy

## CI/CD集成

### GitHub Actions配置
```yaml
# .github/workflows/test.yml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: |
          pytest --cov=src --cov-report=xml --cov-report=html
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### 质量门禁
- **测试通过率**: 100%
- **代码覆盖率**: ≥70%
- **代码质量检查**: 0 errors
- **性能测试**: 响应时间≤5秒

## 团队协作流程

### 分支策略
- **功能开发**: `feature/功能名称`
- **Bug修复**: `hotfix/问题描述`
- **重构**: `refactor/重构描述`

### 代码审查流程
1. 创建Pull Request
2. 自动运行所有测试
3. 代码质量检查通过
4. 至少一人审查通过
5. 合并到主分支

### TDD协作约定
- **红阶段**: 编写失败测试，团队Review测试逻辑
- **绿阶段**: 实现代码，团队Review实现质量
- **重构阶段**: 优化代码，团队Review重构效果

## 测试环境管理

### 环境隔离
- **开发环境**: 本地开发，使用SQLite数据库
- **测试环境**: Docker容器，使用PostgreSQL
- **预发布环境**: 生产镜像，使用生产数据库副本

### 测试数据隔离
- **单元测试**: 使用内存数据库，每个测试独立
- **集成测试**: 使用事务回滚，保持数据独立
- **E2E测试**: 使用专用测试数据，避免污染生产数据

## 性能测试策略

### 性能基准
- **API响应时间**: ≤2秒 (95%请求)
- **数据库查询**: ≤100ms (95%查询)
- **页面加载**: ≤3秒 (95%页面)

### 负载测试
- **并发用户**: 100个并发用户
- **测试时长**: 10分钟持续负载
- **成功率**: ≥99%

> 📝 **文档状态**: TDD策略框架已搭建，等待后续设计完善
