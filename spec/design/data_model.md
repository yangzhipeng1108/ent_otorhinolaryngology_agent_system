---
id: DM-MEDICAL-001
sn: MEDICAL
status: active
source_us: [US-TRIAGE-001, US-DIAGNOSIS-001]
related_api: [API-TRIAGE-001, API-DIAGNOSIS-001]
---

# DM-MEDICAL-001 医疗数据模型设计

## 数据模型设计原则

### 实体关系设计
- **患者实体**: 核心业务实体，关联所有医疗数据
- **问诊会话**: 多轮对话记录，支持上下文管理
- **诊断记录**: 诊断建议和医学推理过程
- **医学知识**: 疾病知识和诊疗指南结构化存储

### 数据一致性保证
- **引用完整性**: 外键引用完整性检查
- **数据完整性**: 必填字段验证和默认值处理
- **版本控制**: 数据模型版本管理和迁移策略

## 核心实体设计

### 患者实体 (Patient)
```yaml
Patient:
  attributes:
    patient_id: string (PK)
    name: string
    age: integer
    gender: enum(MALE, FEMALE, OTHER)
    phone: string
    email: string
    address: text
    created_at: datetime
    updated_at: datetime
    is_active: boolean
  relationships:
    has_many: ConsultationSession
    has_many: MedicalRecord
    has_many: DiagnosisRecord
```

### 问诊会话实体 (ConsultationSession)
```yaml
ConsultationSession:
  attributes:
    session_id: string (PK)
    patient_id: string (FK)
    start_time: datetime
    end_time: datetime
    status: enum(ACTIVE, COMPLETED, CANCELLED)
    triage_result: jsonb
    final_department: string
    urgency_level: enum(LOW, MEDIUM, HIGH, CRITICAL)
    created_at: datetime
    updated_at: datetime
  relationships:
    belongs_to: Patient
    has_many: DialogueMessage
    has_one: PreConsultationReport
```

### 对话消息实体 (DialogueMessage)
```yaml
DialogueMessage:
  attributes:
    message_id: string (PK)
    session_id: string (FK)
    message_type: enum(PATIENT, SYSTEM)
    content: text
    timestamp: datetime
    metadata: jsonb
  relationships:
    belongs_to: ConsultationSession
```

### 诊断记录实体 (DiagnosisRecord)
```yaml
DiagnosisRecord:
  attributes:
    diagnosis_id: string (PK)
    session_id: string (FK)
    patient_id: string (FK)
    primary_diagnosis: string
    confidence_score: float
    differential_diagnosis: jsonb
    evidence_links: jsonb
    treatment_recommendations: jsonb
    doctor_id: string
    created_at: datetime
    updated_at: datetime
  relationships:
    belongs_to: ConsultationSession
    belongs_to: Patient
```

### 医学知识实体 (MedicalKnowledge)
```yaml
MedicalKnowledge:
  attributes:
    knowledge_id: string (PK)
    knowledge_type: enum(DISEASE, SYMPTOM, TREATMENT, GUIDELINE)
    title: string
    content: text
    keywords: array
    evidence_level: enum(LOW, MEDIUM, HIGH)
    last_updated: datetime
    created_at: datetime
    updated_at: datetime
  relationships:
    has_many: DiagnosisRecord
```

## 数据关系映射

### 核心关系图
```
Patient (1) ←→ (N) ConsultationSession (1) ←→ (N) DialogueMessage
Patient (1) ←→ (N) MedicalRecord
ConsultationSession (1) ←→ (1) DiagnosisRecord
DiagnosisRecord (N) ←→ (N) MedicalKnowledge
```

### 引用完整性约束
- **外键约束**: 所有外键引用必须存在有效记录
- **级联删除**: 考虑数据安全，采用软删除策略
- **事务一致性**: 相关操作必须在事务中执行

## 数据存储策略

### PostgreSQL表结构设计

#### 患者表 (patients)
```sql
CREATE TABLE patients (
    patient_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL CHECK (age > 0 AND age < 150),
    gender VARCHAR(10) CHECK (gender IN ('MALE', 'FEMALE', 'OTHER')),
    phone VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT true
);
```

#### 问诊会话表 (consultation_sessions)
```sql
CREATE TABLE consultation_sessions (
    session_id VARCHAR(50) PRIMARY KEY,
    patient_id VARCHAR(50) NOT NULL REFERENCES patients(patient_id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    status VARCHAR(20) DEFAULT 'ACTIVE',
    triage_result JSONB,
    final_department VARCHAR(100),
    urgency_level VARCHAR(20) DEFAULT 'LOW',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
```

#### 对话消息表 (dialogue_messages)
```sql
CREATE TABLE dialogue_messages (
    message_id VARCHAR(50) PRIMARY KEY,
    session_id VARCHAR(50) NOT NULL REFERENCES consultation_sessions(session_id),
    message_type VARCHAR(20) DEFAULT 'PATIENT',
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB,
    FOREIGN KEY (session_id) REFERENCES consultation_sessions(session_id)
);
```

#### 诊断记录表 (diagnosis_records)
```sql
CREATE TABLE diagnosis_records (
    diagnosis_id VARCHAR(50) PRIMARY KEY,
    session_id VARCHAR(50) NOT NULL REFERENCES consultation_sessions(session_id),
    patient_id VARCHAR(50) NOT NULL REFERENCES patients(patient_id),
    primary_diagnosis VARCHAR(200) NOT NULL,
    confidence_score DECIMAL(5,2) CHECK (confidence_score >= 0.0 AND confidence_score <= 1.0),
    differential_diagnosis JSONB,
    evidence_links JSONB,
    treatment_recommendations JSONB,
    doctor_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES consultation_sessions(session_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
```

#### 医学知识表 (medical_knowledge)
```sql
CREATE TABLE medical_knowledge (
    knowledge_id VARCHAR(50) PRIMARY KEY,
    knowledge_type VARCHAR(20) NOT NULL,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    keywords TEXT[],
    evidence_level VARCHAR(20) DEFAULT 'MEDIUM',
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 数据访问层设计

### Repository模式实现
```python
class PatientRepository:
    def create_patient(self, patient_data: dict) -> str:
        # 创建患者记录
        pass
    
    def get_patient_by_id(self, patient_id: str) -> dict:
        # 根据ID获取患者信息
        pass
    
    def update_patient(self, patient_id: str, update_data: dict) -> bool:
        # 更新患者信息
        pass

class ConsultationSessionRepository:
    def create_session(self, session_data: dict) -> str:
        # 创建问诊会话
        pass
    
    def get_session_by_id(self, session_id: str) -> dict:
        # 获取会话详情
        pass
    
    def update_session_status(self, session_id: str, status: str) -> bool:
        # 更新会话状态
        pass
```

### 数据验证策略
```python
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    
    @validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 150:
            raise ValueError('年龄必须在0-150之间')
    
    @validator('gender')
    def validate_gender(cls, v):
        if v not in ['MALE', 'FEMALE', 'OTHER']:
            raise ValueError('性别必须是MALE/FEMALE/OTHER之一')

class ConsultationSessionCreate(BaseModel):
    patient_id: str
    start_time: datetime
    urgency_level: str = 'LOW'
    
    @validator('urgency_level')
    def validate_urgency_level(cls, v):
        if v not in ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']:
            raise ValueError('紧急程度必须是LOW/MEDIUM/HIGH/CRITICAL之一')
```

## 数据迁移策略

### 版本控制
- **数据库版本管理**: 使用Alembic进行数据库版本控制
- **迁移脚本**: 结构化数据迁移脚本，支持向前和向后迁移
- **数据备份**: 迁移前完整数据备份策略

### 数据同步策略
- **实时同步**: 关键数据实时同步到HIS/EMR系统
- **批量同步**: 非实时数据批量同步策略
- **冲突解决**: 数据冲突检测和解决机制

> 📝 **文档状态**: 文档已搭建，等待后续设计完善
