---
id: CQG-GATES-001
sn: CQG
status: active
source_proj: PROJ-STRUCT-001
related_tdd: TDD-STRATEGY-001
---

# CQG-GATES-001 代码质量门禁 ⚡ TDD主场核心

## 质量门禁策略

### 质量标准定义
- **代码覆盖率**: 整体覆盖率≥70%，单元测试≥80%
- **代码质量**: 0 critical issues, 0 major issues
- **性能基准**: API响应时间≤2秒，数据库查询≤100ms
- **安全标准**: 通过所有安全检查，无高危漏洞

### 门禁执行流程
```
代码提交 → 自动检查 → 质量评估 → 门禁判断 → 部署决策
    ↓           ↓           ↓           ↓           ↓
  Git Push   Pre-commit   SonarQube   Quality Gate  Deploy
```

## 静态代码分析

### 代码格式化标准
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3.8
        args: [--line-length=88]
  
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--profile=black, --line-length=88]
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=88, --extend-ignore=E203,W503]
        additional_dependencies:
          - flake8-docstrings
          - flake8-import-order
          - flake8-bugbear
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        args: [--strict, --ignore-missing-imports]
```

### 代码质量检查配置
```ini
# setup.cfg
[flake8]
max-line-length = 88
extend-ignore = E203, W503, E501
exclude = 
    .git,
    __pycache__,
    .venv,
    .eggs,
    *.egg,
    build,
    dist
per-file-ignores =
    __init__.py:F401
    tests/*:S101

[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
warn_unreachable = True
strict_equality = True

[mypy-tests.*]
disallow_untyped_defs = False
```

## 测试质量门禁

### 测试覆盖率配置
```ini
# .coveragerc
[run]
source = src
omit = 
    */tests/*
    */migrations/*
    */venv/*
    */__pycache__/*
    */conftest.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    if self.debug:
    if settings.DEBUG
    raise AssertionError
    raise NotImplementedError
    if 0:
    if __name__ == .__main__.:
    class .*\bProtocol\):
    @(abc\.)?abstractmethod

[html]
directory = htmlcov
```

### 测试质量标准
```python
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --strict-config
    --cov=src
    --cov-report=term-missing
    --cov-report=html:htmlcov
    --cov-report=xml
    --cov-fail-under=70
    --tb=short
    -v

markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests
    external: Tests that require external services
```

### 测试分类执行
```python
# tests/conftest.py
import pytest

def pytest_configure(config):
    """配置pytest标记"""
    config.addinivalue_line(
        "markers", "unit: Mark tests as unit tests"
    )
    config.addinivalue_line(
        "markers", "integration: Mark tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "e2e: Mark tests as end-to-end tests"
    )

def pytest_collection_modifyitems(config, items):
    """根据标记分类测试"""
    for item in items:
        # 为没有标记的测试添加unit标记
        if not any(item.iter_markers()):
            item.add_marker(pytest.mark.unit)
```

## 性能质量门禁

### 性能基准测试
```python
# tests/performance/test_api_performance.py
import pytest
import time
from httpx import Client
from app.main import app

class TestAPIPerformance:
    """API性能测试"""
    
    @pytest.mark.performance
    def test_triage_api_response_time(self):
        """测试导诊API响应时间"""
        with Client(app=app) as client:
            start_time = time.time()
            response = client.post(
                "/api/v1/triage/start",
                json={
                    "patient_id": "P001",
                    "initial_symptoms": "喉咙干痒，持续3天"
                }
            )
            end_time = time.time()
            
            response_time = end_time - start_time
            assert response.status_code == 200
            assert response_time <= 2.0, f"响应时间 {response_time}s 超过2秒限制"
    
    @pytest.mark.performance
    def test_diagnosis_api_response_time(self):
        """测试诊断API响应时间"""
        with Client(app=app) as client:
            start_time = time.time()
            response = client.post(
                "/api/v1/diagnosis/analyze",
                json={"session_id": "SESS001"}
            )
            end_time = time.time()
            
            response_time = end_time - start_time
            assert response.status_code == 200
            assert response_time <= 5.0, f"响应时间 {response_time}s 超过5秒限制"
```

### 数据库性能测试
```python
# tests/performance/test_database_performance.py
import pytest
import time
from sqlalchemy import text
from app.config.database import get_db_session

class TestDatabasePerformance:
    """数据库性能测试"""
    
    @pytest.mark.performance
    def test_patient_query_performance(self):
        """测试患者查询性能"""
        with get_db_session() as session:
            start_time = time.time()
            result = session.execute(
                text("SELECT * FROM patients WHERE id = :patient_id"),
                {"patient_id": "P001"}
            )
            end_time = time.time()
            
            query_time = end_time - start_time
            assert query_time <= 0.1, f"查询时间 {query_time}s 超过100ms限制"
    
    @pytest.mark.performance
    def test_consultation_insert_performance(self):
        """测试问诊记录插入性能"""
        with get_db_session() as session:
            start_time = time.time()
            session.execute(
                text("""
                    INSERT INTO consultation_sessions 
                    (session_id, patient_id, start_time, status)
                    VALUES (:session_id, :patient_id, :start_time, :status)
                """),
                {
                    "session_id": "SESS_PERF_001",
                    "patient_id": "P001",
                    "start_time": time.time(),
                    "status": "ACTIVE"
                }
            )
            session.commit()
            end_time = time.time()
            
            insert_time = end_time - start_time
            assert insert_time <= 0.05, f"插入时间 {insert_time}s 超过50ms限制"
```

## 安全质量门禁

### 安全扫描配置
```yaml
# .bandit
[bandit]
exclude_dirs = tests,docs,build,dist
skips = B101,B601
tests = B201,B301

[bandit.assert_used]
skips = B101,B601
```

### 依赖安全检查
```yaml
# .safety
# safety policy configuration
ignore:
  51658:  # Jinja2 < 3.1.2 (low severity)
  51457:  # urllib3 < 1.26.5 (medium severity)
```

### 安全测试用例
```python
# tests/security/test_security.py
import pytest
from httpx import Client
from app.main import app

class TestSecurity:
    """安全测试"""
    
    @pytest.mark.security
    def test_sql_injection_protection(self):
        """测试SQL注入防护"""
        malicious_input = "'; DROP TABLE patients; --"
        with Client(app=app) as client:
            response = client.post(
                "/api/v1/triage/start",
                json={
                    "patient_id": malicious_input,
                    "initial_symptoms": "正常症状"
                }
            )
            # 应该返回400错误，而不是执行恶意SQL
            assert response.status_code == 400
    
    @pytest.mark.security
    def test_xss_protection(self):
        """测试XSS防护"""
        xss_payload = "<script>alert('xss')</script>"
        with Client(app=app) as client:
            response = client.post(
                "/api/v1/triage/start",
                json={
                    "patient_id": "P001",
                    "initial_symptoms": xss_payload
                }
            )
            # 响应中不应该包含未转义的脚本
            assert "<script>" not in response.text
    
    @pytest.mark.security
    def test_authentication_required(self):
        """测试认证要求"""
        with Client(app=app) as client:
            response = client.get("/api/v1/auth/profile")
            # 未认证应该返回401
            assert response.status_code == 401
```

## CI/CD质量门禁

### GitHub Actions配置
```yaml
# .github/workflows/quality-gates.yml
name: Quality Gates

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  quality-checks:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Run pre-commit checks
      run: |
        pre-commit run --all-files
    
    - name: Run tests with coverage
      run: |
        pytest --cov=src --cov-report=xml --cov-fail-under=70
    
    - name: Run security scan
      run: |
        bandit -r src/ -f json -o bandit-report.json
        safety check --json --output safety-report.json
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
    
    - name: SonarQube Scan
      uses: sonarqube-quality-gate-action@master
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

### 质量门禁配置
```yaml
# sonar-project.properties
sonar.projectKey=ent-otorhinolaryngology-agent-system
sonar.projectName=ENT Otorhinolaryngology Agent System
sonar.projectVersion=1.0.0

sonar.sources=src/
sonar.tests=tests/
sonar.exclusions=**/migrations/**,**/venv/**,**/__pycache__/**

sonar.python.coverage.reportPaths=coverage.xml
sonar.python.xunit.reportPath=pytest-report.xml

# 质量门禁
sonar.qualitygate.wait=true

# 代码覆盖率
sonar.coverage.exclusions=**/tests/**,**/migrations/**
sonar.cpd.exclusions=**/tests/**

# 复杂度
sonar.python.file.suffixes=.py
sonar.python.lcov.reportPaths=coverage.lcov
```

## 代码审查标准

### Pull Request检查清单
```markdown
## 代码审查清单

### 功能性检查
- [ ] 功能实现符合需求规格
- [ ] 边界条件处理正确
- [ ] 错误处理机制完善
- [ ] 性能要求满足

### 代码质量检查
- [ ] 代码风格符合团队规范
- [ ] 函数和类命名清晰
- [ ] 代码注释充分且准确
- [ ] 无重复代码和冗余逻辑

### 测试检查
- [ ] 单元测试覆盖率≥80%
- [ ] 集成测试覆盖主要流程
- [ ] 测试用例设计合理
- [ ] 测试数据管理规范

### 安全检查
- [ ] 输入验证充分
- [ ] 敏感数据处理安全
- [ ] 权限控制正确
- [ ] 无安全漏洞

### 文档检查
- [ ] API文档更新完整
- [ ] 代码注释清晰
- [ ] 变更日志记录
- [ ] 部署说明准确
```

### 代码审查流程
```python
# scripts/pr_validator.py
import subprocess
import sys
import json

def validate_pull_request():
    """验证Pull Request质量"""
    checks = {
        "code_format": check_code_format(),
        "test_coverage": check_test_coverage(),
        "security_scan": check_security_scan(),
        "performance_test": check_performance_test()
    }
    
    all_passed = all(checks.values())
    
    if not all_passed:
        failed_checks = [k for k, v in checks.items() if not v]
        print(f"质量检查失败: {failed_checks}")
        sys.exit(1)
    
    print("所有质量检查通过")
    return True

def check_code_format():
    """检查代码格式"""
    try:
        result = subprocess.run(["black", "--check", "src/"], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except Exception:
        return False

def check_test_coverage():
    """检查测试覆盖率"""
    try:
        result = subprocess.run(["pytest", "--cov=src", "--cov-fail-under=70"],
                              capture_output=True, text=True)
        return result.returncode == 0
    except Exception:
        return False

def check_security_scan():
    """检查安全扫描"""
    try:
        result = subprocess.run(["bandit", "-r", "src/", "-f", "json"],
                              capture_output=True, text=True)
        # 检查是否有高危漏洞
        if result.returncode != 0:
            report = json.loads(result.stdout)
            high_severity = [r for r in report.get("results", []) 
                           if r.get("issue_severity") == "HIGH"]
            return len(high_severity) == 0
        return True
    except Exception:
        return False

def check_performance_test():
    """检查性能测试"""
    try:
        result = subprocess.run(["pytest", "-m", "performance"],
                              capture_output=True, text=True)
        return result.returncode == 0
    except Exception:
        return False

if __name__ == "__main__":
    validate_pull_request()
```

## 质量报告生成

### 质量报告模板
```python
# scripts/quality_report.py
import json
import subprocess
from datetime import datetime

class QualityReportGenerator:
    """质量报告生成器"""
    
    def generate_report(self):
        """生成质量报告"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "project": "ent-otorhinolaryngology-agent-system",
            "version": "1.0.0",
            "metrics": {
                "code_coverage": self.get_coverage_metrics(),
                "code_quality": self.get_code_quality_metrics(),
                "security": self.get_security_metrics(),
                "performance": self.get_performance_metrics()
            }
        }
        
        self.save_report(report)
        return report
    
    def get_coverage_metrics(self):
        """获取覆盖率指标"""
        try:
            result = subprocess.run(
                ["coverage", "json", "--fail-under=0"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                return {
                    "total_coverage": data["totals"]["percent_covered"],
                    "lines_covered": data["totals"]["covered_lines"],
                    "lines_missing": data["totals"]["missing_lines"]
                }
        except Exception:
            pass
        return {"total_coverage": 0, "lines_covered": 0, "lines_missing": 0}
    
    def get_code_quality_metrics(self):
        """获取代码质量指标"""
        try:
            result = subprocess.run(
                ["flake8", "--format=json", "src/"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                issues = json.loads(result.stdout)
                return {
                    "total_issues": len(issues),
                    "error_count": len([i for i in issues if i.get("code") in ["E999"]]),
                    "warning_count": len([i for i in issues if i.get("code").startswith("W")])
                }
        except Exception:
            pass
        return {"total_issues": 0, "error_count": 0, "warning_count": 0}
    
    def get_security_metrics(self):
        """获取安全指标"""
        try:
            result = subprocess.run(
                ["bandit", "-r", "src/", "-f", "json"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                high_severity = [r for r in data.get("results", []) 
                               if r.get("issue_severity") == "HIGH"]
                return {
                    "total_issues": len(data.get("results", [])),
                    "high_severity": len(high_severity),
                    "medium_severity": len([r for r in data.get("results", []) 
                                          if r.get("issue_severity") == "MEDIUM"])
                }
        except Exception:
            pass
        return {"total_issues": 0, "high_severity": 0, "medium_severity": 0}
    
    def get_performance_metrics(self):
        """获取性能指标"""
        try:
            result = subprocess.run(
                ["pytest", "-m", "performance", "--tb=no"],
                capture_output=True, text=True
            )
            return {
                "tests_passed": result.returncode == 0,
                "test_count": result.stdout.count("passed")
            }
        except Exception:
            pass
        return {"tests_passed": False, "test_count": 0}
    
    def save_report(self, report):
        """保存质量报告"""
        with open("quality_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generator = QualityReportGenerator()
    generator.generate_report()
```

> 📝 **文档状态**: 代码质量门禁框架已搭建，等待后续设计完善
