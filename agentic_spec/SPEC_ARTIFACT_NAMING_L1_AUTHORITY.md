# SPEC 命名规范 L1 级权威定义

> **🎯 文档定位**: L1-STREAMLINED 级别命名执行要求的唯一权威定义源
> **🔑 核心对象**: 本级别命名针对 **Artifact (制品)** - 软件开发过程中产生的可追溯文档化实体
> **📋 核心价值**: 定义最小必要命名集的详细执行要求，为快速原型和个人项目提供轻量级追溯能力
> **🔗 引用依赖**:
> - 核心概念定义见 `SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md`
> - 遵循 SOLID 原则: 本文档只定义 L1 级执行要求，不重复核心概念

---

## 1. L1 级别定位概要

### 1.1 L1 命名对象说明

L1 级别命名的核心对象是 **Artifact**（制品）- 软件开发过程中产生的文档化实体。

**必须命名的 Artifacts (6个)**:

| PREFIX | 名称 | 作用 | 示例 ID |
|--------|------|------|--------|
| **US** | User Story | 用户故事，角色视角的业务需求基础 | `US-AUTH-001` |
| **AC** | Acceptance Criteria | 验收标准，定义 User Story 的可测试验收条件 | `AC-AUTH-005` |
| **VS** | Vertical Slice | 端到端价值切片，设计阶段的技术实现路径 | `VS-AUTH-001` |
| **SC** | BDD Scenario | BDD测试场景，基于VS转换的可执行测试规格 | `SC-AUTH-001` |
| **GOAL** | Goal | 声明式执行目标，描述AI要达成的功能目标 | `GOAL-AUTH-001` |
| **CTX** | AI Context | AI上下文，封装执行约束和共享知识 | `CTX-AUTH-055` |

> **CTX 范围选择**: CTX 可定义整个项目的统一上下文，也可针对单个 VS/价值流定制；无论是否共享，每条活跃的 `VS` 都必须能够追溯到一个 CTX，以便 AI 拥有完整执行语境。

**推荐命名的 Artifacts (8个)**: 支持完整追溯链，详见 Section 3.2

**追溯链架构**:
- **核心追溯链 (必须)**: `US → AC / US → VS → SC → GOAL + CTX` - 需求→验收/需求→设计→实施→任务
- **完整追溯链 (推荐)**: `US → AC + US → VS → TAC/FP + VS → SC → GOAL + CTX + TS` - 支持完整设计追溯和TDD全流程

**核心说明: US → VS 流程**:
- **US (User Story)**: L1 **必须**命名，REQUIREMENTS阶段业务需求基础，角色视角表达
- **VS (Vertical Slice)**: L1 **必须**命名，DESIGN阶段端到端技术切片，设计主线
- **关系**: US 是需求输入，VS 是设计产出，一个 US 可派生 1-3 个 VS（通过 source_us 追溯）
- **流程**: REQUIREMENTS(US+AC) → DESIGN(VS+TAC+FP) → IMPLEMENTATION(SC) → TASK_PLANNING(GOAL+CTX)

**L1 标准模式**:

L1 采用统一的四阶段文档组织模式：

| 阶段 | 必填 Artifacts | 追溯关系 | 核心职责 |
|------|---------------|---------|---------|
| **REQUIREMENTS** | US + AC | `US → AC` (1:多) | 业务需求定义和验收标准 |
| **DESIGN** | VS (必填) + TAC/FP (推荐) | `US → VS` (1:多) | 技术设计和实现路径 |
| **IMPLEMENTATION** | SC | `VS → SC` (1:多) | 测试场景和TDD规格 |
| **TASK_PLANNING** | GOAL + CTX | `VS → GOAL, SC → GOAL, VS → CTX` | 执行目标与AI上下文配置 |

**核心原则**: US作为需求起点 → VS作为设计主线 → SC作为实施基础 → GOAL与CTX共同驱动执行

### 1.2 适用场景

**适用场景**:
- ✅ 快速原型、POC、探索性项目
- ✅ 个人学习项目、Hackathon
- ✅ 早期创业项目 (产品验证阶段)

**不适用场景**:
- ❌ 生产环境商业应用
- ❌ 团队协作项目 (3+ 人)
- ❌ 关键系统或高合规项目

### 1.3 核心特征

- ✅ 强制 US + AC + VS + SC + GOAL + CTX 命名 (需求 + 验收 + 设计 + 测试 + 目标 + AI上下文)
- ✅ 核心追溯链完整 (US → AC / US → VS → SC → GOAL + CTX)
- ✅ 推荐命名 8 个额外 artifact (TAC, FP, API, CMP, DM, TS, SEQ, BLK)
- ✅ SN 必须包含 (禁止省略)

---

## 2. 强制要求

### 2.1 必填 Artifacts

按生产阶段顺序排列：

| Artifact | PREFIX | 生产阶段 | Front Matter 必填字段 | 说明 |
|----------|--------|---------|---------------------|------|
| User Story | `US` | REQUIREMENTS | `id`, `sn` | 用户故事，角色视角的业务需求 |
| Acceptance Criteria | `AC` | REQUIREMENTS | `id`, `sn`, `source_us` | 验收标准，验证US的可测试条件 |
| Vertical Slice | `VS` | DESIGN | `id`, `sn`, `source_us` | 端到端价值切片，设计阶段的技术实现路径 |
| BDD Scenario | `SC` | IMPLEMENTATION | `id`, `sn`, `source_vs` | BDD测试场景，基于VS的可执行测试规格 |
| Goal | `GOAL` | TASK_PLANNING | `id`, `sn`, `source_vs`, `related_sc` | 声明式执行目标，AI达成的功能目标（统一记录于 `spec/task_planning/goal_breakdown.md`） |
| AI Context | `CTX` | TASK_PLANNING | `id`, `sn`, `source_vs` | AI上下文配置，封装执行约束与共享知识 |

### 2.2 Front Matter 必填规范

**ID管理要求**:
- 遵循`SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md`中的"ID永久占用原则"和"扫描分配机制"
- 严禁复用已生成的artifact IDs，迭代过程中必须保持引用完整性

**必填字段定义**:

| 字段 | 格式 | 示例 | 规则 |
|------|------|------|------|
| `id` | `<PREFIX>-<SN>-NNN` | `US-AUTH-001`, `VS-AUTH-001` | 2-4位PREFIX + 2-6位SN + 3位序号 |
| `sn` | `[A-Z]{2,6}` | `AUTH`, `PAY`, `MAIN` | 全大写字母,不可省略 |
| `source_us` | `US-<SN>-XXX` | `US-AUTH-001` | AC/VS必填,指向来源US |
| `source_vs` | `VS-<SN>-XXX` | `VS-AUTH-001` | SC/GOAL/CTX必填,指向来源VS |
| `related_sc` | `[SC-<SN>-XXX, ...]` | `[SC-AUTH-001, SC-AUTH-002]` | GOAL类型必填,数组格式,关联SC |

**必填 Artifacts 示例**:

**US (User Story)** - 必填字段: `id` + `sn`
```yaml
---
id: US-AUTH-001
sn: AUTH
---
```

**AC (Acceptance Criteria)** - 必填字段: `id` + `sn` + `source_us`
```yaml
---
id: AC-AUTH-005
sn: AUTH
source_us: US-AUTH-001
---
```

**VS (Vertical Slice)** - 必填字段: `id` + `sn` + `source_us`
```yaml
---
id: VS-AUTH-001
sn: AUTH
source_us: US-AUTH-001
---
```

**SC (BDD Scenario)** - 必填字段: `id` + `sn` + `source_vs`
```yaml
---
id: SC-AUTH-001
sn: AUTH
source_vs: VS-AUTH-001
---
```

**GOAL (Goal)** - 必填字段: `id` + `sn` + `source_vs` + `related_sc`
```yaml
---
id: GOAL-AUTH-001
sn: AUTH
source_vs: VS-AUTH-001
related_sc: [SC-AUTH-001, SC-AUTH-002]
---
```

**CTX (AI Context)** - 必填字段: `id` + `sn` + `source_vs`
```yaml
---
id: CTX-AUTH-055
sn: AUTH
source_vs: VS-AUTH-001
---
```

### 2.3 SN (Story Namespace) 规则

| 要求类型 | 规则 | 示例 |
|---------|------|------|
| **禁止省略** | 所有ID必须包含SN | ✅ `VS-MAIN-001` ❌ `VS-001` |
| **单域项目** | 可用`MAIN`或`CORE`作为默认SN | `VS-MAIN-001`, `SC-CORE-020` |
| **多域项目** | 按业务域定义SN | `AUTH`, `PAY`, `CART` |

---

## 3. 灵活空间

### 3.1 正文标题格式

**灵活性**: front matter 的 `id` 字段才是权威标识，正文标题可以：
- 包含完整ID: `## VS-MAIN-001 用户登录功能`
- 或简化描述: `## 用户登录功能`

**约束**: 如果正文包含ID，必须与 front matter 的 `id` 一致

### 3.2 其他 Artifacts 命名

**推荐命名的 artifacts** (artifact清单及托管文件定义见 `SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` Section 1.6):

> **💡 FP托管说明**: FP (Function Point) 推荐使用独立文档 `[function_point_file]`，也可嵌入 `[component_design_file]`。

#### 3.2.1 推荐 Artifacts 使用优先级

> **💡 使用建议**: L1 级别的推荐 artifacts 配置策略和场景示例，详见 [Section 4. 使用建议和场景指导](#4-使用建议和场景指导)

#### 3.2.2 推荐 Artifacts 详细清单

#### Requirements 阶段 (0个)

所有 Requirements 阶段 artifacts (US, AC) 均为必填，无推荐 artifacts。

> **💡 说明**: CORE_CONCEPTS 中定义的其他 REQUIREMENTS artifacts（如 CN-约束规格, IFR-接口需求）在 L1 级别不作要求，仅在 L2/L3 级别使用。

#### Design 阶段 (5个)

- **TAC (Technical Acceptance Criteria)**: 技术验收标准，QA/架构师视角验收VS技术实现
  - **推荐托管**: `[technical_acceptance_file]`
  - **关系**: 从 VS 派生，补充技术验收维度
  - **适用**: 需要技术质量验收、性能指标、安全要求时使用
  - **示例**: `TAC-AUTH-001` (认证流程技术验收)

- **FP (Function Point)**: 功能点定义，连接需求与架构的设计单元
  - **推荐托管**: `[function_point_file]` 独立文档（也可嵌入 `[component_design_file]`）
  - **关系**: 从 VS 派生，细化技术实现点
  - **适用**: 需要详细功能分解、工作量估算时使用
  - **示例**: `FP-AUTH-001` (用户认证功能点)

- **CMP (Component Specification)**: 系统组件规格定义，指导架构设计（前端GUI组件包含逻辑+视觉混合规格）
  - **推荐托管**: `[component_design_file]`
  - **适用**: 系统有明确的模块化需求时使用
  - **示例**: `CMP-AUTH-015` (认证组件规格)

- **API (API Spec)**: 接口契约定义，支持前后端分离开发
  - **推荐托管**: `[api_design_file]`
  - **适用**: 前后端分离、微服务架构、或需要接口文档时使用
  - **示例**: `API-AUTH-020` (登录接口规格)

- **DM (Data Model)**: 数据模型定义，指导数据库设计
  - **推荐托管**: `[data_model_file]`
  - **适用**: 有数据存储需求，或需要明确实体关系时使用
  - **示例**: `DM-AUTH-012` (用户数据模型)

#### Implementation 阶段 (1个)

所有核心 Implementation artifacts (SC) 均为必填。

- **TS (Test Suite)**: 测试套件组织，支持测试管理
  - **推荐托管**: `[test_suites_file]`
  - **关系**: 组织多个 SC，提供测试分组能力
  - **适用**: 测试用例数量较多，需要分组管理时使用
  - **示例**: `TS-AUTH-035` (登录功能测试套件)

#### Task Planning 阶段 (2个)

Task Planning 阶段核心 artifacts (GOAL + CTX) 均为必填。

- **SEQ (Task Sequence)**: 任务序列定义，明确执行顺序
  - **推荐托管**: `[task_sequence_file]`
  - **适用**: 任务间依赖复杂，需要明确执行顺序时使用
  - **示例**: `SEQ-AUTH-050` (登录功能任务序列)

- **BLK (Blocker Issue)**: 阻塞问题追踪，识别风险点
  - **推荐托管**: `[blocker_anticipation_file]`
  - **适用**: 项目有已知风险，或需要问题追踪时使用
  - **示例**: `BLK-AUTH-060` (登录功能的阻塞问题)

> **CTX 生产提示**: 当同一 CTX 服务于多个 VS 时，需在 CTX 正文中明确共享范围；若 VS 需要差异化执行约束，则为每条 VS 单独生成 CTX，仍通过 `source_vs` 建立派生关系。

**Front Matter 最小要求**: 如使用以上 artifacts，至少包含 `id` + `sn`；设计类推荐补充 `source_vs`，任务编排类需结合 `related_*` 保持连通

**策略**: 这些推荐 artifacts 可扩展核心追溯链，建议根据项目需要选择性命名

#### 3.2.3 推荐 Artifacts Front Matter 示例

**TAC (Technical Acceptance Criteria)** - 推荐字段: `id` + `sn` + `source_vs`
```yaml
---
id: TAC-AUTH-001
sn: AUTH
source_vs: VS-AUTH-001  # 推荐，从VS派生
---
```

**FP (Function Point)** - 推荐字段: `id` + `sn` + `source_vs`
```yaml
---
id: FP-AUTH-025
sn: AUTH
source_vs: VS-AUTH-001  # 推荐，从VS派生
related_sc: [SC-AUTH-010]  # 可选
---
```

**TS (Test Suite)** - 推荐字段: `id` + `sn` + `source_sc`
```yaml
---
id: TS-AUTH-035
sn: AUTH
source_sc: SC-AUTH-010  # 推荐，从SC派生
---
```

**SEQ (Task Sequence)** - 推荐字段: `id` + `sn`
```yaml
---
id: SEQ-AUTH-050
sn: AUTH
---
```

**其他推荐 artifacts** (CMP, API, DM, BLK) 遵循相同模式: `id` + `sn` + `source_vs` (推荐)

### 3.3 追溯链字段

**核心原则**: L1采用双线追溯链（US → AC 验收线 / US → VS → SC → GOAL 实施线）

**必填 Artifacts 追溯字段要求**:

| Artifact | 生产阶段 | source_us | source_vs | related_sc | 说明 |
|----------|---------|-----------|-----------|------------|------|
| **US** | REQUIREMENTS | - | - | - | 需求起点，无上游追溯 |
| **AC** | REQUIREMENTS | **必填** | - | - | 验证US，必须追溯到源US |
| **VS** | DESIGN | **必填** | - | - | 设计切片，必须追溯到源US |
| **SC** | IMPLEMENTATION | - | **必填** | - | 测试场景，必须追溯到源VS |
| **GOAL** | TASK_PLANNING | - | **必填** | **必填** | 执行目标，必须追溯到源VS和关联SC |
| **CTX** | TASK_PLANNING | - | **必填** | - | AI上下文，必须追溯到源VS |

**推荐 Artifacts 追溯字段要求**:

| Artifact | 阶段 | source_* | related_* | 说明 |
|----------|------|----------|-----------|------|
| **TAC** | DESIGN | `source_vs` 推荐 | 可选 | 技术验收，推荐追溯到源VS |
| **FP** | DESIGN | `source_vs` 推荐 | 可选 | 功能点，推荐追溯到源VS |
| **API/CMP/DM** | DESIGN | `source_vs` 推荐 | 可选 | 设计产物，推荐追溯到源VS |
| **TS** | IMPLEMENTATION | `source_sc` 推荐 | 可选 | 测试套件，推荐追溯到源SC |
| **SEQ/BLK** | TASK_PLANNING | 可选 | 可选 | 任务管理产物，追溯字段可选 |

**Front Matter最小集**:
- **所有 artifacts**: `id` + `sn` (必须)
- **必填追溯**: AC需`source_us`, VS需`source_us`, SC需`source_vs`, GOAL需`source_vs`+`related_sc`, CTX需`source_vs`

### 3.4 禁止行为

| 禁止内容 | 说明 |
|---------|------|
| ❌ **缺少Front Matter** | 所有artifacts必须有`id`+`sn`; AC/VS必须有`source_us`; SC/GOAL/CTX必须有`source_vs` |
| ❌ **省略SN** | 禁止`VS-001`格式,必须`VS-<SN>-001` |
| ❌ **追溯链断裂** | AC必须有`source_us`指向有效US; VS必须有`source_us`指向有效US; SC必须有`source_vs`指向有效VS |

---

## 4. 使用建议和场景指导

### 4.1 推荐Artifacts配置策略

L1 级别共有8个推荐 artifacts。如果项目资源有限或处于早期阶段，建议按以下优先级选择性使用：

| 优先级 | Artifacts | 适用场景 | Front Matter 最小要求 |
|--------|-----------|---------|---------------------|
| **P0** (测试套件) | **TS** | 使用 TDD/BDD 开发方式，需要测试套件管理 | `id` + `sn` + `source_sc` (推荐) |
| **P1** (设计追溯) | **TAC**, **FP**, **API**, **CMP**, **DM** | 前后端分离、模块化项目、有数据模型需求 | `id` + `sn` + `source_vs` (推荐) |
| **P2** (任务管理) | **SEQ**, **BLK** | 任务间依赖复杂、有已知风险点、需要任务序列管理 | `id` + `sn` |

**优先级说明**:
- **P0**: 测试套件管理，支持完整 TDD 工作流
- **P1**: 设计文档化，支持前后端协作和架构清晰度（TAC/FP是VS的补充设计）
- **P2**: 任务编排，解决复杂依赖和风险管理
- **P3**: AI 协作工具，提升 AI 辅助开发效果

**使用建议**:
- **最小集** (POC/快速原型): 仅使用必填 artifacts（US + AC + VS + SC + GOAL + CTX）
- **标准集** (个人项目): P0 + P1 (TS + TAC/FP/API/CMP)，支持设计追溯
- **完整集** (团队协作): P0 + P1 + P2，支持任务管理和风险控制

### 4.2 典型项目场景示例

1. **快速原型项目**:
   - 使用: US + AC + VS + SC + GOAL (必须核心链)
   - 理由: 最小追溯链，支持 AI 执行和 TDD 验证

2. **前后端分离项目**:
   - 使用: US + AC + VS + SC + GOAL (必须) + TS (P0) + TAC + FP + API + CMP (P1)
   - 理由: 增加设计文档和测试套件，支持接口契约和组件规格

3. **AI 辅助开发项目**:
   - 使用: 必填链 (US + AC + VS + SC + GOAL + CTX) + TS (P0) + TAC + FP + API (P1) + SEQ (P2)
   - 理由: 在完整 AI 上下文基础上，补充设计追溯与任务序列以提升协作效果

---

## 5. 验收标准

### 5.1 最低要求 (必须满足)

- [ ] **User Story 命名完整**
  - 所有核心 US 有 `id: US-<SN>-NNN` 和 `sn` 字段
  - front matter 格式正确

- [ ] **Acceptance Criteria 命名完整**
  - 所有验收标准有 `id: AC-<SN>-NNN`、`sn`、`source_us`
  - `source_us` 指向有效的 US-ID

- [ ] **Vertical Slice 命名完整**
  - 所有核心 VS 有 `id: VS-<SN>-NNN`、`sn`、`source_us`
  - `source_us` 指向有效的 US-ID

- [ ] **BDD Scenario 命名完整**
  - 所有核心 SC 有 `id: SC-<SN>-NNN`、`sn`、`source_vs`
  - `source_vs` 指向有效的 VS-ID

- [ ] **Goal 命名完整**
  - 所有核心 GOAL 有 `id: GOAL-<SN>-NNN`、`sn`、`source_vs`、`related_sc`
  - `source_vs` 指向有效的 VS-ID
  - `related_sc` 包含至少1个有效的 SC-ID
- [ ] **AI Context 命名完整**
  - 所有核心 CTX 有 `id: CTX-<SN>-NNN`、`sn`、`source_vs`
  - `source_vs` 指向支持该上下文的 VS-ID
  - 如 CTX 供多条 VS 共享，正文需列出覆盖范围并说明共享语境

- [ ] **追溯链基本可用**
  - 能通过 `source_us` 从 AC/VS 追溯到 US
  - 能通过 `source_vs` 从 SC/GOAL/CTX 追溯到 VS
  - 能通过 `sn` 过滤特定业务域的 artifacts

### 5.2 推荐标准 (建议满足)

**推荐 artifacts 命名完整性**:

- [ ] **Design 阶段推荐 artifacts 有命名**
  - TAC (Technical Acceptance Criteria) 有 `id` + `sn` + `source_vs` (推荐)
  - FP (Function Point) 有 `id` + `sn` + `source_vs` (推荐)
  - CMP (Component Specification) 有 `id` + `sn` + `source_vs` (推荐)
  - API (API Spec) 有 `id` + `sn` + `source_vs` (推荐)
  - DM (Data Model) 有 `id` + `sn` + `source_vs` (推荐)

- [ ] **Implementation 阶段推荐 artifacts 有命名**
  - TS (Test Suite) 有 `id` + `sn` + `source_sc` (推荐)

- [ ] **Task Planning 阶段推荐 artifacts 有命名**
  - SEQ (Task Sequence) 有 `id` + `sn`
  - BLK (Blocker Issue) 有 `id` + `sn`

**推荐追溯链完整性**:
- [ ] **Design 阶段推荐 artifacts 的追溯**
  - TAC/FP/CMP/API/DM 推荐有 `source_vs` 字段，指向有效的 VS-ID

- [ ] **Implementation 阶段推荐 artifacts 的追溯**
  - TS 推荐有 `source_sc` 字段，指向有效的 SC-ID

- [ ] **关键 `related_*` 字段已填写**
  - 如 GOAL 的 `related_sc`（必填）
  - 其他可选 `related_*` 字段根据项目需要填写
  - 建立 artifacts 间的关联关系

**SN 定义一致性**:
- [ ] **SN 已定义并保持一致**
  - 单域项目: 使用 `MAIN` 或 `CORE` 作为默认 SN
  - 多域项目: 定义 2-5 个业务域 SN (如 `AUTH`, `PAY`, `CART`)

- [ ] **所有 artifacts 使用一致的 SN 命名**
  - 同一业务域的 artifacts 使用相同 SN
  - 避免 SN 混乱或不一致
