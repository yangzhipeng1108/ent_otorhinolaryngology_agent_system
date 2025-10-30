# SPEC 命名规范核心概念权威定义

> **🎯 文档定位**: SPEC 命名规范体系的唯一核心概念定义源 (Single Source of Truth)
> **🔑 核心对象**: 本命名体系针对 **Artifact (制品)** - 软件开发过程中产生的可追溯文档化实体
> **📋 核心价值**: 定义命名核心术语的精确概念，为所有级别定义文档提供统一语义基础
> **🔗 引用规则**:
> - 本文档是命名体系内所有核心术语的唯一权威定义源
> - 其他文档 (级别权威定义、实施指南) **必须引用**本文档，**不得重复定义**核心术语
> - 遵循 SOLID 原则: Single Responsibility (SRP) - 本文档只负责术语定义，不负责级别选择和执行细节

---

## 1. 核心术语定义

### 1.1 Artifact (制品)

**定义**: 软件开发过程中产生的所有可追溯的文档化实体 (需求、设计、场景、任务等)。

### 1.2 PREFIX (前缀)

**定义**: artifact 类型标识符 (如 `US`, `SC`, `API`)。

**规范**: 全大写、唯一，完整清单及格式约束详见本文档 Section 1.6 和 Section 2.3

### 1.3 SN (Story Namespace)

**定义**: 业务域命名空间，3-10 位大写字母 (推荐 3-6 位)。

**规范**:
- 格式: 全大写字母，可选尾巴数字 (如 `AUTH`, `PAY`, `AUTH2`)
- 尾部数字: 可以用于版本号, 版本迭代号
- 必选: 不允许省略

### 1.4 NNN (序号)

**定义**: 3 位起步十进制数字，在同一 SN 下按 PREFIX 独立递增。

**规范**: 起始 001，可跳号不回退，可扩展到 4 位

**ID永久占用原则**: artifact ID一经生成即为永久占用，不得在后续迭代中复用

**扫描分配机制**: 生成新artifact时，必须扫描宿主文件中所有同PREFIX+SN的现有IDs，取最大序号+1进行分配

**扫描规则**:
- **单文件场景**: 扫描当前文件内所有同PREFIX+SN的artifacts
- **多文件场景**: 扫描同目录下所有包含同PREFIX+SN的文件
- **SN独立计数**: 不同SN的序号独立计算（如AUTH域和MAIN域分别计数）

**ID分配示例**:
```yaml
# 宿主文件现有内容：
SC-AUTH-001: 用户登录成功场景
SC-AUTH-003: 用户登录失败场景  
SC-MAIN-001: 主页加载场景

# 新增场景时的ID分配：
SC-AUTH-004  # AUTH域最大003，分配004
SC-MAIN-002  # MAIN域最大001，分配002
```

### 1.5 Composite ID (复合标识符)

**定义**: `<PREFIX>-<SN>-NNN(-SUFFIX)` 格式的完整标识符。

**SUFFIX** (可选): `-L`/`-P` (逻辑/物理层), `-POST`/`-GET` (HTTP方法), `-P1`/`-P2` (阶段)

### 1.6 PREFIX权威清单与标准托管文件

> **🎯 定位**: 定义所有artifact的PREFIX、完整名称、中文含义及推荐托管文件占位符
> **📋 占位符规则**: 使用`[snake_case_file]`格式,实际文件名由项目决定
> **🔗 引用方式**: 各级别AUTHORITY文档在artifact描述中引用此表的占位符
> **📌 来源说明**: 托管文件占位符提取自CRAFT_L1/L2/L3文件的实际使用,确保一致性
> **⚠️ 级别说明**: 本文档仅定义核心术语,不涉及级别选择决策,级别信息由各级AUTHORITY文档权威定义

#### REQUIREMENTS阶段

| PREFIX | 完整名称 | 中文含义 | 推荐托管文件 |
|--------|---------|---------|------------|
| `US` | User Story | 用户故事 | `[user_stories_file]` |
| `AC` | Acceptance Criteria | 验收标准 | `[acceptance_criteria_file]` |
| `CN` | Constraint Specification | 约束规格 | `[constraints_file]` |
| `IFR` | Interface Requirement | 接口需求 | `[interfaces_file]` |

**其他REQUIREMENTS阶段托管文件** (无直接artifact对应):
- `[business_goals_file]` - 业务目标文档
- `[business_requirements_file]` - 业务需求文档
- `[business_rules_file]` - 业务规则文档
- `[compliance_requirements_file]` - 合规需求文档
- `[glossary_file]` - 术语表
- `[nfr_file]` - 非功能需求文档
- `[performance_requirements_file]` - 性能需求文档
- `[requirements_traceability_file]` - 需求追溯矩阵
- `[security_requirements_file]` - 安全需求文档
- `[stakeholder_file]` - 利益相关方文档
- `[use_cases_file]` - 用例文档

#### DESIGN阶段

| PREFIX | 完整名称 | 中文含义 | 推荐托管文件 |
|--------|---------|---------|------------|
| `VS` | Vertical Slice | 垂直切片 | `[vertical_slice_file]` |
| `TAC` | Technical Acceptance Criteria | 技术验收标准 | `[technical_acceptance_file]` |
| `FP` | Function Point | 功能点 | `[component_design_file]` (嵌入) |
| `DES` | Design Document | 设计文档 | `[system_design_file]` |
| `CMP` | Component Specification | 组件规格 | `[component_design_file]` |
| `API` | API Specification | API规格 | `[api_design_file]` |
| `DM` | Data Model | 数据模型 | `[data_model_file]` |
| `ADR` | Architecture Decision Record | 架构决策记录 | `[decision_records_file]` |
| `INT` | Integration Design | 集成设计 | `[integration_design_file]` |
| `IFS` | Interface Specification | 接口规格 | `[interface_contracts_file]` |

**其他DESIGN阶段托管文件** (无直接artifact对应):
- `[function_points_file]` - 功能点独立文档（FP也可嵌入component_design_file，见上表说明）
- `[architecture_file]` - 系统架构文档
- `[deployment_design_file]` - 部署架构设计
- `[deployment_file]` - 部署设计文档
- `[monitoring_design_file]` - 监控设计架构
- `[performance_design_file]` - 性能设计规范
- `[security_design_file]` - 安全架构设计
- `[system_integration_file]` - 系统集成设计

#### IMPLEMENTATION阶段

| PREFIX | 完整名称 | 中文含义 | 推荐托管文件 |
|--------|---------|---------|------------|
| `SC` | BDD Scenario | BDD场景 | `[bdd_test_scenarios_file]` |
| `TS` | Test Suite | 测试套件 | `[test_suites_file]` |
| `TD` | Test Data | 测试数据 | `[test_data_management_file]` |
| `QD` | Quality Definition | 质量定义 | `[quality_file]` 或 `[quality_gates_file]` |
| `PS` | Performance Specification | 性能规格 | `[performance_testing_file]` |
| `SS` | Security Specification | 安全规格 | `[security_test_scenarios_file]` |
| `IO` | Integration Orchestration | 集成编排 | `[integration_test_orchestration_file]` |
| `RC` | Rollback/Recovery | 回滚/恢复 | (无标准占位符) |

**其他IMPLEMENTATION阶段托管文件** (无直接artifact对应):
- `[project_structure_file]` - 项目目录结构（定义代码、测试、资源的组织结构，所有开发活动的基础）
- `[code_quality_gates_file]` - 代码质量门禁
- `[development_approach_file]` - 开发方法文档
- `[integration_test_file]` - 集成测试文档
- `[performance_test_file]` - 性能测试文档
- `[performance_test_scenarios_file]` - 性能测试场景
- `[quality_verification_spec_file]` - 质量验证规格
- `[tdd_strategy_file]` - TDD策略文档
- `[test_automation_pipeline_file]` - 测试自动化流水线
- `[test_driven_sequence_file]` - 测试驱动序列
- `[test_strategy_file]` - 测试策略文档

#### TASK_PLANNING阶段

| PREFIX | 完整名称 | 中文含义 | 推荐托管文件 |
|--------|---------|---------|------------|
| `GOAL` | Goal/Target | 目标 | `[goal_breakdown_file]` |
| `SEQ` | Task Sequence | 任务序列 | `[task_sequence_file]` |
| `BLK` | Blocker Issue | 阻塞问题 | `[blocker_anticipation_file]` |
| `CTX` | AI Context | AI上下文 | `[ai_context_specification_file]` |
| `COORD` | Coordination Specification | 协调规格 | `[task_coordination_spec_file]` |
| `ACP` | Acceptance Checkpoint | 验收检查点 | `[acceptance_checkpoints_file]` |
| `TR` | Traceability Matrix | 追溯矩阵 | `[traceability_matrix_file]` |

> **级别说明**: CTX 在本清单中作为基础术语定义；从 L1 起的各级权威文档默认将 CTX 视为必填 artifact。若未来出现新的级别或特例，需要显式在对应权威文档中声明豁免条件。

**其他TASK_PLANNING阶段托管文件** (无直接artifact对应):
- `[task_breakdown_file]` - 围绕GOAL的扩展说明（验收标准、成功条件），非独立artifact
- `[audit_tracking_spec_file]` - 审计追踪规格
- `[decision_context_spec_file]` - 决策上下文规格
- `[quality_verification_spec_file]` - 质量验证规格（AI执行任务的质量检查规划）
- `[deployment_automation_file]` - 部署自动化
- `[task_list_file]` - 任务列表文档
- `[task_registry_file]` - 任务注册表

#### AUDIT阶段

| PREFIX | 完整名称 | 中文含义 | 推荐托管文件 |
|--------|---------|---------|------------|
| `AUD` | Audit Log | 审计日志 | `[audit_tracking_spec_file]` |

**其他AUDIT阶段托管文件** (无直接artifact对应):
- 暂无

#### 嵌入式Artifact说明

某些artifact可嵌入其他文件,无需独立文档:

- **FP (Function Point)** - 可嵌入`[component_design_file]`

#### 关键Artifact详细说明

**CMP (Component Specification) - 组件规格详述**:
- **定义**: 系统组件的完整规格定义，包含功能边界、职责划分和接口约束
- **基础规格内容**: 组件功能、状态管理、依赖关系、接口定义的标准化描述
- **前端GUI组件扩展**: 对于前端GUI组件，额外包含视觉设计规格
  - **视觉规格**: 布局结构、样式设计、交互效果、视觉状态变化
  - **逻辑与视觉统一**: 确保功能逻辑与视觉设计作为统一artifact管理
- **技术栈无关**: 提供抽象的组件描述，不绑定具体实现框架
- **重构保护**: 确保技术栈变更时组件规格的完整追溯性
- **统一管理**: 组件规格作为整体artifact进行版本管理，避免分离导致的追溯断裂

> ⚓ **GOAL 统一锚点**: 无论如何组装上游 artifacts，所有执行计划、质量门禁与工具链都以 GOAL 标识作为唯一承接点；各级 Authority 文档需说明如何将本级产物汇聚到 GOAL。**GOAL 是整个 SPEC 系统的最终汇聚点**，通过其 Front Matter 字段体系实现 100% 上游制品追溯覆盖：需求源头(`source_us`) + 设计层决策(`related_adr`) + 架构实现(`related_cmp`/`related_api`) + 测试验证(`related_sc`) + 任务编排(`related_seq`) + 执行上下文(`context_refs`) + 审计链条(`audit_log_ref`)。所有 GOAL front matter 必须集中维护在 `spec/task_planning/[goal_breakdown_file]`（GOAL注册表）；其他 task_planning 文档仅引用 GOAL ID，不得重复定义 front matter。GOAL 记录应按级别要求显式引用其上下游以保持完整追溯链。

### 1.7 value_path (价值路径四向度)

> **🎯 定位**: 端到端价值链路的核心结构化表达，体现用户价值从交互到反馈的完整流动
> **📋 适用范围**: 主要用于 DESIGN 阶段的 VS (L1) 和 FP (L2)，延伸至 IMPLEMENTATION 阶段的 SC (L2)
> **⚠️ 级别差异**: 不同约束级别在命名和语义上有显著差异，详见下方级别对照表

**定义**: value_path（价值路径四向度，Value Path Four Dimensions）是描述端到端价值链路的标准化四向度结构，用于系统化拆解用户价值从前端交互到结果反馈的完整流动路径。

#### 核心四向度（Four Dimensions）

| 向度序号 | 向度名称（中文） | 向度名称（英文） | 核心语义 |
|---------|----------------|----------------|---------|
| **D1** | 前端交互 | Frontend Interaction | 用户与系统的交互入口（UI组件、表单、操作触发点） |
| **D2** | 数据流转 | Data Flow | 数据在系统中的传递路径（请求/响应、跨层传递、状态变更） |
| **D3** | 后端处理 | Backend Processing | 业务逻辑的执行过程（验证、计算、存储、集成） |
| **D4** | 结果反馈 | Result Feedback | 系统向用户反馈的结果（响应呈现、状态更新、反馈机制） |

> **💡 设计原则**: 四个向度**缺一不可**，共同构成端到端价值闭环，确保用户价值从交互输入到反馈输出的完整性。

#### 级别差异对照表

| 约束级别 | 使用术语 | 适用 Artifact | 主要语义侧重 | 典型格式 |
|---------|---------|--------------|------------|---------|
| **L1-STREAMLINED** | `value_path`<br/>（VS的价值路径四向度：Value Path Four Dimensions） | VS (Vertical Slice) | **需求维度**<br/>端到端价值切片，跨层穿透技术栈，快速原型导向 | Section 标题: `## value_path`<br/>内容: 四向度描述 |
| **L2-BALANCED** | `value_path_mapping`<br/>（端到端验证映射：End-to-End Verification Mapping） | FP (Function Point)<br/>SC (BDD Scenario) | **架构映射 + 验证结构维度**<br/>FP: 需求到架构的映射<br/>SC: 完整的端到端验证映射 | FP Section: `## value_path_mapping（端到端验证映射）`<br/>SC Section: `### value_path端到端验证映射` |
| **L3-RIGOROUS** | 不使用 value_path 机制 | - | L3 不依赖 VS 机制，采用 Layer-first 架构，无直接 value_path 概念 | - |

#### 使用场景与追溯链关系

**L1-STREAMLINED 场景**:
- **VS (Vertical Slice)**: 定义 `value_path` 四向度，作为端到端价值切片的核心结构
- **FP (Function Point)**: 基于 VS 的 `value_path` 分解 Function Point
- **TAC (Technical Acceptance Criteria)**: 验收 VS 的 `value_path` 技术实现质量

**L2-BALANCED 场景**:
- **FP (Function Point)**: 定义 `value_path_mapping`（端到端验证映射），建立需求到架构的映射关系
- **SC (BDD Scenario)**: 包含 `value_path端到端验证映射`（End-to-End Verification Mapping），确保 FP 的 value_path 完整转化为可验证的测试场景

**追溯链传递**:
```
L1: US → VS (含 value_path) → FP → SC
L2: US → FP (含 value_path_mapping) → SC (含 value_path端到端验证映射) → TS
```

#### 质量标准

- **完整性**: 四个向度**缺一不可**（前端交互 + 数据流转 + 后端处理 + 结果反馈）
- **端到端性**: 必须覆盖从用户交互到结果反馈的完整闭环
- **可追溯性**: 在 DESIGN → IMPLEMENTATION → TASK_PLANNING 阶段保持一致传递
- **可验证性**: L2 的 value_path 必须可转化为可执行的 BDD 验证场景

> **🔗 引用规则**: 其他文档引用 value_path 概念时，应明确指明约束级别（L1/L2），并使用本文档定义的标准术语

---

## 2. 命名格式规范

### 2.1 基本格式

```
<PREFIX>-<SN>-NNN
```

**示例**:
- `US-AUTH-001`: AUTH 域的第 1 个 User Story
- `SC-PAY-205`: PAY 域的第 205 个 BDD Scenario
- `GOAL-CART-042`: CART 域的第 42 个 Goal

### 2.2 带后缀格式

```
<PREFIX>-<SN>-NNN-<SUFFIX>
```

**示例**:
- `DM-AUTH-010-L`: AUTH 域的第 10 个数据模型 (逻辑层)
- `API-PAY-020-POST`: PAY 域的第 20 个 API (POST 方法)
- `SEQ-AUTH-030-P1`: AUTH 域的第 30 个任务序列 (阶段 1)

### 2.3 格式约束

| 元素 | 规则 | 示例 |
|------|------|------|
| PREFIX | 2-4 位大写字母 | `US`, `SC`, `API` |
| SN | 2-6 位大写字母，可选数字 | `AUTH`, `PAY`, `CORE` |
| NNN | 3 位起步递增，可扩展到 4 位 | `001`, `205`, `1001` |
| SUFFIX | 可选，大写字母或数字，用 `-` 连接 | `-L`, `-POST`, `-P1` |

### 2.4 分隔符规范

- 主要分隔符: `-` (连字符)
- 禁止使用: `_` (下划线)、`.` (点)、`/` (斜杠)

**正确**:
```
US-AUTH-001
API-PAY-020-POST
```

**错误**:
```
US_AUTH_001    # 使用了下划线
US.AUTH.001    # 使用了点
US/AUTH/001    # 使用了斜杠
```

---

## 3. Front Matter 元数据规范

| 字段 | 必选性 | 格式 | 说明 |
|------|-------|------|------|
| `id` | 必选 | `<PREFIX>-<SN>-NNN` | artifact 唯一标识符 |
| `sn` | 必选 | `[A-Z]{2,6}` | 业务域命名空间 |
| `status` | 可选 | 枚举值 | 状态: `active`, `draft`, `deprecated` |
| `owner` | 可选 | 文本 | 责任人标识 |
| `version` | 可选 | `v<MAJOR>.<MINOR>.<PATCH>` | 语义化版本 (必须带 `v` 前缀) |
| `source_*` | 可选 | `source_<TYPE>` | 直接上游 artifact (单个) |
| `related_*` | 可选 | `related_<TYPE>` | 相关 artifacts (列表) |

> **💡 说明**: 除 `id` 和 `sn` 为必选字段外，其他字段是否使用由各级别AUTHORITY文档定义

---

## 4. 追溯链字段规范

### 4.1 字段命名规则

```
source_<TYPE>:     指向直接上游 (单个)
related_<TYPE>:    指向相关 artifacts (多个)
```

**示例**:
- `source_us`: 来源的 User Story (单个)
- `source_vs`: 来源的 Vertical Slice (单个)
- `related_us`: 相关的 User Stories (多个)
- `related_sc`: 相关的 BDD Scenarios (多个)

### 4.2 标准追溯链字段

**source_* 字段示例**:

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `source_us` | 单个 | 直接来源的 User Story | `US-AUTH-002` |
| `source_vs` | 单个 | 直接来源的 Vertical Slice | `VS-AUTH-001` |
| `source_fp` | 单个 | 直接来源的 Function Point | `FP-AUTH-025` |
| `source_des` | 单个 | 直接来源的 Design Document | `DES-AUTH-010` |

**related_* 字段示例**:

| 字段名 | 类型 | 说明 | 示例 |
|--------|------|------|------|
| `related_us` | 列表 | 相关的 User Stories | `[US-AUTH-002, US-AUTH-003]` |
| `related_vs` | 列表 | 相关的 Vertical Slices | `[VS-AUTH-001]` |
| `related_sc` | 列表 | 相关的 BDD Scenarios | `[SC-AUTH-030]` |
| `related_ts` | 列表 | 相关的 Test Suites | `[TS-AUTH-035]` |

> **💡 说明**: 更多追溯链字段遵循相同命名模式 `source_<type>` 和 `related_<type>`，其中 `<type>` 为小写PREFIX

### 4.3 追溯链语义

**`source_*` (直接上游)**: 指向单个上游 artifact，标识直接来源

**`related_*` (相关制品)**: 指向多个相关 artifacts，标识横向关联

---

## 5. 概念间关系与协作模式

### 5.1 派生链 (source_*) vs 组织网 (related_*)

**派生链 (source_*)** - 纵向追溯:
- **单向传递**: 指向1个上游 artifact (禁止列表)
- **阶段传递**: 需求 → 设计 → 实现 → 任务
- **示例**: `AC` ← `source_us` ← `US`（全级别通用）；`SC` ← `source_fp` ← `FP`（L2）；`SC` ← `source_vs` ← `VS`（L1）

**组织网 (related_*)** - 横向关联:
- **多向引用**: 指向多个 artifacts (列表形式)
- **跨阶段协作**: 建立同级或跨级关联网络
- **示例**: `US` ↔ `related_ac` ↔ `AC`, `SC` ↔ `related_ts` ↔ `TS`

### 5.2 协作模式分类

**核心原则**: 一个 artifact 可同时拥有派生链和组织网，两者协作建立完整追溯体系。

| 模式类型 | source_* | related_* | 典型示例 | 说明 |
|---------|----------|-----------|---------|------|
| **纯派生型** | ✅ 有 | ❌ 无 | AC | 从单一上游派生，无横向关联 |
| **纯组织型** | ❌ 无 | ✅ 有 | TS, SEQ | 横向组织同类内容，无上游派生源 |
| **混合协作型** | ✅ 有 | ✅ 有 | SC, DES | 既从上游派生，又建立横向关联 |

**混合协作型示例** (SC):
```yaml
id: SC-AUTH-010
source_us: US-AUTH-001            # 派生链: 从需求派生
related_ts: [TS-AUTH-035]         # 组织网: 关联到测试套件
```

### 5.3 追溯机制说明

#### 5.3.1 追溯链构建原则

**派生链构建** (`source_*`):
- 每个artifact可选择性指向1个直接上游artifact
- 典型派生路径: REQUIREMENTS → DESIGN → IMPLEMENTATION → TASK_PLANNING
- 不同级别和项目可选择不同的派生起点 (如 `source_us`、`source_fp` 或 `source_des`)

**组织网构建** (`related_*`):
- 建立横向关联和跨阶段引用
- 支持多对多关系,增强追溯完整性
- 补充派生链未覆盖的关联关系

#### 5.3.2 追溯链示例

**通用追溯链骨架** (跨阶段派生):
```
US-AUTH-002 (REQUIREMENTS - 用户故事)
  ↓ source_us
[DESIGN 层 artifact]  # L1: VS, L2: FP, L3: DES
  ↓ source_<level>
SC-AUTH-030 (IMPLEMENTATION - 测试场景)
SEQ-AUTH-050 (TASK_PLANNING - 任务序列)  # 通过 related_fp 组织 FP
GOAL-AUTH-045 (TASK_PLANNING - 任务目标)  # source_us + related_sc + related_seq
```

**级别差异示例**:
- **L1-STREAMLINED**: `US → VS → SC → GOAL`（SC/GOAL 使用 `source_vs`）
- **L2-BALANCED**: `US → FP → SC → GOAL`（SC 使用 `source_fp`，GOAL 使用 `source_us`）
- **L3-RIGOROUS**: `US → DES → SC → GOAL`（SC 使用 `source_des`，GOAL 使用 `source_us`）

**追溯能力**:
- **正向追溯** (顺着source_*): `US` → `[DESIGN 层]` → `SC` → `GOAL`
- **反向追溯** (逆着source_*): `GOAL` → `SC` → `[DESIGN 层]` → `US`
- **横向追溯** (通过related_*): `US` ↔ `AC`, `SC` ↔ `TS`, `GOAL` ↔ (`SC` / `SEQ`)

> **💡 说明**: 具体采用哪种派生起点和关联方式由项目和团队决定，`[DESIGN 层]` 需参考对应级别的 Authority 文档；GOAL 的 `related_sc` / `related_seq` 应覆盖执行阶段全部场景与任务序列

---

**SPEC 命名规范核心术语唯一权威定义**
