# 任务规划阶段约束原则 - L1-STREAMLINED

> **级别定位**: L1-STREAMLINED (快速迭代级 - 快速可用优于完美)
> **🤝 哼将配对**: 与 [CRAFT_L1_TASK_PLANNING.md](../four_stage_crafting/CRAFT_L1_TASK_PLANNING.md) 配对协作
> **核心概念参考**: [CONSTRAINT_CORE_CONCEPTS.md](CONSTRAINT_CORE_CONCEPTS.md)
> 🔗 **命名规范权威引用**:
> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L1 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` (必填 artifacts, 灵活模式, 验收标准)
>
> 🔗 **AICodingAgent规范权威引用**:
> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L1宪章**: `../agentic_spec/SPEC_ACA_L1_CHARTER.md` - L1质量标准 (4-6检查点, 通过率≥95%, 单层追溯)

---

## 🔥 TL;DR - 立即开始

> **目标**：快速掌握L1-STREAMLINED任务规划约束标准，确保快速TDD策略任务规划
> 
> **🎯 协作模式路径**：C1-CONFIRM模式直接执行 | C3-LEAD/C2-PARTICIPATE用户选择L1时执行
> 
> **核心价值**：快速声明式目标制定，快速可用优于完美，为AI自主执行提供目标导向指导

### ⚡ LLM策略要点速查
#### 🚫 严禁行为
- 完成当前任务后绝不自动开始下一个任务（必须停止等待用户指示）
- 绝不在未读requirements/design/implementation三阶段文档情况下执行任务
- 绝不在阶段完成前省略tdd_task_tracking.md和tdd_strategy_order.md的创建
- 不过度细分任务，避免复杂项目管理

#### ✅ 必须规划
- **上下文验证**：执行前必须确认已读requirements/design/implementation三文档
- **声明式目标制定**：设定AI要达成的目标和验收标准，而非具体执行步骤
- **AI上下文规格**：定义AI执行所需的完整上下文信息和配置要求
- **简单里程碑**：关键功能点里程碑，基于目标的验收标准
- **高容错变更**：允许目标调整和规格变更，自主执行优先
- **一次一任务**：完成当前任务后必须停止，等待用户指示
- **最终交付物**：阶段完成时必须创建4个核心文档([task_breakdown] + [task_sequence] + [blocker_anticipation] + [ai_context_specification])

---

## 术语口径（中文 → English）
- Goal（目标） - 声明式执行目标，描述要达成的结果而非执行步骤
- Task Sequence（任务序列） - 任务执行的顺序和依赖关系
- Blocker（阻塞点） - 可能阻碍任务执行的潜在问题
- AI Context（AI上下文） - AI执行任务所需的完整上下文信息
- Acceptance Criteria（验收标准） - 目标完成的判定标准
- Prerequisite（前置条件） - 任务执行前必须满足的条件
- Delivery Gate（交付门禁） - 质量检查和发布流程的控制点
- Declarative Goal Setting（声明式目标制定） - 定义目标而非步骤的规划方法
- Autonomous Execution（自主执行） - AI基于目标和上下文自主选择实现路径

---

## 🧪 TDD在任务规划阶段的L1定位

**核心原则**：⭐ TDD的快速策略任务规划阶段 - 基础执行规划准备

```
TDD在L1任务规划阶段的职责边界：
✅ 应该做：规划基础TDD策略任务和验证方法
✅ 应该做：制定粗粒度任务的策略步骤和验证标准
✅ 应该做：为后续TDD实施准备提供基础任务清单
✅ 应该做：基于requirements/design/implementation的基础验证规划
❌ 不应做：修改测试计划（属于implementation阶段职责）
❌ 不应做：直接进行代码生产（应通过task_planning指导后续TDD策略）
❌ 不应做：过度细分任务管理
```

**价值体现**：完成贯通流程的快速文档闭环：基于简化测试计划的TDD策略任务规划

---

## 🎯 L1约束检查重点

### 哼将产出验收标准

> **"哼哈二将"角色分离说明**：在本框架中，CRAFT负责实际内容生产（"哼将"），CONSTRAINT负责质量检查验收（"哈将"）。本文档作为"哈将"，专门验收CRAFT生产的内容质量。

**验收CRAFT生产的任务规划符合L1-STREAMLINED标准：**

- **快速规划验证**: 确保任务规划体现"快速可用优于完美"原则
- **粗粒度验证**: 检查任务颗粒度为1-3天完成，避免过度细分
- **简单里程碑验证**: 确保里程碑设置简单，验收标准基础
- **高容错验证**: 验证允许任务调整和计划变更，快速执行优先
- **上下文验证**: 检查基于requirements/design/implementation三文档
- **节奏控制验证**: 验证一次一任务原则，完成后停止
- **交付物验证**: 检查包含tdd_task_tracking.md和tdd_strategy_order.md
- **🆕 Vertical Slice追溯性**: 验证每个任务标注Vertical Slice ID和Function Point ID
- **🆕 端到端覆盖性**: 确保任务分解覆盖完整价值链路，无遗漏
- **🆕 端到端闭环性**: 检查Task→BDD→FP→VS的完整追溯链路
- **目标业务化验证**: 验证Goal标题使用业务术语，包含业务价值说明
- **验收标准分离验证**: 检查验收标准分为"业务视角"和"技术验证"两部分
- **技术术语密度验证**: 验证技术术语密度 ≤ 50%，目标层面业务化

---

## 📋 验收执行协议 ⭐ AI强制执行指南

> **目的**: Task-S6-3必须输出结构化验收报告，包含：验收对象清单、逐项检查结果（✅/❌+具体证据）、通过率统计、失败项详单、验收结论。
>
> **原则**: 信任AI能力，只定义"要什么结果"，不规定"怎么做"。

> **L1分组验收原则**: L1-STREAMLINED采用"主要验收组3-4个,每组3-5个子项"模式,
> 符合`SPEC_ACA_L1_CHARTER.md`中`CheckpointCount[4-6]`的分组验收语义。
> 通过率≥95%基于总子项计算,确保质量不妥协。

### 🔴 强制验收项（L1-STREAMLINED标准）- 16项验收

#### 1. 任务分解合理性验收
- 任务粒度1-3天，避免过度细分
- 任务描述清晰可执行

#### 2. 任务格式合规验收
- 十进制编号 + 复选框 + 四要素（任务目标、需求引用、测试要求、预期输出）

#### 3. 文档维度完整性验收 ⭐ 新增
- **L1核心维度标准**: 必须覆盖4个核心维度
  - 维度1: Task Breakdown（任务分解维度）- 必需
  - 维度2: Task Sequence（任务序列维度）- 必需
  - 维度3: Blocker Anticipation（阻塞预判维度）- 必需
  - 维度4: AI Context Specification（AI上下文规格维度）- 必需
- **维度覆盖验收**: 4个核心维度必须覆盖
- **检查方法**:
  - 步骤1: 确认4个核心维度必须覆盖（每个维度至少有对应文档体现：Breakdown + Sequence + Blocker + AIContext）
  - 步骤2: 确认CRAFT_L1_TASK_PLANNING.md体现维度驱动原则（维度是核心，文件数量是反映）
- **失败案例**:
  - "4个task_breakdown文件" → 缺少Sequence/Blocker/AIContext维度覆盖
  - "2个Breakdown + 2个Sequence" → 缺少Blocker/AIContext维度覆盖

#### 4. 依赖关系清晰验收
- 主要依赖关系已记录，支持任务执行

#### 5. 优先级排序验收
- 关键功能优先，粗粒度里程碑合理

#### 6. 可执行性验收
- 任务目标明确，验收标准基础清晰
- AI上下文规格完整

#### 7. SC→GOAL转换机制验收 ⭐ 新增
- **转换完整性检查**: GOAL验收标准是否直接基于对应SC的Given-When-Then步骤
- **语义一致性验证**: 确保GOAL目标与SC场景的语义完全一致
- **转换模板应用**: 验证使用了标准的SC→GOAL转换模板

#### 8. 声明式目标验收
- Goal描述结果（不是步骤），避免过程式代码
- **过程式代码深度检查**: 严格检查是否含有函数调用、方法执行等过程式代码片段

#### 9. 技术术语密度量化验收 ⭐ 新增
- **密度计算验证**: Goal标题和验收标准中技术术语占比≤50%
- **量化标准应用**: 使用明确的计算方法验证技术术语密度
- **业务语言比例**: 确保业务术语和价值说明占主导地位

#### 10. 线性目标路径验收 ⭐ 新增
- **串行依赖检查**: 验证目标间的串行依赖关系清晰明确
- **简单数字顺序**: 确保使用简单数字顺序（Goal-01→Goal-02→Goal-03）
- **复杂并行依赖控制**: 避免存在复杂的并行依赖关系

#### 11. 文档行数控制验收 ⭐ 新增
- **行数限制检查**: 各文档控制在400-500行范围内
- **超长处理验证**: 超出时按模块合理拆分的策略检查
- **内容密度平衡**: 确保内容充实而非格式冗余

#### 12. 阻塞预判文档质量验收 ⭐ 新增
- **Risk Signal明确性**: 检查风险信号的可操作性和明确性
- **Detection Hint完整性**: 验证检测方法的具体性和可执行性
- **Mitigation Direction充分性**: 确保缓解方向和升级条件明确
- **四维度完整性**: Risk Signal + Detection Hint + Mitigation Direction + Escalation

#### 13. 节奏控制验收
- 遵循一次一任务原则

#### 14. 上下文验证
- 基于requirements/design/implementation三阶段文档

#### 15. TDD环境准备GOAL验收（⭐ TDD特有需求）
- goal_breakdown.md中存在环境准备GOAL

#### 16. GOAL测试资产驱动验收（⭐ L1核心特色）
- **GOAL分解基础检查**：
  - GOAL是否基于VS的测试资产分解（非凭空想象）
  - GOAL的source_vs是否指向明确的VS
  - GOAL的related_sc是否对应VS的完整测试场景
- **测试资产清单检查**：
  - GOAL是否包含test_assets_checklist字段
  - 测试资产清单是否完整（scenarios/test_data/mock_config/env_setup）
  - 测试资产清单是否与related_sc的具体内容一致
- **验收标准测试驱动检查**：
  - GOAL验收标准是否基于SC的Given-When-Then定义
  - GOAL成功条件是否包含测试资产就绪检查
  - AI执行边界是否明确基于测试资产的实现路径
- 声明三个维度需求：测试/开发环境分离、端口配置、.gitignore配置
- 验收标准明确（环境可运行、端口无冲突、.gitignore覆盖技术栈）
- 任务序列文档中环境GOAL排首位

---

### 📊 强制验收报告格式

```markdown
## 📋 CONSTRAINT验收报告 - L1 Task Planning - 第{N}轮

**验收标准**: CONSTRAINT_L1_TASK_PLANNING.md
**验收对象**: spec/task_planning/ 目录（X个文档，共Y行）

### 验收项结果

1. [✅/❌] 任务分解合理性验收
   - 检查结果: [通过/失败+具体证据（行号+内容）]

2. [✅/❌] 任务格式合规验收
   - 检查结果: ...

3. [✅/❌] 文档维度完整性验收 ⭐
   - 检查结果: ...
   - 核心维度验收: Breakdown [✅/❌] + Sequence [✅/❌] + Blocker [✅/❌] + AIContext [✅/❌]
   - 失败示例: "4个task_breakdown文件，缺少Sequence/Blocker/AIContext维度"

9. [✅/❌] 上下文验证
   - 检查结果: ...

10. [✅/❌] TDD环境准备GOAL验收 ⭐
   - 检查结果: ...
   - 环境GOAL存在性: [✅/❌] goal_breakdown.md中包含环境准备GOAL
   - 三维度声明: [✅/❌] 测试/开发分离 + 端口配置 + .gitignore
   - 验收标准: [✅/❌] 环境可运行/端口无冲突/.gitignore覆盖技术栈
   - 执行顺序: [✅/❌] 任务序列文档中环境GOAL排首位

11. [✅/❌] GOAL测试资产驱动验收 ⭐
   - 检查结果: ...
   - GOAL分解基础: [✅/❌] 基于VS测试资产 + source_vs指向明确 + related_sc对应完整测试场景
   - 测试资产清单: [✅/❌] test_assets_checklist字段存在 + 四维度完整 + 与related_sc一致
   - 验收标准测试驱动: [✅/❌] 基于SC的Given-When-Then + 测试资产就绪检查 + AI执行边界明确

### 通过率统计
- 通过项: X/11
- **通过率**: Z%

### 失败项详单（如有）
- 验收项N: 失败原因 + 修复建议

### 验收结论
[✅ 通过率≥95%，继续Task-S6-4] / [❌ 通过率<95%，触发Human-in-the-loop]
```

**关键要求**:
- 每个验收项必须有明确判定（✅/❌）+ 具体证据（不能说"看起来没问题"）
- 失败项必须包含：行号、具体内容、修复建议
- **通过率标准**: ≥95%通过，继续Task-S6-4；<95%触发Human-in-the-loop（返回Task-S6-3的Act阶段）

---

## 📋 L1质量门禁标准

### ✅ 门1 · 就绪门 [G1-READY|LM1-SWIFT]
按权威文件 `CONSTRAINT_CORE_CONCEPTS.md` 中 LM1-SWIFT 原则逐条自检：
- [ ] Vertical Slice（端到端切片）优先：以功能切片组织任务规划
- [ ] 单文件聚焦：专注核心任务规划文档生成，保持上下文清晰
- [ ] 快速生成：快速产出任务规划方案，减少规划时间
- [ ] 即时验证：规划后立即自检基础可行性和任务合理性

### 📋 门2 · 质量门 [G2-QUAL]
L1质量检查清单（21项核心检查）：
- [ ] **基础规划完整性**: 包含任务跟踪、策略规划、基础验证方法
- [ ] **快速可行性**: 任务规划基于成熟方案，避免复杂项目管理
- [ ] **边界合规性**: 无代码生产内容，保持任务规划职责边界
- [ ] **节奏控制性**: 遵循一次一任务原则，完成后停止等待
- [ ] **🆕 GOAL清单存在性**: `spec/task_planning/goal_breakdown.md` 存在，位于 task_planning 根目录
- [ ] **🆕 GOAL清单完整性**: `goal_breakdown.md` 中每个 GOAL front matter 包含 `id/sn/source_vs/related_sc`（可选 `related_seq/context_refs`）
- [ ] **🆕 Vertical Slice追溯性**: 每个Goal标注Vertical Slice ID（格式：`source_vs: VS-<SN>-NNN`，例如：VS-MAIN-001）
- [ ] **🆕 Goal格式验收**:
  - [ ] **ID格式**: `GOAL-<SN>-NNN`（例如：GOAL-MAIN-001, GOAL-AUTH-002）
  - [ ] **Front Matter（必填）**: `goal_breakdown.md` 中每个 GOAL 记录 `id`, `sn`, `source_vs`, `related_sc`
  - [ ] **声明式目标**: 描述要达成的结果，避免过程式步骤
- [ ] **🆕 Goal内容结构验收**:
  - [ ] **Goal标题**: 清晰描述功能模块（如"实现用户认证功能模块 [基于TDD粒度决策]"）
  - [ ] **声明式目标字段**: 明确描述要实现的完整功能
  - [ ] **验收标准字段**: 列出3-5条具体可验证的标准
  - [ ] **成功条件字段**: 包含功能完整性验证、质量标准达成、AI执行边界3部分
    - 功能完整性验证: 核心流程、业务逻辑、错误处理3个子项
    - 质量标准达成: 单元测试、集成测试、端到端测试引用SC ID
    - AI执行边界: 自主选择实现路径的说明
  - [ ] **下一目标依赖字段**: 说明当前目标为后续目标提供的基础
- [ ] **🆕 Goal追溯性验收**:
  - [ ] **source_vs字段**: 格式正确（VS-<SN>-NNN），指向有效VS ID
  - [ ] **related_sc字段**: 数组格式，包含至少1个SC ID（格式：[SC-<SN>-NNN, ...]）
  - [ ] **VS追溯可达性**: source_vs指向的VS在design/vertical_slices.md中存在
  - [ ] **SC追溯可达性**: related_sc中的SC在implementation/bdd_scenarios.md中存在
- [ ] **🆕 Blocker约束性验收**（存在 `BLK-<SN>-NNN` 时必须执行）:
  - [ ] **Front Matter完整**: `id` / `sn` / `source_vs` 至少三项齐备；如声明 `blocking_goal` 或 `related_sc`，引用必须有效
  - [ ] **Risk Signal明确**: 文档描述的触发信号可操作、不可使用“待确认”类措辞
  - [ ] **Detection Hint明确**: 提供可供AI尝试的检测方法或检查点（声明式描述即可）
  - [ ] **Mitigation Direction & Escalation**: 给出至少一条缓解方向与升级条件，确保哼哈二将（Producer/Consumer）角色分工清晰
  - [ ] **Unblock同步**: 明确解除阻塞后需要同步或更新的上下文，避免空洞记录
- [ ] **🆕 Goal完整示例验收**:
  - [ ] 包含完整Front Matter（id + sn + source_vs + related_sc，遵循 CTX 命名规范）
  - [ ] Goal标题包含功能模块和TDD粒度决策标注
  - [ ] 声明式目标清晰完整（1-2句话）
  - [ ] 验收标准列表完整（3-5条）
  - [ ] 成功条件包含3部分（功能/质量/边界）
  - [ ] 下一目标依赖明确（1-2条）
- [ ] **🆕 价值链路闭环性**: GOAL→SC→FP→VS追溯链路完整
- [ ] **🆕 完整链路覆盖性**: 完整价值链路（前端/数据/后端/反馈）有对应Goal
- [ ] **⭐ AI上下文规格必需性**: task_planning/ 必须包含 AI上下文规格文档，并在Front Matter中声明 id/sn/source_vs
- [ ] **⭐ AI上下文内容完整性**:
  - [ ] **文档追溯路径**: 包含前3阶段文档的相对路径（requirements/, design/, implementation/）
  - [ ] **Front Matter**: 顶部包含 \`id\` / \`sn\` / \`source_vs\`（CTX-<SN>-NNN）
  - [ ] **BDD Scenarios引用**: 明确指向 implementation/bdd_scenarios.md 的路径和场景ID（SC-XXX-NNN）
  - [ ] **项目根目录定义**: 包含 SPEC_PRJ_ROOT_DIR 定义
  - [ ] **AI执行流程**: 包含 5步执行指南（Read VS → Read FP → Read SC → Execute TDD → Verify）
  - [ ] **技术栈上下文**: 包含前端/后端/数据库/测试框架信息
- [ ] **⭐ AI上下文规格格式验收**:
  - [ ] **文档标题**: 明确项目名称（如"AI Context Specification - TaskMaster"）
  - [ ] **文档说明**: 包含用途说明（"提供AI Coding Agent执行TDD代码搭建所需的完整上下文信息"）
  - [ ] **需求文档章节**: 包含路径、关键ID、作用说明
    - 路径示例: `../requirements/user_stories.md`
    - 关键ID示例: US-MAIN-001
    - 作用说明: 理解业务需求和用户角色视角
  - [ ] **设计文档章节**: 包含VS和FP两个路径
    - VS路径: `../design/vertical_slices.md` + VS-XXX-NNN ID + 端到端价值链路说明
    - FP路径: `../design/function_points.md` + FP-XXX-NNN ID + 技术架构说明
  - [ ] **测试场景章节**: 标注为"最有用的信息"
    - 路径: `../implementation/bdd_scenarios.md`
    - 包含3个以上场景ID（正常流程 + 异常流程）
    - 强调BDD格式可直接转换为测试代码
  - [ ] **项目根目录章节**: 包含SPEC_PRJ_ROOT_DIR完整路径
  - [ ] **AI执行流程章节**: 5步指南详细说明
    - Step 1: Read VS (design/vertical_slices.md) - 理解端到端价值链路
    - Step 2: Read FP (design/function_points.md) - 获取技术架构
    - Step 3: Read SC (implementation/bdd_scenarios.md) - 转换为测试代码
    - Step 4: Execute TDD - Red-Green-Refactor循环
    - Step 5: Verify - 验证验收标准
  - [ ] **技术栈上下文章节**: 分前端/后端/数据库/代码规范4部分
  - [ ] **AI执行边界章节**: 分"自主选择权限"和"必须遵守约束"两部分
  - [ ] **阻塞点预判章节**: 包含至少2个潜在阻塞及降级方案
  - [ ] **关键提示**: 强调BDD Scenarios是最有用信息
- [ ] **🎯 TDD环境准备GOAL验收**:
  - [ ] goal_breakdown.md中存在环境准备GOAL（包含Front Matter: id/sn/source_vs）
  - [ ] 声明三个维度需求：测试/开发环境分离、端口配置、.gitignore配置
  - [ ] 验收标准明确（环境可运行、端口无冲突、.gitignore覆盖技术栈）
  - [ ] 任务序列文档中环境GOAL排首位，确保优先执行
- [ ] **📋 LLM质量控制执行验证**: 按 CONSTRAINT_CORE_CONCEPTS.md 中"LLM质量控制通用原则"逐条验收
- [ ] **批准确认性**: 收到用户明确正面回应
- [ ] **受众适配性**: Goal用业务语言，执行细节可用技术语言
- [ ] **技术术语密度**: 技术术语密度 ≤ 50%
- [ ] **目标业务化**: Goal标题包含业务价值说明
- [ ] **验收标准分离**: 分为"业务视角"和"技术验证"
- [ ] **任务序列业务化**: 任务序列标题业务友好，包含业务目标/价值

---

## 📁 文件组织验收标准

### 目录结构检查（spec/task_planning/）
- **位置验收**: 默认`spec/task_planning/`或等效目录
- **核心类目**: 任务跟踪如`[任务跟踪文件名].md`，策略规划如`[策略规划文件名].md`
- **必要分类**: 核心任务如`[核心任务文件名].md`
- **交付物**: tdd_task_tracking.md在根目录，tdd_strategy_order.md在task_planning目录
- **命名规范**: 文件名采用lower_snake_case + `.md`
- **内容边界**: 严禁出现代码生产/具体TDD执行等非规划产物

---

## 🎯 边界约束原则

### ❌ 严禁行为
- **无上下文规划**: 绝不允许在没有前三阶段文档的情况下开始任务规划
- **自动推进**: 完成当前任务后自动开始下一个任务
- **代码生产**: 不进行任何实际代码生产，专注任务规划

### ✅ 专注职责
- **基础任务规划**: 基于前三阶段的快速任务策略规划
- **简单项目管理**: 粗粒度任务分解，基础进度跟踪
- **TDD策略准备**: 为红绿重构循环实施提供基础指导

---

## 🔧 快速任务规划指导

### L1任务粒度原则
- **粗粒度任务**: 1-3天完成，避免过度细分
- **关键功能点**: 专注核心里程碑，简单验收标准
- **基础依赖**: 主要依赖关系记录，避免复杂分析

### 快速项目管理要求
- **简化跟踪**: 基础进度跟踪，日/周粒度状态更新
- **高容错**: 允许任务调整和计划变更，快速执行优先
- **基础文档**: 简化任务清单，核心依赖关系记录

---

## 🔒 质量门禁原则

### 📋 审批流程要求
```
任务规划完成后的强制流程：
1. 创建task_planning/目录结构，包含精简的任务规划体系
2. 基于前三阶段完成基础任务分解和策略规划
3. 创建强制交付物：tdd_task_tracking.md(根目录) + tdd_strategy_order.md(task_planning目录)
4. 遵循一次一任务原则，完成后停止等待用户指示
5. 如用户要求修改，必须调整后重新规划
```

### 🔄 反馈-修订循环机制
- **快速迭代**: 基于用户反馈快速调整任务规划
- **持续修订**: 必须根据用户反馈持续完善规划文档
- **节奏控制**: 严格遵循一次一任务，不自动推进

---

## 📤 输出验收标准

### L1交付物验收
- **结构验收**: 精简`task_planning/`目录结构，覆盖任务分解、任务序列、阻塞预判、AI上下文规格四个核心维度
- **强制交付物**: 
  - tdd_task_tracking.md（根目录）：项目级TDD实施总进度跟踪，供全局查看
  - tdd_strategy_order.md（task_planning目录）：详细策略顺序规划，供执行参考
- **内容验收**: 200-300行范围，聚焦核心任务规划
- **对接验收**: 确保输出能成为TDD实施准备的基础输入
- **质量验收**: 快速可用标准，高容错，允许基础版本通过

### 节奏控制验收
必须遵循一次一任务原则，完成当前任务后停止等待用户指示

---

## 🚨 L1常见违规行为

### ❌ 边界违规
- 在规划中生产实际代码或TDD执行
- 自动推进到下一个任务而不停止
- 跳过前三阶段文档直接开始规划

### ❌ 格式违规
- 缺少强制交付物(tdd_task_tracking.md和tdd_strategy_order.md)
- 任务颗粒度过细，不符合L1粗粒度特征
- 项目管理过于复杂，不符合L1简化特征

### ❌ 质量违规
- 追求过度完善而非快速可用
- 任务规划过于复杂，不符合L1快速特征
- 破坏一次一任务的节奏控制

**修正策略**: 快速回到L1核心原则，重新执行快速模式，确保高容错和快速可用。

---

## 🤖 AI协作策略指导

---

#### 📁 文件操作约束
- **文件操作**: AI必须创建对应的`task_planning/`目录结构（实战模式优先）
- **初始版本生成**：基于前三阶段文档生成任务规划方案初始版本，快速任务分解
- **强制交付物**: 必须创建tdd_task_tracking.md(根目录)和tdd_strategy_order.md(task_planning目录)
- **严禁代码生产**: 本阶段专注任务规划，严禁进行任何代码开发

#### 🎯 策略节奏精确控制
- **快速规划原则**：基于前三阶段快速生成核心任务策略，避免过度规划
- **任务分解策略**：将功能实施转换为可执行任务序列，保持粗粒度
- **节奏控制强制**：必须遵循一次一任务，完成后停止等待用户指示

#### 💬 交互标准化协议
- **节奏控制话术**：完成任务后必须停止，等待用户指示下一步
- **上下文确认**：开始前确认已读requirements/design/implementation三文档
- **修改请求处理**：如用户请求更改，必须对规划文档进行修改

---

## 📄 L1格式模板详解

### 🔥 L1-STREAMLINED格式模板
```markdown
# TDD任务规划（L1精简版）

## TDD策略概述
[核心TDD策略规划概述，1-2段话]

## 任务跟踪矩阵
| 任务类别 | 核心任务 | 状态 | TDD策略要点 |
|----------|----------|------|-------------|
| [功能模块] | [关键任务] | 待开始 | [基础TDD策略] |

## 策略规划
1. [高优先级任务] - [基础依赖分析]
2. [核心集成任务] - [关键策略要点]

## 强制交付物说明
- tdd_task_tracking.md: 项目根目录TDD实施进度总跟踪
- tdd_strategy_order.md: task_planning目录TDD策略顺序规划
```

### 📊 精简结构要求
- **策略部分**：1-2段话说明核心TDD策略任务规划目标
- **跟踪部分**：基础任务跟踪矩阵，粗粒度任务组织
- **规划部分**：核心优先级排序，基础依赖分析
- **交付物**：强制创建两个关键交付物，确保贯通流程闭环

---

*"L1约束以快速任务规划为核心，通过精简检查和高容错机制，确保快速为TDD实施准备提供基础策略指导。"*
