# Build_Spec_Exec_Master_Plan_L3.md

> 🎯 **定位**: L3 级别执行计划生成引擎（Rigorous 模式）
> 📋 **用途**: 读取 SPEC 脚手架，生成 AI Agent 可执行的 ProgressPlan 体系
> 🧠 **本质**: 方法论指导文档，提供判断空间而不是机械脚本

> ⚠️ **执行契约**: 进入本文件 = 立即启动十二步工作流。从 `Step 1` 开始按顺序推进；如需临时分析草稿，只能放入 `_scratch/` 或沙箱，并在进入 `Step 5` 前清理。

---

## 📖 Constitutional 原则引用索引（ACA 宪法桥接）

> **核心依据**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md`
> **桥接方式**: Constitutional-Level 公理 → L3-RIGOROUS 具体执行

### 四大不变量（Four Invariants）
- **I1-CanonicalLocationUniqueness**: 权威位置唯一性  
  L3 应用：Constraints / MasterPlan / SubPlan / Dashboard / Lessons 等核心文档需拥有唯一 canonical 位置，并维护 GOAL registry 与团队 artefact 的同步。
- **I2-CompletenessPrinciple**: 完整性原则  
  L3 应用：MasterPlan / SubPlan / Dashboard / Lessons 必须结合三层追溯字段，实现 artefact 全景覆盖。
- **I3-QualityVerificationTriple**: 质量验证三元组  
  L3 应用：{Pre} AI_Create {Post: Verify}，Step 5-11 中落地质量门禁与 PMI 风格检查。
- **I4-DependencyChainIntegrity**: 依赖链完整性  
  L3 应用：Constraints → MasterPlan → SubPlan → Dashboard → Lessons → GOAL registry 构成平衡依赖链，维护 Function Point / Scenario / Task Sequence 闭环。

### 执行协议（Execution Protocols）
- **C2-PDCA**: Plan → Do → Check → Act  
  L3 应用：ProgressPlan = 团队共创 PDCA；Round.Act 触发 Dashboard 更新并沉淀 Lessons。
- **C3-ProducerConsumerContract**: 生产者-消费者契约  
  L3 应用：SubPlan = Producer，Dashboard = C3.2-Consumer，Lessons = PDCA Reflection 承载体。
- **E1-EmergencyProtocol**: STOP → Report → Rollback → Fix → Verify → Resume  
  L3 应用：分级决策机制结合协调规格与风险矩阵，Lessons 中记录跨角色案例。

### L3 宪章对齐（`SPEC_ACA_L3_CHARTER.md`）
- **CheckpointCount**: 10-15 项检查点，≥95% 通过率，覆盖协作、质量、合规、审计门禁。
- **TraceDepth**: 3+ 层追溯 —— US → FP/DES → SC/TS → GOAL/SEQ/CTX；Dashboard / Lessons 必须回溯到最原始 artefact。
- **协作模式**: C3-LEAD，默认人类主导决策，AI 辅助执行与审计，HITL 频率高于 L2。
- **质量阈值**: 覆盖率 ≥95%、变异测试 ≥85%、CI/CD 门禁全自动、合规/风险零容忍（问题需在 Lessons/E1 中完整记录）。

### 本文档的 Constitutional 桥接说明
- Constitutional 定义“必须遵守什么”（不变量和协议）。
- 本文档定义“如何在 L3 级别执行”（方法论与模板，强调协作与三层追溯）。
- 引用格式 `(I1)` / `(C2-PDCA)` / `(E1)` 指向对应 Constitutional 原则。

---

## 📖 目录与快速导航

**🎯 首次阅读路径**: §0 概览 → §14 十二步执行流程 → 按需查阅 §1-§13。

**📚 章节功能分组**
- **概览** (§0): 文档目的 / ProgressPlan 概念 / HITL 机制 / 执行次序 / 版本说明。
- **方法论** (§1-§9): 引擎架构 / 文件识别 / Phase 划分 / Round 规划 / 上下文提炼 / HITL / Plan 更新。
- **模板** (§10-§13): MasterPlan / SubPlan / Constraints / Dashboard 生成指导。
- **执行** (§14): 十二步工作流 (Step 1-12) — ⭐ AI Agent 执行入口。

---

## § 0. 文档概览与核心概念

### § 0.1 这个文档是什么

**元层次定位**: 生成 ProgressPlan 的 ProgressPlan。

**输入**: SPEC 脚手架（`spec/` 目录 + 四阶段文档）。  
**输出**: 5 类可执行 ProgressPlan 文档（遵循 I1-CanonicalLocation 原则）：
- `SpecExecMasterConstraints_L3.md` — 目录结构与命名约定 (~80-120 行)（I1-Canonical 定义器）。
- `SpecExecMasterPlan_L3.md` — 总控 ProgressPlan (150-250 行)（C3.1-Producer 总控）。
- `SpecExecSubPlan_*.md` — 独立执行单元 (各 400-800 行)（C3.1-Producer 执行单元）。
- `SpecExecMasterDashboard_L3.md` ⭐ — 进度 Contract 验证 (~200-300 行)（C3.2-Consumer）。
- `SpecExecMasterLessons_L3.md` ⭐ — Reflection 知识库 (~300-400 行)（C2-PDCA + E1）。

**生成过程**: 12 步工作流 + Human-in-the-Loop 决策点。  
**文档性质**: 方法论指导，强调 AI Agent 判断空间，避免机械执行。

### § 0.2 什么是 ProgressPlan（Constitutional 桥接）

**C2-PDCA 桥接**  
ProgressPlan = PDCA 循环的 AI Agent 实现。
- **Plan**: 前置条件检查（C2.1-Plan）+ 推理分析（目标/文档/产出）。
- **Do**: 执行创建 + 遵守 Invariants (I1/I2/I3/I4)。
- **Check**: 后置条件验证（C2.3-Check）+ 质量门禁。
- **Act**: 决策路径（继续 / 重试 / 升级 / 回滚）+ Lessons 记录。

**E1-EmergencyProtocol 桥接**  
Reflection 机制 = Check 阶段验证 + E1 的 Report 步骤持久化；分级决策遵循 STOP → Report → Rollback → Fix → Verify → Resume。

### § 0.3 HITL 升级规则
- 缺失核心 artefact（GOAL、value_path、coordination 等）。
- TraceDepth=3+ 断链、审计字段缺失、门禁达标率 <95%。
- 跨团队协作冲突、风险矩阵标红、合规条目无凭证。
- 使用模板时遇到字段无法确定、命名不符合 authority、架构决策未获批等情况。
- HITL 通知格式详见附录模板，必须在输出中说明原因与待确认字段。

### § 0.4 ProgressPlan 输出家族
```
SpecExecMasterConstraints_L3.md  # Canonical 约束
SpecExecMasterPlan_L3.md         # 总控计划
SpecExecSubPlan_XX_*.md          # 执行单元（N 个）
SpecExecMasterDashboard_L3.md    # 进度 + 质量合同
SpecExecMasterLessons_L3.md      # Reflection 知识库
```

### § 0.5 版本说明与迭代路线
- **当前版本**: v1.0（2025-01）— 企业级审计骨架。
- **阶段特征**: Canonical 文件齐备、TraceDepth=3+ 验证、SubPlan/Round 进度播报、Dashboard TODO 保持同步。
- **未来演进**: 计划引入自动差异分析 / 合规报告生成 / 企业级审计 API。
- **原则**: 每阶段可独立审计；决策有证据；版本可追溯、向后兼容。

### § 0.6 步骤完成标准格式（统一播报）
- Step 1-11 禁止使用“全部完成”。
- 输出格式：`🎯 Step {X}/12 ...` + `📋 已产出 ...` + 下一步指引；若已知道 SubPlan/Round 总数需追加 `SubPlan {{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}`、`Round {{PLANNED_OR_DONE_ROUNDS}}/{{TOTAL_ROUNDS}}`。
- Step 5-9 附带 `⚠️ 阶段性输出` 与文件名称，并同步 TODO/Triage 变动（含合规/审计事项）。
- Step 10-11 使用 `📊` 前缀提示 Lessons / Dashboard 更新，播报 GOAL 挂靠与 TODO 勾选进度。
- Step 12 才可输出 `✅ ProgressPlan 体系已就绪`，并附关键审计数据摘要。
- 触发 HITL 时需说明原因与下一步路径。

---

## § 1. 引擎作用与核心依赖（Constitutional 桥接）

**输入**: SPEC 脚手架（`spec/` 目录 + 三支柱体系）。

**输出**: Constraints (1) + MasterPlan (1) + SubPlan (N) + Dashboard (1) + Lessons (1)。

**关键依赖链 (I4)**
1. Constraints 必须最先生成（I1 + C2.1 Plan 前置条件）。
2. MasterPlan → SubPlan → Dashboard/Lessons 依赖链必须保持完整。
3. 每个 artefact（除根节点）都要引用父 artefact，确保追溯链完整。

---

## § 2. L3 特征快照
- **心态**: Balance over Speed。优先结构化协作、审计可证。
- **结构**: Function Point ↔ BDD 场景闭环，value_path 映射贯通设计到验证。
- **门禁**: PMI 式多轨并行；CI/CD 全门禁；TraceDepth=3+；风险零容忍。
- **Artefact 约束**: owner / version / timestamp / audit_log_ref 全量必须填写。

---

## § 3. 方法论依据
- 遵循 SPEC CRAFT 精神（参考 `four_stage_crafting/CRAFT_L3_*.md`）。
- 结合 `SPEC_ACA_*`（宪法）+ `SPEC_ARTIFACT_NAMING_*`（命名 authority）。
- ProgressPlan 输出 = 三支柱（Producer / Consumer / Toolkit）的桥梁。

---

## § 4. 文件发现与识别策略

### 4.1 遍历 `spec/`
- 跳过 `_` 前缀目录，列出其余文件。
- 读取文件开头 50-100 行确认文档类型并记录 artefact。

### 4.2 Artefact 分类速览
| 分类 | 主要来源 | 重点字段 |
|------|----------|----------|
| US / AC | `requirements/` | `id`/`sn`/下游引用 |
| Function Point / value_path | `design/` | `source_us`、`value_path_mapping`、`related_sc` |
| 设计 artefact | `design/` | 架构/组件/接口与 coordination 链接 |
| BDD / Test Suite / Test Data / Quality Definition | `implementation/` | `source_fp`、`related_sc`、门禁指标 |
| GOAL / Task artefact | `task_planning/` | `source_us`、`related_sc`、`related_seq`、`context_refs`、`coordination_refs`、`audit_log_ref` |

### 4.3 缺失处理
- 任何 artefact 缺失即标 `📌 待确认`；必要时触发 HITL。
- value_path 或 coordination 缺口会影响 Phase / Round 规划，提前登记。

### 4.4 技术栈与结构识别
- 阅读 `architecture`、`project_structure`、`tdd_strategy` 等文档识别前后端 / 测试框架 / 目录布局。
- 如无法确定，触发 C2-PARTICIPATE HITL；输出中说明待确认项。

### 4.5 GOAL 与协同 artefact 采集
- 解析 `task_planning/goal_breakdown.md` 生成 `GOAL_INDEX`（`id/sn/source_us/related_sc/related_seq/context_refs/coordination_refs/audit_log_ref`）。
- 核对 `task_breakdown`、`task_sequence`、`task_coordination_spec`、`blocker_anticipation`、`ai_context_specification` 等文档是否覆盖全部 GOAL。
- SC / SEQ 未被任何 GOAL 引用或缺失字段 → 标记差异并在 Step 7/8 前处理。

---

## § 5. Phase 划分方法（L3 核心）

### 5.1 主线策略：Function Point & value_path 链路
- 读取 `CRAFT_L3_DESIGN.md` / `CRAFT_L3_IMPLEMENTATION.md` 中 Function Point 列表、value_path_mapping、BDD 映射。
- 每个 Function Point 为候选 Phase；同一 value_path 且强耦合可组合。
- 结合 `CRAFT_L3_TASK_PLANNING.md` 的 GOAL ↔ FP ↔ SC 关联，确保 Phase 与 GOAL/SEQ 闭环一致。

### 5.2 依赖关系推断
- **技术层**: value_path 四向度（前端交互 → 数据流转 → 后端处理 → 结果反馈）。
- **业务层**: `task_sequence`、`task_coordination_spec` 中的依赖/同步点/优先级。
- **质量层**: `CRAFT_L3_IMPLEMENTATION.md` 的测试数据、质量定义、集成编排文档。

### 5.3 集成 Phase 与协调窗口
- 每 2-3 个 FP Phase 加入集成/协调 Phase；coordination 标记跨模块同步点或 blocker 高风险时必加。
- 终局必须有 FINAL INTEGRATION Phase 负责端到端验收。
- Phase 内需注明协调维度（接口/数据/部署）与预期输出。

### 5.4 SubPlan 划分规则（Master-SubPlan 架构）
- **GOAL SubPlan**: `SpecExecSubPlan_{序号}_{GOAL_ID}_L3.md`，复写 GOAL front matter 全字段。
- **基础设施**: 若 Constraints 强调基础设施 Phase，固定 `SpecExecSubPlan_01_INFRASTRUCTURE_L3.md`。
- **集成 Phase**: `SpecExecSubPlan_{序号}_INTEGRATION_PHASE{N}_L3.md`，终态用 `_INTEGRATION_FINAL_L3.md`。
- **顺序规则**: 两位数字（01-99）表示推荐执行序；基础设施固定 01，GOAL SubPlan 按 `task_sequence` 排序，协调/集成紧随相关 GOAL。

### 5.5 TraceDepth=3+ 检查清单
- **GOAL ↔ US/FP/SC/SEQ/CTX**: `source_us`、`related_fp`（若存在）、`related_sc`、`related_seq`、`context_refs` 必填。
- **DES ↔ 实现**: 组件/API/数据模型的 `source_fp`、`related_coordination`、`audit_log_ref`。
- **测试资产**: SC ↔ TS / Test Data / Quality Definition，需包含 `source_des` 或 `source_fp`。
- **审计层**: 每个关键 artefact 需记录 `owner`、`version`、`timestamp`、`audit_log_ref`，并在 Lessons/Dashboard 中可追溯。
- **验证方法**: Step 7/8 完成后使用 TraceDepth 检查表（见 §14 Step 7/8）逐项打勾；缺失项写入 TODO 并触发 HITL。

---

## § 6. Round 规划方法（value_path + PDCA）

### 6.1 核心理念：value_path 驱动的弹性轮次
- 每条 value_path 至少经历 RED → GREEN → CHECK/REFINE；多人协作的 FP 增加协调轮次。
- 示例结构：
```
Phase: FP/GOAL
├─ Round A: value_path RED（编写场景 + 失败测试）
├─ Round B: value_path GREEN（实现 + 通过测试）
├─ Round C: Refactor / 性能 / 安全
├─ Round D: 协同/集成（coordination 同步）
└─ Round Buffer: 风险或技术债
```

### 6.2 Round 内 PDCA 结构
- **Plan**: 明确 value_path 向度、引用 FP/SC/coordination/ctx 文档、列出质量门禁（覆盖率 ≥95%、变异测试 ≥85%、集成 ≥99%、风险关闭 ≥95%）。
- **Do**: 实施/测试/协作动作，记录涉及 artefact。
- **Check**: 对照 `CONSTRAINT_L3_*` 清单验证质量门禁，复核 TraceDepth 字段。
- **Act**: 决策（继续/重试/HITL），并强制触发 Dashboard & Git 更新（见 §14 Step 11-12）。

### 6.3 Round 估算与分类
- 单 FP 4-6 轮；含集成的 GOAL 6-9 轮；大型协调场景 8-12 轮。
- 分类：value_path Implementation / Coordination & Integration / Quality Gate / Risk & Blocker Resolution。

### 6.4 TDD & value_path 映射
- RED：编写 BDD 场景 + 测试，确保失败。
- GREEN：实现功能并满足 value_path 验证。
- REFACTOR：性能/安全/可维护性优化，符合 L3 质量标准。
- Integration：结合 coordination spec、test data、quality definition，完成跨模块验证。

### 6.5 自信度评估与 HITL
- ≥80%：文档齐全 → 自主执行。
- 50-80%：value_path / coordination 缺确认 → Round Plan 标注 `📌 待确认` 并同步 Dashboard。
- <50%：文档缺失/依赖冲突/风险剧烈 → 触发 C2-PARTICIPATE HITL。

### 6.6 Round 完成后的强制操作
1. Lessons Round-by-Round 更新（Good Practices / Watch Out / Tools & Tricks）。
2. Dashboard 刷新 Round 进度、SubPlan 状态、最后更新时间。
3. 执行 Git 小步提交（`round: <GOAL>/<Round> pass`）。
4. 风险/协调调整 → 更新 blocker / coordination artefact。
5. 若质量门禁未过或 TraceDepth 缺口 → 标记 Dashboard TODO 并触发 HITL。

---

## § 7. 上下文提炼策略

### 7.1 构建多维引用映射
- US ↔ AC ↔ FP：需求到设计桥接。
- FP ↔ SC ↔ TS：value_path & BDD 场景映射。
- FP ↔ API/CMP/DM：组件/接口/数据模型引用关系。
- GOAL ↔ SEQ/BLK/COORD/CTX：Task 规划 artefact 构建执行链路。

### 7.2 精准引用策略
- Round 计划引用格式：`[GOAL_ID] → FP-ID → value_path 维度 → SC-ID → 文档段落`。
- SubPlan 中建立“执行依赖索引”表，减少重复查阅。
- 调试/排查优先查看 coordination spec 与 blocker 文档。

### 7.3 上下文裁剪
- 只加载当前 Round value_path 相关片段，可使用锚点。
- 若引用同一文档多段，建立“章节别名”。
- 长篇 BPMN / 流程说明，用摘要或表格形式复述，避免重复粘贴。

### 7.4 追溯链验证
- 建立映射表后运行 consistency check：每个 FP 有 `source_us`/`related_sc`，每个 SC 可追溯到 GOAL。
- Step 7/8 生成 MasterPlan / SubPlan 前再次审查映射完整性；缺失项立即标记 HITL。

---

## § 8. HITL 检查点设计

### 8.1 Phase 边界协作检查
1. Phase 目标达成（GOAL / FP / SC / SEQ 闭环）。
2. 质量门禁：覆盖率 ≥95%、变异测试 ≥85%、集成 ≥99%、风险关闭 ≥95%。
3. 协作评审：coordination spec 对齐、blocker 处置、Lessons 更新。
4. 决策确认：下一 Phase 是否调整计划或顺序。

### 8.2 Round 内智能触发
- 🔴 阻塞：value_path 闭环失败、沟通中断、门禁未过 → 立即 HITL。
- 🟡 警告：覆盖率低于目标 5%、协调窗口冲突、技术债攀升 → 与用户协商。
- 🟢 建议：优化机会、最佳实践 → 记录 Lessons。

### 8.3 Lessons & Reflection 模板
- Round-by-Round：目标 / 结果 / 工具 / 协作回顾。
- 技术债务：优先级 (H/M/L) / 归属团队 / 预计解决轮次。
- 问题案例：完整 E1 流程 + 决策缘由。
- 协同洞察：跨角色沟通要点 / 同步窗口经验。
- KPI 回顾：覆盖率、缺陷率、响应时间等。

---

## § 9. 动态 Plan 更新策略
- 重大 value_path 调整、FP 新增/拆分、Phase 偏差 >30%、门禁/风险提示 → 可更新。
- Round 微调 ±2、局部实现或测试细节不触发 Plan 更新。
- 更新流程：Phase 评估会 → 生成建议 → HITL 决策 → 更新文档并递增版本号 → Dashboard 与 Lessons 同步记录。
- 更新后重新校验 GOAL registry 与 SubPlan 序号，确保 I4 链完整。

---

## § 10. `SpecExecMasterPlan_L3.md` 生成指导（总控）
1. 复制模板，填入项目信息、约束引用、版本号。
2. 导入 SubPlan 索引表（序号 / 类型 / GOAL / Phase / 预估 Round / 协调窗口 / 状态 / 门禁）。
3. 绘制 Phase 与 value_path 依赖图，标注集成门禁与风险缓冲。
4. 生成 GOAL 覆盖表：`id/sn/source_us/related_sc/related_seq/context_refs/coordination_refs/audit_log_ref/assigned_subplan/status/KPI`。
5. 汇总全局 HITL 检查点、风险/恢复策略、Plan 变更历史、KPI。

**L3 特有检查点**
- 所有 GOAL 在覆盖表中并指向唯一 SubPlan。
- SubPlan 索引突出协调窗口、风险等级、TraceDepth 确认状态。
- 依赖图展示 value_path 顺序 + 集成 Phase。
- Dashboard / Lessons 引用占位留待 Step 9/10 使用。

---

## § 11. `SpecExecSubPlan_*.md` 生成指导（执行单元）
1. 命名：`SpecExecSubPlan_{序号}_{GOAL或类型}_L3.md`（序号两位）。
2. 填写元信息：序号 / 类型 / GOAL / Phase / 预估 Round / 协调窗口 / 质量门禁 / TraceDepth 状态。
3. 引入执行依赖索引：Constraints、FP、value_path、coordination、blocker、Test/Quality artefact。
4. 复写 GOAL_COVERAGE：`id/sn/source_us/related_sc/related_seq/context_refs/coordination_refs/audit_log_ref`，缺项必须标记 `📌`。
5. 嵌入 Step 4 规划的 Round（Plan/Do/Check/Act + Buffer），注明门禁指标。
6. 设置进度 & KPI 表、Lessons & coordination 占位、风险恢复树、TODO/Triage 列表；确保 Round 总数/完成数可快速播报。
7. 记录 Evidence（测试报告、Git commit、Dashboard 截图）链接，便于 Step 9/15 引用。

**L3 特有检查点**
- GOAL 行字段完整，TraceDepth=3+ 可回溯。
- Round 规划包含 value_path 四向度与协调动作。
- Lessons/Dashboard 引用占位存在（Round 完成后立刻更新）。
- 风险/技术债记录与 coordination artefact 对齐。

---

## § 12. `SpecExecMasterConstraints_L3.md` 生成指导（Canonical 约束）

**定位**: 目录 / 命名 / 禁止区域的 Canonical 约束（90-140 行）。

**必备元素**
1. 文档头部 + 版本信息 + 审计字段（owner/version/timestamp/audit_log_ref）。
2. 强约束声明：文件位置、命名规则、禁止区域、引用方式。
3. 技术栈识别表（前端 / 后端 / 测试 / 数据库 / 部署）。
4. 目录结构：根目录 / 源码 / 测试 / 部署 / 合规模块。
5. 命名约定：文件 / 目录 / 组件 / 函数 / 常量，提供正反例。
6. 禁止区域 & 忽略列表；CI/CD、合规、审计输出的存放规范。
7. 执行引用方式（Round / Step 如何使用）。
8. 约定变更日志（含审计证据链接）。

**推荐检查点分层（10-15 项）**
| 维度 | 重点检查 | 参考来源 |
|------|----------|----------|
| 目录结构 | Canonical 根目录、artefact 归位、`goal_breakdown` 唯一性 | `CONSTRAINT_L3_*`、`CRAFT_L3_TASK_PLANNING.md` |
| 命名规范 | Artefact 前缀、Front Matter、owner/version/timestamp/audit_log_ref | `SPEC_ARTIFACT_NAMING_L3_AUTHORITY.md` |
| 质量门禁 | 覆盖率 ≥95%、变异测试 ≥85%、集成 ≥99%、风险关闭 ≥95% | `CONSTRAINT_L3_IMPLEMENTATION.md`、`CONSTRAINT_L3_TASK_PLANNING.md` |
| 合规审计 | 审计记录、追溯矩阵、Evidence 存档、E1 日志 | `CONSTRAINT_L3_DESIGN.md`、`audit_tracking_spec` |
| 变更控制 | CCB、版本递增策略、Dashboard / Lessons 同步 | `CRAFT_L3_IMPLEMENTATION.md`、项目治理文档 |

勾选这 10-15 项检查点时，应引用对应 artefact（文件或章节）并记录审计证据（链接或路径）。

---

## § 13. `SpecExecMasterDashboard_L3.md` 生成指导（Consumer）

**定位**: 进度 Contract 验证文档 (~220-320 行)。

**核心职责**: 项目概览 KPI | SubPlan 状态 | Round 汇总 | 协调预测 | 当前焦点 | 里程碑 | 质量指标 | 更新记录。

**必需章节**
1. 文档头部：标题、引用块（项目名/类型/生成时间）、版本 v1.0。
2. 项目概览与 KPI：表格列出项目名、约束级别 (L3-RIGOROUS)、SubPlan/Phase/GOAL 总数与完成度、Round 指标、风险统计、质量通过率。
3. SubPlan 执行状态：表格（序号/文件/类型/关联 Phase/状态/轮次进度/覆盖率/变异测试/集成/风险关闭/质量门禁/最后更新）。状态图例 ⬜/🔄/✅/❌/⏸。
4. Round 进度汇总：按 SubPlan 绘制 ASCII 条形图，列出已完成轮次、总轮次、质量门禁结果。
5. 协调与风险预测：结合 Lessons 与 coordination spec，列出高风险 SubPlan、关键路径、预计完成时间、建议动作。
6. 当前焦点：正在执行、即将启动、等待 HITL 决策项。
7. 里程碑清单：表格（里程碑/定义/状态/时间/备注），覆盖基础设施、关键 FP、阶段集成、最终交付。
8. 质量指标汇总：覆盖率均值（目标 ≥95%）、变异测试通过率（目标 ≥85%）、集成通过率（≥99%）、风险关闭率（≥95%）、质量门禁通过率、未解决 blocker 数、技术债项数。
9. Dashboard 更新记录：表格（版本/时间/来源/更新内容），初始记录 `v1.0 | {{TIMESTAMP}} | MasterPlan 初始生成 | Dashboard 初始化`。
10. Consumer 验证说明：Producer-Consumer 合同、验证流程、质量门禁失败处理（记录证据 → HITL 决策）。

**数据来源**
- MasterPlan SubPlan 状态区、SubPlan Round 表、Lessons、coordination/blocker 文档。
- KPI 数值必须可追溯到 SubPlan Round 统计、测试/质量报告或 Lessons 数据；无法确认时标注 `📌 待确认` 并将“数据来源补齐”写入 Dashboard TODO。

**生成要点**
- Dashboard 仅验证，不直接修改 Plan。
- 所有统计注明来源；无法确定时标注 `📌 待确认`。
- Round 汇总聚焦结果，不复制详细步骤。
- 质量门禁采用 L3 阈值：覆盖率 ≥95%、变异测试 ≥85%、集成 ≥99%、风险关闭率 ≥95%。
- TODO/Next Actions 需同步列出待补充数据来源、合规检查与 HITL 事项；Step 11 勾选时必须更新时间戳与责任人。

---

## § 14. 十二步工作流（AI Agent 执行指导）

**执行契约摘要**
- 连续执行 Step 1-12，除 HITL 外不暂停。
- 进度透明：按 §0.6 模板输出；播报 SubPlan/Round 完成度。
- Dashboard/TODO 维护：MasterPlan/SubPlan/Lessons 调整后记录待同步项；Dashboard 自 Step 9 起即时刷新 TODO；Step 11 勾选完成项并播报状态。
- HITL 触发：artefact 缺失、TraceDepth 断链、门禁未达标、协作冲突；使用 §0.3 模板。
- 工具提示：CLI/IDE Agent 如需暂停，需说明原因并引用下一步。
- 恢复机制：用户中断后，先检查文件状态，再从中断 Step 继续；如文件已生成可保留。

### Step 1（预计 3-4 分钟）: 读取脚手架 + 识别技术栈
- 输入：`spec/` 目录树。
- 操作：依照 §4 表格核对 artefact，记录缺失；解析 `goal_breakdown.md` 生成 `GOAL_INDEX`；整理技术栈与项目类型。
- 输出：artefact 清单、`GOAL_INDEX`、技术栈/项目类型。
- 进度提示：`🎯 Step 1/12 (8%) — 分析产出，继续执行 Step 2`。

### Step 2（预计 4-6 分钟）: Phase 划分
- 输入：Step 1 结果、CRAFT Phase 指南。
- 操作：依据 Function Point/value_path 制定 Phase 序列，标注集成窗口与风险缓冲。
- 输出：Phase 列表、依赖图草案。
- 进度提示：`🎯 Step 2/12 (17%) — 继续执行 Step 3`。

### Step 3（预计 3-5 分钟）: SubPlan 划分
- 输入：Phase 结果、`GOAL_INDEX`。
- 操作：将 GOAL/协调窗口映射到 SubPlan；编号；识别前置依赖；统计 SubPlan 总数，用于后续进度播报与 Dashboard/TODO。
- 输出：SubPlan 索引表。
- 进度提示：`🎯 Step 3/12 (25%) — 继续执行 Step 4（SubPlan 总数：{{TOTAL_SUBPLANS}}）`。

### Step 4（预计 4-6 分钟）: Round 规划
- 输入：SubPlan 列表、value_path、coordination 数据。
- 操作：为每个 SubPlan 规划 Round（RED/GREEN/REFACTOR/Integration + Buffer），记录门禁指标；统计全局 Round 总数以便播报；确保每个 SubPlan 至少包含测试资产建设/维护 Round（数据、mock、集成环境等）。
- 输出：Round 规划明细。
- 进度提示：`🎯 Step 4/12 (33%) — 继续执行 Step 5（Round 规划进度：{{PLANNED_ROUNDS}}/{{TOTAL_ROUNDS}}）`。

### Step 5（预计 3-5 分钟）: 生成 Master Constraints
- 输入：Round 规划、技术栈信息、`CONSTRAINT_L3_*` 文档。
- 操作：检查 `SpecExecMasterConstraints_L3.md` 是否存在；按 §12 模板生成或经 HITL 决策更新；勾选 10-15 项检查点并记录证据位置（目录/命名/质量门禁/合规/变更控制），缺项加入 TODO。
- 输出：`SpecExecMasterConstraints_L3.md`。
- 进度提示：`🎯 Step 5/12 (42%) — ⚠️ 阶段性输出，继续执行 Step 6`。

### Step 6（预计 3-5 分钟）: 生成 Lessons 框架
- 输入：SubPlan 列表、Constraints。
- 操作：生成或更新 `SpecExecMasterLessons_L3.md` 空框架，挂载 GOAL/SubPlan 占位符，填入审计元数据。
- 输出：Lessons 框架文件。
- 进度提示：`🎯 Step 6/12 (50%) — ⚠️ 阶段性输出，继续执行 Step 7`。

### Step 7（预计 5-7 分钟）: 生成 MasterPlan
- 输入：Constraints、Lessons 框架、SubPlan/Phase 数据、`GOAL_INDEX`。
- 操作：生成 `SpecExecMasterPlan_L3.md`，填充索引表、依赖图、GOAL 覆盖等；完成后执行 TraceDepth=3+ 检查清单：确认每条 GOAL 行具备 `source_us`、`related_sc`、`related_seq`、`context_refs`、`coordination_refs`、`audit_log_ref`，记录缺口至 Dashboard TODO/HITL。
- 输出：MasterPlan 总控文件。
- 进度提示：`🎯 Step 7/12 (58%) — ⚠️ 阶段性输出，继续执行 Step 8`。

### Step 8（预计 8-12 分钟）: 生成 SubPlan × N
- 输入：MasterPlan、Round 规划、`GOAL_INDEX`。
- 操作：为每个 SubPlan 生成/更新文件；显式安排测试资产建设/维护（数据、mock、集成环境）；设置进度追踪小节（Round 总数/完成数 + TODO/Triage）；复写 GOAL 行字段（`source_us`、`related_sc`、`related_seq`、`context_refs`、`coordination_refs`、`audit_log_ref`），缺项打 `📌` 并触发 HITL；引用合规/审计文档时同步 TODO；Round 完成需按 §6.6 更新 Lessons、Dashboard 并 git 提交。
- 输出：`SpecExecSubPlan_*_L3.md`。
- 进度提示：`🎯 Step 8/12 (67%) — ⚠️ 阶段性输出，继续执行 Step 9（SubPlan 已生成：{{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}）`。

### Step 9（预计 4-6 分钟）: 生成 Dashboard 完整版
- 输入：MasterPlan、SubPlan、Lessons、`GOAL_INDEX`。
- 操作：生成 `SpecExecMasterDashboard_L3.md`，填充 KPI、GOAL_STATUS、预测；对照 §13 指标表写入覆盖率（≥95%）、变异测试（≥85%）、集成（≥99%）、风险关闭（≥95%）等数据；所有数值需引用 SubPlan Round 统计、测试/质量 artefact 或 Lessons 证据，无法确认时标注 `📌 待确认` 并加入 TODO；同步/刷新 TODO Checklist（或 Next Actions），列出合规/审计数据待补项。
- 输出：Dashboard 文件。
- 进度提示：`🎯 Step 9/12 (75%) — ⚠️ 阶段性输出，继续执行 Step 10（Dashboard 进度：SubPlan {{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}, Round {{COMPLETED_ROUNDS}}/{{TOTAL_ROUNDS}}）`。

### Step 10（预计 2-3 分钟）: Lessons 挂靠 GOAL
- 输入：MasterPlan、SubPlan、Dashboard、`GOAL_INDEX`。
- 操作：将 GOAL/SubPlan 数据写入 Lessons 对应章节，补齐 Evidence 链接；标记缺失审计凭证的条目。
- 输出：Lessons 更新。
- 进度提示：`🎯 Step 10/12 (83%) — 📊 内容更新，继续执行 Step 11（Lessons 已挂靠 GOAL：{{LESSONS_LINKED}}/{{TOTAL_GOALS}}）`。

### Step 11（预计 1-2 分钟）: Dashboard 最终更新
- 输入：Dashboard、Lessons、最新 SubPlan 状态。
- 操作：更新 Dashboard 里程碑状态、TODO 清单（逐项勾选或保持 `📌`）、记录体系完成时间戳；对每项 TODO 标明责任人与 Evidence 链接。
- 输出：Dashboard 最终状态。
- 进度提示：`🎯 Step 11/12 (92%) — 📊 内容更新，继续执行 Step 12（Dashboard 标记完成：里程碑 {{MILESTONES_DONE}}/{{TOTAL_MILESTONES}}；待办 {{PENDING_TODOS}} 项）`。

### Step 12（预计 1-2 分钟）: Git 阶段提交
- 输入：所有 ProgressPlan 文件。
- 操作：执行 `git add` / `git commit`（如 `plan: add l3 progress suite v1`）；确认无遗漏文件，提交信息中引用关键 Evidence。
- 输出：ProgressPlan 最终提交记录。
- 进度提示：`🎯 Step 12/12 (100%) — ✅ ProgressPlan 体系就绪（审计记录：{{AUDIT_EVIDENCE_LINK}}）`。

---

## § 15. `SpecExecMasterLessons_L3.md` 生成指导（Reflection + 审计）

**定位**: Reflection 知识库 (~300-400 行)，实现 C2-PDCA Reflection + E1 Emergency 桥接。

**审计元数据约束**
- 文档头部必须包含 `owner`、`version`、`timestamp`、`audit_log_ref`，并与 `audit_tracking_spec`、`decision_context_spec` 建立双向链接。
- 每条 Round 记录与问题案例需注明 Evidence 来源（测试报告、Dashboard 截图、Git 提交号）；缺失时标注 `📌 待补证` 并在 TODO 区跟踪。
- 更新记录表必须记录提交者、时间戳、引用的审计 artefact（如 E1 case ID、GOAL 链接），确保 TraceDepth=3+ 延伸到审计层。

**必需章节**
1. 文档头部：标题、引用块（项目名/Lessons 类型/生成时间）、版本。
2. 知识库概览：指标表（总 Round 记录数 / 技术债数量 H/M/L / 问题案例数 / 最佳实践数 / 最后更新时间 / 覆盖率）。
3. Round-by-Round 记录：按 SubPlan 分组；每条 Round → TDD 阶段、实际耗时、状态、Good Practices、Watch Out、Tools & Tricks、Evidence。
4. 技术债务管理：表格（ID / 描述 / 优先级 / 发现 Round / 责任 SubPlan / 预计解决时间 / 状态），状态图例 ⬜/🔄/✅/⏭️。
5. 问题解决案例库（E1 协议）：按类型分类，记录 STOP/Report/Rollback/Fix/Verify/Resume + 经验教训 + Evidence。
6. 最佳实践提炼：A/B/C 分类（实践描述 / 适用场景 / 证据 / 影响）。
7. 数据驱动分析：Round 平均耗时趋势、技术债累积趋势、问题类型分布、TOP 问题/实践。
8. Lessons 更新记录表：更新时间 / 更新人 / 变更内容 / Round ID / 备注（含审计证据链接）。

**生成要点**
- Lessons = 持久化知识库，Round 完成即更新；缺证据则标 `📌` 并列入 TODO。
- 技术债务与 Dashboard TODO 保持对齐；E1 案例与 Dashboard 风险提示同步。
- 最佳实践说明必须引用验证 Round；不可凭空创造。
- 更新记录需与 Git 提交相互引用，形成审计闭环。

---

**End of Build_Spec_Exec_Master_Plan_L3.md**
