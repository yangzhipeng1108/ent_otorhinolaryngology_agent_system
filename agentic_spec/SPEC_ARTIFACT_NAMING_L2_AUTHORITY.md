# SPEC 命名规范 L2 级权威定义

> **🎯 文档定位**: L2-BALANCED 级别命名执行要求的唯一权威定义源
> **🔑 核心对象**: 本级别命名针对 **Artifact (制品)** - 软件开发过程中产生的可追溯文档化实体
> **📋 核心价值**: 定义全量命名和完整追溯链的详细执行要求，为团队协作和商业项目提供标准化流程
> **🔗 引用依赖**:
> - 核心概念定义见 `SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md`
> - 遵循 SOLID 原则: 本文档只定义 L2 级执行要求，不重复核心概念

---

## 1. L2 级别定位概要

### 1.1 L2 命名对象说明

L2 级别命名的核心对象是 **Artifact**（制品）- 软件开发过程中产生的文档化实体。

**必须命名的 Artifacts (8个核心artifacts)**:

按生产阶段顺序排列：

| PREFIX | 名称 | 生产阶段 | 作用 | 示例 ID |
|--------|------|---------|------|--------|
| **US** | User Story | REQUIREMENTS | 团队协作标准需求格式，角色-功能-价值描述 | `US-AUTH-002` |
| **AC** | Acceptance Criteria | REQUIREMENTS | 验收标准，明确需求的可测试边界 | `AC-AUTH-005` |
| **FP** | Function Point | DESIGN | 从需求到设计的桥梁，标准功能点转化 | `FP-AUTH-025` |
| **SC** | BDD Scenario | IMPLEMENTATION | BDD测试场景，验证功能点的价值实现 | `SC-AUTH-030` |
| **TS** | Test Suite | IMPLEMENTATION | 测试套件，TDD策略的实施单元 | `TS-AUTH-035` |
| **SEQ** | Task Sequence | TASK_PLANNING | 任务序列，支持团队协作的开发任务编排 | `SEQ-AUTH-050` |
| **GOAL** | Goal | TASK_PLANNING | 声明式执行目标，统一的执行锚点（记录于 `spec/task_planning/goal_breakdown.md`） | `GOAL-AUTH-070` |
| **CTX** | AI Context | TASK_PLANNING | AI上下文，支撑AI执行的统一约束 | `CTX-AUTH-085` |

> **CTX 范围选择**: L2 CTX 可以描述整个团队共用的执行语境，也可以针对特定场景建立局部上下文；无论采取何种策略，每条投入执行的任务序列 `SEQ` 都必须映射到可用的 CTX。

**推荐命名的 Artifacts (15个)**: 构成完整追溯网，详见 Section 3.2

**追溯架构**:
- **核心派生链**: `US → FP (功能点) → SC (场景)` - 端到端派生链
- **验证层**: `AC (验收)` - 验证US (通过source_us)
- **组织层**: `TS (组织SC), SEQ (编排FP), GOAL (声明式目标锚点)` - 横向组织与执行桥接

### 1.2 适用场景

**适用场景**:
- ✅ 标准商业项目、生产环境应用
- ✅ 团队协作 3+ 人、长期维护项目
- ✅ 多功能模块项目 (需要 SN 分组)

**不适用场景**:
- ❌ 快速原型 / POC (过度严格)
- ❌ 关键系统 / 高合规项目 (不够严格)

### 1.3 核心特征

- ✅ 强制8个核心追溯链 artifacts (US/AC/FP/SC/TS/SEQ/GOAL/CTX)
- ✅ 推荐15个补充 artifacts (支持完整追溯网)
- ✅ Front Matter 完整: `id`, `sn`, `status`, `source_*`, `related_*`
- ✅ 双向追溯网 (source单向 + related多向)
- ✅ SN 必须包含 (禁止省略)

---

## 2. 强制要求

### 2.1 必填 Artifacts (核心追溯链)

按生产阶段顺序排列：

| Artifact | PREFIX | 生产阶段 | Front Matter 必填字段 | 说明 |
|----------|--------|---------|---------------------|------|
| User Story | `US` | REQUIREMENTS | `id`, `sn`, `status`, `related_ac`/`related_fp`(至少1个) | 团队协作核心需求定义,必须建立下游关联 |
| Acceptance Criteria | `AC` | REQUIREMENTS | `id`, `sn`, `status`, `source_us` | 验收标准,必须追溯到US |
| Function Point | `FP` | DESIGN | `id`, `sn`, `status`, `source_us`, `related_*`(至少1个) | 功能点,US到实现的桥梁,必须有横向关联 |
| BDD Scenario | `SC` | IMPLEMENTATION | `id`, `sn`, `status`, `source_fp`, `related_us`/`related_ts`(至少1个) | 测试场景,必须追溯到FP并建立横向关联 |
| Test Suite | `TS` | IMPLEMENTATION | `id`, `sn`, `status`, `related_sc` | 测试套件,组织SC |
| Task Sequence | `SEQ` | TASK_PLANNING | `id`, `sn`, `status`, `related_fp` | 任务序列,关联FP |
| AI Context | `CTX` | TASK_PLANNING | `id`, `sn`, `status`, `related_seq` | AI上下文,绑定任务序列为AI提供执行约束 |
| Goal | `GOAL` | TASK_PLANNING | `id`, `sn`, `status`, `source_us`, `related_sc`, `related_seq` | 声明式目标，串联执行与验证 |

### 2.2 Front Matter 必填规范

**ID管理要求**:
- 遵循`SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md`中的"ID永久占用原则"和"扫描分配机制"
- 严禁复用已生成的artifact IDs，L2双向追溯网中必须保持引用完整性

| 字段 | 格式 | 示例 | 规则 |
|------|------|------|------|
| `id` | `<PREFIX>-<SN>-NNN` | `US-AUTH-002`, `FP-PAY-025` | 2-4位PREFIX + 2-6位SN + 3位序号 |
| `sn` | `[A-Z]{2,6}` | `AUTH`, `PAY`, `MAIN` | 全大写字母,不可省略 |
| `status` | 枚举值 | `active`, `draft`, `deprecated` | 所有artifacts必填 |
| `source_*` | `<PREFIX>-<SN>-XXX` | `source_us: US-AUTH-002` | 指向直接上游artifact |
| `related_*` | 列表 | `related_fp: [FP-AUTH-025]` | 指向相关artifacts |

**必填 Artifacts 示例** (L2核心8个artifacts):

**US (User Story)** - 必填字段: `id` + `sn` + `status` + 指定派生字段（详见 3.2.2） + `status` + `related_ac`/`related_fp`(至少1个)
```yaml
---
id: US-AUTH-002
sn: AUTH
status: active
related_ac: [AC-AUTH-005, AC-AUTH-006]
related_fp: [FP-AUTH-025]
---
```

**AC (Acceptance Criteria)** - 必填字段: `id` + `sn` + `status` + `source_us`
```yaml
---
id: AC-AUTH-005
sn: AUTH
status: active
source_us: US-AUTH-002
---
```

**FP (Function Point)** - 必填字段: `id` + `sn` + `status` + `source_us` + `related_*`(至少1个)
```yaml
---
id: FP-AUTH-025
sn: AUTH
status: active
source_us: US-AUTH-002
related_sc: [SC-AUTH-030, SC-AUTH-031]
related_seq: [SEQ-AUTH-050]
---
```

**SC (BDD Scenario)** - 必填字段: `id` + `sn` + `status` + `source_fp` + `related_us`/`related_ts`(至少1个)
```yaml
---
id: SC-AUTH-030
sn: AUTH
status: active
source_fp: FP-AUTH-025
related_ts: [TS-AUTH-035]
related_us: [US-AUTH-002]
---
```

**TS (Test Suite)** - 必填字段: `id` + `sn` + `status` + `related_sc`
```yaml
---
id: TS-AUTH-035
sn: AUTH
status: active
related_sc: [SC-AUTH-030, SC-AUTH-031]
---
```

**SEQ (Task Sequence)** - 必填字段: `id` + `sn` + `status` + `related_fp`
```yaml
---
id: SEQ-AUTH-050
sn: AUTH
status: active
related_fp: [FP-AUTH-025]
---
```

**CTX (AI Context)** - 必填字段: `id` + `sn` + `status` + `related_seq`
```yaml
---
id: CTX-AUTH-085
sn: AUTH
status: active
related_seq: [SEQ-AUTH-050]
related_fp: [FP-AUTH-025]  # 推荐，绑定关键功能点
---
```

**GOAL (Goal)** - 必填字段: `id` + `sn` + `status` + `source_us` + `related_sc` + `related_seq`
```yaml
---
id: GOAL-AUTH-070
sn: AUTH
status: active
source_us: US-AUTH-002
related_sc: [SC-AUTH-030]
related_seq: [SEQ-AUTH-050]
context_refs: [CTX-AUTH-085]
---
```

### 2.3 SN (Story Namespace) 规则

| 要求类型 | 规则 | 示例 |
|---------|------|------|
| **禁止省略** | 所有ID必须包含SN | ✅ `US-MAIN-002` ❌ `US-002` |
| **单域项目** | 可用`MAIN`或`CORE`作为默认SN | `US-MAIN-002`, `FP-CORE-025` |
| **多域项目** | 按业务域定义SN | `AUTH`, `PAY`, `CART` |

### 2.4 FP (Function Point) 粒度定义标准

**核心定位**: FP 是 L2 关键 artifact，作为"US 到实现的桥梁"，粒度直接影响开发效率。

**粒度原则** (4个核心标准):

1. **功能完整性**: FP 有明确的输入、处理逻辑、输出，能独立提供价值
2. **可测试性**: FP 能映射到 1-3 个 BDD Scenario (`SC`)
3. **开发粒度**: FP 应为适中复杂度，既不过于琐碎也不需要拆分子任务
4. **单一职责**: FP 有明确的单一职责和边界

**粒度判断示例**:

| 判断 | FP 示例 | 说明 |
|------|---------|------|
| ✅ **合适** | `FP-AUTH-025 用户登录验证` | 包含验证、Session生成、返回Token，复杂度适中 |
| ❌ **过大** | `FP-AUTH-001 整个认证系统` | 包含登录/注册/权限等，应拆分为多个FP |
| ❌ **过小** | `FP-AUTH-030 检查密码长度` | 只是验证的一部分，应合并到登录验证 |


---

## 3. 灵活空间

### 3.1 正文标题格式

**灵活性**: front matter 的 `id` 字段才是权威标识，正文标题可以：
- 包含完整ID: `## US-AUTH-002 用户登录功能`
- 或简化描述: `## 用户登录功能`

**约束**: 如果正文包含ID，必须与 front matter 的 `id` 一致

### 3.2 其他 Artifacts 命名

**推荐命名的 artifacts**:

> 🧭 **GOAL 注册表指引**: GOAL front matter 必须集中维护在 `spec/task_planning/goal_breakdown.md`；其他文档仅引用 GOAL ID，不得重复定义。

#### 3.2.1 推荐 Artifacts 使用优先级

**优先级原则**: 根据项目需要选择，不强制全部使用

**高优先级** (常用场景):
- **Requirements阶段**: CN (有约束需求), IFR (有集成需求)
- **Design阶段**: API (前后端分离), DM (有数据存储), ADR (重大决策)
- **Implementation阶段**: TD (复杂测试数据), QD (明确质量标准)
- **Task Planning阶段**: BLK (识别风险) —— CTX 为核心必填 artifact

**中优先级** (特定场景):
- **Design阶段**: CMP (模块化架构), DES (重大设计), IFS (严格契约), INT (集成方案)
- **Implementation阶段**: IO (复杂编排)
- **Task Planning阶段**: COORD (多人协作)

#### 3.2.2 推荐 Artifacts 详细清单

##### Requirements 阶段 (2个)

- **CN (Constraint Specification)**: 约束规格，定义系统边界和限制
  - **推荐托管**: `[constraint_spec_file]`
  - **关系**: 从 US 派生约束条件
  - **Front Matter 必填**: id/sn/status + `source_us`
  - **适用**: 需要明确技术约束、业务规则、合规要求时使用
  - **示例**: `CN-AUTH-010` (登录安全约束规格)

- **IFR (Interface Requirement)**: 接口需求，定义系统间集成要求
  - **推荐托管**: `[interface_requirements_file]`
  - **关系**: 从 US 衍生的集成需求
  - **Front Matter 必填**: id/sn/status + `source_us`
  - **适用**: 多系统集成、第三方对接时使用
  - **示例**: `IFR-AUTH-020` (SSO集成接口需求)

##### Design 阶段 (7个)

- **DM (Data Model)**: 数据模型定义，指导数据库设计
  - **推荐托管**: `[data_model_file]`
  - **关系**: 从 US/FP 转化而来
  - **Front Matter 必填**: id/sn/status + `source_fp`（若 FP 暂缺可临时使用 `source_us` 占位，完成后须回写）
  - **适用**: 有数据存储需求，或需要明确实体关系时使用
  - **示例**: `DM-AUTH-030` (用户数据模型)

- **API (API Spec)**: 接口契约定义，支持前后端分离开发
  - **推荐托管**: `[api_design_file]`
  - **关系**: 从 FP 转化的API设计
  - **Front Matter 必填**: id/sn/status + `source_fp`
  - **适用**: 前后端分离、微服务架构、或需要接口文档时使用
  - **示例**: `API-AUTH-035` (登录接口规格)

- **CMP (Component Specification)**: 系统组件规格定义，指导架构设计（前端GUI组件包含逻辑+视觉混合规格）
  - **推荐托管**: `[component_design_file]`
  - **关系**: 从多个 FP 组织而来
  - **Front Matter 必填**: id/sn/status + `related_fp`（至少1个）
  - **适用**: 系统有明确的模块化需求时使用
  - **示例**: `CMP-AUTH-040` (认证组件规格)

- **DES (Design Document)**: 设计决策文档，记录架构选择
  - **推荐托管**: `[design_documentation_file]`
  - **关系**: 覆盖多个 FP 的设计方案
  - **Front Matter 必填**: id/sn/status + `related_fp`（列表）
  - **适用**: 需要记录重大设计决策、技术选型时使用
  - **示例**: `DES-AUTH-045` (认证架构设计)

- **INT (Integration)**: 集成设计，定义系统集成方案
  - **推荐托管**: `[integration_design_file]`
  - **关系**: 从 IFR 接口需求转化
  - **Front Matter 必填**: id/sn/status + `source_ifr`
  - **适用**: 多系统集成、消息队列、事件驱动架构时使用
  - **示例**: `INT-AUTH-050` (SSO集成设计)

- **IFS (Interface Specification)**: 接口规格，详细接口契约
  - **推荐托管**: `[interface_spec_file]`
  - **关系**: API 的详细规格扩展，从 IFR 需求转化
  - **Front Matter 必填**: id/sn/status + `source_ifr`（可选补充 `related_api`）
  - **适用**: 需要严格接口契约定义时使用（L2推荐，L3强制）
  - **示例**: `IFS-AUTH-055` (登录接口契约)

- **ADR (Architecture Decision Record)**: 架构决策记录，记录重大技术选择
  - **推荐托管**: `[adr_file]`
  - **关系**: 从 DES 衍生的决策记录，横向关联设计文档
  - **Front Matter 必填**: id/sn/status + `source_des` + `related_fp`（至少1个）
  - **适用**: 需要记录架构决策的理由、备选方案、影响分析时使用（L2推荐，L3必填）
  - **示例**: `ADR-AUTH-060` (JWT认证方案决策记录)
  - **格式**: 遵循 Context-Decision-Consequences 标准模板

**API vs IFS 区分说明**:

| 维度 | API (API Specification) | IFS (Interface Specification) |
|------|------------------------|------------------------------|
| **定位** | 应用程序编程接口 (HTTP/RPC) | 系统间集成协议规格 |
| **适用** | REST API, GraphQL, gRPC | 消息队列、事件总线、第三方对接 |
| **详细程度** | 接口级 (路径/方法/参数/响应) | 协议级 (消息格式/状态机/错误处理) |
| **来源** | 从 FP 转化 | 从 IFR 转化 |
| **示例** | `API-AUTH-035 POST /api/v1/login` | `IFS-PAY-055 支付成功事件发布协议` |

**使用决策**:
- **用 API**: 前后端分离 HTTP 接口、微服务 RPC
- **用 IFS**: 系统集成协议、消息队列事件、第三方对接
- **L2 策略**: 默认用 API，复杂集成场景用 IFS

##### Implementation 阶段 (4个)

- **TD (Test Data)**: 测试数据定义，支持测试执行
  - **推荐托管**: `[test_data_file]`
  - **关系**: 从 SC 衍生的测试数据需求
  - **Front Matter 必填**: id/sn/status + `source_sc`
  - **适用**: 需要标准测试数据集、或复杂数据准备时使用
  - **示例**: `TD-AUTH-060` (登录测试数据)

- **QD (Quality Definition)**: 质量定义，明确质量标准
  - **推荐托管**: `[quality_definition_file]`
  - **关系**: 从 AC 衍生的质量要求
  - **Front Matter 必填**: id/sn/status + `source_ac`
  - **适用**: 需要明确性能、安全、可用性等质量标准时使用
  - **示例**: `QD-AUTH-065` (登录响应时间要求)

- **IO (Integration Orchestration)**: 集成编排，定义集成执行逻辑
  - **推荐托管**: `[integration_orchestration_file]`
  - **关系**: 从 INT 设计实施
  - **Front Matter 必填**: id/sn/status + `source_int`
  - **适用**: 复杂集成场景、服务编排时使用
  - **示例**: `IO-AUTH-075` (SSO集成编排)

##### Task Planning 阶段 (2个推荐)

Task Planning 阶段核心 artifacts (SEQ + CTX) 已纳入必填，以下为补充项：

- **BLK (Blocker Issue)**: 阻塞问题，识别开发风险
  - **推荐托管**: `[blocker_anticipation_file]`
  - **关系**: 从 SEQ 识别的阻塞任务
  - **Front Matter 必填**: id/sn/status + `source_seq`
  - **适用**: 需要明确风险管理、阻塞识别时使用
  - **示例**: `BLK-AUTH-080` (第三方依赖阻塞问题)

- **COORD (Coordination)**: 协调规格，定义团队协作接口
  - **推荐托管**: `[coordination_file]`
  - **关系**: 多个 SEQ 之间的协调关系
  - **Front Matter 必填**: id/sn/status + `related_seq`（至少1个）
  - **适用**: 多人协作、并行开发时使用
  - **示例**: `COORD-AUTH-090` (前后端协调规格)

> **CTX 生产提示**: 若一个 CTX 服务多个 SEQ，请在 CTX 正文中明示共享边界；如某条价值流需要额外的执行 guardrail，应为对应 `SEQ` 单独生成 CTX，保持 `related_seq` 单值约束。

**Front Matter 最小要求**: 所有推荐 artifacts 必须包含 `id` + `sn` + `status`，并按下方规定补齐派生字段；缺失指定的 `source_*`/`related_*` 视为未建立追溯链。

**策略**: 这些 artifacts 构成 L2 完整追溯网，根据项目需要选择性命名

#### 3.2.3 推荐 Artifacts Front Matter 示例

**CN (Constraint Specification)** - Requirements阶段
```yaml
---
id: CN-AUTH-010
sn: AUTH
status: active
source_us: US-AUTH-002
---
```

**API (API Specification)** - Design阶段
```yaml
---
id: API-AUTH-035
sn: AUTH
status: active
source_fp: FP-AUTH-025
related_us: [US-AUTH-002]
---
```

**TD (Test Data)** - Implementation阶段
```yaml
---
id: TD-AUTH-060
sn: AUTH
status: active
source_sc: SC-AUTH-030
---
```

**CTX (AI Context)** - Task Planning阶段
```yaml
---
id: CTX-AUTH-085
sn: AUTH
status: active
related_seq: [SEQ-AUTH-050]
related_fp: [FP-AUTH-025]
---
```

### 3.3 追溯链字段

**核心原则**: L2使用双向追溯网（source派生链 + related组织网）

**追溯字段分类**:

**派生型artifacts (使用source_*)**:
| Artifact类型 | 生产阶段 | source_* | related_* | 说明 |
|-------------|---------|----------|-----------|------|
| User Story (US) | REQUIREMENTS | 无 (起点) | `related_ac` / `related_fp` **(至少1个必须)** | 需求起点，必须关联下游AC或FP建立双向网 |
| Acceptance Criteria (AC) | REQUIREMENTS | `source_us` **(必须)** | `related_fp` (推荐), `related_sc` (推荐) | 验收标准,必须追溯到US |
| Function Point (FP) | DESIGN | `source_us` **(必须)** | **(至少1个必须)**: `related_ac` (推荐), `related_sc` (推荐), `related_seq` (推荐) | 从US转化的功能点，必须有横向关联 |
| BDD Scenario (SC) | IMPLEMENTATION | `source_fp` **(必须)** | `related_us` / `related_ts` **(至少1个必须)** | 从FP派生的测试场景，必须建立横向追溯 |

**组织型artifacts (使用related_*)**:
| Artifact类型 | 生产阶段 | source_* | related_* (至少1个) | 说明 |
|-------------|---------|----------|-------------------|------|
| Test Suite (TS) | IMPLEMENTATION | 无 | `related_sc` **(必须)** | 组织多个SC的测试套件 |
| Task Sequence (SEQ) | TASK_PLANNING | 无 | `related_fp` **(必须)** | 编排多个FP的任务序列 |
| AI Context (CTX) | TASK_PLANNING | 无 | `related_seq` **(必须)** | 为任务序列配置AI上下文，推荐补充`related_fp` |

**职责说明**:
- **派生型**: 从上游artifact派生，继承需求/设计意图，用`source_*`建立单向链
- **组织型**: 横向组织同类artifacts，支持批量管理，用`related_*`建立多向网

**Front Matter 最小要求**: 
- 派生型: `id` + `sn` + `status` + `source_*` (必须)
- 组织型: `id` + `sn` + `status` + `related_*` (必须)，其中 CTX 必须提供 `related_seq`，`related_fp` 推荐补充

**策略**: 这些 artifacts 构成 L2 完整追溯网，根据项目需要选择性命名

### 3.4 禁止行为

| 禁止内容 | 说明 |
|---------|------|
| ❌ **缺少Front Matter** | 核心8个artifacts必须有`id`+`sn`+`status`+追溯字段 |
| ❌ **追溯链断裂** | 核心追溯链artifacts必须有正确的`source_*`或`related_*` |
| ❌ **省略SN** | 禁止`US-001`格式,必须`US-<SN>-001` |
| ❌ **source多值** | `source_*`只能指向单个上游，禁止列表 |

---

## 4. 使用建议和场景指导

### 4.1 推荐Artifacts配置策略

L2 级别共有15个推荐 artifacts。基于L1基础配置策略，建议按以下优先级选择性使用：

| 优先级 | Artifacts | 适用场景 | Front Matter 最小要求 |
|--------|-----------|---------|---------------------|
| **P0** (测试套件) | **TS** | 使用 TDD/BDD 开发方式，需要测试套件管理 | `id` + `sn` + `status` + `source_sc` |
| **P1** (设计追溯) | **FP**, **API**, **DM**, **CMP** | 前后端分离、模块化项目、有数据模型需求 | `id` + `sn` + `status` + 指定派生字段（详见 3.2.2） |
| **P2** (任务管理) | **BLK** | 任务间依赖复杂、有已知风险点、需要任务序列管理 | `id` + `sn` + `status` + `source_seq` |

**优先级说明**:
- **P0**: 测试套件管理，支持完整 TDD 工作流
- **P1**: 设计文档化，支持前后端协作和架构清晰度（L2核心必填artifacts）
- **P2**: 任务编排，解决复杂依赖和风险管理
- **P3**: AI 协作工具，提升 AI 辅助开发效果

**使用建议**:
- **最小集**: 核心8个 (US/AC/FP/SC/TS/SEQ/GOAL/CTX)，L2标准配置
- **标准集**: 核心8个 + P1 (API/DM/CMP)，支持设计追溯
- **完整集**: 核心8个 + P1 + P2，支持任务管理和风险控制
- **全量集**: 核心8个 + 全部15个推荐 artifacts，充分利用所有补充 artifacts

### 4.2 典型项目场景示例

1. **快速原型项目**:
   - 使用: 核心8个 (US/AC/FP/SC/TS/SEQ/GOAL/CTX)
   - 理由: L2最小追溯链，支持 AI 执行和 TDD 验证

2. **前后端分离项目**:
   - 使用: 核心8个 + API + DM + CMP
   - 理由: 增加接口契约、数据模型和组件规格

3. **AI 辅助开发项目**:
   - 使用: 核心8个 + API + DM (P1) + BLK (P2) + COORD (中优先级)
   - 理由: 在统一 AI 上下文基础上，加强设计追溯、风险治理与协作接口

### 4.3 软件架构复杂度配置

根据软件架构复杂度，建议以下分层配置策略：

**单体架构配置**:
- 使用: 核心8个 + API + DM
- 适用: 简单接口和数据模型，集中式部署

**分层架构配置**:
- 使用: 核心8个 + CMP + API + DM
- 适用: 组件分层清晰，职责分离明确

**微服务架构配置**:
- 使用: 核心8个 + CMP + API + INT + IFS
- 适用: 服务间集成，分布式通信协议

**分布式系统配置**:
- 使用: 核心8个 + 高优先级推荐artifacts (CN + API + DM + CMP + INT + IFS + TD + QD)
- 适用: 复杂系统间协作，需要完整追溯网

### 4.4 AI Coding协作模式

根据AI协作复杂度，建议以下配置模式：

**单AI开发模式**:
- 使用: 核心8个 + API + DM
- 适用: 基础AI协作，单一AI Agent执行

**多AI协作模式**:
- 使用: 核心8个 + CMP + DES + COORD
- 适用: AI间协调，复杂任务分工

**持续集成模式**:
- 使用: 核心8个 + TD + QD + IO
- 适用: 自动化集成，质量门禁控制

---

## 5. 生产次序指导

### 5.1 端到端次序概览

**L2完整生产次序**：
```
US → AC → FP → SC → TS → SEQ → CTX
(REQUIREMENTS) (DESIGN) (IMPLEMENTATION) (TASK_PLANNING)
```

> **执行一致性**: 任何被投入执行的价值流都必须在生成 `SEQ` 之后立即落地 CTX；若团队选择复用共享 CTX，应确保所有关联的 `SEQ` 均已登记至该 CTX 的 `related_seq` 列表。

**阶段内次序**：

#### REQUIREMENTS 阶段
- **核心次序**: US → AC（必须严格串行）
- **推荐 artifacts**（如使用）: US → AC → CN/IFR

#### DESIGN 阶段  
- **核心次序**: FP（必须首先，其他都依赖FP）
- **推荐 artifacts**（如使用）: FP → API/DM/CMP → DES/INT/IFS → ADR

#### IMPLEMENTATION 阶段
- **核心次序**: SC → TS（严格串行，TS依赖SC）
- **推荐 artifacts**（如使用）: SC/TS → TD/QD

#### TASK_PLANNING 阶段
- **核心次序**: SEQ → CTX（串行，CTX 依赖 SEQ）
- **推荐 artifacts**（如使用）: CTX/SEQ → BLK → COORD

### 5.2 双网结构约束

**派生链（source_*）必须先于组织网（related_*）**：

| 依赖类型 | 约束规则 | 示例 |
|----------|----------|------|
| **派生链** | source_* 字段的父 artifact 必须先存在 | SC 依赖 FP，FP 必须先生产 |
| **组织网** | related_* 字段的被引用 artifacts 必须先存在 | TS 引用 SC，SC 必须先生产 |

**核心串行约束**：
- AC 必须在 US 之后（source_us 依赖）
- FP 必须在 US 之后（source_us 依赖）
- SC 必须在 FP 之后（source_fp 依赖）
- TS 必须在 SC 之后（related_sc 依赖）
- SEQ 必须在 FP 之后（related_fp 依赖）
- CTX 必须在 SEQ 之后（related_seq 依赖）

### 5.3 生产次序价值

**双网结构保障**：派生链（source_us/source_fp）先于组织网（related_sc/related_fp/related_seq）

**串行次序约束**：当前 AI Coding 平台限制，必须串行生产

**方法论纪律**：价值层（US）→ 设计层（FP）→ 测试层（SC）→ 编排层（TS/SEQ）→ 上下文层（CTX）的渐进路径

---

## 6. 验收标准

### 6.1 最低要求 (必须满足)

- [ ] **核心8个artifacts命名完整**
  - US, AC, FP, SC, TS, SEQ, CTX 都有 `id` + `sn` + `status`
  - front matter 格式正确

- [ ] **核心追溯链可用 (派生链)**
  - AC 有 `source_us` 指向有效US
  - FP 有 `source_us` 指向有效US
  - SC 有 `source_fp` 指向有效FP
  - 能通过source字段追踪完整派生链路

- [ ] **组织层基本建立 (横向网)**
  - TS 有 `related_sc` 指向至少1个SC
  - SEQ 有 `related_fp` 指向至少1个FP
  - CTX 有 `related_seq` 指向至少1个SEQ
  - 组织型artifacts正确使用related字段
  - 如 CTX 为共享上下文，正文需声明覆盖的 `SEQ` 列表及共享准则

- [ ] **双向引用网基本建立**
  - US 有 `related_ac` 或 `related_fp`
  - FP 有至少一个 `related_*` 字段
  - SC 有 `related_ts` 或 `related_us`

### 6.2 推荐标准 (建议满足)

**推荐 artifacts 命名完整性**:
- [ ] **Requirements 阶段推荐 artifacts 有命名**
  - CN (Constraint Specification) 有 `id` + `sn` + `status`
  - IFR (Interface Requirement) 有 `id` + `sn` + `status`
  
- [ ] **Design 阶段推荐 artifacts 有命名**
  - DM (Data Model) 有 `id` + `sn` + `status`
  - API (API Spec) 有 `id` + `sn` + `status`
  - CMP (Component Specification) 有 `id` + `sn` + `status`
  - DES (Design Document) 有 `id` + `sn` + `status`
  - INT (Integration) 有 `id` + `sn` + `status`
  - IFS (Interface Specification) 有 `id` + `sn` + `status`
  - ADR (Architecture Decision Record) 有 `id` + `sn` + `status`
  
- [ ] **Implementation 阶段推荐 artifacts 有命名**
  - TD (Test Data) 有 `id` + `sn` + `status`
  - QD (Quality Definition) 有 `id` + `sn` + `status`
  - GOAL (Goal) 有 `id` + `sn` + `status`
  - IO (Integration Orchestration) 有 `id` + `sn` + `status`
  
- [ ] **Task Planning 阶段推荐 artifacts 有命名**
  - BLK (Blocker Issue) 有 `id` + `sn` + `status`
  - COORD (Coordination) 有 `id` + `sn` + `status`

**完整追溯网建立**:
- [ ] **核心派生链完整**
  - US → FP → SC 派生链路完整
  - AC 验证 US (通过source_us)
  - 派生型artifacts都有正确的 `source_*`
  
- [ ] **组织层完整**
  - TS 正确组织 SC (通过`related_sc`)
  - SEQ 正确编排 FP (通过`related_fp`)
  - 组织型artifacts都有正确的 `related_*`
  
- [ ] **横向关联充分**
  - FP 关联 AC、SC、SEQ
  - SC 关联 US、TS
  - 推荐 artifacts 与核心链有关联
  
- [ ] **追溯网可查询**
  - 从 US 可追溯到所有下游 artifacts
  - 从 SC 可回溯到 US 和 FP
  - 支持按 SN 过滤特定业务域

**SN 定义一致性**:
- [ ] **SN 已定义并保持一致**
  - 单域项目: 使用 `MAIN` 或 `CORE` 作为默认 SN
  - 多域项目: 定义 3-7 个业务域 SN (如 `AUTH`, `PAY`, `CART`)
  
- [ ] **所有 artifacts 使用一致的 SN 命名**
  - 同一业务域的 artifacts 使用相同 SN
  - 避免 SN 混乱或不一致

---
