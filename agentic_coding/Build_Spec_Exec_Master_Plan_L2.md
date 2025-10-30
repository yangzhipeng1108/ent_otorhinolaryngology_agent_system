# Build_Spec_Exec_Master_Plan_L2.md

> 🎯 **定位**: L2级别执行计划生成引擎
> 📋 **用途**: 读取SPEC脚手架,生成AI Agent可执行的ProgressPlan体系
> 🧠 **本质**: 方法论指导文档,非机械脚本

> ⚠️ **执行契约**: 进入本文件 = 立即启动十二步工作流。从`Step 1`开始按顺序推进，禁止生成额外临时文档；分析草稿若确需暂存，只能放到`_scratch/`或沙箱并在进入`Step 5`前清理。

---

## 📖 Constitutional原则引用索引 (ACA宪法桥接)

> **核心依据**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md`
> **桥接方式**: Constitutional-level公理 → L2级别具体实现

### 四大不变量 (Four Invariants)
- **I1-CanonicalLocationUniqueness**: 权威位置唯一性
  - L2应用: Constraints/MasterPlan/SubPlan/Dashboard/Lessons等核心文档拥有唯一Canonical位置，并保持 GOAL registry 与团队协作 artefact 的同步
- **I2-CompletenessPrinciple**: 完整性原则
  - L2应用: MasterPlan/SubPlan/Constraints/Dashboard/Lessons 结合双层追溯字段，要求 artefact 完整覆盖协作视角
- **I3-QualityVerificationTriple**: 质量验证三元组
  - L2应用: {Pre} AI_Create {Post: Verify} → Step 5~11 验证清单，同时引入 L2 协作门禁与 PMI 风格检查
- **I4-DependencyChainIntegrity**: 依赖链完整性
  - L2应用: Constraints → MasterPlan → SubPlan → Dashboard → Lessons → GOAL registry 构成平衡依赖链，保持 Function Point / Scenario / Task Sequence 的闭环追溯

### 执行协议 (Execution Protocols)
- **C2-PDCA**: Plan → Do → Check → Act
  - L2应用: ProgressPlan = 团队共创的 PDCA 实现，Round.Act 触发 Dashboard 更新并沉淀 Lessons
- **C3-ProducerConsumerContract**: 生产者-消费者契约
  - L2应用: SubPlan = Producer（驱动团队协作），Dashboard = C3.2-Consumer（验证里程碑与门禁）
- **E1-EmergencyProtocol**: STOP → Report → Rollback → Fix → Verify → Resume
  - L2应用: 分级决策机制结合协调规格与风险矩阵，Lessons沉淀跨角色案例

### 本文档Constitutional桥接说明
本文档是Constitutional原则在L2-BALANCED级别的**具体实现指导**：
- Constitutional定义"必须遵守什么"（不变量和协议）
- 本文档定义"如何在L2级别执行"（方法论和模板，强调协作与双层追溯）
- 引用格式: `(I1)` `(C2-PDCA)` `(E1)` 表示桥接Constitutional原则

---

## 📖 目录与快速导航

**🎯 首次阅读路径**: §0 文档概览 → §14 十二步执行流程 → 按需查阅§1-§13

**📚 章节功能分组**:
- **概览** (§0): 文档目的/ProgressPlan概念/HITL机制/执行次序/版本说明
- **方法论** (§1-§9): 引擎架构/文件识别/Phase划分/Round规划/上下文提炼/HITL设计/Plan更新
- **模板** (§10-§13): MasterPlan/SubPlan/Constraints/Dashboard生成指导
- **执行** (§14): 十二步工作流(Step 1-12) ⭐ AI Agent执行入口

---

## § 0. 文档概览与核心概念

### § 0.1 这个文档是什么

**元层次定位**: 生成ProgressPlan的ProgressPlan

**输入**: SPEC脚手架(spec/目录 + 4阶段文档)
**输出**: 5类可执行ProgressPlan文档 (遵循I1-CanonicalLocation原则)
  - **SpecExecMasterConstraints_L2.md** - 目录结构与命名约定 (~80-120行) (I1-Canonical定义器)
  - **SpecExecMasterPlan_L2.md** - 总控ProgressPlan (150-250行) (C3.1-Producer总控)
  - **SpecExecSubPlan_*.md** - 独立执行单元 (各400-800行) (C3.1-Producer执行单元)
  - **SpecExecMasterDashboard_L2.md** ⭐ - 进度Contract验证 (~200-300行) (C3.2-Consumer)
  - **SpecExecMasterLessons_L2.md** ⭐ - Reflection知识库 (~300-400行) (C2-PDCA + E1)

**生成过程**: 12步工作流 + Human-in-the-Loop决策点

**文档性质**: 方法论指导,强调AI Agent判断空间,灵活应用而非机械执行

### § 0.2 什么是ProgressPlan ⭐ Constitutional桥接

### Constitutional依据（SPEC_ACA_CORE_PRINCIPLES.md）

**C2-PDCA桥接** (Plan → Do → Check → Act):
- ProgressPlan = PDCA循环的AI Agent实现
- **Plan阶段**: 前置条件检查(C2.1-Plan) + 推理分析(目标/文档/产出)
- **Do阶段**: 执行创建 + 遵守Invariants(I1/I2/I3/I4)
- **Check阶段**: 后置条件验证(C2.3-Check) + Quality Gates
- **Act阶段**: 决策路径(继续|重试|升级|回滚) + Lessons记录

**E1-EmergencyProtocol桥接** (失败恢复机制):
- **Reflection机制** = Check阶段验证 + E1的Report步骤持久化
- **分级决策** = E1协议实现:
  - Level 1 (自主): 明确问题 → Fix → Verify → Resume
  - Level 2 (协商): 模糊问题 → Report(诊断) → HITL → Fix
  - Level 3 (升级): 架构问题 → STOP → Report → HITL → Rollback/Fix
- **Lessons记录** = E1的Report + Fix经验积累（持久化知识库）

**ProgressPlan vs 传统计划**:

| 维度 | 传统计划 | ProgressPlan (AI Agent) |
|------|---------|------------------------|
| 执行方式 | 瀑布式,预先固定 | 迭代式,动态调整 |
| 失败处理 | 回退重做 | Reflection+分级恢复 |
| 学习机制 | 无 | Lessons记录+经验积累 |
| 人机协作 | 人工控制 | HITL检查点+自信度评估 |
| 进度追踪 | 完成百分比 | Round状态+质量指标+反思记录 |

**Master-SubPlan架构价值** (I4-DependencyChain + C3-ProducerConsumer):
- **问题**: 单文件MasterPlan 1500-3000行臃肿，AI Agent上下文负担过重
- **解决**: I4依赖链 → Constraints → MasterPlan(总控) → SubPlan(执行单元)
- **职责分离** (C3):
  - MasterPlan (C3.2-Consumer): 只追踪SubPlan状态，不追踪Round细节
  - SubPlan (C3.1-Producer): 独立维护Round执行记录
  - Dashboard (C3.2-Consumer): 验证SubPlan产出，质量门禁判定
- **架构优势**: 150-250行总控 + N个400-800行SubPlan，清晰 SubPlan 边界，支持并行协作

### § 0.3 Human-in-the-Loop协作机制

**HITL不是Bug,是Feature**:
- 本文档生成过程需要13-25轮Human-in-the-loop协作
- HITL是质量保障机制,非执行阻碍

**HITL触发场景**:

1. **技术栈识别不确定** (Step 1):
   - 罕见技术栈/架构选择矛盾/测试策略不明确
   - 触发条件: 自信度<50%

2. **Phase划分自信度<80%** (Step 2):
   - 依赖关系复杂/集成策略模糊/Phase数量难以判断

3. **文件已存在需要决策** (Step 5/6/7/8/9):
   - 现有文件备份后覆盖/保留现有/手动Review
   - 用户主导决策,AI提供上下文
   - 特别注意: Lessons/SubPlan包含宝贵经验,强烈建议保留现有

4. **Constraints约定不明确** (Step 5):
   - 目录结构不明/命名规则模糊/测试组织策略不确定

**HITL标准模板**:
```
🤝 需要您的决策 - [标题]

**背景**: [简要说明当前执行到哪个步骤]

**不确定项**:
- 来源: [哪个文档/哪个章节发现的问题]
- 问题: [具体不确定的点]
- 推测: [基于现有信息的初步判断]
- 选项: [可选方案A/B/C]

**影响范围**: [该决策会影响哪些后续步骤]
```

### § 0.4 执行次序速览

| 阶段 | 步骤 | 关键产出 |
|------|------|-----------|
| 分析 | Step 1-4 | artefact 清单、GOAL_INDEX、Phase/Round 草案 |
| 生成 | Step 5-9 | Constraints / Lessons / MasterPlan / SubPlan×N / Dashboard |
| 同步 | Step 10-12 | Lessons GOAL 挂靠、Dashboard 更新、Git 提交 |

> 详细操作与 HITL 条件见对应 Step 章节。保持顺序执行：每步依赖前一步的文件或信息产出。
### § 0.5 版本说明与迭代路线

**当前版本**: v2.0 - 阶段1基础版(2025-01)

**阶段1特征**: 
- 安全可靠的文件检查 + 用户主导HITL决策
- 简洁执行流程(~40-75行/Step)
- 版本号标准: v1.0.0(所有生成文件统一)

**未来演进计划**:
- **阶段2** [计划]: AI辅助分析 + 智能推荐(spec变化对比/变化摘要展示)
- **阶段3** [未来]: 自动化决策 + 增量更新(🟢🟡🔴自动分级/轻微变化自动执行)

**核心设计原则**:
- 每个阶段都是可工作的完整系统
- 基于实际使用反馈迭代
- 保持向后兼容

### § 0.6 步骤完成标准格式 ⭐

- **统一约束**: Step 1-11 禁止使用“任务完成/结束/全部完成”，仅 Step 12 可宣布全部完成。
- **Step 1-4 (分析阶段)**: `🎯 进度：Step {X}/12 ...` + `📋 已产出：...` + `⏭️ 继续执行 Step {X+1}`。
- **Step 5-9 (生成阶段)**: 同上并追加 `⚠️ 阶段性输出` 与文件名称。
- **Step 10-11 (同步阶段)**: 使用 `📊` 标注内容更新，提醒尚未最终完成。
- **Step 12**: `🎯 进度：Step 12/12 ...` + `✅ ProgressPlan 体系已就绪`。
- 进度百分比、剩余步数按实际填写；如触发 HITL，在输出中说明原因即可。
## § 1. 引擎作用与核心依赖 ⭐ Constitutional桥接

**Constitutional原则**:
- **I1-CanonicalLocation**: Constraints定义文件权威位置（唯一性保证）
- **I4-DependencyChain**: Constraints → MasterPlan → SubPlan → Dashboard/Lessons依赖链
- **C2.1-Plan**: Constraints必须第一个生成（前置条件检查）

**输入**: SPEC脚手架目录（spec/目录 + 三柱体系）

**输出**: 本引擎生成**N+4**个文件
- **Constraints文档** (1个): 目录结构与命名约定 (~80-120行) ⭐ **必须第一个生成** (I1)
- **MasterPlan文档** (1个): 总控Progress Plan (~150-250行) (C3.1-Producer总控)
- **SubPlan文档** (N个): 独立可执行Progress Plan (各~400-800行) (C3.1-Producer单元)
- **Dashboard文档** ⭐ (1个): 进度Contract验证 (~200-300行) (C3.2-Consumer)
- **Lessons文档** ⭐ (1个): Reflection知识库 (~300-400行) (C2-Reflection + E1)

**⚠️ 执行顺序关键约束** (I4-DependencyChain):
1. Constraints必须第一个生成 (I1-Canonical + C2.1-Plan前置条件)
2. MasterPlan → SubPlan → Dashboard/Lessons依赖链 (I4)
3. 依赖原因: I4要求∀ artifact ≠ root: ∃ parent，Constraints = root

**详细生成流程**: 参见§14十二步工作流

---

## § 2. L2特征

**L2核心**: 平衡团队协作 | Function Point ↔ BDD 场景闭环 | value_path_mapping 贯通设计→验证 | PMI/质量门禁双轨 | GOAL registry 严格闭环  
**L2心态**: Balance over Speed - 在结构化流程中迭代，风险前置管理，记录每一次协作判断与追溯链

---

## § 3. 核心方法论依据

**遵循SPEC CRAFT精神**: 协作平衡、模块间引用网络、测试驱动(详见`four_stage_crafting/CRAFT_L2_*.md`)

---

## § 4. 文件发现与识别策略

**核心要点**
- 仅需确认各类 artefact 是否齐备；字段/模板细则参考 `four_stage_crafting/CRAFT_L2_*.md` 与命名 authority。
- ProgressPlan 额外关注 GOAL registry（`source_us/related_sc/related_seq`）与协调 artefact 的闭环。

### § 4.1 遍历 spec 目录
- 跳过 `_` 前缀目录，列出剩余文件。
- 读取开头 50-100 行确认文档类型，并记录在 artefact 清单（US/AC/FP/SC/TS/SEQ/CTX/GOAL + 推荐项）。

### § 4.2 Artefact 分类速览
| 分类 | 主要来源 | 重点字段 |
|------|-----------|-----------|
| US / AC | `requirements/` | `id/sn`、关联下游 |
| Function Point / value_path | `design/` | `source_us`、`value_path_mapping`、`related_sc` |
| 设计 artefact (API/CMP/DM/接口契约) | `design/` | 关联 FP 或 coordination |
| BDD / Test Suite / Test Data / Quality Definition | `implementation/` | `source_fp`、`related_sc`、质量门禁 |
| 项目结构 & TDD 策略 | `implementation/` | 目录布局、测试分层 |
| GOAL / 任务规划 artefact | `task_planning/` | `source_us`、`related_sc`、`related_seq`、coordination/blocker |

（若需详细关键词，可在需要时跳转对应 CRAFT 文档。）

### § 4.3 缺失处理
- 任何 artefact 缺失即标记 "📌 待确认"；必要时触发 HITL。
- value_path 或 coordination 缺口通常影响 Phase/Round 规划，提前记录。

### § 4.4 技术栈与结构识别
- 依据 `architecture`、`project_structure`、`tdd_strategy` 等文档识别前端/后端/测试框架与目录布局。
- 无法确定时使用 C2-PARTICIPATE HITL 与用户协商。

### § 4.5 GOAL 与协同 artefact 采集
- 解析 `task_planning/goal_breakdown.md`，生成 `GOAL_INDEX`：记录 `id/sn/source_us/related_sc/related_seq/context_refs` 以及 coordination/blocker 依赖。
- 对应 `task_breakdown`、`task_sequence`、`task_coordination_spec`、`blocker_anticipation`、`ai_context_specification` 仅需抓取引用并检查是否覆盖所有 GOAL。
- 若某 GOAL 的 `related_sc`/`related_seq` 缺失或 SC/SEQ 未被任何 GOAL 引用 → 标记差异，后续步骤补齐。
## § 5. Phase划分方法（L2核心）

#### 5.1 主线策略：Function Point & value_path链路

**第一优先**: 读取 `CRAFT_L2_DESIGN.md` / `CRAFT_L2_IMPLEMENTATION.md` 中的 Function Point 列表、value_path_mapping 以及 BDD 场景映射。
- 每个 Function Point (FP) = 1 个候选 Phase；若 FP 隶属于同一 value_path（四向度映射）且高度耦合，可打包为一个 Phase。
- 结合 `CRAFT_L2_TASK_PLANNING.md` 的 GOAL ↔ FP ↔ SC 关联，确保 Phase 划分与 GOAL/SEQ 闭环一致。

**回退方案**: 按以下顺序推导 Phase：
1. GOAL → `related_seq` → `related_fp`
2. FP → `related_sc`（value_path_mapping 四向度）
3. 需求层 Feature/Epic（US + Business Rules + AC）

#### 5.2 依赖关系推断

**技术层**: value_path_mapping 提供“前端交互 → 数据流转 → 后端处理 → 结果反馈”四链路，对应到 Phase 顺序：数据模型 → 服务/组件 → API → 前端 → 集成。
**业务层**: `task_sequence.md` 与 `task_coordination_spec.md` 中的依赖、同步点和优先级。
**质量层**: `CRAFT_L2_IMPLEMENTATION.md` 的测试数据、质量定义、集成编排文档决定测试门禁与风险缓冲位置。

#### 5.3 集成 Phase 与协调窗口

**L2策略**: 每 2-3 个 FP Phase 后安排一个协调/集成 Phase；当 coordination spec 标记跨模块同步点或 blocker 预判标记高风险依赖时，必须新增 INTEGRATION Phase；终局仍需 FINAL INTEGRATION Phase 完成端到端门禁。
- 集成 Phase 需要明确协调维度（接口、数据、部署）、预期输出与验证门禁。
- 若 blocker 文档提示关键风险，提前安插“风险管控”子 Phase。

#### 5.4 SubPlan划分规则 ⭐ Master-SubPlan架构核心

**核心理念**: 维持 MasterPlan 总控 + SubPlan 执行单元的依赖链，并让每个 SubPlan 显式绑定 GOAL / FP / SC / SEQ。

**规则1: GOAL 映射**
- 每个 GOAL SubPlan 覆盖 1 组 FP/SC/SEQ；SubPlan 命名 `SpecExecSubPlan_{序号}_{GOAL_ID}_L2.md`。
- GOAL front matter (`source_us/related_sc/related_seq/context_refs`) 是 SubPlan 的首要输入，需在 SubPlan 头部复写。

**规则2: 基础设施 / 平台能力**
- 若 Constraints 或项目结构文档强调基础设施 Phase，创建 `SpecExecSubPlan_01_INFRASTRUCTURE_L2.md`（序号固定 01）。
- 结合同步的 `project_structure_file`、`tdd_strategy_file`、CI/CD 约定。

**规则3: 集成 / 协调 Phase**
- 根据 coordination spec 的同步窗口创建 `SpecExecSubPlan_{序号}_INTEGRATION_PHASE{N}_L2.md`。
- 最终端到端集成命名为 `SpecExecSubPlan_{序号}_INTEGRATION_FINAL_L2.md`，负责最终门禁验证。

**命名规范**:
| SubPlan类型 | 命名格式 | 示例 |
|------------|---------|------|
| GOAL SubPlan | `SpecExecSubPlan_{执行序号}_{GOAL_ID}_L2.md` | `SpecExecSubPlan_03_GOAL-AUTH-002_L2.md` |
| 基础设施 | `SpecExecSubPlan_01_INFRASTRUCTURE_L2.md` | `SpecExecSubPlan_01_INFRASTRUCTURE_L2.md` |
| 阶段集成 | `SpecExecSubPlan_{执行序号}_INTEGRATION_PHASE{N}_L2.md` | `SpecExecSubPlan_06_INTEGRATION_PHASE2_L2.md` |
| 最终集成 | `SpecExecSubPlan_{执行序号}_INTEGRATION_FINAL_L2.md` | `SpecExecSubPlan_10_INTEGRATION_FINAL_L2.md` |

**执行序号规则**:
- 两位数字 (01-99) 显式体现推荐执行顺序。
- 基础设施固定 01；GOAL SubPlan 按 `task_sequence` 顺序递增；协调/集成 Phase 紧随相关 GOAL。
- 可根据团队分工在 GOAL SubPlan 后附加后缀（如 `_UI`/`_API`），但必须在 MasterPlan 的 SubPlan 表中说明。

**验收**:
- SubPlan 列表完整覆盖 GOAL_INDEX。
- 集成 Phase 与 coordination spec 对应。
- 每个 SubPlan 写明前置依赖与交接物。
- 命名、结构、追溯字段符合 L2 规范。
## § 6. Round规划方法（value_path + PDCA）

#### 6.1 核心理念：value_path驱动的弹性轮次

**L2原则**: Round 数量随 value_path 四向度验证与团队协作完成度动态调整，不预设固定长度。
- 每条 value_path (前端交互 / 数据流转 / 后端处理 / 结果反馈) 都需要至少一次 RED → GREEN → CHECK 验证。
- 对于多人协作的 FP，增加协调轮次（例如 API 与 UI 并行开发后再同步的协调 Round）。

**参考结构**:
```
Phase: FP / GOAL
├─ Round A: value_path 前后端 RED（编写场景 + 失败测试）
├─ Round B: value_path GREEN（实现 + 通过测试）
├─ Round C: Refactor / 性能 / 安全 (按质量门禁)
├─ Round D: 协同/集成（对应 coordination spec 同步点）
└─ Round Buffer 1~2: 处理风险或技术债
```

#### 6.2 Round 内 PDCA 结构

每个 Round 必须包含完整 PDCA：
- **Plan**: 明确 value_path 向度、引用 FP/SC/ctx/coordination 文档、列出目标质量门禁（覆盖率 75-85%、集成通过率 ≥95%）。
- **Do**: 实施/测试/协作动作，记录涉及的 artefact（代码、测试、配置、脚手架）。
- **Check**: 验证结果、门禁指标、协作回顾；对照 `CONSTRAINT_L2_*` 检查列表。
- **Act**: 决策路径（继续 / 重试 / 升级 HITL），并强制触发 Dashboard & Git 更新（详见 Step 11 & Step 12 说明）。

#### 6.3 Round 估算与分类

**典型估算**: 单 FP 4-6 轮；包含集成的 GOAL 6-9 轮；大型协调场景 8-12 轮。
**分类建议**:
- Value-path Implementation Rounds
- Coordination / Integration Rounds
- Quality Gate Rounds（性能、安全、观测）
- Risk / Blocker Resolution Rounds

#### 6.4 TDD & value_path 映射

- **RED**: 编写 BDD 场景与测试（含 value_path 四向度）、确保失败。
- **GREEN**: 实现功能并满足 value_path 验证。
- **REFACTOR**: 综合考虑性能/安全/可维护性，符合 L2 质量标准。
- **Integration**: 使用 coordination spec、test data、quality definition 文档执行跨模块验证。

#### 6.5 自信度评估与 HITL 决策

- **高自信 (≥80%)**: Function Point 文档齐全，value_path、SC、TD、QD、coordination 一致 → 自主执行。
- **中自信 (50-80%)**: value_path 或 coordination 缺少确认 → 在 Round Plan 标注“📌 待用户确认”，并同步 Dashboard 提醒。
- **低自信 (<50%)**: 文档缺失、依赖冲突、风险剧烈 → 触发 C2-PARTICIPATE HITL，使用 §0.3 模板。

#### 6.6 Round 完成后的强制操作

Round Act = ✅ 通过后必须执行：
1. 更新 Lessons Round-by-Round 记录、技术债、问题案例。
2. 更新 Dashboard Round 进度、SubPlan 状态、最后更新时间。
3. 执行 Git 小步提交（`round: <GOAL>/<Round> pass`）。
4. 若产生风险/协调调整 → 更新 blocker / coordination artefact。

保持上述闭环 = L2 Balanced 的核心：团队协作有据可依、traceability 全程可追。
## § 7. 上下文提炼策略

**核心问题**: Function Point / value_path / BDD / coordination 等多源信息易造成上下文爆炸。

**解决方案**: 构建多层映射表，按 value_path 维度与团队角色提炼必需上下文。

#### 7.1 构建多维引用映射

- **US ↔ AC ↔ FP**: 从 `user_stories`、`acceptance_criteria`、`Function Point` 文档建立需求→设计桥接。
- **FP ↔ SC ↔ TS**: 基于 value_path_mapping 和 BDD 场景，确保测试引用精准。
- **FP ↔ API / CMP / DM**: 从设计文档提取组件/接口/数据模型引用关系。
- **GOAL ↔ SEQ / BLK / COORD / CTX**: 结合 task planning artefact，呈现执行链路。

#### 7.2 精准引用策略

- Round 计划引用格式：`[GOAL_ID] → FP-ID → value_path维度 → SC-ID → 相关文档段落`。
- 将关键信息编入 SubPlan 的“执行依赖索引”表，减少重复查阅。
- 对于调试/排查，优先阅读 coordination spec 与 blocker 文档对应段落。

#### 7.3 上下文裁剪建议

- 仅加载与当前 Round value_path 相关的文档片段（可使用章节锚点）。
- 若引用同一文档多处，建立“章节别名”，方便 Round Plan、Lessons 重复引用。
- 对长篇 BPMN/流程说明，使用总结或表格形式在 SubPlan 中复述，避免重复粘贴。

#### 7.4 追溯链验证

- 映射表建立后，运行 consistency check：每个 FP 均有 `source_us`、`related_sc`，每个 SC 反向可追到 GOAL。
- 在 Step 7/8 生成 MasterPlan/SubPlan 前再次审查映射是否完整，缺失项立即标注 HITL。
## § 8. HITL检查点设计

#### 8.1 Phase边界协作检查

每个 Phase 结束时触发 C2-PARTICIPATE HITL：
1. Phase 目标达成（GOAL / FP / SC / SEQ 是否闭环）。
2. 质量门禁：覆盖率 75-85%、集成通过率 ≥95%、风险处置状态。
3. 协作评审：coordination spec 对齐、blocker 是否清零、Lessons 是否更新。
4. 决策确认：下一 Phase 是否需要调整计划或重新排序。

**决策选项**: ✅继续 | 🔄局部重构 | 🟡需求澄清 | ⏸️风险缓冲。

#### 8.2 Round内智能触发

- 🔴 阻塞性：value_path 闭环失败、跨团队沟通中断、质量门禁未通过 → 立即 HITL。
- 🟡 警告性：覆盖率低于目标 5%、协调窗口冲突、技术债增加 → 与用户共商策略。
- 🟢 建议性：优化机会、最佳实践沉淀 → 记录于 Lessons。

#### 8.3 Lessons & Reflection 模板

- Round-by-Round：目标/结果/工具/协作回顾。
- 技术债务：优先级(H/M/L)、归属团队、预期解决轮次。
- 问题与解决案例：完整 E1 流程 + 决策缘由。
- 协同洞察：跨角色沟通要点、同步窗口经验。
- KPI 回顾：覆盖率、缺陷率、响应时间等指标。

Lessons 是 HITL 的持续输入，确保团队决策具备历史数据支撑。
## § 9. 动态Plan更新策略

**核心理念**: 保持计划稳定，同时依据协作门禁和风险策略进行受控更新。

**触发条件**:
- value_path 发生重大调整或 FP 新增/拆分。
- Phase 执行偏差 > 30% 或出现新的协调窗口。
- 质量门禁/风险矩阵提示需要重排顺序。
- 用户在 C2 协作中提出策略变更请求。

**不触发**:
- Round 微调 ±2 轮。
- 局部实现或测试细节调整（保持门禁通过）。
- Lessons 记录小幅补充。

**更新流程**:
1. Phase 评估会（引用 Dashboard 状态 + Lessons 总结）。
2. 生成更新建议：影响范围 / 新旧差异 / 对 GOAL/SEQ/coordination 的调整。
3. HITL 决策：确认是否执行、是否需要额外缓冲。
4. 更新文档并递增版本号（Constraints/MasterPlan/SubPlan/Dashboard/Lessons）；在 Git 中形成清晰历史节点。
5. 将变更记录同步到 Dashboard “Plan 变更历史” 与 Lessons 中的“计划调整”章节。

**提示**: 每次更新后重新检查 GOAL registry 与 SubPlan 序号，确保依赖链(I4)完整。
## 模板使用说明

**占位符替换**: `{{SPEC_PRJ_NAME}}` `{{SPEC_PRJ_DESC}}` `{{SPEC_USER_COLLABORATION_MODE}}` `{{SPEC_PRJ_ROOT_DIR}}` `{{TIMESTAMP}}` `{{N/X/MIN/MAX}}`

**核心规则**: 
- `[使用§X的模板]` → 完整复制§X内容并填充占位符
- 多实例展开 → 每个Phase/Round完整复制模板，禁止"同上"或"参考"
- 映射关系 → 生成实际映射表，不留空占位符

---

## § 10. SpecExecMasterPlan_L2.md 生成指导 ⭐ 总控概览

**定位**: 总控 Progress Plan（约 180~280 行），链接所有 SubPlan、GOAL、协调窗口与质量门禁。

**生成步骤（参考 `CRAFT_L2_*` 模板）**
1. 复制模板，填入项目元信息、Constraints 引用、执行版本。
2. 导入 SubPlan 索引表（序号 / 类型 / GOAL / Phase / 预估 Round / 协调窗口 / 状态）。
3. 绘制 Phase 与 value_path 依赖图，标注集成门禁与风险缓冲。
4. 生成 GOAL 覆盖表：`id/sn/source_us/related_sc/related_seq/assigned_subplan/status/KPI`。
5. 汇总全局 HITL 检查点、风险/恢复策略、Plan 变更历史与 KPI。

**L2 特有检查点**
- ✅ 所有 GOAL 在覆盖表中并指向唯一 SubPlan。
- ✅ SubPlan 索引突出协调窗口与风险等级。
- ✅ 依赖图展示 value_path 顺序 + 集成 Phase。
- ✅ Dashboard / Lessons 引用占位（供 Step 9/10 使用）。
## § 11. SpecExecSubPlan_*.md 生成指导 ⭐ 执行单元

**定位**: 独立执行 Plan（450~900 行），记录 Round PDCA、协调信息与质量门禁。

**生成步骤**
1. 新建 `SpecExecSubPlan_{序号}_{GOAL或TYPE}_L2.md`（序号两位，GOAL SubPlan 使用 GOAL ID）。
2. 填写元信息表：序号 / 类型 / GOAL / Phase / 预估 Round / 协调窗口 / 质量门禁。
3. 引入执行依赖索引：Constraints、Function Point、value_path、coordination、blocker、Test/Quality artefact。
4. 复写 GOAL_COVERAGE：`id/sn/source_us/related_sc/related_seq/context_refs/coordination_refs/blocker_refs`。
5. 嵌入 Step 4 规划的 Round（Plan/Do/Check/Act + Buffer），并注明质量门禁指标。
6. 设置进度 & KPI 表、Lessons & coordination 占位、完成 HITL 清单与风险恢复树，并在 SubPlan 内部明确 Round 总数/完成数与 TODO/Triage 列表，方便随时播报。

**L2 特有检查点**
- ✅ GOAL SubPlan 必须有 GOAL_COVERAGE 表且字段完整。
- ✅ Round 规划包含 value_path 四向度 + 协调动作。
- ✅ Lessons & Dashboard 引用占位存在（Round 完成后强制更新）。
- ✅ 风险/技术债记录与 coordination artefact 对齐。
## § 12. SpecExecMasterConstraints_L2.md 生成指导

**定位**: 目录 / 命名 / 禁止区域的 Canonical 约束（90~140 行）。

**必备元素**
1. 文档头部 + 版本。
2. 强约束声明：文件位置、命名规则、禁止区域、引用方式。
3. 技术栈识别表（前端/后端/测试/数据库/部署）。
4. 目录结构：根目录、源码、测试、部署/配置。
5. 命名约定：文件/目录/组件/函数/常量，给出正反例。
6. 禁止区域 & 路径关系；忽略列表。
7. 执行引用方式（Round/Step 如何使用）。
8. 约定变更日志。

**检查清单**: 路径与命名规则清晰、测试目录标注分层、GOAL/SubPlan 命名约束同步说明。
## § 13. SpecExecMasterDashboard_L2.md 生成指导 ⭐ Constitutional桥接

**文档定位**: 进度 Contract 验证文档 (典型 220-320 行)，实现 C3.2-Consumer 角色。

**核心职责**: 项目概览 KPI | SubPlan 执行状态总览 | Round 汇总 | 协调预测 | 当前焦点 | 里程碑清单 | 质量指标。

**与 MasterPlan 关系**: Dashboard 验证 SubPlan 产出和质量门禁；MasterPlan 负责计划与依赖；Dashboard 不改写 Plan，只提供验证与风险提示。

**Constitutional 原则**:
- **I1-CanonicalLocation**: `{{SPEC_PRJ_ROOT_DIR}}/SpecExecMasterDashboard_L2.md`
- **I2-Completeness**: Dashboard = 文档头部 ∧ KPI ∧ SubPlan 状态总览 ∧ Round 汇总 ∧ 协调预测 ∧ 当前焦点 ∧ 里程碑 ∧ 质量指标 ∧ 更新记录。
- **C3.2-ConsumerRole**: Consumer 验证 Producer 产出，判定质量门禁。

---

**必需章节**：

1. **文档头部**: 标题、引用块(项目名/类型/生成时间)、版本 v1.0。
2. **项目概览与 KPI**: 表格列出项目名、约束级别 (L2-BALANCED)、SubPlan/Phase/GOAL 总数及完成度、Round 指标、风险统计、质量通过率。
3. **SubPlan 执行状态总览**: 表格(序号/文件/类型/关联Phase/状态/轮次进度/覆盖率/集成通过率/质量门禁/最后更新)。状态图例 ⬜/🔄/✅/❌/⏸。
4. **Round 进度汇总**: 按 SubPlan 绘制 ASCII 条形图，列出已完成轮次、总轮次、质量门禁结果。
5. **协调与风险预测**: 基于 Lessons 与 coordination spec，列出高风险 SubPlan、关键路径、预计完成时间、建议动作。
6. **当前焦点**: 正在执行、即将启动、等待 HITL 决策的条目。
7. **里程碑清单**: 表格(里程碑/定义/状态/时间/备注)，覆盖基础设施、关键 FP、阶段集成、最终交付等。
8. **质量指标汇总**: 覆盖率均值（目标 75-85%）、集成通过率（≥95%）、质量门禁通过率、未解决 blocker 数量、技术债项数。
9. **Dashboard 更新记录**: 表格(版本/时间/来源/更新内容)，初始记录 v1.0|{{TIMESTAMP}}|MasterPlan 初始生成|Dashboard 初始化。
10. **Consumer 验证说明**: 定义 Producer-Consumer 合同、验证流程、质量门禁失败处理 (记录证据 → HITL 决策)。

**变量替换**: `{{SPEC_PRJ_NAME}}` `{{SPEC_PRJ_LEVEL}}` `{{TIMESTAMP}}` 等；KPI 数值来自 MasterPlan / SubPlan / Lessons。

**典型长度**: 220-320 行；大型项目可扩展到 350+ 行。

**数据来源**: 主要来自 MasterPlan SubPlan 状态区、SubPlan Round 表、Lessons、coordination/blocker 文档。

**生成要点**:
- Dashboard 是只读验证文档，不直接修改 Plan。
- 所有统计需注明来源；无法确定时标注“📌 待确认”。
- Round 汇总聚焦结果，不复述详细步骤。
- 质量门禁标准采用 L2 阈值：覆盖率 75-85%、集成 ≥95%、风险关闭率 ≥90%。
## § 14. 十二步工作流 ⭐ AI Agent 执行指导

**执行契约摘要**
- **连续执行**: Step 1-12 顺序推进，除 HITL 外不暂停。
- **进度透明**: 按 §0.6 模板输出进度与剩余步骤；Step 1-11 不得宣称“全部完成”，并播报 SubPlan 完成度（{{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}）与 Round 规划/完成度（{{PLANNED_OR_DONE_ROUNDS}}/{{TOTAL_ROUNDS}}）。
- **Dashboard/TODO 维护**: MasterPlan/SubPlan/Lessons 调整后记录待同步项；Dashboard 自 Step 9 生成起即时刷新 TODO/Next Actions，Step 11 勾选完成项并播报当前状态。
- **HITL 触发**: artefact 缺失、技术栈不确定、Phase 冲突、GOAL 漏挂；使用 §0.3 模板。
- **工具提示**: CLine/Cursor 等 Agent 若需暂停，仍须在输出中说明原因并引用下一步。
- **恢复机制**: 用户中断后，先检查文件状态，再从中断的 Step 继续（若文件已生成可选择保留）。

详细操作与输出示例请参见各 Step 小节。
### Step 1 (预计3-4分钟): 读取脚手架 + 识别技术栈
- **输入**: `spec/` 目录树。
- **操作**: 依照 §4 表格核对 artefact，记录缺失；解析 `goal_breakdown.md` 生成 `GOAL_INDEX`；整理技术栈与项目类型。
- **输出**: artefact 清单、`GOAL_INDEX`、技术栈/项目类型。
- **进度提示**: 输出 `🎯 Step 1/12 (8%) — 分析产出，继续执行 Step 2`。

### Step 2 (预计4-6分钟): Phase 划分
- **输入**: Step 1 结果、CRAFT Phase 指南。
- **操作**: 依据 Function Point/value_path 制定 Phase 序列，标注集成窗口与风险缓冲。
- **输出**: Phase 列表、依赖图草案。
- **进度提示**: `🎯 Step 2/12 (17%) — 继续执行 Step 3`。

### Step 3 (预计3-5分钟): SubPlan 划分
- **输入**: Phase 结果、`GOAL_INDEX`。
- **操作**: 将 GOAL/协调窗口映射到 SubPlan；编号；识别前置依赖；统计 SubPlan 总数，供后续进度播报与 Dashboard/TODO 使用。
- **输出**: SubPlan 索引表。
- **进度提示**: `🎯 Step 3/12 (25%) — 继续执行 Step 4（SubPlan 总数：{{TOTAL_SUBPLANS}}）`。

### Step 4 (预计4-6分钟): Round 规划
- **输入**: SubPlan 列表、value_path、coordination 数据。
- **操作**: 为每个 SubPlan 规划 Round（RED/GREEN/REFACTOR/Integration + 缓冲），记录门禁指标；统计全局 Round 总数以便播报；确保每个 SubPlan 至少包含测试资产建设/维护相关 Round（数据、mock、集成环境等）。
- **输出**: Round 规划明细。
- **进度提示**: `🎯 Step 4/12 (33%) — 继续执行 Step 5（Round 规划进度：{{PLANNED_ROUNDS}}/{{TOTAL_ROUNDS}}）`。

### Step 5 (预计3-5分钟): 生成 Master Constraints
- **输入**: Round 规划、技术栈信息。
- **操作**: 检查 `SpecExecMasterConstraints_L2.md` 是否存在；按 §12 模板生成或经 HITL 决策更新。
- **输出**: `SpecExecMasterConstraints_L2.md`。
- **进度提示**: `🎯 Step 5/12 (42%) — 阶段性输出，继续执行 Step 6`。

### Step 6 (预计3-5分钟): 生成 Lessons 框架
- **输入**: SubPlan 列表、Constraints。
- **操作**: 生成或更新 `SpecExecMasterLessons_L2.md` 空框架，并挂载 GOAL/SubPlan 占位符。
- **输出**: Lessons 框架文件。
- **进度提示**: `🎯 Step 6/12 (50%) — 阶段性输出，继续执行 Step 7`。

### Step 7 (预计5-7分钟): 生成 MasterPlan
- **输入**: Constraints、Lessons 框架、SubPlan/Phase 数据。
- **操作**: 生成 `SpecExecMasterPlan_L2.md`，填充索引表、依赖图、GOAL 覆盖等。
- **输出**: MasterPlan 总控文件。
- **进度提示**: `🎯 Step 7/12 (58%) — 阶段性输出，继续执行 Step 8`。

### Step 8 (预计8-12分钟): 生成 SubPlan×N
- **输入**: MasterPlan、Round 规划、`GOAL_INDEX`。
- **操作**: 为每个 SubPlan 生成/更新文件，包含 GOAL_COVERAGE 和 Round PDCA；显式安排测试资产建设/维护任务（数据、mock、集成环境等）；在 SubPlan 内设置进度追踪小节（Round 总数/完成数 + TODO/Triage 列表）；如项目提供便携性/可移植性文档，补充引用并在 TODO 中标记后续核查；提醒 Round 完成时需按照 §6.6 更新 Lessons、Dashboard 并执行 git commit。
- **输出**: `SpecExecSubPlan_*_L2.md`。
- **进度提示**: `🎯 Step 8/12 (67%) — 阶段性输出，继续执行 Step 9（SubPlan 已生成：{{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}）`。

### Step 9 (预计4-6分钟): 生成 Dashboard 完整版
- **输入**: MasterPlan、SubPlan、`GOAL_INDEX`。
- **操作**: 生成 `SpecExecMasterDashboard_L2.md`，填充 KPI、GOAL_STATUS、预测等；同步/刷新 TODO Checklist（或 Next Actions），记录当前 SubPlan/Round 完成度，并添加便携性/可移植性文档检查项（若尚未完成）。
- **输出**: Dashboard 文件。
- **进度提示**: `🎯 Step 9/12 (75%) — 阶段性输出，继续执行 Step 10（Dashboard 进度：SubPlan {{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}, Round {{COMPLETED_ROUNDS}}/{{TOTAL_ROUNDS}}）`。

### Step 10 (预计2-3分钟): Lessons 挂靠 GOAL
- **输入**: MasterPlan、SubPlan、Dashboard、`GOAL_INDEX`。
- **操作**: 将 GOAL/SubPlan 数据写入 Lessons 对应章节，保持占位。
- **输出**: Lessons 更新。
- **进度提示**: `🎯 Step 10/12 (83%) — 内容更新，继续执行 Step 11（Lessons 已挂靠 GOAL：{{LESSONS_LINKED}}/{{TOTAL_GOALS}}）`。

### Step 11 (预计1-2分钟): Dashboard 最终更新
- **输入**: Dashboard、Lessons、最新 SubPlan 状态。
- **操作**: 更新 Dashboard 里程碑状态，记录体系完成时间戳（但保持 GOAL 状态未开始），并勾选/清理 TODO Checklist 中已完成项。
- **输出**: Dashboard 最终状态。
- **进度提示**: `🎯 Step 11/12 (92%) — 内容更新，继续执行 Step 12（Dashboard 标记完成：里程碑 {{MILESTONES_DONE}}/{{TOTAL_MILESTONES}}）`。

### Step 12 (预计1-2分钟): Git 阶段提交
- **输入**: 所有 Progress Plan 文件。
- **操作**: 按需 git add/commit（如 `plan: add constraints v1` 等）；确认无遗漏文件。
- **输出**: ProgressPlan 最终提交记录。
- **进度提示**: `🎯 Step 12/12 (100%) — ✅ ProgressPlan 体系就绪`。
## § 15. SpecExecMasterLessons_L2.md 生成指导 ⭐ Constitutional桥接

**文档定位**: Reflection知识库文档 (典型300-400行), 实现C2-PDCA Reflection + E1-EmergencyProtocol案例库

**核心职责**: Round-by-Round实践记录 | 技术债务管理 | 问题解决案例库 | 最佳实践提炼 | 数据驱动分析

**与MasterPlan关系**: Lessons = C2-Reflection持久化 | SubPlan执行时边学边干 | 记录E1完整流程

**Constitutional原则**:
- **I1-CanonicalLocation**: 权威位置 `{{SPEC_PRJ_ROOT_DIR}}/SpecExecMasterLessons_L2.md`
- **I2-Completeness**: Lessons完整性=文档头部 ∧ 知识库概览 ∧ Round-by-Round记录 ∧ 技术债务管理 ∧ 问题解决案例库 ∧ 最佳实践提炼 ∧ 数据驱动分析 ∧ 更新记录表
- **C2-PDCA**: Lessons = Check阶段验证 + Act阶段Reflection持久化
- **E1-EmergencyProtocol**: 问题解决案例库记录E1完整流程 (STOP → Report → Rollback → Fix → Verify → Resume)
- **I4-DependencyChain**: Lessons记录 → Round执行 → SubPlan → Phase依赖链

---

**必需章节** (按顺序生成):

**1. 文档头部**:
- 标题: `# SpecExecMasterLessons_L2.md`
- 引用块 (markdown `>`格式): 项目名/Lessons类型(Reflection知识库)/生成时间
- Lessons版本: 初始1.0

**2. 知识库概览**:
- 表格格式 (2列: 指标|当前值)
- 必含: 总Round记录数/总技术债数量(H/M/L分级)/总问题案例数/最佳实践数量(A/B/C三级)/最后更新时间/知识库覆盖率
- 知识库覆盖率: (已记录Round / 总已完成Round) × 100%
- 替换变量: {{TOTAL_ROUND_RECORDED}} {{TOTAL_TECH_DEBT}} {{TOTAL_PROBLEM_CASES}} {{BEST_PRACTICES_COUNT}}

**3. Round-by-Round实践记录** ⭐ **C2-Reflection核心**:
- 组织方式: 按SubPlan分组，每个SubPlan一个章节
- **每个SubPlan章节结构**:
  ```markdown
  ### SubPlan_{{序号}}_{{TYPE}} - {{功能简称}}

  **SubPlan元信息**:
  - 执行序号: {{序号}}
  - 关联Phase: {{Phase名称}}
  - 总Round数: {{总数}}
  - 已记录Round数: {{已记录数}}

  **Round-by-Round记录**:

  #### Round {{X}}: {{Round目标}}

  **元信息**:
  - TDD阶段: RED/GREEN/REFACTOR/Integration
  - 实际耗时: {{时间}}
  - 状态: ✅已完成 / ❌失败 / ⏭️已跳过

  **Good Practices** ✅:
  - [实践1]: 具体描述
  - [实践2]: 具体描述

  **Watch Out** ⚠️:
  - [注意点1]: 问题 → 改进方向
  - [注意点2]: 问题 → 改进方向

  **Tools & Tricks** 🔧:
  - [工具1]: 工具名称 + 使用场景 + 效果
  - [技巧1]: 技巧描述 + 提效程度
  ```

**4. 技术债务管理**:
- 技术债清单表格(7列): ID|描述|优先级(H/M/L)|发现Round|责任SubPlan|预计解决时间|状态
- 状态图例: ⬜未解决 🔄解决中 ✅已解决 ⏭️已忽略
- 优先级说明:
  - H (High): 阻塞后续开发，必须立即解决
  - M (Medium): 影响质量，应尽快解决
  - L (Low): 优化项，可延后解决

**5. 问题解决案例库** ⭐ **E1协议记录**:
- 组织方式: 按问题类型分类
- 问题类型: 测试失败 (Test Failures) | 架构冲突 (Architecture Conflicts) | 依赖问题 (Dependency Issues) | 性能偏差 (Performance Deviations) | 集成错误 (Integration Errors)
- **每个案例结构**:
  ```markdown
  #### 案例{{ID}}: {{问题标题}}

  **问题类型**: {{类型}}

  **E1协议流程记录**:
  1. **STOP**: 问题发现时刻和现象
     - 时间: {{时间戳}}
     - 现象: {{具体现象描述}}
     - 影响范围: {{Round/SubPlan/Phase}}

  2. **Report**: 问题根因分析
     - 根因: {{根本原因}}
     - 诊断过程: {{如何定位的}}

  3. **Rollback**: 回滚操作（如有）
     - 回滚内容: {{回滚的代码/配置}}
     - 回滚原因: {{为什么回滚}}

  4. **Fix**: 修复方案
     - 修复方案: {{具体修复措施}}
     - 实施步骤: {{步骤列表}}

  5. **Verify**: 修复验证
     - 验证方法: {{如何验证}}
     - 验证结果: {{验证通过/失败}}

  6. **Resume**: 恢复执行
     - 恢复时间: {{时间戳}}
     - 后续影响: {{对后续Round的影响}}

  **经验教训**:
  - {{关键经验1}}
  - {{关键经验2}}

  **相关Round**: Round {{X}}, SubPlan_{{序号}}
  ```

**6. 最佳实践提炼**:
- 组织方式: A/B/C三级分类
- **A级实践** (必须遵守): 实践描述 | 适用场景 | 证据(哪些Round验证有效) | 影响
- **B级实践** (强烈推荐): 实践描述 | 适用场景 | 证据 | 影响
- **C级实践** (可选优化): 实践描述 | 适用场景 | 证据 | 影响

**7. 数据驱动分析**:
- Round平均耗时趋势: 图表/数据（学习曲线）
- 技术债累积趋势: 按时间轴统计
- 问题类型分布: 饼图/百分比
- 最常见问题TOP 5: 排序列表
- 最有效实践TOP 5: 基于应用频率排序

**8. Lessons更新记录表**:
- 表格(5列): 更新时间|更新人|变更内容|Round ID|备注
- 审计追踪: 每次Round.Act强制添加记录
- 初始记录: v1.0|AI Agent|初始生成|N/A|基于MasterPlan生成

---

**变量替换规则**:
- `{{SPEC_PRJ_NAME}}` `{{TIMESTAMP}}` 替换为实际值
- `{{TOTAL_ROUND_RECORDED}}` `{{TOTAL_TECH_DEBT}}` `{{TOTAL_PROBLEM_CASES}}` `{{BEST_PRACTICES_COUNT}}` 替换为统计值
- `{{序号}}` `{{TYPE}}` `{{功能简称}}` `{{Phase名称}}` `{{Round目标}}` `{{时间}}` `{{状态}}` 替换为SubPlan数据
- `{{ID}}` `{{问题标题}}` `{{类型}}` `{{时间戳}}` `{{描述}}` `{{经验}}` 替换为案例数据

**典型长度**: 300-400行 (小型200-300/大型500-600，随Round增加而增长)

**强制更新机制** (边学边干):
- **触发时机**: SubPlan Round.Act(全部通过✅) 或 Round遇到问题时
- **强制更新内容**:
  ```
  Round.Act(全部通过✅):
    1. Round-by-Round添加本Round记录 (C2-Reflection)
       - Good Practices: 本Round有效实践
       - Watch Out: 本Round注意事项
       - Tools & Tricks: 本Round使用的工具/技巧

    2. 如有技术债 → 添加到技术债务清单 (E1-Report)
       - 技术债描述/优先级(H/M/L)/预计解决时间/责任SubPlan

    3. 如有问题解决 → 添加到问题解决案例库 (E1完整流程)
       - 问题类型/E1流程记录/解决方案/经验教训

    4. 仪表盘同步 (C3.2-Consumer)
       - 立即更新 `SpecExecMasterDashboard_L2.md` Round进度、SubPlan状态与“最后更新”时间
       - 若MasterPlan/各SubPlan存在Round进度表，同步标记该Round完成

    5. Git 小步提交 (I4-版本控制)
       - 执行 `git add` & `git commit -m "round: <GOAL>/<Round> pass"` 形成可回溯节点
       - 与 Step 12 的阶段性提交配合，确保每轮通过后都有版本记录
  ```

**生成策略**:
- **新项目**: 基于MasterPlan的SubPlan索引表生成初始Lessons，所有章节为空结构
- **已有项目**: 读取Dashboard和SubPlan执行记录，同步已完成Round的Lessons
- **不确定时**: HITL（Round记录缺失/技术债优先级不明/问题案例分类模糊）

**数据来源**:
- 主要: 从各SubPlan的Round小结和Lessons & Learning章节提取
- 辅助: 从MasterPlan的SubPlan执行状态记录区提取
- 更新频率: Round完成时强制更新，边学边干

**生成要点**:
- Lessons是持久化知识库，记录随Round增加而增长
- Round-by-Round记录按SubPlan组织，保持追溯性
- E1案例库记录完整的6步流程（STOP→Report→Rollback→Fix→Verify→Resume）
- 技术债务管理提供H/M/L优先级分级
- 最佳实践提炼提供A/B/C三级分类

---

**End of Build_Spec_Exec_Master_Plan_L2.md**
