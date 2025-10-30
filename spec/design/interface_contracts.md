---
id: IFC-CONTRACTS-001
sn: IFC
status: active
source_api: API-DESIGN-001
source_cmp: CMP-BACKEND-001
related_dm: [DM-MEDICAL-001]
---

# IFC-CONTRACTS-001 接口契约定义

## 契约设计原则

### 标准化契约管理
- **接口规范统一**: 所有接口遵循统一的契约格式
- **版本兼容性**: 支持接口版本管理和向后兼容
- **契约驱动开发**: 基于契约进行组件开发和集成

### 契约完整性保证
- **输入输出定义**: 明确定义所有接口的输入输出格式
- **错误处理规范**: 标准化的错误处理和异常情况
- **性能约束**: 接口性能要求和约束条件

## 核心服务契约

### 认证服务契约

#### 用户登录契约
```yaml
contract_name: UserLoginContract
version: v1.0
service: AuthenticationService
endpoint: /api/v1/auth/login
method: POST
input_contract:
  schema:
    type: object
    required: [username, password]
    properties:
      username:
        type: string
        format: email
        description: 用户邮箱
      password:
        type: string
        minLength: 8
        description: 用户密码
      device_info:
        type: object
        properties:
          device_type: string
          device_id: string
          user_agent: string
        description: 设备信息
output_contract:
  success_response:
    type: object
    properties:
      data:
        type: object
        properties:
          access_token:
            type: string
            description: JWT访问令牌
          refresh_token:
            type: string
            description: 刷新令牌
          expires_in:
            type: integer
            description: 令牌过期时间(秒)
          user_info:
            type: object
            properties:
              user_id: string
              name: string
              role: string
      message:
        type: string
        example: "登录成功"
      timestamp:
        type: string
        format: date-time
  error_responses:
    - status_code: 401
      error_code: INVALID_CREDENTIALS
      message: "用户名或密码错误"
    - status_code: 400
      error_code: VALIDATION_ERROR
      message: "请求参数验证失败"
performance_constraints:
  response_time: <= 2s
  throughput: >= 100 req/s
```

#### 令牌验证契约
```yaml
contract_name: TokenValidationContract
version: v1.0
service: AuthenticationService
endpoint: /api/v1/auth/validate
method: POST
input_contract:
  schema:
    type: object
    required: [token]
    properties:
      token:
        type: string
        description: JWT令牌
output_contract:
  success_response:
    type: object
    properties:
      data:
        type: object
        properties:
          valid:
            type: boolean
          user_info:
            type: object
          expires_at:
            type: string
            format: date-time
      message: string
      timestamp: string
performance_constraints:
  response_time: <= 500ms
  throughput: >= 500 req/s
```

### 智能导诊服务契约

#### 开始导诊契约
```yaml
contract_name: StartTriageContract
version: v1.0
service: TriageService
endpoint: /api/v1/triage/start
method: POST
input_contract:
  schema:
    type: object
    required: [patient_id, initial_symptoms]
    properties:
      patient_id:
        type: string
        description: 患者ID
      initial_symptoms:
        type: string
        maxLength: 1000
        description: 初始症状描述
      input_type:
        type: string
        enum: [text, voice]
        default: text
        description: 输入类型
output_contract:
  success_response:
    type: object
    properties:
      data:
        type: object
        properties:
          session_id:
            type: string
            description: 导诊会话ID
          first_question:
            type: object
            properties:
              question: string
              question_type: string
              options: array
          estimated_duration:
            type: integer
            description: 预估问诊时长(分钟)
      message: string
      timestamp: string
performance_constraints:
  response_time: <= 3s
  throughput: >= 50 req/s
```

#### 处理消息契约
```yaml
contract_name: ProcessMessageContract
version: v1.0
service: TriageService
endpoint: /api/v1/triage/message
method: POST
input_contract:
  schema:
    type: object
    required: [session_id, message]
    properties:
      session_id:
        type: string
        description: 会话ID
      message:
        type: string
        maxLength: 1000
        description: 患者消息
      message_type:
        type: string
        enum: [text, voice]
        default: text
output_contract:
  success_response:
    type: object
    properties:
      data:
        type: object
        properties:
          response:
            type: string
            description: 系统回复
          next_question:
            type: object
            properties:
              question: string
              question_type: string
              options: array
          is_complete:
            type: boolean
            description: 问诊是否完成
          triage_result:
            type: object
            description: 导诊结果(如果完成)
      message: string
      timestamp: string
performance_constraints:
  response_time: <= 5s
  throughput: >= 30 req/s
```

### 辅助诊断服务契约

#### 诊断分析契约
```yaml
contract_name: DiagnosisAnalysisContract
version: v1.0
service: DiagnosisService
endpoint: /api/v1/diagnosis/analyze
method: POST
input_contract:
  schema:
    type: object
    required: [session_id]
    properties:
      session_id:
        type: string
        description: 问诊会话ID
      include_examination_results:
        type: boolean
        default: true
        description: 是否包含检查结果
output_contract:
  success_response:
    type: object
    properties:
      data:
        type: object
        properties:
          diagnosis_suggestions:
            type: array
            items:
              type: object
              properties:
                disease: string
                confidence: number
                evidence: array
          differential_diagnosis:
            type: array
            items: string
          examination_recommendations:
            type: array
            items: string
          treatment_recommendations:
            type: array
            items: string
      message: string
      timestamp: string
performance_constraints:
  response_time: <= 10s
  throughput: >= 20 req/s
```

## 数据契约定义

### 患者数据契约
```yaml
contract_name: PatientDataContract
version: v1.0
description: 患者基本信息数据结构
schema:
  type: object
  required: [patient_id, name, age, gender]
  properties:
    patient_id:
      type: string
      pattern: ^P[0-9]+$
      description: 患者唯一标识
    name:
      type: string
      maxLength: 100
      description: 患者姓名
    age:
      type: integer
      minimum: 0
      maximum: 150
      description: 患者年龄
    gender:
      type: string
      enum: [MALE, FEMALE, OTHER]
      description: 性别
    phone:
      type: string
      pattern: ^1[3-9][0-9]{9}$
      description: 手机号码
    email:
      type: string
      format: email
      description: 邮箱地址
    address:
      type: string
      maxLength: 500
      description: 地址
validation_rules:
  - name: "姓名不能为空"
  - age: "年龄必须在0-150之间"
  - gender: "性别必须是有效值"
```

### 症状数据契约
```yaml
contract_name: SymptomDataContract
version: v1.0
description: 症状描述数据结构
schema:
  type: object
  required: [description, duration]
  properties:
    description:
      type: string
      maxLength: 1000
      description: 症状描述
    duration:
      type: string
      description: 持续时间
    severity:
      type: string
      enum: [mild, moderate, severe]
      description: 严重程度
    accompanying_symptoms:
      type: array
      items:
        type: string
      description: 伴随症状
    onset_time:
      type: string
      format: date-time
      description: 发作时间
validation_rules:
  - description: "症状描述不能为空"
  - duration: "持续时间不能为空"
```

### 诊断结果契约
```yaml
contract_name: DiagnosisResultContract
version: v1.0
description: 诊断结果数据结构
schema:
  type: object
  required: [primary_diagnosis, confidence_score]
  properties:
    primary_diagnosis:
      type: string
      maxLength: 200
      description: 主要诊断
    confidence_score:
      type: number
      minimum: 0.0
      maximum: 1.0
      description: 置信度分数
    differential_diagnosis:
      type: array
      items:
        type: string
      description: 鉴别诊断
    evidence_links:
      type: array
      items:
        type: object
        properties:
          symptom: string
          weight: number
      description: 证据链接
    treatment_recommendations:
      type: array
      items:
        type: string
      description: 治疗建议
    examination_recommendations:
      type: array
      items:
        type: string
      description: 检查建议
validation_rules:
  - primary_diagnosis: "主要诊断不能为空"
  - confidence_score: "置信度必须在0-1之间"
```

## 集成契约

### HIS系统集成契约
```yaml
contract_name: HISIntegrationContract
version: v1.0
service: HISIntegrationService
description: HIS系统集成接口契约
endpoints:
  - name: GetPatientInfo
    method: GET
    path: /his/api/v1/patients/{patient_id}
    input:
      path_params:
        patient_id: string
    output:
      success:
        patient_data: PatientDataContract
      errors:
        - code: PATIENT_NOT_FOUND
          message: "患者不存在"
        - code: SYSTEM_ERROR
          message: "系统错误"
  - name: SyncAppointmentData
    method: POST
    path: /his/api/v1/appointments/sync
    input:
      body:
        appointment_data: object
    output:
      success:
        sync_result: object
      errors:
        - code: SYNC_FAILED
          message: "同步失败"
performance_requirements:
  response_time: <= 5s
  availability: >= 99.5%
```

### LIS系统集成契约
```yaml
contract_name: LISIntegrationContract
version: v1.0
service: LISIntegrationService
description: LIS系统集成接口契约
endpoints:
  - name: GetExaminationResults
    method: GET
    path: /lis/api/v1/results/{patient_id}
    input:
      path_params:
        patient_id: string
      query_params:
        start_date: string
        end_date: string
    output:
      success:
        results: array
        items:
          type: object
          properties:
            exam_id: string
            exam_type: string
            result: string
            reference_range: string
            exam_date: string
      errors:
        - code: NO_RESULTS_FOUND
          message: "未找到检查结果"
        - code: SYSTEM_ERROR
          message: "系统错误"
performance_requirements:
  response_time: <= 3s
  availability: >= 99.0%
```

## 契约版本管理

### 版本控制策略
- **语义化版本**: 采用主版本.次版本.修订版本格式
- **向后兼容**: 主版本变更可能破坏兼容性，次版本向后兼容
- **废弃通知**: 提前3个月通知API废弃计划

### 版本迁移指南
```yaml
version_migration:
  from: v1.0
  to: v2.0
  breaking_changes:
    - field: patient_id
      old_type: string
      new_type: string
      pattern_change: "P[0-9]+" -> "PAT[0-9]+"
      migration_required: true
    - endpoint: /api/v1/auth/login
      change: "新增device_info字段"
      migration_required: false
  migration_timeline:
    deprecation_date: "2025-12-01"
    removal_date: "2026-03-01"
    migration_support: "2025-12-01 to 2026-03-01"
```

## 契约测试

### 契约验证测试
```yaml
contract_tests:
  - name: UserLoginContractTest
    contract: UserLoginContract
    test_cases:
      - name: ValidLoginTest
        input:
          username: "test@example.com"
          password: "password123"
        expected_output:
          status_code: 200
          data.access_token: not_null
          data.refresh_token: not_null
      - name: InvalidPasswordTest
        input:
          username: "test@example.com"
          password: "wrongpassword"
        expected_output:
          status_code: 401
          error_code: INVALID_CREDENTIALS
```

### 性能测试契约
```yaml
performance_tests:
  - name: TriageServiceLoadTest
    contract: ProcessMessageContract
    test_config:
      concurrent_users: 50
      duration: 300s
      ramp_up_time: 60s
    success_criteria:
      avg_response_time: <= 5s
      p95_response_time: <= 8s
      error_rate: <= 1%
```

> 📝 **文档状态**: 文档已搭建，等待后续设计完善
