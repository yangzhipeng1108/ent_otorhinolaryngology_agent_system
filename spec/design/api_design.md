---
id: API-DESIGN-001
sn: API
status: active
source_arch: ARCH-DESIGN-001
related_dm: [DM-USER-001, DM-MEDICAL-001]
---

# API-DESIGN-001 API设计规范

## API设计原则

### RESTful设计标准
- **资源导向**: 以业务资源为中心设计API端点
- **HTTP方法语义**: 严格按照HTTP方法语义使用（GET查询、POST创建、PUT更新、DELETE删除）
- **状态码规范**: 标准HTTP状态码，配合业务错误码
- **版本管理**: API版本通过URL路径管理（/api/v1/）

### 数据格式标准
- **请求格式**: JSON格式，Content-Type: application/json
- **响应格式**: 统一JSON响应结构，包含data、message、timestamp字段
- **错误处理**: 标准错误响应格式，包含错误码、错误信息、错误详情

## 核心API设计

### 患者端API

#### 智础服务API
```
POST /api/v1/auth/login
POST /api/v1/auth/logout
GET /api/v1/auth/profile
```

#### 智能导诊API
```
POST /api/v1/triage/start
POST /api/v1/triage/message
GET /api/v1/triage/status/{session_id}
POST /api/v1/triage/complete
```

#### 预问诊报告API
```
GET /api/v1/triage/report/{session_id}
POST /api/v1/triage/report/share
```

### 医生端API

#### 辅助诊断API
```
POST /api/v1/diagnosis/analyze
GET /api/v1/diagnosis/suggestions/{session_id}
POST /api/v1/diagnosis/report
```

#### 患查结果API
```
POST /api/v1/examination/results
GET /api/v1/examination/results/{result_id}
```

#### 诊断报告API
```
GET /api/v1/diagnosis/report/{report_id}
POST /api/v1/diagnosis/report/save
```

### 管理端API

#### 数据统计API
```
GET /api/v1/analytics/usage
GET /api/v1/analytics/performance
GET /api/v1/analytics/quality
```

#### 系统配置API
```
GET /api/v1/config/system
PUT /api/v1/config/system
POST /api/v1/config/medical-knowledge
```

## 数据模型设计

### 请求响应格式标准

#### 统一响应格式
```json
{
  "data": {
    // 具体业务数据
  },
  "message": "操作成功",
  "timestamp": "2025-10-29T15:57:10Z",
  "request_id": "req_123456789"
}
```

#### 错误响应格式
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "请求参数验证失败",
    "details": {
      "field": "email",
      "issue": "邮箱格式不正确"
    }
  },
  "timestamp": "2025-10-29T15:57:10Z",
  "request_id": "req_123456789"
}
```

### 核心数据结构

#### 患者症状输入
```json
{
  "patient_info": {
    "patient_id": "P001",
    "age": 35,
    "gender": "female"
  },
  "symptoms": {
    "description": "喉咙干痒，持续3天",
    "duration": "3天",
    "severity": "moderate",
    "accompanying_symptoms": ["轻微咳嗽"]
  }
}
```

#### 导诊响应
```json
{
  "session_id": "sess_123456",
  "triage_result": {
    "department": "耳鼻喉科",
    "sub_department": "咽喉科",
    "urgency_level": "normal",
    "recommendations": ["建议尽快就诊", "避免辛辣食物"]
  },
  "next_question": {
    "question": "您是否有发热症状？",
    "question_type": "boolean"
  }
}
```

#### 诊断建议
```json
{
  "diagnosis_suggestions": [
    {
      "disease": "急性咽炎",
      "confidence": 0.85,
      "evidence": ["喉咙干痒", "持续时间3天", "无发热"]
    }
  ],
  "differential_diagnosis": [
    "急性咽炎",
    "慢性咽炎",
    "过敏性咽炎"
  ],
  "examination_recommendations": [
    "血常规检查",
    "咽拭子培养"
  ]
}
```

## 接口契约设计

### 内部服务接口契约

#### AI对话服务接口
```yaml
service: DialogueService
interface:
  process_message:
    input:
      session_id: string
      message: string
      context: object
    output:
      response: string
      next_question: object
      is_complete: boolean
    constraints:
      - session_id must be valid
      - message length <= 1000 chars
```

#### 医学推理服务接口
```yaml
service: MedicalReasoningService
interface:
  analyze_symptoms:
    input:
      symptoms: array
      medical_history: object
      patient_info: object
    output:
      diagnosis_suggestions: array
      confidence_scores: array
      evidence_links: array
    constraints:
      - symptoms array must not be empty
      - medical_history must include relevant fields
```

#### 外部系统集成接口
```yaml
service: HISIntegrationService
interface:
  sync_patient_info:
    input:
      patient_id: string
      sync_type: string
    output:
      patient_data: object
      sync_status: string
    constraints:
      - patient_id must exist in HIS system
      - sync_type must be valid type
```

## 安全设计

### 认证授权
- **JWT令牌认证**: 无状态认证，支持令牌刷新
- **API密钥管理**: 客户端API密钥，服务端API密钥
- **权限控制**: 基于角色的API访问控制

### 数据验证
- **输入验证**: 严格的参数验证和业务规则检查
- **输出过滤**: 敏感数据脱敏处理
- **审计日志**: 完整的API调用审计记录

### 限流控制
- **请求限流**: 基于用户和IP的请求频率限制
- **并发控制**: 系统级并发控制，防止过载
- **熔断机制**: 服务降级和熔断保护

## 版本管理

### API版本策略
- **URL版本控制**: /api/v1/, /api/v2/ 等
- **向后兼容**: 保持旧版本API的兼容性
- **废弃通知**: 提前通知API废弃计划

### 变更管理
- **ADR记录**: 重大架构决策记录和影响分析
- **版本发布**: 标准化版本发布流程
- **变更通知**: 向相关方发送变更通知

> 📝 **文档状态**: 文档已搭建，等待后续设计完善
