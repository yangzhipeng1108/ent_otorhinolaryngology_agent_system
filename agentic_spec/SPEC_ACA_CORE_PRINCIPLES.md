# SPEC AI Coding Agent 执行原则（AI Execution Charter）

> 🎯 **文档定位**: AI Coding Agent的Constitutional-level执行原则 - 框架无关的核心不变量与契约协议
> 📊 **适用范围**: 任何基于契约式设计的AI-Assisted开发框架
> 🏛️ **权威级别**: Constitutional-level（宪法级）- 定义"AI必须遵守什么"的基本公理
> 🔗 **泛化性**: 与具体实现解耦，可应用于多种框架（SPEC/其他AI框架）
>
> **核心哲学**: Design by Contract（契约式设计）最大化AI-Human协作效能
> **设计原则**: 抽象优先（Abstract First）、实现示例（Implementation Examples）、框架无关（Framework-Agnostic）

---

## 📋 可引用原则清单 (Constitutional Reference Index)

### 四大不变量 (Four Invariants)
- **I1-CanonicalLocationUniqueness** - 权威位置唯一性: ∀ asset_type: ∃! canonical_location
- **I2-CompletenessPrinciple** - 完整性原则: ∀ artifact: Complete(artifact) = true
- **I3-QualityVerificationTriple** - 质量验证三元组: {Pre} AI_Create {Post: Verify}
- **I4-DependencyChainIntegrity** - 依赖链完整性: ∀ artifact ≠ root: ∃ trace_link → parent

### 核心概念 (Core Concepts)
- **C1-ConstraintGradient** - 约束级别梯度原则: Level → (CheckpointCount, PassThreshold, TraceDepth)
  - **C1.1-MinimalLevel** - Minimal级别: CheckpointCount[n_min], PassThreshold≥0.95, TraceDepth=1
  - **C1.2-StandardLevel** - Standard级别: CheckpointCount[n_std], PassThreshold≥0.95, TraceDepth=2
  - **C1.3-StrictLevel** - Strict级别: CheckpointCount[n_max], PassThreshold≥0.95, TraceDepth=3+
- **C2-PDCA** - PDCA循环执行协议: Plan → Do → Check → Act (契约式设计实践形式)
  - **C2.1-Plan** - Plan阶段 (Preconditions): 规划执行方案 + 前置条件检查
  - **C2.3-Check** - Check阶段 (Postconditions): 后置条件验证 + Quality Gates
  - Note: Do和Act融合在PDCA闭环中,无独立谓词定义
- **C3-ProducerConsumerContract** - 生产者-消费者契约: Producer ⊥ Consumer (职责分离)
  - **C3.1-ProducerRole** - 生产者职责: {Pre: Goals/Intent/Constraints} → {Post: Verify(artifacts)}
  - **C3.2-ConsumerRole** - 消费者职责: {Pre: Artifacts存在} → {Post: Quality gates通过 ∨ Failure}

### 验证机制 (Verification Mechanisms)
- **V1-ScriptDrivenVerification** - 脚本驱动验证: CLI命令执行, 结构化日志输出
- **V2-AINativeVerification** - AI原生验证: 工具检查 + 结构化报告 + 阈值判定 (≥95%)
- **V3-HybridVerification** - 混合验证: 脚本自动检查 + AI语义验证

### 紧急协议 (Emergency Protocol)
- **E1-EmergencyProtocol** - 紧急协议: STOP → Report → Rollback → Fix → Verify → Resume

---

## 形式化定义域 (Formal Definition Domain)

```
∀ framework ∈ DbC_AI_Frameworks:
  Constitutional_Axioms(framework) = {I1, I2, I3, I4} ∧ {C1, C2, C3}

层次关系:
  Constitutional(axioms) → Framework(protocols) → Implementation(artifacts)
  Implementation不得修改Constitutional公理 (单调性)
```

---

## 基本定理 (Fundamental Theorem)

```
∀ project ∈ DbC_AI_Assisted_Systems:
  Invariants_Hold(project) → Quality_Guaranteed(project)
                            ∧ Traceability_Complete(project)
                            ∧ DRY_Enforced(project)

形式化表达:
  ⊢ (I1 ∧ I2 ∧ I3 ∧ I4) → (Quality ∧ Traceability ∧ DRY)

  where:
    I1 = Canonical_Location_Uniqueness
    I2 = Completeness_Principle
    I3 = Quality_Verification_Triple
    I4 = Dependency_Chain_Integrity
```

---

## 四大不变量 (Four Invariants) - 绝对不可违反

### I1-CanonicalLocationUniqueness: Canonical Location Uniqueness（权威位置唯一性）

```
∀ asset_type（资产类型）: ∃!（存在唯一）canonical_location（权威位置）

抽象定义:
  asset_type → canonical_location 的映射必须是单射（injective）
  同类型资产只能存在于唯一的权威位置
  权威位置必须明确定义且可验证
```

---

### I2-CompletenessPrinciple: Completeness Principle（完整性原则）

```
∀ artifact: Complete(artifact) := 满足artifact类型的完整性定义

抽象完整性定义（type-parametric template）:
  ∀ stage ∈ DevelopmentStages:
    Complete(stage) := CoreDeliverable(stage) ∧ VerificationCriteria(stage) ∧ ConstraintSpecification(stage)

  通用三元组模板:
    Stage_Completeness := {What: 核心产出, How: 验证标准, Boundary: 约束边界}

  形式化映射示例:
    Requirements_Stage   := Description ∧ AcceptanceCriteria ∧ ConstraintDeclaration
    Design_Stage         := Architecture ∧ InterfaceSpecification ∧ DataFlowDefinition
    Implementation_Stage := TestStrategy ∧ TestScenarios ∧ ExecutionPath
    TaskPlanning_Stage   := TaskDecomposition ∧ DependencyGraph ∧ CompletionCriteria
```

**Precondition（前置条件）**: artifact类型的完整性定义已知
**Postcondition（后置条件）**: ∀ artifact: Complete(artifact) = true

---

### I3-QualityVerificationTriple: Quality Verification Triple（质量验证三元组）

```
{Goals已定义 ∧ Constraints清晰}
  AI创建artifact（产物）
{Complete（完整） ∧ Satisfiable（可满足） ∧ Traceable（可追溯）}
```

**验证谓词 (Verify predicate)**:
```
Verify(artifact) :=
  Complete(artifact) ∧      // 完整性：满足类型定义
  Satisfiable(artifact) ∧   // 可满足性：Constraints可验证
  Traceable(artifact)       // 追溯性：依赖链路存在
```

---

### I4-DependencyChainIntegrity: Dependency Chain Integrity（依赖链完整性）

```
∀ artifact (除根节点): ∃ traceability_link → parent_artifact

抽象追溯链模板:
  MandatoryTrace := ChildArtifact → ParentArtifact  (同Stage内细化关系强制)
  OptionalTrace  := Stage_N → Stage_(N-1)           (跨Stage依赖关系可选)

形式化追溯类型:
  1. Refinement Trace (强制):
     AcceptanceCriteria → RequirementDescription

  2. Cross-Stage Trace (可选):
     DesignArtifacts → RequirementsArtifacts
     ImplementationArtifacts → DesignArtifacts
     TaskPlanningArtifacts → ImplementationArtifacts
```

**传递追溯性 (Transitive traceability)**:
```
∀ a, b, c ∈ artifacts:
  Trace(a, b) ∧ Trace(b, c) ⊢ Trace_Transitive(a, c)

抽象示例:
  RequirementsArtifacts → AcceptanceCriteria ∧ AcceptanceCriteria ⇝ TaskPlanningArtifacts
  ⊢ RequirementsArtifacts ⇝ TaskPlanningArtifacts (端到端追溯性保证)
```

---

## C1-ConstraintGradient: 约束级别梯度原则 (Constraint Level Gradient Principle)

```
定义域:
  Level ∈ {Minimal, Standard, Strict}
  ConstraintGradient: Level → ℕ × ℝ × ℕ

量化函数:
  ConstraintGradient(l) = (CheckpointCount(l), PassThreshold(l), TraceDepth(l))

  where:
    CheckpointCount: ℕ       // 检查点数量
    PassThreshold: ℝ ∈ [0,1] // 通过率阈值
    TraceDepth: ℕ            // 追溯链路深度

严格偏序关系 (Strict Partial Order):
  ∀ l1, l2 ∈ Level: l1 ≤ l2 ⟺
    CheckpointCount(l1) ≤ CheckpointCount(l2) ∧
    TraceDepth(l1) ≤ TraceDepth(l2)

  偏序链: Minimal ≤ Standard ≤ Strict

  核心设计原则:
    PassThreshold = 0.95 (所有级别统一) - 防范LLM幻觉的质量底线
    级别区分通过CheckpointCount实现 - 检查全面性而非容错率

抽象参数范围:
  n_min, n_std, n_max ∈ ℕ+  (框架自定义检查点数量范围)
  δ ∈ ℕ+                    (级别内浮动空间)
```

### 约束级别定义 (Constraint Level Definitions)

#### C1.1-MinimalLevel: Minimal级别 (最小约束级)

```
CheckpointCount: [n_min, n_min+δ]
PassThreshold: ≥0.95
TraceDepth: 1

特性 (Characteristics):
  Essential ∧ Fast ∧ Hallucination-Resistant
```

#### C1.2-StandardLevel: Standard级别 (标准约束级)

```
CheckpointCount: [n_std, n_std+δ]
PassThreshold: ≥0.95
TraceDepth: 2

特性 (Characteristics):
  Balanced ∧ Team ∧ Hallucination-Resistant
```

#### C1.3-StrictLevel: Strict级别 (严格约束级)

```
CheckpointCount: [n_max, n_max+δ]
PassThreshold: ≥0.95
TraceDepth: 3+

特性 (Characteristics):
  Complete ∧ Full ∧ Hallucination-Resistant
```

---

## 执行协议 (Execution Protocol)

### C2-PDCA: PDCA循环 - 契约式设计的实践形式

```
Plan:  规划执行方案 + Precondition检查
Do:    创建artifact + 遵守Invariants
Check: Postcondition验证 + Quality Gates
Act:   决策(继续|重试|升级|回滚)
```

#### C2.1-Plan: Preconditions（前置条件）- Plan阶段

```
Pre(create_artifact) :≡
  1. Canonical_Uniqueness_Check(artifact_type, location)
     → ¬∃ duplicate(artifact_type, canonical_location)

  2. Parent_Existence_Check(artifact)
     → (artifact = root_node) ∨ ∃ parent ∈ artifacts: Valid_Chain(parent)

  3. Goal_Coverage_Check(artifact_type, goals)
     → Completeness_Definition(artifact_type) ⊆ Goals

形式化保证:
  Pre ≡ true ⟺ Safe_To_Create(artifact)
  Pre ≡ false → FORBIDDEN(create_artifact)
```

**失败语义**:
- Pre ≡ false → STOP ∧ Report(PreViolation) ∧ Fix ∧ Retry
- 无法修复 → Escalate(Human-in-the-loop)

#### C2.3-Check: Postconditions（后置条件）- Check阶段

```
Post(artifact_created) :≡
  1. ¬∃ duplicate_outside_canonical(artifact)
  2. Completeness_Definition_Satisfied(artifact)
  3. Traceability_Link_Valid(artifact)

形式化验证:
  ∀ artifact ≠ root_node:
    Post(artifact) = true ⟺ Verify(artifact) = true
```

**失败语义**:
- Post ≡ false → Act(修正) ∨ Escalate(Human-in-the-loop)
- Retry机制: retry_count ≤ max_retry_threshold

---

## 契约定义 (Contract Definitions)

### C3-ProducerConsumerContract: Producer-Consumer Contract（生产者-消费者契约）

#### C3.1-ProducerRole: Producer（生产者）角色定义

```
职责 (Responsibilities):
  创建Development Artifacts (覆盖所有开发阶段)

契约 (Contract):
  Precondition:  Goals/Intent/Constraints已定义
  Produces: Development Artifacts (Requirements, Design, Implementation, Tasks)
  Postcondition: Verify(artifacts) = true

形式化表达:
  {Pre: Goals ∧ Intent ∧ Constraints}
    Producer.Create(artifacts)
  {Post: ∀a ∈ artifacts: Verify(a) = true}
```

#### C3.2-ConsumerRole: Consumer（消费者）角色定义

```
职责 (Responsibilities):
  验证Artifacts质量,执行Quality Gates

契约 (Contract):
  Precondition:  Artifacts存在
  Verifies: Complete ∧ Satisfiable ∧ Traceable
  Postcondition: Quality gates通过 ∨ QualityGateFailure

形式化表达:
  {Pre: ∃artifacts}
    Consumer.Verify(artifacts)
  {Post: QualityGates(Pass) ∨ QualityGateFailure(Evidence)}

失败处理:
  QualityGateFailure → Escalate(Human-in-the-loop) ∨ Retry(Producer)
```

---

## 验证机制 (Verification Mechanisms)

### 验证模式分类

### V1-ScriptDrivenVerification: Script-Driven Verification (脚本驱动验证)
```
抽象模式:
  verify_invariant_i1 → check_canonical_uniqueness
  verify_invariant_i2 → check_completeness
  verify_invariant_i4 → check_traceability
  verify_all          → aggregate(i1, i2, i3, i4)
```

### V2-AINativeVerification: AI-Native Verification (AI原生验证)
```
执行流程:
  1. AI Agent reads verification standards (machine-readable format)
  2. AI Agent uses tools (Read/Grep/AST parsing) to inspect artifacts
  3. AI Agent outputs structured report:
     ✅ Passed items (n/total) + evidence
     ❌ Failed items (m/total) + evidence + remediation suggestions
     Pass rate: (n/total) × 100%
  4. AI Agent determines: pass rate ≥ threshold → ✅ | < threshold → ❌
  5. If failed: Trigger escalation (e.g., Human-in-the-loop)
```

### V3-HybridVerification: Hybrid Verification (混合验证)
```
Script verification for automated checks (e.g., file existence, syntax)
AI-native verification for semantic checks (e.g., completeness, traceability)
```

---

## E1-EmergencyProtocol: 紧急协议 (Emergency Protocol)

```
若任何invariant被违反:
  1. 立即停止 (STOP)
  2. 报告违反情况（哪个invariant、在哪、为何）
  3. 回滚变更 (ROLLBACK)
  4. 修复根因 (FIX)
  5. 验证修复 (VERIFY)
  6. 继续执行 (RESUME)
```

---

*Constitutional Principles: 通过形式化契约和不变量，最大化AI Coding Agent潜力*
