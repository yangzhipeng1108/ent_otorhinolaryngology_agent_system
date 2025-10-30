# SPEC_ACA_L2_CHARTER - L2 BALANCED Constitutional Axioms

> 🎯 **文档定位**: L2-BALANCED质量控制宪法 + 执行层桥接索引
> 📊 **依赖文档**: `SPEC_ACA_CORE_PRINCIPLES.md` (最高抽象层,本文档实现其Constitutional Axioms)
> 🏛️ **文档级别**: Constitutional Layer - Constraint Level Philosophy
> 🔗 **对齐概念**: 本文档与`CONSTRAINT_CORE_CONCEPTS.md`中L2-BALANCED定义完全对齐
>
> **核心原则**: 本文档定义L2-BALANCED的质量控制哲学和Constitutional原则,不依赖任何具体实施文档,保持宪法层独立性。

---

## 📋 可引用原则清单 (L2 Constitutional Reference Index)

### L2约束参数 (L2 Constraint Parameters)
- **L2-P1-ConstraintParameters** - L2约束级别参数
  - **L2-P1.1-CheckpointCount** - 检查点数量: 6-10 (标准检查项,含端到端验证)
  - **L2-P1.2-PassThreshold** - 通过阈值: ≥0.95 (统一质量底线)
  - **L2-P1.3-TraceDepth** - 追溯深度: 2 (双层追溯)

### L2验收与管理 (L2 Acceptance & Management)
- **L2-P2-AcceptanceCriteria** - L2验收标准
  - **L2-P2.1-CoreDesignPrinciple** - 核心设计原则: 检查项增多(6-10) ∧ 质量不降(≥95%) ∧ 端到端验证
- **L2-P3-ArtifactManagement** - L2 Artifact管理原则
  - **L2-P3.1-Comprehensiveness** - 全面性原则: 完整价值链Artifacts (5-7个)
  - **L2-P3.2-Organization** - 组织性原则: 派生链+组织网双重追溯
  - **L2-P3.3-EndToEnd** - 端到端原则: Requirements→Design→Implementation→TaskPlanning验证映射
  - **L2-P3.4-Balance** - 平衡性原则: 核心(必须)+推荐(按需)

### L2追溯与机制 (L2 Traceability & Mechanisms)
- **L2-P4-TraceabilityChain** - L2追溯链原则
  - **L2-P4.1-DoubleLayerTrace** - 双层追溯: 同Stage内+跨Stage一层
  - **L2-P4.2-DerivationChain** - 派生链追溯: 验收标准→需求, 功能点→需求, 场景→功能点
  - **L2-P4.3-OrganizationalNet** - 组织网追溯: 测试套件→场景, 任务序列→功能点
- **L2-P5-ProducerConsumer** - L2生产者-消费者机制
  - **L2-P5.1-ThreePillarMapping** - 三支柱映射: Producer/Consumer/Toolkit
- **L2-P6-Verification** - L2验证机制
  - **L2-P6.1-AINativeFlow** - AI原生验收流程 (5步+端到端验证)
  - **L2-P6.2-ProtocolCommands** - >>protocol命令 (>>req_scan_l2等)
- **L2-P7-PDCA** - L2 PDCA循环实现

---

## TL;DR - L2 Constitutional Philosophy

**L2-BALANCED 核心哲学**:
```
质量控制偏好: 团队协作,平衡全面性与效率,标准化流程支持业务交付

Constitutional原则实现:
  CheckpointCount: 6-10 (标准检查项,覆盖完整性+可执行性+端到端)
  PassThreshold: 0.95 (统一质量底线,防范LLM幻觉)
  TraceDepth: 2 (双层追溯,支持派生链+组织网)

验收哲学:
  检查项增多 (6-10项) ∧ 质量要求不降低 (≥95%) ∧ 端到端验证
  通过率≥95% (PassThreshold统一质量底线)

Artifact管理原则:
  全面性: 命名完整价值链所需Artifacts (5-7个核心类型)
  组织性: 支持派生链+组织网的双重追溯模式
  端到端: 建立Requirements→Design→Implementation→TaskPlanning验证映射

三支柱机制:
  Producer guidance        → 建议性推敲指导
  Consumer standards       → 强制性质量门禁 (≥95%)
  Quality assurance toolkit → >>protocol质量保障工具

DbC Contract实现:
  Producer职责: 提供完整命名的价值链Artifacts
  Consumer职责: 全面验证Artifact完整性+可执行性+端到端映射 (≥95%通过)
  Invariants: PassThreshold统一 ≥ 0.95 + 端到端验证映射强制检查
```

---

## A1: L2 约束级别参数 (Constraint Level Parameters)

### L2-P1-ConstraintParameters: Constitutional原则映射
```
ConstraintGradient(Standard) = (CheckpointCount, PassThreshold, TraceDepth)
```

### L2 量化参数

| 参数 | L2取值 | 说明 |
|------|--------|------|
| **CheckpointCount** | 6-10 | 标准检查项，覆盖完整性+可执行性+端到端验证 |
| **PassThreshold** | 0.95 | 统一质量底线，防范LLM幻觉 |
| **TraceDepth** | 2 | 双层追溯（同Stage内+跨Stage一层） |

### L2 特性

| 特性 | 说明 |
|------|------|
| **Balanced** | 平衡检查全面性与执行效率 |
| **Team** | 适合团队协作，标准化流程 |
| **Hallucination-Resistant** | ≥95%通过率，质量不妥协 |

---

## A2: L2 验收标准 (Acceptance Criteria)

### L2-P2-AcceptanceCriteria: L2 核心设计原则

#### L2-P2.1-CoreDesignPrinciple: 设计原则表达
```
检查项增多 (6-10项)
  ∧
质量要求不降低 (≥95%通过率)
  ∧
端到端验证映射存在 (L2特色)
```

### L2 验收标准应用原则

**四阶段验收模式** (每个Stage应用相同的Constitutional原则):

#### 通用验收结构 (6-10项标准检查)
```markdown
## 标准验收标准（6-10项）

### 完整性验证（4项）
1. ✅ 核心Artifact存在于唯一权威位置 (独立文件或聚合文件section)
2. ✅ Artifact包含必需的追溯字段 (强制追溯链)
3. ✅ Artifact满足Stage特定完整性定义
4. ✅ Artifact覆盖价值交付路径 (包含组织型Artifacts)

### 可执行性验证（3项）
5. ✅ Artifact内容可测试/可执行 (明确边界和验收条件)
6. ✅ Artifact有唯一标识
7. ✅ 追溯链完整可验证

### 端到端验证（1项 - L2特色）
8. ✅ 端到端验证映射存在 (Requirements→Design→Implementation→TaskPlanning)

通过标准: 通过率≥95%
说明: 检查项增多（完整性+可执行性+端到端），质量要求不降低
```

**L2验收哲学**:
- **全面化检查**: 每个Stage 6-10项检查，覆盖完整性+可执行性+端到端
- **统一通过阈值**: 所有Stage采用≥95%通过率，防范LLM幻觉
- **端到端强制**: 第8项检查点强制验证跨Stage追溯链完整性 (L2核心特色)
- **双重追溯**: 支持派生链(source_*)和组织网(related_*)的验证
- **三层验证**: 完整性(4项)+可执行性(3项)+端到端(1项)的标准结构

---

## A3: L2 Artifact管理原则 (Artifact Management Principles)

### L2-P3-ArtifactManagement: Constitutional原则
```
RequirementsStage完整 := 需求描述 ∧ 验收标准 ∧ 约束声明
DesignStage完整 := 功能点定义 ∧ 价值路径映射 ∧ 接口定义
ImplementationStage完整 := 测试场景 ∧ 测试套件 ∧ 执行策略
TaskPlanningStage完整 := 任务编排 ∧ 依赖管理 ∧ 验收条件
```

### L2 Artifact管理哲学

**L2-P3.1-Comprehensiveness: 全面性原则**:
- L2命名**完整价值链所需的核心Artifacts** (5-7个核心类型)
- 覆盖派生链(需求→设计→实现→任务)的完整路径
- 每个Stage定义2-3个核心Artifact,支持团队协作

**L2-P3.2-Organization: 组织性原则**:
- 支持**派生链(source_*)**和**组织网(related_*)**的双重追溯模式
- 派生型Artifacts: 承载价值转化(需求→设计→实现)
- 组织型Artifacts: 管理协作结构(测试套件,任务编排)

**L2-P3.3-EndToEnd: 端到端原则**:
- 建立**Requirements→Design→Implementation→TaskPlanning**的验证映射
- 每个Stage的Artifacts必须支持跨Stage追溯验证
- 价值路径映射贯穿四个Stage,形成完整可追溯链

**L2-P3.4-Balance: 平衡性原则**:
- 核心Artifacts(必须命名) + 推荐Artifacts(按需命名)
- 标准化命名支持团队协作,避免过度复杂
- 追溯字段设计平衡完整性与简洁性

---

## A4: L2 追溯链原则 (Traceability Chain Principles)

### L2-P4-TraceabilityChain: Constitutional原则
```
∀ artifact ≠ root_node: ∃ traceability_link → parent_artifact

追溯完整性: 每个非根节点Artifact必须有明确的追溯关系
追溯验证性: 追溯链必须可验证,支持DbC Contract检查
双重追溯性: 支持派生链(source_*)和组织网(related_*)
```

### L2-P4.1-DoubleLayerTrace: L2 追溯深度原则 (TraceDepth = 2)

**L2追溯哲学**:
- **双层追溯**: 同Stage内直接追溯 + 跨Stage一层追溯
- **派生链强制**: 核心派生路径(需求→设计→实现→任务)必须建立source_*追溯
- **组织网强制**: 组织型Artifacts必须建立related_*关联关系
- **端到端验证**: 追溯链支持完整的跨Stage端到端验证

**L2追溯模式**:

**L2-P4.2-DerivationChain: 派生链追溯**:
- 验收标准→需求描述, 功能点→需求描述, 场景→功能点
**L2-P4.3-OrganizationalNet: 组织网追溯**:
- 测试套件→场景, 任务序列→功能点
- **双向验证**: 支持自顶向下(需求覆盖)和自底向上(实现追溯)的验证
- **网状结构**: 允许多对多关联,支持复杂团队协作场景

**L2追溯验证原则**:
- 所有派生型Artifacts必须有source_*字段
- 所有组织型Artifacts必须有related_*字段
- 追溯链完整性可通过自动化工具验证
- 端到端追溯路径必须可查询可审计

---

## A5: L2 Producer-Consumer机制 (P-C Mechanism)

### L2-P5-ProducerConsumer: Constitutional原则
```
Producer: Goals → Artifacts (Verify = true)
Consumer: Artifacts → Complete ∧ Satisfiable ∧ Traceable
职责分离: Producer ⊥ Consumer
```

### L2-P5.1-ThreePillarMapping: L2 三支柱映射

| 角色 | L2实现 | 位置 | 特征 | 禁止内容 |
|------|--------|------|------|---------|
| **Producer** | Producer guidance | 建议性语言、动态内容 | ❌不包含验收标准、质量门禁 |
| **Consumer** | Consumer standards | 强制性语言、结构化报告 | ❌不包含推敲指导、实现建议 |
| **Toolkit** | Quality assurance toolkit | >>protocol、100%触发 | 质量保障与修复机制 (尤其人介入后) |

### L2 职责分离验证

**验证维度**:
- Producer文档: 不应包含强制性语言 (必须满足, 通过标准等)
- Consumer文档: 不应包含建议性语言 (可以考虑, 建议等)
- Toolkit文档: 必须使用>>protocol确保质量保障，尤其支持人介入后的修复流程

---

## A6: L2 验证机制 (Verification Mechanism)

### L2-P6-Verification: Constitutional原则
```
每个Invariant必须有验证机制
验证失败必须提供失败原因与修复建议
```

### L2-P6.1-AINativeFlow: L2 AI-native验收流程

```
验证流程 (5步):
  1. Read Consumer standards document
  2. 使用Read/Grep/Find检查artifacts
  3. 输出结构化验收报告
     ### ✅ 通过项 (n/total) + 证据
     ### ❌ 失败项 (m/total) + 证据 + 修复建议
     通过率: (n/total) × 100%
  4. 判定: 通过率 ≥ 0.95 → ✅ | < 0.95 → ❌
  5. 失败 → Trigger Human-in-the-loop

L2判定阈值: ≥95% (统一质量底线，防范LLM幻觉)

L2特色: 端到端验证映射检查（第8项检查点）
```

### L2-P6.2-ProtocolCommands: L2 >>protocol命令

```
>>protocol机制 (抽象定义):
  用户输入: >>quality_check_l2
    → AI Agent强制读取Quality assurance toolkit document
    → 执行质量检查与修复指导流程
    → 输出L2结构化报告 + 修复建议

质量保障类型:
  - Requirements quality assurance
  - Design quality assurance
  - Implementation quality assurance
  - Task Planning quality assurance

说明: 具体>>命令映射见附录"SPEC框架实现映射"
```

---

## A7: L2 PDCA循环实现 (PDCA Cycle)

### L2-P7-PDCA: Constitutional原则
```
∀ task: Pre(task) → (Plan → Do → Check → Act) → Post(task)
Pre ≡ false → FORBIDDEN | Post ≡ false → Rollback ∧ EmergencyProtocol
```

### L2 PDCA执行协议

| 阶段 | L2实现 | 失败处理 |
|------|--------|---------|
| **Plan** | Precondition检查(3项): Canonical_Uniqueness + Parent_Existence + Goal_Coverage | Pre失败 → STOP + 修复 + 重试 |
| **Do** | 创建artifact + 遵守I1-I4 + 参考Producer guidance(可选) + 建立端到端追溯(推荐) | - |
| **Check** | Postcondition验证(3项) + Consumer standards验收(≥95%) + 端到端映射检查 | Post失败 → Act决策 |
| **Act** | 通过→Continue \| retry<3→Retry \| retry≥3→Escalate \| 严重违反→Rollback | - |

### L2 PDCA示例

```
任务: 创建Requirements Stage的UserStory artifact (L2级别)

Plan:
  ✓ Goals: 定义用户登录需求
  ✓ Constraints: 使用L2-BALANCED约束
  ✓ Precondition:
    - Canonical_Uniqueness: 权威位置不存在重复artifact
    - Parent_Existence: 根节点artifact，无需parent
    - Goal_Coverage: US完整性定义在Goals中

Do:
  ✓ 创建artifact: 写入唯一权威位置 (独立文件或聚合文件section)
  ✓ 填充内容: 遵守I1-I4
  ✓ 参考Producer guidance(可选)
  ✓ 准备端到端追溯: 预留AC→US强制追溯

Check:
  ✓ Postcondition验证(3项):
    - ¬∃ duplicate_outside_canonical
    - Completeness_Definition_Satisfied
    - Traceability_Link_Valid
  ✓ Consumer standards验收:
    - 完整性验证（4项）: 全部通过
    - 可执行性验证（3项）: 全部通过
    - 端到端验证（1项）: AC创建后可建立完整追溯链
    - 通过率: 8/8 = 100%

Act:
  ✓ Continue (100% ≥ 95%)
```

---

## 📊 L2 完整映射表

### L2 量化参数总览

| 参数 | L2取值 | Constitutional映射 |
|------|--------|-------------------|
| CheckpointCount | 6-10 | Standard检查点 |
| PassThreshold | 0.95 | 统一质量底线 |
| TraceDepth | 2 | 双层追溯 |
| 验收标准 | 通过率≥95% | ≥95%通过率 |

### L2 四阶段验收清单

| Stage | 核心检查项 | 通过标准 |
|-------|----------|---------|
| Requirements | 6-10项（完整性4+可执行性3+端到端1） | ≥95% |
| Design | 6-10项（完整性4+可执行性3+端到端1） | ≥95% |
| Implementation | 6-10项（完整性4+可执行性3+端到端1） | ≥95% |
| Task_Planning | 6-10项（完整性4+可执行性3+端到端1） | ≥95% |

### L2 vs Constitutional 映射关系

```
Constitutional Axioms (SPEC_ACA_CORE_PRINCIPLES.md)
         ↓ 实现
L2-BALANCED Constitutional Principles (本文档)
         ↓ 指导
Framework Implementation (Producer/Consumer/Toolkit)
         ↓ 生成
Project Artifacts
```

### L2 端到端验证映射原则

**端到端链路** (L2核心特色):
```
Requirements → Design → Implementation → Task_Planning
(需求定义)   (价值映射)  (场景验证)      (任务编排)
```

**L2验证哲学**:
- **第8项检查点强制**: 每个Stage必须验证端到端追溯链存在性
- **派生链验证**: 验收标准→需求, 功能点→需求, 场景→功能点的完整路径
- **组织网验证**: 测试套件→场景, 任务序列→功能点的关联关系
- **双重可追溯性**: 支持自顶向下和自底向上的双向追溯验证

---

## Bridge Reference

### Core Signals
- PassThreshold ≥ 0.95；CheckpointCount 6–10；TraceDepth = 2。
- Requirements → Design → Implementation → Task_Planning 需形成端到端验证链并保持组织网追溯。

### Execution Guidance (概念层)
- 以方法论总览校准 AI 执行节奏，保持四阶段串联顺畅。
- Authoring 阶段落实 L2 完整性：覆盖端到端链路与组织网追溯。
- 按 L2 质量门禁模板组织 6–10 项检查点，兼顾完整性、可执行性与端到端映射。
- 分阶段执行 L2 级别的 >>protocol 流程，保存判定、证据与整改动作。
- 维护命名与追溯约束，确保 ID、SN、source_*、related_* 等字段可双向追溯。
- 结合调整指南实现整改闭环，必要时触发 Emergency Protocol。
- 将 L2 checkpoint 融入 AI 执行流程，维持审查与交付节奏的稳定。

### Collaboration & Operations
- 交互模式通常为 C2-PARTICIPATE；阶段交付后记录端到端链路状态与证据。
- >>protocol 输出低于 0.95 时按 E1 紧急协议执行，补写或回滚并归档。
- 执行 >>req/>>design/>>impl/>>task_scan_l2；TraceDepth = 2，保持派生链与组织网的双向追溯。

---

*L2 Authority: Standard约束级别的Constitutional原则*
