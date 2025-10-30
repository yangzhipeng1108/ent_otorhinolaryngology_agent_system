---
id: TDM-MANAGEMENT-001
sn: TDM
status: active
source_proj: PROJ-STRUCT-001
related_bdd: BDD-SCENARIOS-001
---

# TDM-MANAGEMENT-001 测试数据管理 ⚡ TDD主场核心

## 测试数据管理策略

### 数据管理原则
- **数据隔离**: 测试数据与生产数据完全隔离
- **数据一致性**: 确保测试数据的可重复性和一致性
- **数据清理**: 每个测试后自动清理测试数据
- **数据安全**: 敏感数据脱敏处理

### 数据分类管理
```
测试数据分类:
├── 固定数据 (Fixed Data) - 可重复使用的标准数据
├── 动态数据 (Dynamic Data) - 随机生成的测试数据
├── 边界数据 (Boundary Data) - 边界条件测试数据
└── 异常数据 (Exception Data) - 异常情况测试数据
```

## Factory模式实现

### 患者数据工厂
```python
# tests/factories/patient_factory.py
import factory
from faker import Faker
from app.models.patient import Patient

fake = Faker('zh_CN')

class PatientFactory(factory.Factory):
    """患者数据工厂"""
    class Meta:
        model = Patient
    
    id = factory.Sequence(lambda n: f"P{n:03d}")
    name = factory.LazyAttribute(lambda _: fake.name())
    age = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=80))
    gender = factory.Iterator(["MALE", "FEMALE"])
    phone = factory.LazyAttribute(lambda _: fake.phone_number())
    email = factory.LazyAttribute(lambda _: fake.email())
    address = factory.LazyAttribute(lambda _: fake.address())
    is_active = True

class AdultPatientFactory(PatientFactory):
    """成年患者工厂"""
    age = factory.LazyAttribute(lambda _: fake.random_int(min=18, max=80))

class ChildPatientFactory(PatientFactory):
    """儿童患者工厂"""
    age = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=17))
```

### 问诊会话数据工厂
```python
# tests/factories/consultation_factory.py
import factory
from datetime import datetime, timedelta
from app.models.consultation import ConsultationSession
from .patient_factory import PatientFactory

class ConsultationSessionFactory(factory.Factory):
    """问诊会话数据工厂"""
    class Meta:
        model = ConsultationSession
    
    session_id = factory.Sequence(lambda n: f"SESS{n:03d}")
    patient = factory.SubFactory(PatientFactory)
    start_time = factory.LazyAttribute(lambda _: datetime.now())
    end_time = None
    status = "ACTIVE"
    triage_result = factory.LazyAttribute(lambda _: {
        "department": "耳鼻喉科",
        "urgency_level": "NORMAL",
        "recommendations": ["建议尽快就诊"]
    })
    final_department = "耳鼻喉科"
    urgency_level = "NORMAL"

class CompletedConsultationFactory(ConsultationSessionFactory):
    """已完成问诊会话工厂"""
    status = "COMPLETED"
    end_time = factory.LazyAttribute(
        lambda obj: obj.start_time + timedelta(minutes=30)
    )
```

### 诊断记录数据工厂
```python
# tests/factories/diagnosis_factory.py
import factory
from datetime import datetime
from app.models.diagnosis import DiagnosisRecord
from .consultation_factory import ConsultationSessionFactory

class DiagnosisRecordFactory(factory.Factory):
    """诊断记录数据工厂"""
    class Meta:
        model = DiagnosisRecord
    
    diagnosis_id = factory.Sequence(lambda n: f"DIAG{n:03d}")
    session = factory.SubFactory(ConsultationSessionFactory)
    primary_diagnosis = factory.Iterator([
        "急性咽炎", "急性中耳炎", "过敏性鼻炎", "慢性咽炎"
    ])
    confidence_score = factory.LazyAttribute(
        lambda _: round(fake.random.uniform(0.7, 0.95), 2)
    )
    differential_diagnosis = factory.LazyAttribute(lambda _: [
        fake.random_element(["急性咽炎", "慢性咽炎", "过敏性鼻炎"])
    ])
    evidence_links = factory.LazyAttribute(lambda _: [
        {
            "symptom": fake.random_element(["喉咙痛", "鼻塞", "耳痛"]),
            "weight": round(fake.random.uniform(0.5, 1.0), 2)
        }
    ])
    treatment_recommendations = factory.LazyAttribute(lambda _: [
        "多喝水", "注意休息", "避免辛辣食物"
    ])
    doctor_id = factory.Sequence(lambda n: f"DOC{n:03d}")
```

## 测试数据场景

### 智能导诊测试数据
```python
# tests/fixtures/triage_data.py
TRIAGE_TEST_DATA = {
    "throat_symptoms": {
        "input": "喉咙干痒，持续3天",
        "expected_department": "耳鼻喉科",
        "expected_sub_department": "咽喉科",
        "expected_urgency": "NORMAL"
    },
    "ear_pain_symptoms": {
        "input": "右耳疼痛，伴有听力下降",
        "expected_department": "耳鼻喉科", 
        "expected_sub_department": "耳科",
        "expected_urgency": "HIGH"
    },
    "nasal_congestion": {
        "input": "鼻塞，流清涕，持续1周",
        "expected_department": "耳鼻喉科",
        "expected_sub_department": "鼻科", 
        "expected_urgency": "NORMAL"
    },
    "hoarseness": {
        "input": "声音嘶哑，持续2周",
        "expected_department": "耳鼻喉科",
        "expected_sub_department": "咽喉科",
        "expected_urgency": "MEDIUM"
    }
}
```

### 辅助诊断测试数据
```python
# tests/fixtures/diagnosis_data.py
DIAGNOSIS_TEST_DATA = {
    "acute_pharyngitis": {
        "symptoms": ["喉咙痛", "发热", "咽部充血"],
        "expected_diagnosis": "急性咽炎",
        "expected_confidence": 0.85,
        "expected_treatment": ["抗生素治疗", "多喝水", "休息"]
    },
    "acute_otitis_media": {
        "symptoms": ["耳痛", "听力下降", "鼓膜充血"],
        "expected_diagnosis": "急性中耳炎",
        "expected_confidence": 0.90,
        "expected_treatment": ["抗生素治疗", "止痛药", "定期复查"]
    },
    "allergic_rhinitis": {
        "symptoms": ["鼻塞", "流清涕", "打喷嚏", "鼻痒"],
        "expected_diagnosis": "过敏性鼻炎",
        "expected_confidence": 0.80,
        "expected_treatment": ["抗组胺药", "鼻用激素", "避免过敏原"]
    }
}
```

### 系统集成测试数据
```python
# tests/fixtures/integration_data.py
INTEGRATION_TEST_DATA = {
    "his_patient_sync": {
        "patient_id": "HIS001",
        "name": "张三",
        "age": 35,
        "gender": "MALE",
        "phone": "13800138000",
        "email": "zhangsan@example.com"
    },
    "lis_lab_results": {
        "patient_id": "LIS001",
        "test_type": "血常规",
        "results": {
            "wbc": 8.5,
            "rbc": 4.5,
            "hb": 140,
            "plt": 250
        },
        "reference_range": {
            "wbc": "4.0-10.0",
            "rbc": "4.0-5.5",
            "hb": "120-160",
            "plt": "100-300"
        }
    }
}
```

## Mock和Stub策略

### 外部系统Mock
```python
# tests/mocks/his_service_mock.py
from unittest.mock import Mock
from app.services.integration.his_service import HISIntegrationService

class MockHISIntegrationService:
    """HIS系统服务Mock"""
    
    @staticmethod
    def create_mock():
        mock = Mock(spec=HISIntegrationService)
        
        # Mock患者信息同步
        mock.sync_patient_info.return_value = {
            "patient_id": "HIS001",
            "name": "张三",
            "age": 35,
            "gender": "MALE",
            "phone": "13800138000",
            "sync_status": "success"
        }
        
        # Mock挂号信息获取
        mock.get_appointment_info.return_value = {
            "appointment_id": "APT001",
            "department": "耳鼻喉科",
            "doctor": "李医生",
            "appointment_time": "2025-10-30 09:00:00"
        }
        
        return mock
```

### API响应Mock
```python
# tests/mocks/api_responses.py
import json
from unittest.mock import Mock

class MockAPIResponses:
    """API响应Mock"""
    
    @staticmethod
    def create_triage_response():
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "data": {
                "session_id": "SESS001",
                "triage_result": {
                    "department": "耳鼻喉科",
                    "sub_department": "咽喉科",
                    "urgency_level": "NORMAL"
                },
                "next_question": {
                    "question": "您是否有发热症状？",
                    "question_type": "boolean"
                }
            },
            "message": "导诊分析完成",
            "timestamp": "2025-10-29T16:14:36Z"
        }
        return response
    
    @staticmethod
    def create_diagnosis_response():
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "data": {
                "diagnosis_suggestions": [
                    {
                        "disease": "急性咽炎",
                        "confidence": 0.85,
                        "evidence": ["喉咙痛", "发热", "咽部充血"]
                    }
                ],
                "treatment_recommendations": [
                    "抗生素治疗",
                    "多喝水",
                    "休息"
                ]
            },
            "message": "诊断分析完成",
            "timestamp": "2025-10-29T16:14:36Z"
        }
        return response
```

## 数据清理策略

### 测试数据清理
```python
# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.database import get_database_url
from app.models.base import Base

@pytest.fixture(scope="function")
def test_db_session():
    """测试数据库会话fixture"""
    # 创建测试数据库引擎
    engine = create_engine(get_database_url(test=True))
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    
    # 创建会话
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    
    yield session
    
    # 清理：删除所有数据
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(autouse=True)
def cleanup_test_data(test_db_session):
    """自动清理测试数据"""
    yield
    # 测试后清理所有表数据
    for table in reversed(Base.metadata.sorted_tables):
        test_db_session.execute(table.delete())
    test_db_session.commit()
```

### 数据隔离策略
```python
# tests/utils/data_isolation.py
import uuid
from contextlib import contextmanager

class DataIsolationManager:
    """数据隔离管理器"""
    
    @staticmethod
    @contextmanager
    def isolated_transaction(session):
        """创建隔离的事务"""
        transaction = session.begin_nested()
        try:
            yield session
            transaction.rollback()  # 总是回滚，确保数据隔离
        finally:
            transaction.close()
    
    @staticmethod
    def generate_test_id(prefix="TEST"):
        """生成测试专用ID"""
        return f"{prefix}_{uuid.uuid4().hex[:8]}"
    
    @staticmethod
    def create_test_suffix():
        """创建测试后缀"""
        return f"_test_{uuid.uuid4().hex[:6]}"
```

## 数据验证工具

### 数据完整性验证
```python
# tests/utils/data_validator.py
from typing import Dict, Any, List

class DataValidator:
    """数据验证工具"""
    
    @staticmethod
    def validate_patient_data(data: Dict[str, Any]) -> bool:
        """验证患者数据完整性"""
        required_fields = ['id', 'name', 'age', 'gender']
        return all(field in data for field in required_fields)
    
    @staticmethod
    def validate_consultation_data(data: Dict[str, Any]) -> bool:
        """验证问诊会话数据完整性"""
        required_fields = ['session_id', 'patient_id', 'start_time', 'status']
        return all(field in data for field in required_fields)
    
    @staticmethod
    def validate_diagnosis_data(data: Dict[str, Any]) -> bool:
        """验证诊断记录数据完整性"""
        required_fields = ['diagnosis_id', 'session_id', 'primary_diagnosis', 'confidence_score']
        return all(field in data for field in required_fields)
    
    @staticmethod
    def validate_triage_result(result: Dict[str, Any]) -> bool:
        """验证导诊结果格式"""
        required_fields = ['department', 'urgency_level']
        return all(field in result for field in required_fields)
```

### 测试数据生成器
```python
# tests/utils/data_generator.py
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('zh_CN')

class TestDataGenerator:
    """测试数据生成器"""
    
    @staticmethod
    def generate_symptoms_text() -> str:
        """生成症状描述文本"""
        symptoms = [
            "喉咙干痒，持续3天",
            "右耳疼痛，伴有听力下降", 
            "鼻塞，流清涕，持续1周",
            "声音嘶哑，持续2周",
            "耳鸣，伴有头晕"
        ]
        return random.choice(symptoms)
    
    @staticmethod
    def generate_medical_history() -> Dict[str, Any]:
        """生成病史信息"""
        return {
            "allergies": random.choice(["无", "青霉素过敏", "花粉过敏"]),
            "chronic_diseases": random.choice(["无", "高血压", "糖尿病"]),
            "medications": random.choice(["无", "降压药", "降糖药"]),
            "previous_surgeries": random.choice(["无", "扁桃体切除术", "鼻中隔矫正术"])
        }
    
    @staticmethod
    def generate_vital_signs() -> Dict[str, Any]:
        """生成生命体征数据"""
        return {
            "temperature": round(random.uniform(36.0, 38.5), 1),
            "blood_pressure": f"{random.randint(110, 140)}/{random.randint(70, 90)}",
            "heart_rate": random.randint(60, 100),
            "respiratory_rate": random.randint(12, 20)
        }
```

> 📝 **文档状态**: 测试数据管理框架已搭建，等待后续设计完善
