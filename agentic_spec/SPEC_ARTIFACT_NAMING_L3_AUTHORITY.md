# SPEC 命名规范 L3 级权威定义

> **🎯 文档定位**: L3-RIGOROUS 级别命名执行要求的唯一权威定义源
> **🔑 核心对象**: 本级别命名针对 **Artifact (制品)** - 软件开发过程中产生的可追溯文档化实体
> **📋 核心价值**: 定义审计级命名的详细执行要求，为关键系统和高合规项目提供完整追溯和审计能力
> **🔗 引用依赖**:
> - 核心概念定义见 `SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md`
> - 遵循 SOLID 原则: 本文档只定义 L3 级执行要求，不重复核心概念

---

## 1. L3 级别定位概要

### 1.1 L3 命名对象说明

L3 级别命名的核心对象是 **Artifact**（制品）- 软件开发过程中产生的可追溯文档化实体。

**必须命名的 Artifacts (14个审计级核心artifacts)**:

按生产阶段顺序排列：

| PREFIX | 名称 | 生产阶段 | 作用 | 示例 ID |
|--------|------|---------|------|--------|
| **US** | User Story | REQUIREMENTS | 需求标准格式，支持严格 INVEST 评价 | `US-AUTH-002` |
| **AC** | Acceptance Criteria | REQUIREMENTS | 验收标准，严格 Given-When-Then 格式 | `AC-AUTH-005` |
| **DES** | Design Document | DESIGN | 架构设计决策，Layer-first 原则 | `DES-AUTH-010` |
| **CMP** | Component Specification | DESIGN | 组件规格，严格边界定义（GUI组件含逻辑+视觉） | `CMP-AUTH-015` |
| **API** | API Specification | DESIGN | 接口规格，Contract-first 设计 | `API-AUTH-020` |
| **ADR** | Architecture Decision Record | DESIGN | 架构决策记录，支持审计 | `ADR-AUTH-025` |
| **SC** | BDD Scenario | IMPLEMENTATION | 测试场景，严格 Gherkin 语法 | `SC-AUTH-030` |
| **TS** | Test Suite | IMPLEMENTATION | 测试套件，测试金字塔组织 | `TS-AUTH-035` |
| **SEQ** | Task Sequence | TASK_PLANNING | 任务序列，支持团队协作 | `SEQ-AUTH-040` |
| **GOAL** | Goal | TASK_PLANNING | 声明式目标，审计级执行锚点（记录于 `spec/task_planning/goal_breakdown.md`） | `GOAL-AUTH-070` |
| **CTX** | AI Context | TASK_PLANNING | AI上下文，提供审计级执行约束 | `CTX-AUTH-085` |
| **BLK** | Blocker Issue | TASK_PLANNING | 阻塞问题，风险识别 | `BLK-AUTH-045` |
| **AUD** | Audit Log | 审计层 (跨阶段) | 审计记录，合规追踪 | `AUD-AUTH-050` |
| **TR** | Traceability Matrix | 审计层 (跨阶段) | 追溯矩阵，Release 级可视化 | `TR-AUTH-R1.0` |

> **CTX 范围选择**: L3 CTX 可以代表整个项目的审计级执行语境，或针对关键价值流单独设立；无论采取共享或专属模式，每条列入发布计划的 `SEQ` 都必须在 CTX 中登记，以确保可审计的上下文链路。

**推荐命名的 Artifacts (6个)**: 支持完整审计体系，详见 Section 4.2

**核心追溯架构**:
- **派生链**: `US → DES (架构) → CMP (组件)` / `US → DES → API (接口)` / `DES → SC (场景)` - 端到端派生链
- **验证层**: `AC (验收)` - 验证US (通过source_us)
- **横向关联**: `ADR (决策)` ↔ `DES (设计)` - 双向追溯 (related_adr/related_des)
- **组织层**: `TS (组织SC)`, `SEQ (编排任务)`, `GOAL (执行锚点)`, `BLK (识别风险)` - 横向组织与执行桥接
- **审计层**: `AUD (审计记录)`, `TR (追溯矩阵)` - 全局追溯


### 1.2 适用场景

**适用场景**:
- ✅ 关键系统 (金融支付、医疗健康、基础设施)
- ✅ 高合规审计项目 (ISO 9001、CMMI Level 3+、SOX)
- ✅ 低容错系统 (故障影响大、修复成本高)

**⚠️ 重要**: L3 不等于"大型企业"，决策标准是**审计要求**和**风险承受能力**

**不适用场景**:
- ❌ 快速原型 / POC (过度严格)
- ❌ 标准商业应用 (推荐使用 L2)

### 1.3 核心特征

- ✅ 强制 14 个审计级核心 artifacts (US/AC/DES/CMP/API/ADR/SC/TS/SEQ/GOAL/CTX/BLK/AUD/TR)
- ✅ 推荐 6 个补充 artifacts (支持完整审计体系)
- ✅ Front Matter 完整: `id`, `sn`, `status`, `owner`, `version`, `source_*`, `related_*`
- ✅ 完整追溯链 (所有核心 artifacts 必须有追溯字段)
- ✅ 审计记录 (AUD): 所有关键决策有记录
- ✅ 追溯矩阵 (TR): 每 Release 自动生成 (CSV + DOT + Markdown)
- ✅ 版本管理: 所有 artifact 必填 `version`
- ✅ ADR 决策记录: 所有架构决策形式化记录
- ✅ CI/CD 门禁: 违规自动阻塞
- ✅ 正文格式统一: 强制完整 ID

---

## 2. 强制要求

### 2.1 必填 Artifacts (审计级核心链)

**说明**: L3 要求14个核心 artifacts 必须命名，确保完整审计追溯链。

按生产阶段顺序排列：

| Artifact | PREFIX | 生产阶段 | Front Matter 必填字段 | 说明 |
|----------|--------|---------|---------------------|------|
| User Story | `US` | REQUIREMENTS | `id`, `sn`, `status`, `owner`, `version`, `related_ac`/`related_des`(至少1个) | 需求核心定义，支持INVEST评价，必须建立下游关联 |
| Acceptance Criteria | `AC` | REQUIREMENTS | `id`, `sn`, `status`, `owner`, `version`, `source_us`, `related_des`/`related_sc`(至少1个) | 验收标准，严格Given-When-Then格式，必须建立横向追溯 |
| Design Document | `DES` | DESIGN | `id`, `sn`, `status`, `owner`, `version`, `source_us`, `related_adr` | 架构设计，Layer-first原则 |
| Component Specification | `CMP` | DESIGN | `id`, `sn`, `status`, `owner`, `version`, `source_des`, `related_api` | 组件规格，严格边界定义（GUI组件含逻辑+视觉） |
| API Specification | `API` | DESIGN | `id`, `sn`, `status`, `owner`, `version`, `source_des`, `related_cmp` | 接口规格，Contract-first设计 |
| Architecture Decision Record | `ADR` | DESIGN | `id`, `sn`, `status`, `owner`, `version`, `date`, `decision`, `alternatives`, `consequences`, `related_des` | 架构决策记录，支持审计 |
| BDD Scenario | `SC` | IMPLEMENTATION | `id`, `sn`, `status`, `owner`, `version`, `source_des`, `related_us` | 测试场景，严格Gherkin语法 |
| Test Suite | `TS` | IMPLEMENTATION | `id`, `sn`, `status`, `owner`, `version`, `related_sc` | 测试套件，测试金字塔组织 |
| Task Sequence | `SEQ` | TASK_PLANNING | `id`, `sn`, `status`, `owner`, `version`, `related_sc`/`related_cmp`(至少1个) | 任务序列，支持团队协作 |
| AI Context | `CTX` | TASK_PLANNING | `id`, `sn`, `status`, `owner`, `version`, `context_type`, `related_seq` | AI上下文，绑定任务序列并定义执行模式 |
| Goal | `GOAL` | TASK_PLANNING | `id`, `sn`, `status`, `owner`, `version`, `source_us`, `related_sc`, `related_seq`, `context_refs`, `related_adr`, `related_cmp`, `related_api`, `audit_log_ref` | **声明式目标，审计级执行锚点，系统最终汇聚点**；完整继承所有上游制品关联，确保100%追溯覆盖 |
| Blocker Issue | `BLK` | TASK_PLANNING | `id`, `sn`, `status`, `owner`, `version`, `severity`, `impact`, `mitigation`, `related_seq` | 阻塞问题，风险识别，必须关联任务序列 |
| Audit Log | `AUD` | 审计层 (跨阶段) | `id`, `sn`, `timestamp`, `actor`, `action`, `related_artifact`, `reason` | 审计记录，合规追踪 |
| Traceability Matrix | `TR` | 审计层 (跨阶段) | `id`, `sn`, `status`, `owner`, `version`, `release`, `format` | 追溯矩阵，Release级可视化 |

**ADR 与 DES 双向追溯说明**:

L3 级别强制要求 ADR (Architecture Decision Record) 与 DES (Design Document) 建立双向追溯关系：

- **DES → ADR**: DES 通过 `related_adr` 字段引用相关的架构决策记录
  - **语义**: 设计文档依据哪些架构决策制定
  - **示例**: `related_adr: [ADR-AUTH-025]` (认证设计依据JWT认证方案决策)

- **ADR → DES**: ADR 通过 `related_des` 字段引用影响的设计文档
  - **语义**: 架构决策影响哪些设计文档
  - **示例**: `related_des: [DES-AUTH-010, DES-AUTH-012]` (JWT决策影响认证设计和会话设计)

**双向追溯价值**:
- **正向追溯**: 从设计查询决策依据 (DES → ADR)，支持设计审查
- **反向追溯**: 从决策查询影响范围 (ADR → DES)，支持变更影响分析
- **审计支持**: 完整记录架构决策与设计实施的关联关系

### 2.2 Front Matter 必填规范

**ID管理要求**:
- 遵循`SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md`中的"ID永久占用原则"和"扫描分配机制"
- 严禁复用已生成的artifact IDs，L3审计级追溯链中必须保持完整性和可审计性

**基础字段** (所有 artifacts 必填):

| 字段 | 格式 | 示例 | 规则 |
|------|------|------|------|
| `id` | `<PREFIX>-<SN>-NNN` | `US-AUTH-002`, `DES-PAY-010` | 2-4位PREFIX + 2-6位SN + 3位序号 |
| `sn` | `[A-Z]{2,6}` | `AUTH`, `PAY`, `MAIN` | 全大写字母,不可省略 |
| `status` | 枚举值 | `active`, `draft`, `deprecated` | 所有artifacts必填 |
| `owner` | 文本 | `@team-auth`, `@project-core` | 责任人标识,所有artifacts必填 |
| `version` | `v<MAJOR>.<MINOR>.<PATCH>` | `v1.0.0`, `v2.1.3` | 语义化版本,必须带`v`前缀 |

**追溯字段** (根据 artifact 类型必填):

| 字段类型 | 格式 | 示例 | 说明 |
|---------|------|------|------|
| `source_*` | `<PREFIX>-<SN>-XXX` | `source_us: US-AUTH-002` | 指向直接上游artifact (单个) |
| `related_*` | 列表 | `related_ac: [AC-AUTH-005, AC-AUTH-006]` | 指向相关artifacts (多个) |

**完整示例**:

```yaml
---
id: DES-AUTH-010
sn: AUTH
status: active
owner: @team-auth
version: v1.0.0
source_us: US-AUTH-002
related_adr: [ADR-AUTH-025]
related_cmp: [CMP-AUTH-015]
related_api: [API-AUTH-020]
---
```

```yaml
---
id: CTX-AUTH-085
sn: AUTH
status: active
owner: @aca-ops
version: v1.0.0
context_type: execution_guardrails
related_seq: [SEQ-AUTH-040]
---
```

**GOAL完整汇聚示例**:
```yaml
---
id: GOAL-AUTH-070
sn: AUTH
status: active
owner: @project-manager
version: v1.0.0
source_us: US-AUTH-002           # 需求源头追溯
related_sc: [SC-AUTH-030]        # 测试场景验证
related_seq: [SEQ-AUTH-040]      # 任务序列编排
context_refs: [CTX-AUTH-085]     # AI执行上下文
related_adr: [ADR-AUTH-025]      # 架构决策依据 ⭐ 新增
related_cmp: [CMP-AUTH-015]      # 组件规格支撑 ⭐ 新增
related_api: [API-AUTH-020]      # 接口规格实现 ⭐ 新增
audit_log_ref: AUD-AUTH-050      # 审计记录关联 ⭐ 新增
---
```


```yaml
---
id: ADR-AUTH-025
sn: AUTH
status: accepted
owner: @arch-team
version: v1.0.0
date: 2024-01-15
decision: 采用JWT进行无状态认证
alternatives:
  - Session-based认证
  - OAuth 2.0
consequences:
  - 优势: 无状态、可扩展、跨域支持
  - 劣势: Token过期管理复杂
  - 影响: 需要Redis存储黑名单
---
```

### 2.3 SN (Story Namespace) 规则

| 要求类型 | 规则 | 示例 |
|---------|------|------|
| **禁止省略** | 所有ID必须包含SN | ✅ `US-MAIN-001` ❌ `US-001` |
| **单域项目** | 可用`MAIN`或`CORE`作为默认SN | `US-MAIN-001`, `SC-CORE-020` |
| **多域项目** | 按业务域定义SN | `AUTH`, `PAY`, `CART` |
| **命名规范** | 全大写字母，可选数字，2-6位 | `AUTH`, `PAY2`, `CORE` |

---

## 3. L3 审计特性

### 3.1 版本管理

| 要求类型 | 规则 |
|---------|------|
| **语义化版本** | 遵循 `vMAJOR.MINOR.PATCH` 格式，必须带 `v` 前缀 |
| **版本递增** | 重大变更必须递增版本号 (MAJOR: 破坏性变更, MINOR: 功能增强, PATCH: 问题修复) |
| **变更追踪** | 版本变更必须生成 AUD 记录，记录变更原因和影响范围 |
| **版本一致性** | 相关 artifacts 版本变更应协调一致，避免版本不匹配 |

### 3.2 审计记录 (AUD)

| 要求类型 | 规则 |
|---------|------|
| **必填字段** | `id`, `sn`, `timestamp`, `actor`, `action`, `related_artifact`, `reason` |
| **记录决策** | 架构批准、需求变更、SN变更、门禁豁免、安全审查、上线审批 |
| **保留期限** | 至少3年，关键系统建议永久保留 |
| **审计格式** | 统一使用 ISO 8601 时间戳，记录完整操作上下文 |

**审计示例**:

```yaml
---
id: AUD-AUTH-100
sn: AUTH
timestamp: 2024-01-15T10:30:00Z
actor: @team-arch-lead
action: architecture_decision_approved
related_artifact: ADR-AUTH-025
reason: JWT认证方案经技术委员会评审通过
---
```

### 3.3 架构决策记录 (ADR)

| 要求类型 | 规则 |
|---------|------|
| **必填字段** | `id`, `sn`, `status`, `owner`, `version`, `date`, `decision`, `alternatives`, `consequences` |
| **记录范围** | 所有重大架构决策、技术选型、设计权衡 |
| **格式标准** | 遵循 ADR 标准模板 (Context-Decision-Consequences) |
| **决策类型** | 架构模式选择、技术栈选型、组件边界定义、API设计原则、数据模型决策 |
| **保留要求** | 永久保留，支持审计追溯和未来架构演进参考 |
| **状态管理** | `proposed` (提议) → `accepted` (接受) → `superseded` (取代) / `deprecated` (废弃) |

### 3.4 追溯矩阵生成

| 要求类型 | 规则 |
|---------|------|
| **生成时机** | 每个Release生成完整追溯矩阵 (需求→设计→实现→测试→任务) |
| **支持格式** | CSV (导入Excel/DB), Graphviz DOT (可视化), Markdown表格 |
| **矩阵覆盖** | 横向追溯 (需求→测试), 纵向追溯 (阶段内追溯), 影响分析 (反向追溯) |
| **自动化要求** | 通过 CI/CD 自动生成，确保追溯矩阵与代码同步 |

### 3.5 质量门禁自动化

| 要求类型 | 规则 |
|---------|------|
| **CI集成** | 命名覆盖率检查、追溯链完整性检查、SN合法性检查、版本一致性检查 |
| **阻断条件** | 覆盖率<100%, 追溯链断裂, 使用未登记SN, 缺少必填字段 |
| **豁免流程** | 需生成`AUD-<SN>-NNN`记录，说明豁免原因，经授权人批准 |
| **报告输出** | 自动生成质量报告，包含违规详情和修复建议 |

---

## 4. 使用建议和场景指导

### 4.1 推荐Artifacts配置策略

L3 级别共有6个推荐 artifacts。基于L1基础配置策略，建议按以下优先级选择性使用：

| 优先级 | Artifacts | 适用场景 | Front Matter 最小要求 |
|--------|-----------|---------|---------------------|
| **P0** (审计核心) | **CN**, **QD** | 约束规格和质量定义，支持审计追溯 | `id` + `sn` + `status` + `owner` + `version` |
| **P1** (数据密集) | **DM**, **TD** | 数据模型和测试数据，支持数据完整性 | `id` + `sn` + `status` + `owner` + `version` |
| **P2** (系统集成) | **INT**, **COORD** | 集成设计和协调规格，支持复杂系统 | `id` + `sn` + `status` + `owner` + `version` |

**优先级说明**:
- **P0**: 审计追溯核心，所有L3项目基础需求
- **P1**: 数据密集型系统，需要详细数据建模和测试
- **P2**: 复杂系统集成，多组件协调管理
- **P3**: AI 协作工具，提升 AI 辅助开发效果

**使用建议**:
- **最小集**: 核心14个 + P0 (CN + QD)，L3审计基础配置
- **标准集**: 核心14个 + P0 + P1 (CN + QD + DM + TD)，支持数据完整性
- **完整集**: 核心14个 + P0 + P1 + P2 (添加 INT + COORD)，支持复杂系统集成
- **全量集**: 核心14个 + 全部6个推荐 artifacts，充分利用所有审计能力

### 4.2 典型项目场景示例

1. **快速原型项目**:
   - 使用: 核心14个 + CN + QD
   - 理由: L3最小审计配置，支持基础约束和质量追溯

2. **前后端分离项目**:
   - 使用: 核心14个 + CN + DM + TD + QD
   - 理由: 增加数据模型和测试数据，支持完整数据追溯

3. **AI 辅助开发项目**:
   - 使用: 核心14个 + CN + QD (P0) + INT/COORD (P2)
   - 理由: 在审计级 AI 上下文基础上，强化系统集成与协作接口

### 4.3 软件质量等级配置

根据软件质量要求，建议以下分层配置策略：

**基础质量配置**:
- 使用: 核心14个 + CN + QD
- 适用: 约束和质量定义，基础审计追溯

**生产质量配置**:
- 使用: 核心14个 + CN + DM + TD + QD
- 适用: 数据和测试完备，生产环境质量保障

**关键质量配置**:
- 使用: 核心14个 + CN + DM + INT + TD + QD
- 适用: 系统集成完备，关键业务质量保障

**审计质量配置**:
- 使用: 核心14个 + 全部6个推荐 artifacts
- 适用: 完整审计追溯，最高质量标准

### 4.4 系统复杂度管理

根据系统复杂度，建议以下配置模式：

**简单系统配置**:
- 使用: 核心14个 + CN + QD
- 适用: 单体架构，基础约束和质量控制

**复杂系统配置**:
- 使用: 核心14个 + CN + DM + TD + QD
- 适用: 数据密集型，需要详细数据建模

**大规模系统配置**:
- 使用: 核心14个 + CN + DM + INT + COORD + QD
- 适用: 多组件集成，需要协调规格

**分布式系统配置**:
- 使用: 核心14个 + 全部6个推荐 artifacts
- 适用: 最高复杂度，完整审计和质量保障

---

## 5. 扩展规范

### 5.1 正文标题格式

**强制要求**: front matter 的 `id` 字段是权威标识，正文标题必须包含完整ID。

**格式要求**:
- ✅ **必须**: `## US-AUTH-002 用户登录功能`
- ❌ **禁止**: `## US-002 ...` (缺少SN)
- ❌ **禁止**: `## 用户登录功能` (缺少ID)

**约束**: 正文ID必须与 front matter 的 `id` 严格一致，支持审计追溯和自动化检查。

### 5.2 推荐 Artifacts 命名

**说明**: 以下6个 artifacts 为推荐命名，用于支持完整审计体系和特殊场景需求。

#### Requirements 阶段 (1个)

| PREFIX | 名称 | 适用场景 | Front Matter 关键字段 |
|--------|------|---------|---------------------|
| **CN** | Constraint Specification | 需要显式记录业务约束与技术约束 | `id`, `sn`, `status`, `owner`, `version`, `type` (business/technical), `related_us` |

#### Design 阶段 (2个)

| PREFIX | 名称 | 适用场景 | Front Matter 关键字段 |
|--------|------|---------|---------------------|
| **DM** | Data Model | 数据密集型系统，需要详细数据建模 | `id`, `sn`, `status`, `owner`, `version`, `model_type` (logical/physical), `related_des` |
| **INT** | Integration Design | 复杂系统对接，多系统集成场景 | `id`, `sn`, `status`, `owner`, `version`, `integration_type`, `related_des`, `related_api` |

#### Implementation 阶段 (2个)

| PREFIX | 名称 | 适用场景 | Front Matter 关键字段 |
|--------|------|---------|---------------------|
| **TD** | Test Data | 复杂测试场景，需要专门的测试数据规格 | `id`, `sn`, `status`, `owner`, `version`, `data_category`, `related_sc`, `related_ts` |
| **QD** | Quality Definition | 需要显式质量标准定义（性能/安全/可用性） | `id`, `sn`, `status`, `owner`, `version`, `quality_type`, `related_sc` |

#### Task Planning 阶段 (1个)

| PREFIX | 名称 | 适用场景 | Front Matter 关键字段 |
|--------|------|---------|---------------------|
| **COORD** | Coordination Specification | 多团队协作，需要显式协调规格 | `id`, `sn`, `status`, `owner`, `version`, `coord_type`, `related_seq` |

> **CTX 生产提示**: 审计级 CTX 必须保持 `related_seq` 单值或严格列举共享范围；共享 CTX 时需在正文中说明哪些 `SEQ` 同步受控，并确保查验时可以溯源到所有关联价值流。

**推荐使用原则**:
- 仅在实际需要时使用，避免过度文档化
- 所有推荐 artifacts 如使用，必须遵循完整的 Front Matter 规范（包括 `version` 字段）
- 必须与必填 artifacts 建立完整追溯链（通过 `source_*` 和 `related_*` 字段）

### 5.3 追溯链完整性

**核心原则**: L3 要求完整追溯链，所有核心 artifacts 必须有明确的追溯字段。

**追溯字段分类**:

| Artifact类型 | 生产阶段 | source_* (必填) | related_* 必填字段 | 说明 |
|-------------|---------|---------------|------------------|------|
| User Story (US) | REQUIREMENTS | 无 (起点) | `related_ac` / `related_des` **(至少1个)** | 需求起点，必须关联下游 |
| Acceptance Criteria (AC) | REQUIREMENTS | `source_us` | `related_des` / `related_sc` **(至少1个)** | 验收标准,必须追溯到US |
| Design Document (DES) | DESIGN | `source_us` | `related_adr` **(必须)** + 其他可选 (`related_cmp`, `related_api`) | 架构设计，强制关联ADR决策 |
| Component Specification (CMP) | DESIGN | `source_des` | `related_api` **(Section 2.1推荐)** / `related_seq` **(至少1个)** | 组件规格，推荐关联API |
| API Specification (API) | DESIGN | `source_des` | `related_cmp` **(Section 2.1推荐)** / `related_sc` **(至少1个)** | 接口规格，推荐关联组件 |
| Architecture Decision Record (ADR) | DESIGN | 无 (横向关联) | `related_des` **(必须)** | 架构决策，强制关联设计 |
| BDD Scenario (SC) | IMPLEMENTATION | `source_des` | `related_us` **(必须)** + 其他可选 (`related_ts`) | 测试场景，强制追溯需求 |
| Test Suite (TS) | IMPLEMENTATION | 无 | `related_sc` **(必须)** | 组织多个SC的测试套件 |
| Task Sequence (SEQ) | TASK_PLANNING | 无 | `related_sc` / `related_cmp` **(至少1个)** | 编排任务序列 |
| AI Context (CTX) | TASK_PLANNING | 无 | `context_type` **(必须)** + `related_seq` **(必须)** | 统一AI执行上下文，记录上下文类别 |
| Blocker Issue (BLK) | TASK_PLANNING | 无 | `related_seq` **(必须)** | 从SEQ识别的阻塞问题 |
| Audit Log (AUD) | 审计层 (跨阶段) | 无 | `related_artifact` **(必须)** | 审计记录 |
| Traceability Matrix (TR) | 审计层 (跨阶段) | 无 | 特殊字段 (见下方说明) | Release级追溯矩阵 |

**重要说明**:
- **强制特定字段**: DES→`related_adr`, ADR→`related_des`, SC→`related_us` 是 L3 审计要求，必须使用这些特定字段
- **Section 2.1 推荐**: CMP→`related_api`, API→`related_cmp` 是 Section 2.1 列出的推荐必填字段，标准情况下应使用
- **AI 上下文要求**: CTX 必须填写 `context_type`，并通过 `related_seq` 绑定生产任务序列
- **至少1个**: 其他情况至少要有1个 related 字段，可根据实际情况选择合适的字段

**TR 特殊字段说明**:

TR (Traceability Matrix) 不使用标准的 `related_*` 字段，而是使用以下特殊字段：

```yaml
---
id: TR-AUTH-R1.0
sn: AUTH
status: active
owner: @team-arch
version: v1.0.0
release: v1.0.0  # 特殊字段：标识 Release 版本
format: CSV      # 特殊字段：标识追溯矩阵格式 (CSV/DOT/Markdown)
---
```

- **release** (必须): 标识 Release 版本号 (如 `v1.0.0`, `v2.0.0`)
- **format** (必须): 标识追溯矩阵格式 (`CSV` | `DOT` | `Markdown`)

**职责说明**:
- **派生型 artifacts**: 从上游派生，用 `source_*` 建立单向追溯链
- **组织型 artifacts**: 横向组织同类内容，用 `related_*` 建立多向关联网
- **横向关联 artifacts**: 支持决策、审计等特殊场景，用 `related_*` 建立关联

**SC (BDD Scenario) 追溯逻辑详细说明**:

L3 强制要求 SC 的 `source_des` 字段（L2 中 SC 从 FP 派生），核心原则是 **设计驱动测试 (Design-Driven Testing)**。

**追溯字段要求**:

| 字段 | 要求 | 语义 |
|------|------|------|
| `source_des` | **必须** | 测试场景验证哪个设计文档 |
| `related_us` | **必须** | 测试场景覆盖哪个用户故事，强制建立需求追溯 |
| `related_ts` | 推荐 | 测试场景归属哪个测试套件 |

**L3 vs L2 对比**:

| 级别 | SC 的 source 字段 | 设计理念 |
|------|------------------|---------|
| **L2** | `source_fp` (必须) | 功能驱动测试 (功能点 → 测试) |
| **L3** | `source_des` **(必须)** | **设计驱动测试 (设计 → 测试)** |

**为什么从 DES 派生？**
1. **审计追溯**: L3 必须追溯"设计是否正确实现"，而非仅"需求是否满足"
2. **设计覆盖率**: 确保所有设计文档都有对应测试验证
3. **变更影响分析**: 设计变更时快速定位需更新的测试
4. **质量门禁**: CI/CD 强制"所有 DES 必须有至少 1 个 SC"

**追溯路径**:
```
US-AUTH-002 (需求)
  ↓ source_us
DES-AUTH-010 (设计)
  ↓ source_des
SC-AUTH-030 (测试) ← related_us → US-AUTH-002 (横向追溯)
```

### 5.4 禁止行为

| 禁止内容 | 说明 |
|---------|------|
| ❌ **缺少Front Matter** | 所有artifact必须有`id`+`sn`+`status`+`owner`+`version` |
| ❌ **追溯链断裂** | 所有artifact必须有完整`source_*`或`related_*` (根据类型要求) |
| ❌ **正文格式错误** | 标题必须完整ID格式: `## US-AUTH-001 ...` |
| ❌ **缺少审计记录** | 架构批准、需求变更、SN变更、门禁豁免必须生成AUD |
| ❌ **版本缺失** | 所有artifact必须有 `version` 字段 |
| ❌ **SN省略** | 禁止`US-001`格式,必须`US-<SN>-001` |
| ❌ **source多值** | `source_*`只能指向单个上游，禁止列表 |

---

## 6. Artifact生产次序指导

### 6.1 四阶段生产流程概览

L3-RIGOROUS遵循严格的四阶段顺序生产，确保完整追溯链和审计就绪：

```
REQUIREMENTS → DESIGN → IMPLEMENTATION → TASK_PLANNING
(需求阶段)     (设计阶段)  (实施阶段)          (任务规划阶段)
```

**阶段间依赖原则**：
- ✅ **顺序执行**: 必须完成前一阶段才能开始下一阶段
- ✅ **追溯就绪**: 每个阶段完成时必须建立向上追溯链
- ✅ **质量门禁**: 每个阶段结束时必须通过G1-READY和G2-QUAL验证

---

### 6.2 REQUIREMENTS阶段生产顺序

**阶段目标**: 建立需求基线，定义业务价值和验收标准

**推荐生产顺序**:
1. **US (User Story)** - 需求起点
   - 定义业务需求和用户价值
   - 完成INVEST六维评价
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `related_ac`/`related_des`(至少1个)

2. **AC (Acceptance Criteria)** - 验收标准
   - 基于US定义验收条件
   - 使用Given-When-Then格式
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `source_us`, `related_des`/`related_sc`(至少1个)
   - **追溯关系**: `source_us` → US

**阶段完成标志**:
- [ ] 所有US通过INVEST评价
- [ ] 所有US至少有1个AC
- [ ] 追溯链完整: US ← AC

---

### 6.3 DESIGN阶段生产顺序

**阶段目标**: 将需求转化为技术架构，建立设计决策追溯

**推荐生产顺序**:
1. **DES (Design Document)** - 架构设计核心
   - 基于US进行架构设计
   - Layer-first原则，分层架构
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `source_us`, `related_adr`
   - **追溯关系**: `source_us` → US

2. **ADR (Architecture Decision Record)** - 架构决策记录
   - 记录DES中的重要技术决策
   - Context-Decision-Consequences格式
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `date`, `decision`, `alternatives`, `consequences`, `related_des`
   - **追溯关系**: `related_des` ↔ DES (双向追溯，L3特性)

3. **CMP (Component Specification)** - 组件规格
   - 基于DES拆分组件
   - 严格边界定义，SOLID原则
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `source_des`, `related_api`
   - **追溯关系**: `source_des` → DES

4. **API (API Specification)** - 接口规格
   - 基于DES定义接口
   - Contract-first设计
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `source_des`, `related_cmp`
   - **追溯关系**: `source_des` → DES

**阶段完成标志**:
- [ ] 所有DES有对应ADR记录
- [ ] DES↔ADR双向追溯完整
- [ ] 追溯链完整: US → DES → CMP/API

---

### 6.4 IMPLEMENTATION阶段生产顺序

**阶段目标**: 制定TDD策略，建立设计驱动测试体系

**推荐生产顺序**:
1. **SC (BDD Scenario)** - BDD测试场景
   - 基于DES制定测试场景 (L3设计驱动测试)
   - 严格Gherkin语法，Given-When-Then格式
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `source_des`, `related_us`, `related_ts`
   - **追溯关系**: `source_des` → DES, `related_us` → US (L3横向追溯)

2. **TS (Test Suite)** - 测试套件
   - 组织多个SC，建立测试金字塔
   - 70%单元+20%集成+10%E2E
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `related_sc`
   - **追溯关系**: `related_sc` → SC (组织关系)

**阶段完成标志**:
- [ ] 所有DES有对应SC验证
- [ ] SC同时追溯DES和US
- [ ] 追溯链完整: US → DES → SC → TS

---

### 6.5 TASK_PLANNING阶段生产顺序

**阶段目标**: 制定任务序列，识别风险阻塞

**推荐生产顺序**:
1. **SEQ (Task Sequence)** - 任务序列
   - 基于SC/CMP规划任务执行顺序
   - 定义依赖关系和关键路径
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `related_sc`/`related_cmp`(至少1个)
   - **追溯关系**: `related_sc` → SC, `related_cmp` → CMP (横向组织)

2. **BLK (Blocker Issue)** - 阻塞问题
   - 基于SEQ识别潜在阻塞
   - 定义严重性、影响和缓解方案
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `severity`, `impact`, `mitigation`, `related_seq`
   - **追溯关系**: `related_seq` → SEQ

**阶段完成标志**:
- [ ] 所有SEQ有完整依赖关系定义
- [ ] 关键路径识别完成
- [ ] 追溯链完整: US → DES → SC → SEQ → BLK

---

### 6.6 审计层Artifacts (跨阶段)

**生产时机**: 根据项目需要随时生成

1. **AUD (Audit Log)** - 审计记录
   - 记录关键决策和变更
   - Front Matter必填: `id`, `sn`, `timestamp`, `actor`, `action`, `related_artifact`, `reason`
   - **推荐时机**: 架构批准、需求变更、SN变更、门禁豁免时

2. **TR (Traceability Matrix)** - 追溯矩阵
   - 每个Release生成完整追溯矩阵
   - Front Matter必填: `id`, `sn`, `status`, `owner`, `version`, `release`, `format`
   - **推荐时机**: 每个Release发布前

---

### 6.7 阶段内并行生产建议

**REQUIREMENTS阶段**:
- US和AC可部分并行（先定义部分US，再补充AC）
- 建议比例: 完成70% US后开始AC

**DESIGN阶段**:
- DES必须先行，ADR同步记录
- CMP和API可并行生产（基于DES）
- 建议顺序: DES → ADR → (CMP || API)

**IMPLEMENTATION阶段**:
- SC必须先行，TS后续组织
- 建议比例: 完成80% SC后开始TS

**TASK_PLANNING阶段**:
- SEQ必须先行，CTX绑定SEQ输出执行上下文，BLK基于SEQ/CTX识别
- 建议顺序: SEQ → CTX → BLK

> **执行一致性**: 任何进入发布节奏的任务序列都不得跳过 CTX；如需复用共享 CTX，应在 CTX 记录中追加所有相关 `SEQ`，并说明上下文化的覆盖边界与审计口径。

---

### 6.8 完整追溯链验证清单

**端到端追溯链** (L3标准):
```
US-XXX-NNN (需求起点)
  ↓ source_us
AC-XXX-NNN (验收标准)
  ↓ source_us
DES-XXX-NNN (架构设计)
  ↔ related_adr/related_des (双向)
ADR-XXX-NNN (架构决策)
  ↓ source_des
CMP-XXX-NNN (组件规格)
API-XXX-NNN (接口规格)
  ↓ source_des
SC-XXX-NNN (测试场景)
  → related_us (横向追溯)
  ↓ related_sc
TS-XXX-NNN (测试套件)
  ↓ related_sc/related_cmp
SEQ-XXX-NNN (任务序列)
  ↘ related_seq
CTX-XXX-NNN (AI 上下文)
  ↓ related_seq
BLK-XXX-NNN (阻塞问题)
```

**验证步骤**:
1. [ ] US可追溯到AC (source_us)
2. [ ] US可追溯到DES (source_us)
3. [ ] DES可追溯到ADR (related_adr ↔ related_des)
4. [ ] DES可追溯到CMP/API (source_des)
5. [ ] DES可追溯到SC (source_des)
6. [ ] SC可横向追溯到US (related_us)
7. [ ] SC可追溯到TS (related_sc)
8. [ ] SC/CMP可追溯到SEQ (related_sc/related_cmp)
9. [ ] CTX通过 `related_seq` 绑定到目标SEQ
10. [ ] BLK通过 `related_seq` 绑定到同一SEQ

---

## 7. 验收标准

### 7.1 最低要求 (必须满足)

- [ ] **核心14个artifacts命名完整**
  - US, AC, DES, CMP, API, ADR, SC, TS, SEQ, CTX, BLK, AUD, TR 都有 `id` + `sn` + `status` + `owner` + `version`
  - front matter 格式正确

- [ ] **完整追溯链可用**
  - AC 有 `source_us` 指向有效US
  - DES 有 `source_us` 指向有效US
  - CMP 有 `source_des` 指向有效DES
  - API 有 `source_des` 指向有效DES
  - SC 有 `source_des` 指向有效DES
  - 能通过source字段追踪完整派生链路

- [ ] **组织层建立**
  - TS 有 `related_sc` 指向至少1个SC
  - SEQ 有 `related_sc` 或 `related_cmp` 指向有效 artifacts
  - CTX 有 `related_seq` 指向有效SEQ，并声明 `context_type`
  - BLK 有 `related_seq` 指向有效SEQ
  - 共享 CTX 必须在正文中标明所有受控 `SEQ` 及审计覆盖边界

- [ ] **审计体系完整**
  - 所有关键决策有对应AUD记录
  - ADR覆盖所有重大架构决策
  - 每个Release有完整追溯矩阵(TR)

- [ ] **版本管理规范**
  - 所有14个核心artifacts有 `version` 字段
  - 版本格式遵循 `vMAJOR.MINOR.PATCH`
  - 版本变更有对应AUD记录

- [ ] **SN不省略**
  - 所有artifact的 `id` 都包含SN
  - 格式正确: `<PREFIX>-<SN>-NNN`

### 7.2 推荐标准 (建议满足)

- [ ] **推荐artifacts按需使用**
  - 根据项目特点选择性使用6个推荐artifacts (CN, DM, INT, TD, QD, COORD)
  - 推荐artifacts遵循完整Front Matter规范

- [ ] **横向追溯网建立**
  - 使用 `related_*` 字段建立artifact之间的横向关联
  - 支持双向追溯查询 (正向: 需求→设计→实现, 反向: 实现→设计→需求)

- [ ] **自动化门禁集成**
  - CI/CD集成命名覆盖率检查
  - 自动生成追溯矩阵和质量报告
  - 违规自动阻断并生成修复建议

- [ ] **ADR决策体系完善**
  - 所有架构决策有Context-Decision-Consequences完整描述
  - ADR状态管理规范 (proposed/accepted/superseded/deprecated)
  - 相关artifacts引用ADR,建立决策追溯

- [ ] **审计记录完整性**
  - 除必须记录外，重要操作均有AUD记录
  - 审计日志保留期限≥3年
  - 审计记录格式统一，支持自动化分析

---
