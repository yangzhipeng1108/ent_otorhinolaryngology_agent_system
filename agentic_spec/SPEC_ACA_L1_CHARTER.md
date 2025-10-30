# SPEC_ACA_L1_CHARTER - L1 STREAMLINED Constitutional Axioms & Execution Index

> 🎯 **文档定位**: L1-STREAMLINED质量控制宪法 + 执行层桥接索引
> 📊 **依赖文档**: `SPEC_ACA_CORE_PRINCIPLES.md` (最高抽象层,本文档实现其Constitutional Axioms)
> 🏛️ **文档级别**: Constitutional Layer - Constraint Level Philosophy
> 🔗 **对齐概念**: 本文档与`CONSTRAINT_CORE_CONCEPTS.md`中L1-STREAMLINED定义完全对齐
>
> **核心原则**: 本文档定义L1-STREAMLINED的质量控制哲学和Constitutional原则,不依赖任何具体实施文档,保持宪法层独立性。

---

## 📋 可引用原则清单 (L1 Constitutional Reference Index)

### L1约束参数 (L1 Constraint Parameters)
- **L1-P1-ConstraintParameters** - L1约束级别参数
  - **L1-P1.1-CheckpointCount** - 检查点数量: 4-6 (核心检查项)
  - **L1-P1.2-PassThreshold** - 通过阈值: ≥0.95 (统一质量底线)
  - **L1-P1.3-TraceDepth** - 追溯深度: 1 (单层追溯)

### L1验收与管理 (L1 Acceptance & Management)
- **L1-P2-AcceptanceCriteria** - L1验收标准
  - **L1-P2.1-CoreDesignPrinciple** - 核心设计原则: 检查项少(4-6) ∧ 质量高(≥95%) ∧ 容忍低
- **L1-P3-ArtifactManagement** - L1 Artifact管理原则
  - **L1-P3.1-CoreFocus** - 核心性原则: 仅命名核心价值交付所需的关键Artifacts (3-5个)
  - **L1-P3.2-Simplicity** - 简洁性原则: 平面结构, 避免过度设计
  - **L1-P3.3-Traceability** - 追溯性原则: TraceDepth=1的基础追溯链

### L1追溯与机制 (L1 Traceability & Mechanisms)
- **L1-P4-TraceabilityChain** - L1追溯链原则
  - **L1-P4.1-SingleLayerTrace** - 单层追溯: 同Stage内直接追溯关系
- **L1-P5-ProducerConsumer** - L1生产者-消费者机制
  - **L1-P5.1-ThreePillarMapping** - 三支柱映射: Producer/Consumer/Toolkit
- **L1-P6-Verification** - L1验证机制
  - **L1-P6.1-AINativeFlow** - AI原生验收流程 (5步)
  - **L1-P6.2-ProtocolCommands** - >>protocol命令 (>>req_scan_l1等)
- **L1-P7-PDCA** - L1 PDCA循环实现

---

## TL;DR - L1 Constitutional Philosophy

**L1-STREAMLINED 核心哲学**:
```
质量控制偏好: 快速迭代,聚焦核心价值交付,优先速度容忍合理妥协

Constitutional原则实现:
  CheckpointCount: 4-6 (最小化检查项,聚焦核心)
  PassThreshold: 0.95 (统一质量底线,防范LLM幻觉)
  TraceDepth: 1 (单层追溯,简化依赖)

验收哲学:
  检查项少 (4-6项) ∧ 质量要求高 (≥95%) ∧ 容忍度极低
  通过率≥95% (PassThreshold统一质量底线)

Artifact管理原则:
  核心性: 仅命名核心价值交付所需的关键Artifacts (3-5个核心类型)
  简洁性: 平面结构,避免过度设计
  追溯性: 建立基础追溯链,支持DbC Contract

三支柱机制:
  Producer guidance        → 建议性推敲指导
  Consumer standards       → 强制性质量门禁 (≥95%)
  Quality assurance toolkit → >>protocol质量保障工具

DbC Contract实现:
  Producer职责: 提供清晰命名的核心Artifacts
  Consumer职责: 快速验证Artifact可用性 (≥95%通过)
  Invariants: PassThreshold统一 ≥ 0.95
```

---

## A1: L1 约束级别参数 (Constraint Level Parameters)

### L1-P1-ConstraintParameters: Constitutional原则映射
```
ConstraintGradient(Minimal) = (CheckpointCount, PassThreshold, TraceDepth)
```

### L1 量化参数

| 参数 | L1取值 | 说明 |
|------|--------|------|
| **CheckpointCount** | 4-6 | 核心检查项，覆盖关键质量维度 (主要验收组数量,每组可包含3-5个子验收项) |
| **PassThreshold** | 0.95 | 统一质量底线，防范LLM幻觉 |
| **TraceDepth** | 1 | 单层追溯（同Stage内强制追溯） |

### L1 特性

| 特性 | 说明 |
|------|------|
| **Essential** | 仅检查核心必要项，聚焦价值交付 |
| **Fast** | 检查项少，验收速度快 |
| **Hallucination-Resistant** | ≥95%通过率，质量不妥协 |

---

## A2: L1 验收标准 (Acceptance Criteria)

### L1-P2-AcceptanceCriteria: L1 核心设计原则

#### L1-P2.1-CoreDesignPrinciple: 设计原则表达
```
检查项少 (4-6项)
  ∧
质量要求高 (≥95%通过率)
  ∧
容忍度极低 (最多允许5%失败)
```

### L1 验收标准应用原则

**四阶段验收模式** (每个Stage应用相同的Constitutional原则):

#### 通用验收结构 (4-6项核心检查)
```markdown
## 核心验收标准（4-6项）

### 完整性验证（典型4项）
1. ✅ 核心Artifact存在于唯一权威位置 (独立文件或聚合文件section)
2. ✅ Artifact包含必需的追溯字段 (强制追溯链)
3. ✅ Artifact满足Stage特定完整性定义
4. ✅ Artifact覆盖核心价值交付路径

通过标准: 通过率≥95%
说明: 检查项少但质量要求高，容忍度极低
```

**L1验收哲学**:
- **最小化检查项**: 每个Stage仅4-6项核心检查，聚焦关键质量维度
- **统一通过阈值**: 所有Stage采用≥95%通过率，防范LLM幻觉
- **快速失败机制**: 任何核心检查失败立即触发Human-in-the-loop
- **通用模板**: 四个Stage应用相同的验收结构原则,体现L1统一质量哲学

---

## A3: L1 Artifact管理原则 (Artifact Management Principles)

### L1-P3-ArtifactManagement: Constitutional原则
```
RequirementsStage完整 := 需求描述 ∧ 验收标准 ∧ 约束声明
DesignStage完整 := 架构设计 ∧ 接口定义 ∧ 数据流向
ImplementationStage完整 := 测试策略 ∧ 测试场景 ∧ 实现路径
TaskPlanningStage完整 := 任务分解 ∧ 依赖关系 ∧ 验收条件
```

### L1 Artifact管理哲学

**L1-P3.1-CoreFocus: 核心性原则**:
- L1仅命名**核心价值交付所需的关键Artifacts**
- 保持**3-5个核心类型**,避免过度设计
- 每个Stage定义1-2个核心Artifact即可

**L1-P3.2-Simplicity: 简洁性原则**:
- 采用**平面结构**,避免复杂层次嵌套
- 独立文档设计,最小化依赖关系
- 每个Artifact职责单一,边界清晰

**L1-P3.3-Traceability: 追溯性原则**:
- 建立**TraceDepth=1的基础追溯链**
- 强制追溯关系保持简单明确
- 支持DbC Contract验证机制
- 每个Stage 1-2个核心Artifact,追溯链平面简洁

---

## A4: L1 追溯链原则 (Traceability Chain Principles)

### L1-P4-TraceabilityChain: Constitutional原则
```
∀ artifact ≠ root_node: ∃ traceability_link → parent_artifact

追溯完整性: 每个非根节点Artifact必须有明确的追溯关系
追溯验证性: 追溯链必须可验证,支持DbC Contract检查
```

### L1-P4.1-SingleLayerTrace: L1 追溯深度原则 (TraceDepth = 1)

**L1追溯哲学**:
- **单层追溯**: 同Stage内的Artifacts建立直接追溯关系
- **简化依赖**: 避免复杂的跨Stage多层追溯
- **快速验证**: 追溯链验证成本低,支持快速迭代

**L1追溯模式**:
- **强制追溯**: 核心Artifacts必须建立明确的追溯关系
- **可选追溯**: 推荐Artifacts的追溯关系可根据项目需要选择
- **双线架构**: 支持验收线和实施线的并行追溯
- **简化验证**: 追溯链验证使用简单的存在性检查即可

---

## A5: L1 Producer-Consumer机制 (P-C Mechanism)

### L1-P5-ProducerConsumer: Constitutional原则
```
Producer: Goals → Artifacts (Verify = true)
Consumer: Artifacts → Complete ∧ Satisfiable ∧ Traceable
职责分离: Producer ⊥ Consumer
```

### L1-P5.1-ThreePillarMapping: L1 三支柱映射

| 角色 | Constitutional定义 | 特征 | 职责边界 |
|------|-------------------|------|---------|
| **Producer** | Producer guidance | 建议性语言、动态内容 | ❌不包含验收标准、质量门禁 |
| **Consumer** | Consumer standards | 强制性语言、结构化报告 | ❌不包含推敲指导、实现建议 |
| **Toolkit** | Quality assurance toolkit | >>protocol、100%触发 | 质量保障与修复机制 (尤其人介入后) |

### L1 职责分离验证原则

**验证维度**:
- Producer文档: 不应包含强制性语言 (必须满足, 通过标准等)
- Consumer文档: 不应包含建议性语言 (可以考虑, 建议等)
- Toolkit文档: 必须使用>>protocol确保质量保障，尤其支持人介入后的修复流程

---

## A6: L1 验证机制 (Verification Mechanism)

### L1-P6-Verification: Constitutional原则
```
每个Invariant必须有验证机制
验证失败必须提供失败原因与修复建议
```

### L1-P6.1-AINativeFlow: L1 AI-native验收流程

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

L1判定阈值: ≥95% (统一质量底线，防范LLM幻觉)
```

### L1-P6.2-ProtocolCommands: L1 >>protocol命令

```
>>protocol机制 (抽象定义):
  用户输入: >>quality_check_l1
    → AI Agent强制读取Quality assurance toolkit document
    → 执行质量检查与修复指导流程
    → 输出L1结构化报告 + 修复建议

质量保障类型:
  - Requirements quality assurance
  - Design quality assurance
  - Implementation quality assurance
  - Task Planning quality assurance

说明: 具体>>命令映射见附录"SPEC框架实现映射"
```

---

## A7: L1 PDCA循环实现 (PDCA Cycle)

### L1-P7-PDCA: Constitutional原则
```
∀ task: Pre(task) → (Plan → Do → Check → Act) → Post(task)
Pre ≡ false → FORBIDDEN | Post ≡ false → Rollback ∧ EmergencyProtocol
```

### L1 PDCA执行协议

| 阶段 | L1实现 | 失败处理 |
|------|--------|---------|
| **Plan** | Precondition检查(3项): Canonical_Uniqueness + Parent_Existence + Goal_Coverage | Pre失败 → STOP + 修复 + 重试 |
| **Do** | 创建artifact + 遵守I1-I4 + 参考Producer guidance(可选) | - |
| **Check** | Postcondition验证(3项) + Consumer standards验收(≥95%) | Post失败 → Act决策 |
| **Act** | 通过→Continue \| retry<3→Retry \| retry≥3→Escalate \| 严重违反→Rollback | - |

### L1 PDCA示例

```
任务: 创建Requirements Stage的UserStory artifact (L1级别)

Plan:
  ✓ Goals: 定义用户需求
  ✓ Constraints: 使用L1-STREAMLINED约束
  ✓ Precondition:
    - Canonical_Uniqueness: 权威位置不存在重复artifact
    - Parent_Existence: 根节点artifact，无需parent
    - Goal_Coverage: artifact完整性定义在Goals中

Do:
  ✓ 创建artifact: 写入唯一权威位置 (独立文件或聚合文件section)
  ✓ 填充内容: 遵守I1(权威位置) + I2(完整性) + I3(质量三元组) + I4(追溯链)
  ✓ 参考Producer guidance(可选)

Check:
  ✓ Postcondition验证(3项):
    - ¬∃ duplicate_outside_canonical
    - Completeness_Definition_Satisfied
    - Traceability_Link_Valid
  ✓ Consumer standards验收:
    - 4项核心检查全部通过
    - 通过率: 4/4 = 100%

Act:
  ✓ Continue (100% ≥ 95%)
```

---

## 📊 L1 完整映射表

### L1 量化参数总览

| 参数 | L1取值 | Constitutional映射 |
|------|--------|-------------------|
| CheckpointCount | 4-6 | Minimal检查点 |
| PassThreshold | 0.95 | 统一质量底线 |
| TraceDepth | 1 | 单层追溯 |
| 验收标准 | 通过率≥95% | ≥95%通过率 |

### L1 四阶段验收清单

| Stage | 核心检查项 | 通过标准 |
|-------|----------|---------|
| Requirements | 4-6项（需求描述+验收标准+约束声明存在性+完整性） | ≥95% |
| Design | 4-6项（架构设计+接口定义+数据流向存在性+完整性） | ≥95% |
| Implementation | 4-6项（测试策略+测试场景+实现路径存在性+完整性） | ≥95% |
| Task_Planning | 4-6项（任务分解+依赖关系+验收条件存在性+完整性） | ≥95% |

### L1 vs Constitutional 映射关系

```
Constitutional Axioms (SPEC_ACA_CORE_PRINCIPLES.md)
         ↓ 实现
L1-STREAMLINED Constitutional Principles (本文档)
         ↓ 指导
Framework Implementation (Producer/Consumer/Toolkit)
         ↓ 生成
Project Artifacts
```

---

## Bridge Reference

### Core Signals
- PassThreshold ≥ 0.95；CheckpointCount 4–6；TraceDepth = 1。
- Producer / Consumer / Toolkit：建议性推敲、质量门禁、>>protocol。
- Implementation 与 Task Planning 聚焦于支撑快速交付的必要要素。

### Execution Guidance (概念层)
- 依据整体方法论，保持四阶段策划与 AI 协作节奏一致。
- Authoring 阶段确保 L1 完整性：聚焦最小化的核心产物与对应追溯要求。
- 应用 L1 质量门禁定义（4–6 项检查点、Pass ≥0.95），生成可复核的验收记录。
- 在关键节点执行 L1 级 >>protocol 流程，并保留证据与整改动作。
- 严格维护命名与追溯不变量（ID、SN、source_* 等），保证唯一性与可逆追溯。
- 结合调整指南维护整改闭环；当质量不足时触发 Emergency Protocol。
- 将 L1 checkpoint 嵌入 AI 执行流程，确保节奏与上下文保持一致。

### Collaboration & Operations
- 交互默认 C1-CONFIRM；阶段转换前执行一次目标复述，确保上下文一致。
- >>protocol 报告 <0.95 时，按 E1 紧急协议决定回滚或补写并归档证据。
- 生成或修订阶段资产后执行 >>req/>>design/>>impl/>>task_scan_l1；TraceDepth 保持 1，必要时在后续阶段补充追溯链。

---

*L1 Authority: Minimal约束级别的Constitutional原则*
