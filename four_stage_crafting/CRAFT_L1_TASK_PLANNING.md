# CRAFT_L1_TASK_PLANNING 任务精控指导文档

> 🎯 **系统执行指令**: 声明式目标制定场景→TASK_PLANNING阶段关联复杂度声明式目标激发，独立文档导向
> 📊 **核心聚焦**: 声明式目标制定关联复杂度控制 - 独立文档关系→系统理解目标导向执行→实现质量提升
> 📁 **级别特征**: L1-STREAMLINED (4个核心文件，平面结构，独立文档，快速开发偏好，线性流程，AI快速理解)
> 🤖 **AI执行视角**: AI需要快速理解4个独立模块、保持简单线性流程、聚焦核心目标快速执行
> 🔧 **协作模式**: C1-CONFIRM模式("你看着办") - 系统主导声明式目标制定→用户简单确认→快速执行
> ⚡ **体系定位**: 创意激发者，支撑脚手架生产+后期推敲，验收标准由four_stage_constraints定义
> 🏗️ **文档架构**: MD+XML混合设计，核心指导内容全部封装在XML标记内，实现系统精确提取和Level间无缝切换

> 🔗 **命名规范权威引用**:
> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L1 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` (必填 artifacts, 灵活模式, 验收标准)
>
> 🔗 **AICodingAgent规范权威引用**:
> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L1宪章**: `../agentic_spec/SPEC_ACA_L1_CHARTER.md` - L1质量标准 (4-6检查点, 通过率≥95%, 单层追溯)

## 🎯 XML标记体系说明

### 第一级标记 (craft-task-planning-req[1-4]-l1)
**目的**: 包含L1级别TASK_PLANNING阶段的**完整指导内容**，作为系统提取和Level切换的**整体单位**

### 第二级标记 (完整说明)

#### 6个标准维度子标签 (所有阶段通用 - 要求1):
1. `<document-organization>` - **文档组织架构策略**: 该级别需要多少文档、如何配置文档结构、基本协作约束、目录结构展示
2. `<directory-hierarchy>` - **目录层级组织**: 文件夹结构、层级深度控制、文件布局规范、导航方式设计  
3. `<categorization-granularity>` - **分类粒度策略**: 如何分类任务规划内容、分类细度控制、组织逻辑设计
4. `<interconnection-complexity>` - **关联复杂度管理**: 文档间引用关系、依赖复杂度、交叉引用策略
5. `<content-depth>` - **内容深度策略**: 每个文档写多少内容、详细程度把握、充实度标准定义
6. `<formalization-level>` - **形式化程度** [TASK_PLANNING主攻]: 模板规范度、结构严格性、系统执行技巧、认知要点集成

#### TASK_PLANNING阶段专项子标签:
**要求2_策略规划** (3个子标签):
- `<planning-methodology>` - **规划方法论和框架**: 规划方法、框架选择、管理工具
- `<execution-orchestration>` - **执行编排和调度策略**: 执行顺序、并行策略、调度优化
- `<task-sequence-management>` - **任务序列管理和控制**: 任务顺序、依赖关系、执行控制

**要求3_验证跟踪** (3个子标签):
- `<progress-tracking>` - **进度跟踪机制和工具**: 进度监控、跟踪工具、状态管理
- `<prerequisite-validation>` - **前置条件验证和确认**: 环境就绪性检查、依赖完整性验证、配置正确性确认
- `<completion-criteria>` - **完成标准和检查**: 完成定义、检查标准、验收条件

**要求4_质量标准** (3个子标签):
- `<delivery-gates>` - **交付门禁和流程**: 交付门禁、质量检查、发布流程
- `<context-management>` - **上下文管理和传递**: 上下文保持、信息传递、状态同步
- `<stage-verbatim-directive>` - **逐字传递指令**: 对下一阶段的逐字传递与接口要求

## 术语口径（中文 → English）
- Goal（目标） - 声明式执行目标，描述要达成的结果而非执行步骤
- Task Sequence（任务序列） - 任务执行的顺序和依赖关系
- Blocker（阻塞点） - 可能阻碍任务执行的潜在问题
- AI Context（AI上下文） - AI执行任务所需的完整上下文信息
- Acceptance Criteria（验收标准） - 目标完成的判定标准
- Prerequisite（前置条件） - 任务执行前必须满足的条件
- Delivery Gate（交付门禁） - 质量检查和发布流程的控制点

### Task Sequence / Blocker 补充指南（推荐）

- **Task Sequence (`SEQ-<SN>-NNN`)**  
  - **何时创建**: L1 仍以“单任务拉通”取胜，但当同一 VS 需要 4 个以上任务才能交付，或存在严格的串行依赖时，可以额外产出 Task Sequence 文档，把关键任务和依赖一口气列清。  
  - **Front Matter 最小字段**（参见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` Section 3.2）:
    ```yaml
    ---
    id: SEQ-AUTH-050
    sn: AUTH
    related_sc: [SC-AUTH-001]   # 可选，指向驱动该序列的关键场景
    ---
    ```
  - **正文建议**: 用列表或表格说明执行顺序、责任角色（若已知）与里程碑，避免扩展为详细甘特。遇到并行窗口时可插入一句“Task B、Task C 可并行执行”，保持声明式描述。

- **Blocker (`BLK-<SN>-NNN`)**  
  - **何时创建**: 只要发现“若未处理将阻断 AI 后续执行”的风险，就立即记录 Blocker（常见来源：外部依赖、关键凭证、合规审批等）。  
  - **Front Matter 建议**:
    ```yaml
    ---
    id: BLK-AUTH-060
    sn: AUTH
    source_vs: VS-AUTH-001      # 对齐价值链
    related_sc: [SC-AUTH-002]   # 可选，受影响的场景
    blocking_goal: GOAL-AUTH-002  # 可选，被阻塞的目标
    ---
    ```
  - **正文需覆盖四个判断点**（保持声明式，避免过程细节）:
    1. **Risk Signal** — 风险触发时可观测到的客观现象或状态。
    2. **Detection Hint** — AI 可在执行阶段尝试的检测手段（命令或检查点描述即可）。
    3. **Mitigation Direction** — 至少给出一条可行的临时缓解方向（如切换到 mock、延后执行顺序）。
    4. **Escalation/Unblock** — 说明何时需要人工介入，以及解除后需要同步或更新的上下文信息。
  - **执行提醒**: Blocker 文档的目标是让 AI 能快速判断、尝试缓解并在必要时升级处理，因此禁止模板化的“待确认”语句。生成后仍需满足 `CONSTRAINT_L1_TASK_PLANNING.md` 的风险验收。

> 以上两个 artifacts 均属“推荐”范畴：当项目规模很小、任务清单简单时可以不创建；一旦生成，需在任务规划验收环节（见 `CONSTRAINT_L1_TASK_PLANNING.md`）中提供对应证据。

## 🤖 AI执行约束

> 📋 **快速理解原则**: AI需要快速理解4个独立模块的声明式目标，立即开始执行
> 🚫 **简化约束**: 避免过度复杂的嵌套结构，保持线性流程，确保AI上下文清晰
> 💼 **目标导向**: 优先聚焦核心目标和验收标准，确保独立文档关系服务快速执行
> 🎯 **简洁表达**: 使用AI能理解的简洁任务术语，确保独立文档关系清晰简单
> 📐 **轻量体系**: 建立轻量化执行体系，采用简化表达确保AI快速理解和执行

## ⚠️ 重要原则澄清

> 🎯 **维度本质 > 表面形式**: L1/L2/L3的核心是约束复杂度的不同维度，不是具体的文件组织形式
> 📁 **文件/目录是表现**: 文件数量、目录结构只是维度的外在表现，重点是背后的指导价值和复杂度控制
> 🚫 **避免表面约束**: 不要被"平面结构"、"基础任务"等表面描述约束，关注L1快速简洁的维度本质
> ✨ **指导性优先**: CRAFT是创意激发者，松耦合高内聚的指导性存在，而非行为约束者

## 🎯 统一命名权威标准
**⭐ 以下为权威引用基准，确保系统一致性**

<craft-task-planning-req1-l1>
🚫 **严格禁止**：直接编写具体执行步骤、提供过程式任务分解、详细实施指令
✅ **应该产出**：声明式执行目标（如"实现用户认证功能"）、验收标准定义、AI执行上下文规格
⚠️ **脚手架约束**：提供目标导向指令和上下文规格，告诉AI要达成什么目标，但让AI自主选择实现路径

**任务规划_要求1_文档体系** L1任务精控：

<document-organization>
> **⭐ 权威来源**:
> - Artifact定义、PREFIX清单及标准托管文件: `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` Section 1.6
> - L1级别推荐托管映射: `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` Section 3.2
>
> 以下为L1-TASK_PLANNING阶段的标准维度定义和文档组织指引

**📋 受众定位约束**（TASK_PLANNING阶段质量标准）：
- **主要读者**: 开发者/AI Agent（技术执行者）
- **语言要求**: 声明式目标业务化，执行细节可技术化
- **可读性标准**: "做什么"用业务语言（PM能看懂目标），"怎么做"用技术语言（开发者能执行）

**目标层面**（业务语言）：
- ✅ Goal标题使用业务术语（如："实现用户登录功能"而非"实现AuthService"）
- ✅ 验收标准描述业务价值
- ✅ Goal描述是声明式的（"做什么"而非"怎么做"） ← 允许声明式表达
- ✅ 成功条件关联用户体验

**执行层面**（技术语言）：
- ✅ 任务序列可用技术术语
- ✅ 阻塞预判可用技术细节
- ✅ AI执行上下文可技术化
- ❌ 禁止过程式代码（函数调用、方法执行） ← ⚠️ 硬性约束
- ✅ 允许声明式代码（配置、数据结构、接口声明）

**⚖️ 平衡原则**：
- "做什么"用业务语言（PM能看懂目标）
- "怎么做"用技术语言（开发者能执行）
- **技术术语密度 ≤ 50%**（TASK_PLANNING阶段约束）

🎯 **核心维度特征**（必须遵循）：
L1必须体现"快速简洁，独立关联"的本质特征
- **复杂度控制**：最小化依赖，独立文档设计，简单声明式目标制定组织
- **协作特征**：支持C1-CONFIRM模式("你看着办")，快速声明式目标制定优先
- **质量标准**：声明式目标制定优先，将TDD/BDD战略目标化，避免过度项目管理

📋 **强制实施方案**：
**⭐ L1-STREAMLINED 任务规划文档组织架构**：

**L1-STREAMLINED 声明式目标制定组织架构**：
```
task_planning/                     # 声明式目标制定根目录（独立文档少量关联）
├── [goal_breakdown.md]            # GOAL front matter 聚合，唯一真相源
├── [task_breakdown.md]            # 目标分解：围绕 GOAL 的声明式说明与验收
├── [task_sequence.md]             # 任务序列：任务执行顺序和依赖关系
├── [blocker_anticipation.md]      # 阻塞预判：潜在阻塞识别和清障策略
└── [ai_context_specification.md]  # AI上下文规格：AI执行所需的完整上下文信息
```

**文档组织要求**：4个核心维度必须覆盖（目标分解 + 任务序列 + 阻塞预判 + AI上下文），通常对应4个文档
**策略定位**：每个独立文档对应核心声明式目标制定关注点
**任务精控指导**：5个核心文件结构化组织，平面结构便于快速导航，包含 [goal_breakdown.md]、[task_breakdown.md]、[task_sequence.md]、[blocker_anticipation.md]、[ai_context_specification.md]
**开发导向**：`goal_breakdown.md` 聚合 GOAL front matter，其余文档基于 GOAL 进行声明式扩展：目标分解([primary_focus]) + AI上下文规格([primary_focus]) + 任务序列([supporting_focus]) + 阻塞预判([supporting_focus])，重点是“将 IMPLEMENTATION 的 TDD 粒度决策收束为 GOAL，再以 GOAL 引导执行”。
**质量标准**：文档组织最优化，声明式目标制定组织最清晰，避免过度复杂结构
**灵活性说明**：可调整文档内容详细程度，但需保持4个核心文档的声明式目标制定特征
**多角色协作约束**：L1-STREAMLINED任务精控策略重点确保AI能够快速理解声明式目标，立即开始自主执行，避免复杂过程式指导和严格格式，采用自由Markdown，便于快速编辑，优先体现声明式目标和验收标准，AI上下文规格服务于AI自主执行适配，使用AI和开发者都能理解的目标导向表达，确保独立文档关联复杂度控制简单有效

**📋 文档生产次序**：[goal_breakdown.md]（集中维护 GOAL front matter） → [task_breakdown.md]（围绕 GOAL 扩展验收/成功条件） → [task_sequence.md]（引用 GOAL ID 排序） → [blocker_anticipation.md] → [ai_context_specification.md]
**次序原因**：先统一 GOAL 追溯链，再在各文档中引用同一 GOAL；task_sequence/ai_context 等依赖 GOAL ID、source_vs、related_sc 的追溯信息。

📁 **核心文档组织维度说明** (L1-STREAMLINED特征): 以下帮助理解占位符背后的文件组织思考维度，具体文件组织可灵活适配项目需要

**文档组织原则**:
- **维度优先**: 必需的是覆盖核心维度，文件组织形式灵活
- **按阶段分目录**: requirements/design/implementation/task_planning
- **按粒度分层**: 核心文档放根目录，细节文档可放子目录或拆分文件
- **命名规范**: snake_case，语义化文件名
- **关联管理**: 使用相对路径引用，保持文档间关联清晰
- **灵活适配**: 内容少时合并文档，内容多时拆分文件（如`xxx_part1.md`），复杂时建子目录

**维度0: GOAL 清单维度 (必需)**
- **对应占位符**: `[goal_breakdown.md]`
- **参考示例**: `goal_breakdown.md`
- **维度职责**: 统一维护 GOAL front matter（`id`, `sn`, `source_vs`, `related_sc`, `related_seq`, 可选 `context_refs`）
- **文档组织方式**:
  - 单文件形式: `goal_breakdown.md`（推荐）
  - 分组形式: `goal_breakdown/core.md`, `goal_breakdown/extension.md`（目标过多时）
- **内容要求**: 仅保留 front matter 与简要说明，不写执行细节
- **L1特征**: 所有 GOAL 必须集中在此文件，其它文档只引用 GOAL ID

**维度1: 任务分解维度 (必需)**
- **对应占位符**: `[task_breakdown.md]`
- **参考示例**: `task_breakdown.md` 或 `task_goals.md`
- **维度职责**: 围绕 `goal_breakdown.md` 中的 GOAL 提供声明式解读、验收标准与成功条件
- **文档组织方式**:
  - 单文件形式: `task_breakdown.md`
  - 多文件形式: `tasks_part1.md`, `tasks_part2.md` (任务多时)
  - 目录结构形式: `tasks/feature_goals.md`, `tasks/infra_goals.md`
  - 合并文档形式: 所有目标合并在一个文件中
- **内容要求**: 声明式目标、验收标准、成功条件、依赖关系
- **L1特征**: 优先单文件，快速目标定义，简洁实用

**维度2: 任务序列维度 (必需)**
- **对应占位符**: `[task_sequence.md]`
- **参考示例**: `task_sequence.md` 或 `execution_order.md`
- **维度职责**: 记录任务执行顺序和依赖关系
- **文档组织方式**:
  - 单文件形式: `task_sequence.md`
  - 合并文档形式: 作为任务分解文档的"执行顺序"章节
  - 分组文件形式: `sequence_phase1.md`, `sequence_phase2.md`
- **内容要求**: 执行顺序定义、任务依赖、前置条件、下一步依赖
- **L1特征**: 优先单文件，线性顺序表达，便于快速理解

**维度3: 阻塞预判维度 (必需)**
- **对应占位符**: `[blocker_anticipation.md]`
- **参考示例**: `blocker_anticipation.md` 或 `blockers.md`
- **维度职责**: 记录潜在阻塞识别和清障策略
- **文档组织方式**:
  - 单文件形式: `blocker_anticipation.md`
  - 合并文档形式: 作为任务分解文档的"阻塞预判"章节
  - 分类文件形式: 按阻塞类型分文件（依赖、环境、知识）
- **内容要求**: 阻塞识别、降级方案、清障行动、验证条件
- **L1特征**: 优先单文件，简洁明确的阻塞清除方案

**维度4: AI上下文规格维度 (必需) ⭐ 核心价值**
- **对应占位符**: `[ai_context_specification.md]`
- **参考示例**: `ai_context_specification.md` 或 `ai_context.md`
- **维度职责**: 记录AI Coding Agent执行TDD所需的**完整上下文信息**，包括文档追溯路径、BDD Scenarios引用、项目根目录定义
- **文档组织方式**:
  - 单文件形式: `ai_context_specification.md`（强烈推荐）
  - 合并文档形式: 作为任务分解文档的"AI上下文"章节
  - 分阶段形式: 按开发阶段分文件
- **内容要求**（⭐ 关键信息）:
  - **文档追溯路径**: 前3阶段文档的相对路径（requirements/, design/, implementation/）
  - **项目结构文档**: implementation/[project_structure_file] 的路径和目录结构定义（源代码/测试代码位置）
  - **BDD Scenarios引用**: 明确指向 implementation/bdd_scenarios.md 的路径和场景ID（SC-XXX-NNN）
  - **项目根目录**: SPEC_PRJ_ROOT_DIR定义（AI应该在哪里执行TDD代码搭建）
  - **技术栈上下文**: 前端/后端/数据库/测试框架
  - **AI执行流程**: 5步执行指南（Read VS → Read FP → Read SC → Execute TDD → Verify）
  - **执行边界**: AI自主选择实现路径的边界和约束
- **⭐ BDD Scenarios的核心价值**:
  - BDD格式（Given-When-Then）是AI Coding Agent最有用的信息
  - 可直接转换为测试代码（Jest/Mocha/Pytest等）
  - 提供完整的用户行为流程和验收标准
- **L1特征**: 必需文档，优先单文件，包含完整的文档追溯链和AI执行上下文
</document-organization>

<directory-hierarchy>**策略定位**：平面目录支持独立文档的简单声明式目标制定组织
**任务精控指导**：task_planning/直接存放核心文件，无子目录，平面结构或单层目录支持独立文档快速组织和导航
**质量标准**：目录结构简洁清晰，便于快速定位和理解，支持独立文档的基础分类

**与主攻维度的协同点**：平面目录支持独立文档的简单声明式目标制定组织，独立文档支持简单目标分组关联

**L1-STREAMLINED平面结构控制**：
- 是否采用L1标准的4文档平面结构？
- 是否体现独立文档关系特征？
- 是否保持平面结构，便于AI目标达成？</directory-hierarchy>

<categorization-granularity>**任务规划架构核心定位**：独立文档关系 - 用独立文档关系的自由格式组织实现声明式目标制定→AI与用户快速确认目标方案→实现质量提升（核心工作做快速），C1-CONFIRM模式下AI快速决策基础目标制定方案，用户信任确认即可，"你看着办" - 用户信任AI的目标制定决策，重点在快速目标启动而非完美格式化

**IMPLEMENTATION承接策略**：基于IMPLEMENTATION阶段的TDD粒度决策和项目规划，保持实施战略→声明式目标的直接映射；简单引用格式："基于implementation/[tdd_strategy_file]→task_planning/[task_breakdown_file]直接转化"；快速验证目标覆盖所有TDD战略，确保声明式目标制定完整性

**L1分类粒度策略**：粗分类声明式目标文档间保持独立，少量交叉引用，[task_breakdown_file]可引用[task_sequence_file]，[ai_context_specification_file]引用[task_breakdown_file]

**声明式目标制定强制要求**：

1. **[task_breakdown.md]**: 目标分解声明式定义([primary_focus]) - 🎯 核心文档：按功能模块分组的声明式目标，每组清晰的验收标准，**AI上下文适配**（每个目标都有明确的成功条件），告诉AI应该实现什么目标而非如何实现；引用规范："基于 [task_sequence.md] 任务序列S01实现目标G01完成条件"
   
   **🎯 声明式目标映射机制**：将IMPLEMENTATION阶段的TDD粒度决策转化为目标导向的验收标准
   - **原始问题**: implementation/包含TDD战略和项目规划，需要转化为AI可理解的声明式目标
   - **目标导向解决方案**: 按功能相关性和验收条件分组，每组明确的成功标准，确保AI能够理解预期结果
   - **目标制定原则**: 核心功能目标→扩展功能目标→集成验证目标的渐进明确度
   
   - 示例格式：
     ```markdown
     ## Goal_01_CoreModels (用户、产品核心功能实现目标)
     **声明式目标**: 实现完整的用户和产品核心功能模块
     **验收标准**:
     - 用户注册功能正常，能创建有效用户记录并返回成功状态
     - 用户登录功能正常，能验证用户身份并返回用户信息
     - 产品创建功能正常，能保存产品数据并建立用户关联
     **成功条件**: 所有核心CRUD操作通过验证，数据模型关系正确
     **AI执行边界**: 基于现有TDD策略自主选择实现路径，重点关注功能完整性
     **下一目标依赖**: 为Goal_02_AdvancedFeatures提供功能基础
     ```

2. **[task_sequence.md]**: 任务序列编排声明式定义([primary_focus]) - 🎯 核心文档：任务执行顺序和依赖关系，**任务到序列的编排和依赖**，告诉AI按什么顺序执行什么任务，每个任务的前置条件；引用规范："基于 [task_breakdown.md] Goal_01→Goal_02→Goal_03任务序列"

   **🔄 IMPLEMENTATION→TASK_PLANNING声明式转换机制**：
   - **转换输入**: implementation/[tdd_strategy_file]的TDD粒度决策 + implementation/[development_approach_file]的项目规划
   - **转换输出**: AI可理解的任务执行序列，每个任务节点包含明确的执行顺序和依赖关系
   - **转换原则**: 每个TDD战略转换为具体的任务序列，包含前置条件和执行顺序要求

   - 示例格式：
     ```markdown
     ## 任务序列S01: 开发环境准备 → 测试基础搭建 → 功能开发 [执行顺序: 第1阶段]
     
     **业务目标**: 为用户登录功能开发做好准备
     **业务价值**: 确保开发过程质量可控，功能可靠
     
     **执行顺序**:
       1. 环境搭建（检查开发环境就绪状态）
       2. 测试搭建（搭建质量验证基础）
       3. 功能开发（实现核心业务功能）

     **依赖关系**:
       - 环境搭建完成 → 才能进行测试搭建
       - 测试搭建完成 → 才能开始功能开发
       - S01完成 → 才能进入S02（集成验证）

     **前置条件**:
       - 开发环境已配置
       - 项目文件结构已建立
       - 版本控制已就绪

     **下一任务序列**: S02_集成验证 → S03_E2E测试
     ```

3. **[blocker_anticipation.md]**: 阻塞预判声明式定义([supporting_focus]) - **潜在阻塞识别和清障策略**，预判AI实施过程中的潜在阻塞，制定绕过和解除方案，确保任务执行的流畅性；引用规范："基于 [task_breakdown.md] Goal_01阻塞扫描和 [task_sequence.md] S01执行前清障"

   **🎯 AI实施阻塞预判控制**：
   - **依赖阻塞**: 识别版本冲突、API不可用等依赖问题，准备Mock/降级方案
   - **执行阻塞**: 基于任务依赖关系预判执行阻塞点，提前准备workaround策略
   - **环境阻塞**: 识别环境配置、权限、网络等问题，制定清障行动

   - 示例格式：
     ```markdown
     ## 阻塞B01: 核心API依赖不可用
     **阻塞描述**: GraphQL API可能版本冲突或服务不稳定
     **阻塞优先级**: 高优先级（关键路径）
     **降级方案**: 使用Mock Schema先搭建框架，待API稳定后替换
     **清障行动**: 创建mock-schema.graphql，配置Mock Server
     **验证条件**: Mock Schema可正常返回测试数据，TDD循环可启动
     ``` 
</categorization-granularity>

<interconnection-complexity>**策略定位**：采用独立文档为主的清晰关联体系，每个文档最多2-3个引用点，专注声明式目标制定的快速价值交付

**具体操作指导**：
- **[goal_breakdown.md]引用规范**: "集中定义 GOAL-<SN>-NNN front matter（source_vs、related_sc、related_seq）"
- **[task_breakdown.md]引用规范**: "基于 [goal_breakdown.md] GOAL-AUTH-001 → 定义验收/成功条件"
- **[task_sequence.md]引用规范**: "按照 [goal_breakdown.md] GOAL 列表 → S01/S02 执行序列"  
- **[blocker_anticipation.md]引用规范**: "基于 [goal_breakdown.md] GOAL-AUTH-001 阻塞扫描"
- **引用密度控制**: 每个文档≤2个引用点，专注声明式目标制定指导
- **AI友好性**: 每个引用都明确告诉AI要达成什么目标

**AI目标检查点**：
1. 目标分解是否具体明确，能指导AI理解预期结果？
2. 任务序列是否清晰，AI能理解执行依赖和顺序？
3. 阻塞预判是否简洁明确，AI能应用清障方案？

**质量标准**：独立性检验通过，声明式目标指导性明确，支持C1-CONFIRM模式快速理解和执行</interconnection-complexity>

<content-depth>**策略定位**：每个独立文档保持核心声明式目标制定内容，避免冗余引用
**任务精控指导**：必须保持轻量级内容，概要了解，每个文档必须控制篇幅，核心目标制定信息必须突出，严格关注声明式目标制定充实度的完整记录。协同强制要求：每个独立文档必须保持核心目标制定内容，严禁冗余引用
**质量标准**：声明式目标制定的明确性比文档数量更重要，目标导向的执行效率比结构完美更关键</content-depth>

<formalization-level>**主攻维度核心定位**：形式化程度（Formalization Level）- 基础Markdown结构
**任务精控目标**：用简洁Markdown组织声明式目标制定，保持2-3层基础结构（目标→验收标准→成功条件）
**形式化平衡**：结构清晰但不过度复杂，保持AI可理解的基础组织形式（避免超过3层嵌套）
**协作特色**："你看着办" - 用户信任AI的格式决策，重点在快速目标制定启动而非完美格式化

**⭐ Artifact ID分配**: 保持现有artifact ID不变(确保引用完整性)，仅对新增artifact扫描宿主文件同PREFIX+SN，取max序号+1分配新ID

**L1形式化程度策略**：必须采用基础Markdown自由格式组织目标制定，严禁复杂目标组织模板和过度结构化，必须专注目标制定内容的快速表达和执行

**L1特异性检查**：
- 是否避免了复杂的目标组织模板结构和严格格式强制要求？
- 是否用基础Markdown覆盖核心声明式目标制定要素？
- 是否便于快速理解和声明式目标制定启动？

**与其他维度协同**：
- **文档组织协同**：每个自由格式文档对应核心声明式目标制定关注点，4个核心文件覆盖目标制定全貌，格式简单便于维护
- **目录层级协同**：平面目录支持自由格式文档的简单声明式目标制定组织，task_planning/直接存放核心文件，无复杂子目录
- **分类粒度协同**：粗分类声明式目标文档用自由格式简单表达，目标分解、任务序列、阻塞预判、AI上下文规格四大类，格式自由灵活
- **关联复杂度协同**：自由格式支持独立文档的简单目标关联，文档间简单引用，格式灵活不强制
- **内容深度协同**：每个自由格式文档保持核心声明式目标制定内容，内容精简直接，核心目标制定信息突出

**目标业务化要求**：
- Goal标题必须包含业务价值说明
- 验收标准优先使用业务语言
- 技术验证作为"成功条件"补充说明
</formalization-level>
</craft-task-planning-req1-l1>

<planning-methodology>
L1级别声明式目标制定方法和策略：从IMPLEMENTATION阶段直接提取TDD战略和项目规划，转化为AI可理解的声明式目标，重点关注目标制定和验收标准方法：如何将IMPLEMENTATION的战略转化为声明式目标？如何确定目标达成的验收标准？如何识别目标间依赖关系？

**目标制定强制要求**：
- L1执行标准：必须从IMPLEMENTATION阶段的TDD粒度决策和项目规划提取核心目标，采用声明式格式快速表达
- 制定策略：用基础目标列表组织声明式目标，重点突出目标预期结果

**🎯 VS测试资产驱动的GOAL分解策略 (⭐ L1核心特色)**

- GOAL分解基于VS测试资产，不脱离测试驱动基础
- `source_vs`、`related_sc` 承载测试资产追溯关系
- 测试资产 → GOAL验收标准，确保可验证性

**🎯 IMPLEMENTATION战略驱动的目标制定策略**：

**TDD战略→声明式目标转换**：
- **TDD粒度决策 → 功能目标 → 验收标准**的完整转换
- **目标标题必须包含**：
  - 功能模块标识 (GOAL-<SN>-NNN)
  - 验收条件定义
  - 成功状态描述

**Goal格式要求（推荐）**：
- **ID格式**：`GOAL-<SN>-NNN`（例如：GOAL-MAIN-001, GOAL-AUTH-002）
- **Front Matter（推荐）**：包含 `id`, `sn`, `source_vs`, `related_sc` 字段
- **目标标题**：声明式描述，避免过程式步骤

**目标制定完整示例**：
```yaml
---
id: GOAL-MAIN-001
sn: MAIN
source_vs: VS-MAIN-001
related_sc: [SC-MAIN-001, SC-MAIN-005]
test_assets_checklist:
  scenarios: [SC-MAIN-001, SC-MAIN-005]
  test_data: ["user_credentials.json", "login_responses.json"]
  external_deps: ["auth_service_mock", "session_storage"]
  execution_env: ["test_db_setup", "mock_server_config"]
---

Goal: 实现用户登录功能（让用户能安全进入系统） [基于TDD粒度决策]

  声明式目标: 实现完整的用户登录功能，让用户能够安全访问系统

  验收标准（业务视角）:
    - 用户能够输入用户名密码后成功登录
    - 系统能够识别用户身份并记住登录状态
    - 错误的登录信息会被拒绝并给出清晰提示

  成功条件（技术验证）:
    功能完整性:
      - 登录流程正常运行
      - 身份验证机制正确
      - 错误处理有效

    质量标准达成:
      - 通过所有相关单元测试（基于SC-MAIN-001）
      - 通过集成测试验证
      - 满足端到端测试要求（基于SC-MAIN-005）

    用户体验:
      - 操作响应时间<200ms
      - 错误提示清晰易懂
      - 登录流程流畅自然

    AI执行边界:
      - 基于现有TDD策略自主选择实现路径
      - 重点关注功能完整性而非具体实现细节
      - 确保验收标准全部达成

  下一目标依赖:
    - 为GOAL-MAIN-002提供用户认证基础
    - 支持后续功能模块的用户身份验证需求
```

**Front Matter字段说明**：
- `id`: Goal或CTX的唯一标识符（Goal使用GOAL-<SN>-NNN，CTX使用CTX-<SN>-NNN）
- `sn`: Story Namespace，业务域标识（如MAIN, AUTH）
- `source_vs`: 派生来源Vertical Slice（格式：VS-<SN>-NNN）
- `related_sc`: 关联的BDD Scenario列表（格式：[SC-<SN>-NNN, ...]；CTX建议引用关键场景）

---

# ⭐ AI上下文规格完整示例 (`ai_context_specification.md`):
```yaml
---
id: CTX-MAIN-001
sn: MAIN
source_vs: VS-MAIN-001
---
```

```markdown
# AI Context Specification - TaskMaster

> **文档说明**: 本文档提供AI Coding Agent执行TDD代码搭建所需的完整上下文信息。

---

## 文档追溯路径

### 需求文档
- **路径**: `../requirements/user_stories.md`
- **关键ID**: US-MAIN-001（用户创建任务）
- **作用**: 理解业务需求和用户角色视角

### 设计文档
- **路径**: `../design/vertical_slices.md`
- **关键ID**: VS-MAIN-001（用户创建任务成功 - 端到端价值切片）
- **作用**: 理解用户成功状态和价值路径（value_path，即VS的价值路径四向度：Value Path Four Dimensions，包含前端交互/数据流转/后端处理/结果反馈）

- **路径**: `../design/function_points.md`
- **关键ID**: FP-MAIN-001（任务创建功能点）
- **作用**: 理解技术架构、组件设计、API端点、数据模型

### 测试场景 ⭐ **最有用的信息**
- **路径**: `../implementation/bdd_scenarios.md`
- **关键ID**:
  - SC-MAIN-001（成功创建任务 - 正常流程）
  - SC-MAIN-002（标题为空失败 - 异常流程）
  - SC-MAIN-003（后端故障失败 - 异常流程）
- **作用**: BDD格式（Given-When-Then）可直接转换为测试代码
- **核心价值**: 提供完整的用户行为流程和验收标准

### 项目结构文档
- **路径**: `../implementation/project_structure.md` (或其他语义匹配的文件名)
- **关键信息**: 项目根目录结构、源代码目录位置、测试代码目录位置
- **作用**: AI Coding Agent需要知道在哪里创建源代码文件和测试文件
- **核心价值**: 确保TDD代码搭建符合项目目录组织约定

---

## 项目根目录

**当前目录即为项目根目录**

> 💡 **执行说明**: AI Coding Agent应在此文档所在项目的根目录下执行TDD代码搭建
> 📂 **根目录识别**: 本文件位于 `spec/task_planning/` 下，向上两级（`../../`）即为项目根目录

---

## AI执行流程（5步指南）

1. **Read Vertical Slice** (`../design/vertical_slices.md`)
   - 理解 VS-MAIN-001 的用户成功状态
   - 理解 value_path（VS的价值路径四向度：Value Path Four Dimensions，包含前端交互/数据流转/后端处理/结果反馈）

2. **Read Function Point** (`../design/function_points.md`)
   - 理解 FP-MAIN-001 的技术架构
   - 获取组件设计（TaskCreateForm、TaskService等）
   - 获取 API 端点设计（POST /api/tasks）
   - 获取数据模型（Task entity结构）

3. **Read BDD Scenarios** (`../implementation/bdd_scenarios.md`) ⭐ 核心步骤
   - 读取 SC-MAIN-001/002/003 的 Given-When-Then 步骤
   - 将 BDD 场景转换为测试代码（Jest/Mocha/Pytest）
   - 理解正常流程 + 异常流程的完整覆盖

4. **Execute TDD** (在 SPEC_PRJ_ROOT_DIR)
   - 先写测试（Red阶段）：基于 BDD Scenarios 编写测试用例
   - 再写实现（Green阶段）：编写最小实现使测试通过
   - 最后重构（Refactor阶段）：优化代码质量

5. **Verify All Acceptance Criteria**
   - 验证 GOAL-MAIN-001 的所有验收标准
   - 确保测试覆盖率 ≥ 80%
   - 确保 API 响应时间 < 200ms (P95)

---

## 技术栈上下文

### 前端
- **框架**: React 18+ TypeScript
- **Form管理**: react-hook-form 或 formik
- **测试**: Jest + React Testing Library

### 后端
- **框架**: Node.js 18+ TypeScript + Express
- **测试**: Jest + Supertest

### 数据库
- **类型**: PostgreSQL 14+
- **ORM**: Prisma 或 TypeORM

### 代码规范
- **TypeScript**: 严格模式
- **Linter**: ESLint
- **Formatter**: Prettier

---

## AI执行边界

### 自主选择的权限
- ✅ Form库选择（react-hook-form 或 formik）
- ✅ 具体验证逻辑实现方式
- ✅ 组件内部状态管理方式
- ✅ 测试用例的具体断言方式

### 必须遵守的约束
- ❌ 不能修改 API 端点（POST /api/tasks 已定义）
- ❌ 不能修改数据模型（Task entity结构已定义）
- ❌ 不能跳过测试（TDD流程必须遵守）
- ❌ 不能降低测试覆盖率（必须 ≥ 80%）

---

## 阻塞点预判与降级方案

### 潜在阻塞1: 数据库连接配置
- **降级方案**: 先使用内存数据库（SQLite）进行开发和测试
- **清障行动**: 准备数据库配置文档和示例 .env 文件

### 潜在阻塞2: 用户认证系统未完成
- **降级方案**: 使用 Mock 用户ID进行开发（hardcode userId = "test_user"）
- **清障行动**: 与认证模块负责人确认 API 接口和 JWT 格式

---

**⭐ 关键提示**: BDD Scenarios（Given-When-Then）是 AI Coding Agent 最有用的信息，可直接转换为测试代码。
```

**目标优先级排序（强制原则）**：
- 必须按业务价值和TDD战略重要性排序
- 高价值核心功能目标必须优先设定
- 目标间依赖关系必须明确标注

**🎯 项目类型智能目标制定**（承接IMPLEMENTATION阶段TDD战略）：

**前端项目目标制定**：
- **UI功能目标序列**：核心组件目标 → 业务功能目标 → 用户体验目标 → 性能优化目标
- **声明式目标转换**：每个UI需求转换为具体的功能完成目标和用户体验验收标准
- **前端特定验收**：组件渲染正确性 → 交互响应准确性 → 状态管理有效性 → 集成功能完整性
- **目标依赖管理**：基础功能目标 → 业务功能目标 → 集成验证目标

**后端项目目标制定**：  
- **服务功能目标序列**：数据模型目标 → 业务逻辑目标 → API接口目标 → 集成验证目标
- **声明式目标转换**：每个服务需求转换为具体的功能完成目标和API性能验收标准
- **后端特定验收**：数据处理正确性 → 业务逻辑准确性 → API响应稳定性 → 系统性能达标
- **目标依赖管理**：核心服务目标 → 扩展功能目标 → 性能优化目标

**全栈项目目标制定**：
- **全栈功能目标序列**：后端API目标 → 前端功能目标 → 前后端集成目标 → 端到端验证目标
- **声明式目标协调**：后端功能目标稳定后设定前端对接目标，确保集成目标可达成
- **集成验证重点**：API契约目标 → 数据一致性目标 → 用户流程完整性目标

---

**🎯 TDD环境准备GOAL生成策略**（⭐ TDD特有需求）：

TDD开发要求先准备执行环境。建议生成**环境准备GOAL**，让AI根据技术栈自主决定配置方案。

**环境准备三个维度**：
1. **测试环境按类型思考**：根据技术栈和项目需求，思考不同测试类型（单元/集成/E2E）的环境需求
   - 💡 **核心目的**：环境隔离，避免不同测试类型相互干扰
   - 💡 **技术栈相关**：前端/后端/全栈项目对各层级环境的需求不同，AI应灵活决策
2. **端口配置避免冲突**：声明端口需求，AI自选可用端口并提供配置方案
3. **.gitignore配置**：根据技术栈配置忽略规则，AI自动生成适配规则

**验收标准**：
- 测试环境能够独立运行，相互隔离不干扰
- 端口无冲突，配置清晰
- .gitignore覆盖技术栈，不提交无关文件

**L1执行要点**：在 goal_breakdown.md 生成环境GOAL，在任务序列文档中排首位

---

**方法论基础**：基础目标制定方法 + 声明式验收标准定义 + 项目类型智能目标适配 + TDD环境准备</planning-methodology>

<execution-orchestration>
L1级别目标编排策略：必须采用线性目标路径，必须通过简单顺序编排实现清晰的目标达成，严格平衡业务价值与技术依赖的串行目标设定。

**串行目标强制策略**：
- 必须采用简单的数字顺序（Goal-01→Goal-02→Goal-03）建立目标路径
- 必须按业务价值驱动的线性目标达成节奏
- 必须通过最小依赖原则降低目标间复杂度

**🎯 项目类型目标编排思考**（承接IMPLEMENTATION的dependency-mapping）：

**前端项目目标编排**：
- **必须的目标节奏**：基础功能目标先行 → 业务功能目标跟进 → 集成功能目标收尾 → 优化目标点缀
- **强制的串行路径**：功能依赖链必须线性展开，每个目标达成后必须触发下一个
- **必须识别的检查点**：功能间依赖边界、状态隔离点、交互独立性
- **必须的达成反馈**：每个目标达成后必须即时验证

**后端项目目标编排**：
- **必须的目标层次**：[数据层目标]奠基 → [业务层目标]构建 → [接口层目标]暴露 → 集成验证目标
- **强制的依赖流向**：必须从数据模型目标到业务逻辑目标的自然流转
- **必须控制的节点**：数据库就绪目标、业务规则稳定目标、接口冻结目标
- **串行目标强制要求**：必须避免并发修改数据模型目标带来的冲突

**全栈项目目标编排**：
- **强制的协调策略**：后端API目标必须优先达成，为前端目标提供可靠基础
- **强制的目标分界**：后端功能目标阶段 → 前端功能目标阶段 → 集成测试目标阶段
- **必须同步的机制**：API契约目标必须作为前后端目标的同步点
- **串行与并行强制要求**：后端内部目标必须串行、前端内部目标必须串行、两者间严格控制并行</execution-orchestration>

<task-sequence-management>
L1级别任务序列规划：自然语言描述，具体可执行，方法重于策略：先把任务分解和关键顺序理清楚，再考虑如何表达，任务执行的可验证性比规划复杂度更重要。

**验收标准设定**：
- L1声明式目标要点：自然语言描述，具体可达成
- 制定策略：每个任务节点对应明确可验证的完成标准</task-sequence-management>
</craft-task-planning-req2-l1>

<craft-task-planning-req3-l1>
**任务规划_要求3_验证跟踪** L1任务精控：

<progress-tracking>
L1级别目标进度跟踪：简单达成状态标记便于跟踪，基础状态跟踪便于管理，重点关注验证标准和跟踪机制充实度：每个目标的达成标准是否明确可验证？检查点是否具体可达成？状态跟踪是否支持进度管控？

**机制保持简单**：自然语言验收标准，具体可达成检查点便于操作，简单完成状态标记便于跟踪，基础状态跟踪便于管理</progress-tracking>

<prerequisite-validation>
L1级别前置条件检查：实用性优先：环境就绪性的可验证性比配置完美更重要，依赖完整性的检查效率比机制复杂度更关键，配置正确性的简单验证比流程完美更重要。

**就绪性检查要点**：
- L1声明式目标要点：基础环境检查清单，简单直接，便于快速验证和确认
- 检查策略：每个任务执行前都验证基础依赖就绪，专注可执行性而非流程形式</prerequisite-validation>

<completion-criteria>
L1级别完成标准：C1-CONFIRM模式协作精髓："你看着办" = AI主推自由格式目标方案 + 用户快速确认 + 高效执行

**L1核心特征对齐**：
- **质量控制偏好**: 快速迭代，聚焦核心价值交付
- **协作风格**: 信任AI判断，减少反复确认
- **交付节奏**: 优先速度，容忍合理妥协
- **适用场景**: 任意规模团队，偏好快速验证想法

**自由格式核心价值**: 零格式学习成本，零模板负担，最大效率表达核心声明式目标要素

**L1级快速目标制定哲学**: 内容为王，格式从简，行动胜过完美，自由表达即可支撑目标达成

**选择L1的适用场景**: 任意规模团队，偏好快速迭代验证想法的用户的最佳选择</completion-criteria>
</craft-task-planning-req3-l1>

<craft-task-planning-req4-l1>
**任务规划_要求4_质量标准** L1任务精控：

<delivery-gates>L1级别交付门禁和流程：重点关注声明式执行目标文档充实度：是否将TDD战略转化为具体声明式目标？是否提供明确的验收标准和成功条件？是否明确AI执行边界和上下文要求？

**声明式目标组织保持简洁**：4个核心声明式目标制定文档，平面结构便于快速导航，目标清单格式支持AI理解和执行

**内容充实优先**：声明式目标的可达成性比文档数量更重要，目标验收标准的明确性比结构完美更关键

**声明式目标交付门禁**：每个目标达成后必须验证AI执行质量，确保生成的结果符合验收标准强制要求

**完整追溯强制要求**：Goal必须包含完整Front Matter追溯链路（`source_vs: VS-<SN>-NNN` + `related_sc: [SC-<SN>-NNN, ...]`），建立从需求到测试到目标的端到端追溯</delivery-gates>

<context-management>L1级别上下文管理和传递：AI执行上下文策略保持简单：粗粒度声明式目标分解，简单数字排序或分级，直观目标优先级表达便于理解，线性目标达成顺序便于理解，业务价值导向排序支持AI快速决策。

**AI执行上下文管理方法重于策略**：先把声明式目标分解和关键达成顺序理清楚，再考虑如何表达，声明式目标的可达成性比规划复杂度更重要

**AI执行上下文传递机制**：
- 基于implementation/[tdd_strategy_file]的TDD战略上下文，传递给AI具体的实现目标
- 基于implementation/[development_approach_file]的项目规划，传递给AI明确的实现路径
- 每个声明式目标包含完整的TDD战略上下文和预期成果标准</context-management>

<stage-verbatim-directive>
**【任务规划阶段L1 MD文件的质量控制】**

- **适用范围**: 仅对spec/目录下非_前缀的MD文件生效（排除_开头的目录和文件）
- **长度控制**: 400-500行限制，超出按模块拆分
- **补丁保护**: 修改后检查基础完整性要求，核心一致性保护
- **质量预防**: 基础信息密度监控，结构清晰保持，术语统一验证
- **阶段特异**: 目标制定合理性，达成可行性，AI执行指导有效性

**自检清单**:
  - □ 内容组织是否简洁清晰？
  - □ 文档结构是否便于快速理解？
  - □ 目标制定是否合理可达成？
  - □ 验收标准是否具体可验证？

- **修正触发**: 发现问题立即停止，然后让Human-in-the-loop，建议审查、整理和修复
</stage-verbatim-directive>
</craft-task-planning-req4-l1>
