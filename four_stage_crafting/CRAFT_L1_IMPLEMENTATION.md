# CRAFT_L1_IMPLEMENTATION 实施精策指导文档

> 🎯 **LLM执行指令**: TDD实施场景→IMPLEMENTATION阶段关联复杂度实施精策激发，平面结构导向
> 📊 **核心聚焦**: 实施架构关联复杂度控制 - 独立文档少量关联→系统理解基础TDD→实现质量提升
> 📁 **级别特征**: L1-STREAMLINED (3±2核心文件，平面结构，独立关联，快速迭代偏好，适用于任意规模团队)
> 🔧 **协作模式**: C1-CONFIRM模式("你看着办") - 系统主导TDD组织→用户快速确认策略→立即执行
> ⚡ **体系定位**: 创意激发者，支撑脚手架生产+后期推敲，验收标准由four_stage_constraints定义
> 🏗️ **文档架构**: MD+XML混合设计，核心指导内容全部封装在XML标记内，支持LLM精确提取和Level间无缝切换

> 🔗 **命名规范权威引用**:
> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L1 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` (必填 artifacts, 灵活模式, 验收标准)
>
> 🔗 **AICodingAgent规范权威引用**:
> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L1宪章**: `../agentic_spec/SPEC_ACA_L1_CHARTER.md` - L1质量标准 (4-6检查点, 通过率≥95%, 单层追溯)

## 🎯 XML标记体系说明

### 第一级标记 (craft-implementation-req[1-4]-l1)
**目的**: 包含L1级别IMPLEMENTATION阶段的**完整指导内容**，作为LLM提取和Level切换的**整体单位**

### 第二级标记 (完整说明)

#### 6个标准维度子标签 (所有阶段通用 - 要求1):
1. `<document-organization>` - **文档组织架构策略**: 该级别需要多少文档、如何配置文档结构、基本协作约束、目录结构展示
2. `<directory-hierarchy>` - **目录层级组织** [IMPLEMENTATION主攻]: 文件夹结构、层级深度控制、文件布局规范、导航方式设计
3. `<categorization-granularity>` - **分类粒度策略**: 如何分类实施内容、分类细度控制、组织逻辑设计
4. `<interconnection-complexity>` - **关联复杂度管理**: 文档间引用关系、依赖复杂度、交叉引用策略
5. `<content-depth>` - **内容深度策略**: 每个文档写多少内容、详细程度把握、充实度标准定义
6. `<formalization-level>` - **形式化程度**: 模板规范度、结构规范性、系统执行技巧、认知要点集成

#### IMPLEMENTATION阶段专项子标签:
**要求2_TDD深度** (3个子标签):
- `<tdd-strategy>` - **TDD策略设计和实施**: 测试驱动开发策略、红绿重构循环、测试金字塔
- `<test-coverage>` - **测试覆盖度要求和监控**: 测试覆盖率目标、覆盖度统计、质量监控
- `<bdd-scenarios>` - **BDD场景定义和验证**: 行为驱动开发、场景定义、验证标准

**要求3_任务颗粒度** (3个子标签):
- `<task-breakdown>` - **任务分解结构和粒度**: 开发任务拆分、优先级排序、粒度控制
- `<granularity-control>` - **颗粒度控制和标准**: 任务粒度标准、分解原则、执行标准
- `<dependency-mapping>` - **依赖关系映射管理**: 任务依赖关系、关系映射、依赖管理

**要求4_质量标准** (3个子标签):
- `<code-quality>` - **代码质量标准和检查**: 代码质量基线、审查机制、质量度量
- `<integration-gates>` - **集成门禁和流程**: 持续集成、质量门禁、集成流程
- `<stage-verbatim-directive>` - **逐字传递指令**: 对下一阶段/环节的逐字传递与接口要求

## 术语口径（中文 → English）
- TDD（Test-Driven Development） - 测试驱动开发，先写测试后写代码的开发方法
- BDD（Behavior-Driven Development） - 行为驱动开发，基于用户行为场景的测试方法
- Red-Green-Refactor（红绿重构） - TDD核心循环：写失败测试(Red)→写代码让测试通过(Green)→优化代码(Refactor)
- Given-When-Then - BDD场景结构：前置条件(Given)→用户操作(When)→预期结果(Then)
- BDD Scenario（BDD场景） - 基于Vertical Slice转换的可执行测试场景，连接需求与实现
- Test Coverage（测试覆盖率） - 测试代码对业务代码的覆盖程度
- Test Suite（测试套件） - 一组相关的测试场景集合，用于组织和管理测试

### Test Suite 命名与落地（推荐）

- **触发场景**: 当同一 Vertical Slice 推导出 3 条以上 `SC-<SN>-NNN` 场景，或需要把多条 BDD 场景编排成一次端到端执行批次时，引入 `TS-<SN>-NNN` 作为“测试套件”封装执行顺序。
- **Front Matter**: 参考 `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` Section 3.2，至少填写
  ```yaml
  ---
  id: TS-AUTH-035
  sn: AUTH
  source_sc: SC-AUTH-001   # 主场景，若套件涵盖多场景可列数组
  ---
  ```
  > `source_sc` 可接收单个值或 `source_sc: [SC-AUTH-001, SC-AUTH-002]` 的数组写法，保持追溯链与 `CONSTRAINT_L1_IMPLEMENTATION.md` 的验收要求一致。
- **内容建议**:
  - 摘要所有纳入套件的 SC 标题及执行顺序，必要时标注关键差异（正常流 / 异常流）。
  - 说明测试入口命令、依赖环境或初始化步骤，但仍保持声明式描述。
  - 在需要对接持续集成脚本时，可追加“如何触发该套件”的一句话提示，禁止粘贴具体 shell 脚本。
- **交付提醒**: TS 属于推荐 artifact，若项目规模很小、SC 数量 ≤2，可不创建；一旦生成，必须接受 `CONSTRAINT_L1_IMPLEMENTATION.md` 中“Test Suite格式”检查。

## 🤝 多角色协作约束

> 📋 **快速实施原则**: L1-STREAMLINED实施精策策略重点确保Dev/Test能够快速理解TDD结构，立即开始实施
> 🚫 **TDD简化约束**: 避免复杂[testing_framework]配置，采用独立文档少量关联，便于快速上手
> 💼 **原型测试导向**: 优先体现快速原型测试价值，关联复杂度服务于快速迭代目标
> 🎯 **技术角色表达**: 重点使用Dev和Test都能理解的TDD术语，确保独立文档关联复杂度控制清晰简洁

## ⚠️ 重要原则澄清

> 🎯 **维度本质 > 表面形式**: L1/L2/L3的核心是约束复杂度的不同维度，不是具体的文件组织形式
> 📁 **文件/目录是表现**: 文件数量、目录结构只是维度的外在表现，重点是背后的指导价值和复杂度控制
> 🚫 **避免表面约束**: 不要被"平面结构"、"基础TDD"等表面描述约束，关注L1快速简洁的维度本质
> ✨ **指导性优先**: CRAFT是创意激发者，松耦合高内聚的指导性存在，而非行为约束者

## 🎯 统一命名权威标准
**⭐ 以下为权威引用基准，确保系统一致性**

<craft-implementation-req1-l1>
🚫 **应当禁止**：直接编写可执行的业务逻辑代码、函数内部实现细节
✅ **应当产出**：BDD测试场景模板（Given-When-Then结构）、TDD策略指导、测试驱动开发方法
⚠️ **脚手架约束**：提供测试场景框架和TDD策略，指导开发者如何实现，但不提供具体业务代码实现

**实施精策_要求1_文档体系** L1实施精策：

<document-organization>
> **⭐ 权威来源**:
> - Artifact定义、PREFIX清单及标准托管文件: `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` Section 1.6
> - L1级别推荐托管映射: `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` Section 3.2
>
> 以下为L1-IMPLEMENTATION阶段的标准维度定义和文档组织指引

**📋 受众定位约束**（IMPLEMENTATION阶段质量标准）：
- **主要读者**: 开发者（技术专业人员）
- **语言要求**: 可使用技术语言，但必须保留业务上下文
- **可读性标准**: 开发者能看懂技术实现，也能理解业务意图

**✅ 允许的技术内容**：
- 技术实现细节（TDD策略、测试框架、代码结构）
- 技术指标（代码覆盖率、性能标准、响应时间）
- 开发工具和命令（npm、测试命令、构建脚本）
- 技术术语和专业概念

**🔴 强制要求**：
- 每个技术决策必须说明业务理由
- 测试场景必须关联业务功能
- 技术指标必须解释业务价值

**❌ 禁止项**：
- **过程式代码示例**（函数调用、类方法、执行步骤） ← ⚠️ 硬性约束
- 纯技术术语堆砌，无业务上下文
- 技术细节不说明"为什么这样做"
- 脱离业务价值的技术炫技

**✅ 容许项**：
- **声明式代码**（测试配置、数据模型、接口声明） ← 允许使用

**技术术语密度 ≤ 40%**（IMPLEMENTATION阶段约束）

🎯 **核心维度特征**（应当遵循）：
L1应当体现"快速简洁，独立关联"的本质特征
- **复杂度控制**：最小化依赖，独立文档设计，基础TDD实施组织
- **协作特征**：支持C1-CONFIRM模式("你看着办")，快速原型测试优先
- **质量标准**：MVP测试价值优先，用测试指导开发，避免过度TDD管理

📋 **推荐实施方案**（可参考调整）：
**⭐ L1-STREAMLINED 实施文档组织架构 - 创建implementation时的核心指导**：
```
implementation/                     # TDD粒度决策+项目规划根目录（独立文档少量关联）
├── [project_structure_file]         # 🆕 项目目录结构：定义代码、测试、资源的组织结构
├── [tdd_strategy_file]              # TDD粒度决策：unit/integration/e2e分配策略
├── [bdd_test_scenarios_file]        # 🎯 核心：具体可执行的BDD场景集合
└── [test_driven_sequence_file]      # 🎯 核心：项目实施规划与构建策略指导
```

**文档组织要求**：适量核心文档（参考范围3-5个），具体数量取决于维度覆盖需要
**策略定位**：每个独立文档对应核心TDD实施关注点
**实施精策指导**：4个核心文件精简为主，平面结构便于快速导航，开发指导为主，包含[project_structure_file]、[tdd_strategy_file]、[bdd_test_scenarios_file]、[test_driven_sequence_file]四个核心文档
**开发导向**：每个文档都是"TDD粒度决策+项目规划的指导框架"，价值分配：BDD场景(50%精力) + TDD粒度决策(30%精力) + 项目实施规划(20%精力)，重点是"确定unit/integration/e2e测试分配策略并转化为项目实施计划"而非单纯测试管理
**质量标准**：文档组织最优化，TDD组织最清晰，避免过度复杂结构
**灵活性说明**：可增加[quality_file]或合并某些策略文档，但需保持独立文档少量关联的特征
**多角色协作约束**：L1-STREAMLINED实施精策策略重点确保PM/Dev/Test能够快速理解TDD意图，减少沟通成本，避免复杂TDD术语，采用直观的实施表达便于快速决策和执行，优先体现快速原型测试价值和MVP场景，TDD策略服务于快速交付目标，重点使用PM和Dev都能理解的简洁术语，确保独立文档关联复杂度控制清晰可执行

**📋 文档生产次序**：[project_structure_file] → [tdd_strategy_file] → [bdd_test_scenarios_file]（获得SC ID，填写source_vs） → [test_driven_sequence_file]（引用SC场景ID排序）
**次序原因**：目录结构需要先定义（TDD策略依赖测试文件位置） + sequence依赖场景ID排序 + BDD Scenario的source_vs需要从DESIGN阶段获取VS ID

📁 **核心文档组织维度说明** (L1-STREAMLINED特征): 以下帮助理解占位符背后的文件组织思考维度，具体文件组织可灵活适配项目需要

**文档组织原则**:
- **维度优先**: 必需的是覆盖核心维度，文件组织形式灵活
- **按阶段分目录**: requirements/design/implementation/task_planning
- **按粒度分层**: 核心文档放根目录，细节文档可放子目录或拆分文件
- **命名规范**: snake_case，语义化文件名
- **关联管理**: 使用相对路径引用，保持文档间关联清晰
- **灵活适配**: 内容少时合并文档，内容多时拆分文件（如`xxx_part1.md`），复杂时建子目录

**维度1: 项目结构维度 (必需)**
- **对应占位符**: `[project_structure_file]`
- **文件命名**: 由AI Agent根据项目特点智能决定文件名
- **维度职责**: 定义项目实际代码的目录结构（⭐ 项目根目录与spec/平级）
- **文档组织方式**:
  - 单文件形式（AI Agent智能命名）
- **前置条件**: 
  - ⚠️ 技术栈必须在DESIGN阶段完全敲定
  - ⚠️ 如技术栈未确定，必须提示用户先澄清技术栈
- **内容要求**: 
  - 项目根目录结构（⭐ 关键约束：项目根目录是spec/的父目录，实际代码目录与spec/平级）
  - 源代码目录位置（具体组织方式由技术栈决定）
  - ⭐ **测试代码目录位置（TDD核心基础设施，必须明确三类测试位置）**:
    - **单元测试目录**：根据技术栈惯例智能决定（可能多处，如与源码同目录、独立tests/unit/、或技术栈特定位置如src/test/java/）
    - **集成测试目录**：根据项目架构智能决定（可能多处，如独立tests/integration/、服务级integration测试目录等）
    - **端到端测试目录**：根据E2E工具智能决定（通常一处，如e2e/、tests/e2e/、或工具特定目录如cypress/e2e/）
    - **指导原则**：遵循技术栈社区惯例，支持TDD工作流，测试位置清晰可发现
  - 配置/资源目录位置（如适用）
  - 构建输出目录位置（如适用）
- **生成方式**: 
  - 完全由AI Agent根据技术栈、语言、项目特点智能生成
  - 不预设固定模板，不规定具体文件命名规范
  - ⭐ **只聚焦目录结构层面（文件夹组织），不涉及具体文件名**
  - ⭐ **如需提及文件类型，必须使用泛化的[]占位符形式**，如`[组件名].vue`、`[控制器名].js`
  - ⭐ **禁止列举具体文件名**，如Button.vue、authController.js等
- **L1特征**: 极简目录结构，快速启动项目，满足基本开发需求即可

**维度2: TDD策略维度 (必需)**
- **对应占位符**: `[tdd_strategy_file]`
- **参考示例**: `tdd_strategy.md`
- **维度职责**: 记录TDD粒度决策和测试策略
- **文档组织方式**:
  - 单文件形式: `tdd_strategy.md`
  - 多文件形式: `tdd_strategy_part1.md`, `tdd_strategy_part2.md` (策略复杂时)
  - 目录结构形式: `tdd/strategy.md`, `tdd/guidelines.md`
  - 合并文档形式: 作为实施总览文档的"TDD策略"章节
- **内容要求**: 测试粒度选择、TDD工作流、质量标准
- **L1特征**: 优先单文件，简洁实用

**维度3: BDD场景维度 (必需)**
- **对应占位符**: `[bdd_test_scenarios_file]`
- **参考示例**: `bdd_test_scenarios.md`
- **维度职责**: 记录具体可执行的BDD场景集合
- **文档组织方式**:
  - 单文件形式: `bdd_test_scenarios.md`
  - 多文件形式: `bdd_scenarios_part1.md`, `bdd_scenarios_part2.md` (场景多时)
  - 目录结构形式: `bdd/auth_scenarios.md`, `bdd/business_scenarios.md`
  - 合并文档形式: 作为TDD策略文档的"BDD场景"章节
- **内容要求**: Given-When-Then格式场景，映射到Vertical Slice
- **L1特征**: 优先单文件或合并

**维度4: 实施规划维度 (必需)**
- **对应占位符**: `[test_driven_sequence_file]`
- **参考示例**: `test_driven_sequence.md` 或 `implementation_plan.md`
- **维度职责**: 记录项目实施规划与构建策略指导
- **文档组织方式**:
  - 单文件形式: `test_driven_sequence.md`
  - 多文件形式: `sequence_part1.md`, `sequence_part2.md` (阶段多时)
  - 目录结构形式: `sequence/phase1.md`, `sequence/phase2.md`
  - 合并文档形式: 作为TDD策略文档的"实施顺序"章节
- **内容要求**: 构建顺序、里程碑、依赖关系
- **L1特征**: 优先单文件或合并

**维度5: 质量管理维度 (可选)**
- **对应占位符**: `[quality_file]`
- **参考示例**: `quality_standards.md`
- **维度职责**: 记录质量标准和代码规范
- **文档组织方式**: 单文件或合并到TDD策略文档
- **L1特征**: 通常合并或省略
</document-organization>

<directory-hierarchy>**策略定位**：平面目录支持独立文档的简单TDD组织
**实施精策指导**：implementation/直接存放核心文件，无子目录，平面结构或单层目录支持独立文档快速组织和导航
**质量标准**：目录结构简洁清晰，便于快速定位和理解，支持独立文档的基础分类</directory-hierarchy>  

<categorization-granularity>**实施架构核心定位**：独立文档少量关联 - 用独立文档少量关联的清晰组织实现TDD管理→系统快速决策最简关联方案→实现质量提升（核心工作做简洁），C1-CONFIRM模式下系统快速决策最简关联方案，用户信任确认即可，"你看着办" - 用户信任系统的关联决策，重点在快速TDD启动而非完美关联

**设计承接策略**：基于DESIGN阶段的实施响应：基于Function Point的TDD直接映射策略，保持Function Point→BDD测试的直接映射；
**Function Point→TDD直接映射**：
- **直接转化原理**：每个Function Point直接转化为一个BDD场景，最大化简化效率
- **快速原型导向**：Function Point→Given-When-Then场景→开发策略指导
简单目录引用格式："FP-<SN>-NNN → SC-<SN>-NNN Given-When-Then"（例如：FP-MAIN-001 → SC-MAIN-001）；快速验证TDD覆盖所有Function Point，无测试盲区

**L1分类粒度策略**：粗分类TDD文档间保持独立，少量交叉引用，[tdd_strategy_file]可引用[bdd_test_scenarios_file]，[test_driven_sequence_file]引用[bdd_test_scenarios_file]

**实施精策要求**：
- **[tdd_strategy_file]**: TDD策略基础指导(5%精力) - 应当提供Red-Green-Refactor循环简洁说明，为开发团队提供基础TDD规范；简化引用："基于 [bdd_test_scenarios_file] 场景执行"，重点是提供开发实现的[testing_framework]
- **[bdd_test_scenarios_file]**: BDD场景开发指令集(70%精力) - 🎯 核心文档：应当包含具体可执行的Given-When-Then场景，每个场景都应当是开发实现的具体指令，指导开发者应该采用什么策略来满足测试；场景格式："Given 用户登录 → 应当采用认证策略"
- **[test_driven_sequence_file]**: 代码构建顺序指导(25%精力) - 🎯 重要文档：应当指导开发者按什么顺序制定策略，基于BDD场景的实现顺序，确保按测试驱动的方式逐步构建功能

**L1特异性检查**：是否避免了复杂的文档间依赖？BDD场景是否能有效指导开发实现？代码构建顺序是否清晰可执行？是否体现"用测试策略指导开发思路"的核心理念？

**与其他维度协同**：
- **文档组织协同** (L1: 少量核心文件)：每个平面目录对应核心TDD文档，文档组织最优化，TDD组织最清晰
- **目录层级协同** (L1: 平面结构或单层目录)：粗分类TDD要素在平面目录中独立组织，策略-场景-顺序三大类，无子分类  
- **内容深度协同** (L1: 轻量级内容，概要了解)：每个平面目录文档保持TDD核心内容，避免冗余，每个文档控制篇幅，核心TDD信息突出
- **形式化程度协同** (L1: 自由格式，基础Markdown)：平面实施文档体系化但组织格式简洁，统一模板，标准标题，TDD流程清晰但不复杂

**策略定位**：用独立文档少量关联的清晰组织实现开发驱动，C1-CONFIRM模式下系统快速决策最简关联方案
**实施精策指导**：BDD场景为核心([major_focus])，构建顺序为重点([primary_focus])，TDD策略为基础([basic_focus])？场景指导开发实现，顺序指导团队实施，策略提供开发框架？
**质量标准**：独立文档少量关联，每个BDD场景能有效指导开发实现，支持C1-CONFIRM模式的用户快速信任确认开发方案</categorization-granularity>

<interconnection-complexity>**策略定位**：采用独立文档为主的清晰关联体系，每个文档最多2-3个引用点，专注开发指导的快速价值交付

**具体操作指导**：
- **[tdd_strategy_file]引用规范**: "基于 [bdd_test_scenarios_file] 场景执行TDD循环"
- **[bdd_test_scenarios_file]引用规范**: "为 [test_driven_sequence_file] 提供实现顺序基础"  
- **[test_driven_sequence_file]引用规范**: "按照 [bdd_test_scenarios_file] 场景S01→S02→S03顺序实现"
- **引用密度控制**: 每个文档≤2个引用点，专注开发指导
- **开发友好性**: 每个引用都明确告诉开发团队应该做什么

**系统执行检查点**：
1. BDD场景是否具体可执行，能指导开发实现？
2. 代码构建顺序是否清晰，开发团队能理解执行？
3. TDD策略是否简洁明确，团队能应用？

**质量标准**：独立性检验通过，开发指导性明确，支持C1-CONFIRM模式快速理解和执行</interconnection-complexity>

<content-depth>**策略定位**：每个独立文档保持核心TDD内容，避免冗余引用
**实施精策指导**：应当保持轻量级内容，概要了解，每个文档控制篇幅，核心TDD信息突出，重点关注TDD策略制定充实度的完整记录。协同要求：每个独立文档应当保持核心TDD内容，避免冗余引用
**质量标准**：TDD策略的可执行性比文档数量更重要，测试先行原则的贯彻比结构完美更关键

**业务上下文要求**：
- 技术决策必须说明业务背景
- 测试策略必须关联业务场景
- 性能指标必须解释用户价值
</content-depth>

<formalization-level>**策略定位**：独立文档结构化但引用格式简洁
**实施精策指导**：应当采用自由格式，基础Markdown，统一模板，标准标题，引用清晰但不复杂。协同要求：独立文档应当结构化但引用格式简洁
**质量标准**：可用性比完美更重要，格式标准化支持协作效率和快速交付

**⭐ Artifact ID分配**: 保持现有artifact ID不变(确保引用完整性)，仅对新增artifact扫描宿主文件同PREFIX+SN，取max序号+1分配新ID

**L1实施精策执行技巧**：
1. **TDD策略理解** - 核心TDD原则，简单测试金字塔，快速反馈循环→用红-绿-重构循环组织实施流程，重点突出TDD价值
2. **测试环境配置** - 基础[testing_framework]选型，简单配置管理，快速环境搭建→按主流[testing_framework]标准化配置，重点保证测试环境可用性
3. **任务清单组织** - 线性任务组织，测试先行步骤，简单状态跟踪→基础任务分组（准备/执行/验证）简单管理
4. **质量门禁机制** - 核心检查点：独立关联复杂度控制→TDD可执行性→快速实施性，协作流程：系统分析TDD需求→提出4文档独立关联方案→用户快速浏览确认核心TDD思路→立即执行生产，通过标准：\"项目结构清晰了吗？TDD策略清晰了吗？测试环境能快速搭建吗？任务能立即开始执行吗？\"

**TDD专业优化**：测试先行原则，快速迭代周期，持续集成就绪；每个实施文档直接支持TDD实践，平面目录便于快速导航和执行

**认知补强要点**：C1-CONFIRM模式协作精髓\"你看着办\" = 系统主推独立关联方案 + 用户快速确认 + 高效执行，L1核心特征对齐：质量控制偏好（快速迭代，聚焦核心价值交付）、协作风格（信任系统判断，减少反复确认）、交付节奏（优先速度，容忍合理妥协）、适用场景（任意规模团队，偏好快速验证想法），独立关联核心价值：零关联学习成本，零管理负担，最大效率覆盖核心TDD关联要素，L1级TDD启动哲学：速度为王，可测胜过完美，行动胜过分析，独立关联即可支撑TDD，选择L1的适用场景：任意规模团队，偏好快速迭代验证想法的用户的最佳选择

**结构准确性检查**：是否采用L1标准的四文档独立关联结构？是否包含[project_structure_file]、[tdd_strategy_file]、[bdd_test_scenarios_file]、[test_driven_sequence_file]四个核心文档？是否体现AI编程驱动导向？</formalization-level>

**⚡ 执行技巧集成**
**L1实施精策执行技巧**：
1. **TDD策略基础** - [tdd_strategy_file]：Red-Green-Refactor循环简洁说明(5%精力)，为开发团队提供基础[testing_framework]
2. **BDD场景核心** - [bdd_test_scenarios_file]：具体可执行的Given-When-Then场景(70%精力)，每个场景指导开发策略思路
3. **构建顺序指导** - [test_driven_sequence_file]：开发实现的具体顺序(25%精力)，基于BDD场景的渐进式构建
4. **质量门禁机制** - 核心检查点：项目结构清晰度→BDD场景开发指导性→代码构建顺序清晰度→TDD策略可执行性，协作流程：系统分析设计需求→提出4文档开发指导方案→用户快速确认项目结构、BDD场景和构建顺序→立即执行开发实现，通过标准：\"项目结构是否支持TDD工作流？BDD场景能否有效指导开发实现？构建顺序是否清晰可执行？团队能否立即开始测试驱动开发？\"

</craft-implementation-req1-l1>

<craft-implementation-req2-l1>
**实施精策_要求2_TDD深度** L1实施精策：

<tdd-strategy>**开发[testing_framework](5%精力)**：Red-Green-Refactor循环的实施指导，告诉开发团队如何按TDD方式开发：
1. **Red阶段**：先写失败的测试案例，明确测试场景与测试数据关联
2. **Green阶段**：制定最简策略让测试通过，建立外部依赖与环境配置清晰关系  
3. **Refactor阶段**：优化策略保持测试通过，确保测试资产完整性验证

**🎯 项目类型智能构建顺序**（承接DESIGN阶段组件设计）：

**前端项目构建顺序**：
- **基础[frontend_component]优先**：Button, Input, Modal等通用[frontend_component] → 独立测试，无外部依赖
- **业务[frontend_component]构建**：UserCard, ProductItem等业务[frontend_component] → 基于基础[frontend_component]测试
- **页面[frontend_component]集成**：HomePage, UserProfile等页面[frontend_component] → 集成多个业务[frontend_component]测试
- **交互逻辑验证**：状态管理、路由跳转、[api_interface]调用 → 端到端行为测试

**后端项目构建顺序**：
- **[data_layer]测试**：Repository, DAO测试 → [data_store]操作验证
- **[business_layer]测试**：Service层测试 → 核心业务规则验证  
- **[api_layer]测试**：Controller测试 → 请求响应验证
- **集成测试**：完整业务流程 → 端到端[api_interface]验证

**全栈项目构建顺序**：
- **后端[api_interface]优先**：确保[api_interface]稳定后前端对接
- **前端[frontend_component]并行**：基础[frontend_component]可与[api_interface]开发并行
- **集成测试收尾**：前后端联调和端到端测试

**方法论基础**：TDD核心循环(Red-Green-Refactor) + 基础BDD场景驱动(Given-When-Then) + 项目类型适配构建顺序
**实施要点**：根据项目类型智能选择构建顺序，确保开发团队按正确依赖关系开发，避免构建混乱</tdd-strategy>

<test-coverage>**开发覆盖强制要求**：指导开发过程中的测试重点（70%精力投入）：
- **核心逻辑必须**：必须为核心业务逻辑编写BDD测试
- **边界案例必要**：必须覆盖基本的边界情况
- **快速反馈原则**：开发必须以快速测试反馈为驱动
**实施要点**：告诉开发团队什么地方必须写测试，什么地方可以简化</test-coverage>

<bdd-scenarios>**开发场景指令([major_focus]) 🎯 核心重点**：每个BDD场景都是开发策略的指导框架

**🎯 VS测试资产载体理念 (⭐ L1核心特色)**

VS承载完整测试资产，支持独立验证：
1. **测试场景**：VS对应的验证场景定义
2. **测试数据**：场景执行的数据要求
3. **外部依赖**：外部服务的集成策略  
4. **执行环境**：测试运行的环境配置

**核心目的**: VS测试资产完整性，支持后续GOAL分解基础

**🎯 Vertical Slice → BDD场景转换机制**：

**转换原理**：
- Vertical Slice的user_success → BDD的Feature描述
- Vertical Slice的value_path → BDD的Scenario步骤
- 完整的端到端价值链路 → 完整的Given-When-Then-And步骤

**转换模板**：
```gherkin
Feature: [Vertical Slice的user_success]
  Background:
    Given [系统初始状态]
  
  Scenario: [价值路径实现 - VS ID]
    # 前端交互 → Given/When
    Given [VS的前端交互-前置条件]
    When [VS的前端交互-用户操作]
    
    # 数据流转 → And验证
    And [VS的数据流转-前后端交换验证]
    
    # 后端处理 → And验证
    And [VS的后端处理-业务逻辑验证]
    
    # 结果反馈 → Then
    Then [VS的结果反馈-成功状态验证]
    And [端到端一致性验证]
```

**转化示例**：VS-MAIN-001 → SC-MAIN-001（user_success → Feature + value_path四向度 → Given-When-Then-And）

**🔄 转换关键点**：
- **Feature标题**：直接使用Vertical Slice的user_success
- **Scenario标题**：标注Vertical Slice ID，建立追溯链路
- **Given步骤**：来自"前端交互"的前置条件部分
- **When步骤**：来自"前端交互"的用户操作部分
- **And步骤（数据/后端）**：分别对应"数据流转"和"后端处理"
- **Then步骤**：对应"结果反馈"的验证点
- **最后And**：确保端到端一致性

**📋 与Function Point的协同**：
- Function Point (FP-<SN>-NNN) → BDD Scenario的代码实现指导（例如：FP-MAIN-001）
- Vertical Slice (VS-<SN>-NNN) → BDD Scenario的测试需求来源（例如：VS-MAIN-001）
- 双重追溯：VS-<SN>-NNN → FP-<SN>-NNN → SC-<SN>-NNN (BDD Scenario) → Code（例如：VS-MAIN-001 → FP-MAIN-001 → SC-MAIN-001 → Code）

**基础场景结构**：
- **场景格式**：Given(前置条件) → When(用户行为) → Then(期望结果) → 应实现的代码
- **开发指导**：每个场景明确告诉开发者应该写什么功能代码
- **具体可执行**：场景应当具体到开发者可以直接转化为代码实现

**🎯 项目类型智能场景转换**（承接DESIGN阶段组件设计）：

**前端项目场景生成**：
- **[frontend_component]渲染场景**：Given [frontend_component]数据 → When [frontend_component]渲染 → Then 正确显示内容
  * 示例：Given 用户列表数据 → When UserList[frontend_component]渲染 → Then 显示用户名和头像
- **交互行为场景**：Given 初始状态 → When 用户操作 → Then 状态变化和UI更新
  * 示例：Given 登录表单 → When 用户输入并提交 → Then 显示加载状态并跳转
- **状态管理场景**：Given 全局状态 → When 状态更新 → Then 相关[frontend_component]重新渲染
  * 示例：Given 购物车空 → When 添加商品 → Then 购物车图标显示数量

**后端项目场景生成**：
- **[api_interface]功能场景**：Given 请求参数 → When 调用[api_interface] → Then 返回期望数据
  * 示例：Given 用户ID → When 获取用户信息 → Then 返回用户详情JSON
- **数据操作场景**：Given [data_store]状态 → When 执行操作 → Then 数据正确更新
  * 示例：Given 空数据表 → When 创建用户 → Then [data_store]新增一条记录
- **业务逻辑场景**：Given 业务前置条件 → When 执行业务操作 → Then 业务结果符合预期
  * 示例：Given 库存充足 → When 下单 → Then 扣减库存并生成订单

**全栈项目场景生成**：
- **端到端场景**：Given 完整业务流程 → When 用户完整操作 → Then 前后端协同正确
- **集成场景**：Given [api_interface]就绪 → When 前端调用 → Then 数据正确展示

**场景数量控制（与TASK_PLANNING Suite分组协同）**：
- **每个Feature建议3-7个Scenario** - 避免单个Feature过于庞大
- **场景粒度适配** - 便于TASK_PLANNING阶段按Suite分组（每组3-5个场景）
- **AI上下文友好** - 确保场景数量在AI单次处理能力范围内

**实施要点**：这是开发实现的主要指导文档，[major_focus]投入在这里，根据项目类型智能生成相应的BDD场景模板</bdd-scenarios>
</craft-implementation-req2-l1>

<craft-implementation-req3-l1>
**实施精策_要求3_任务颗粒度** L1实施精策：

<task-breakdown>**开发任务分解指导**：不是管理任务，而是指导开发者按什么顺序编程
- **代码构建顺序([primary_focus])**：告诉开发者先写什么代码，后写什么代码
- **测试驱动节奏**：按BDD场景→测试代码→功能代码的节奏实施
- **线性执行路径**：提供清晰的代码实现路径，避免开发混乱
**实施要点**：这是开发实现的实施顺序指导，确保按正确顺序构建功能</task-breakdown>

<granularity-control>**开发粒度控制**：控制开发过程的步骤大小，确保能有效执行
- **场景粒度**：每个BDD场景对应一个开发单元
- **代码块粒度**：一次实现一个完整的功能块（适中工作量）
- **测试粒度**：每个功能块都有对应的测试代码
**实施要点**：帮助开发团队合理拆分开发任务，既不过细也不过粗</granularity-control>

<dependency-mapping>**开发依赖管理**：告诉开发团队代码模块之间的依赖关系，指导实现顺序
- **简单依赖链**：A功能→B功能→C功能，按依赖顺序开发
- **循环依赖检查**：避免陷入循环依赖的开发困境
- **清晰依赖图**：提供可视化的实现依赖关系

**后端三层架构与BDD场景协同策略**：
- **Phase 1 - 数据层优先**：优先完成data_layer基础（所有Repository/DAO测试通过）
- **Phase 2 - 场景驱动**：按BDD场景顺序实现business_layer + api_layer
- **避免策略**：单个BDD场景不应跨三层同时开发，应按层完成后再组装
- **执行示例**：BDD场景"用户登录" → 确保User Repository就绪 → 实现AuthService + LoginController
- **前端项目**：无三层约束，直接按BDD场景顺序开发组件

**实施要点**：确保按正确的依赖顺序开发，避免实现冲突</dependency-mapping>
</craft-implementation-req3-l1>

<craft-implementation-req4-l1>
**实施精策_要求4_质量标准** L1实施精策：

<code-quality>**开发质量检查要点**：
- **BDD场景完整性**：每个场景是否能有效指导开发实现？
- **代码构建顺序清晰度**：开发团队是否能理解实现顺序？
- **TDD策略可执行性**：团队能否按Red-Green-Refactor循环开发？

**质量标准**：采用L1标准的四文档独立关联结构，包含[project_structure_file]、[tdd_strategy_file]、[bdd_test_scenarios_file]、[test_driven_sequence_file]四个核心文档，每个都是开发指令集

**BDD Scenario格式要求（推荐）**：
- **ID格式**：`SC-<SN>-NNN`（例如：SC-MAIN-001, SC-AUTH-002）
- **Front Matter**（推荐）：包含 `id`, `sn`, `source_vs` 字段
- **场景标题标注**：必须标注Vertical Slice ID（格式：Scenario: [场景描述] - VS-<SN>-NNN），建立与REQUIREMENTS和DESIGN的追溯链路

**BDD Scenario示例**（包含Front Matter）：
```yaml
---
id: SC-MAIN-001
sn: MAIN
source_vs: VS-MAIN-001
---

Feature: 用户认证成功状态实现
  业务价值: 确保用户能够安全登录系统
  
  Scenario: 用户登录认证完整流程 - VS-MAIN-001
    Given 系统中存在已注册用户
    When 用户提交正确的登录信息
    Then 用户成功进入系统并获得访问权限
    
  技术验证: 系统返回成功状态和身份令牌
```</code-quality>

<integration-gates>**开发门禁机制**：
- **开发指导有效性检查**：BDD场景是否具体可执行？
- **构建顺序逻辑性检查**：开发顺序是否合理？
- **[testing_framework]适用性检查**：团队能否应用TDD策略？
**门禁标准**：C1-CONFIRM模式单检查点快速确认，3个开发指导文档无复杂关联负担，用户能快速确认开发方案可行性

**交付标准整合内容**：
- **开发成果验收**：是否按BDD场景成功实现功能代码？
- **测试驱动完整性**：是否为每个功能编写了对应测试？
- **代码质量基线**：生成的代码是否符合基本质量要求？
**交付准则**：体现L1-STREAMLINED快速交付特征，开发方案具体可执行，L1级开发指导便于TDD实际应用，避免复杂流程，支持C1-CONFIRM模式快速验收</integration-gates>

<stage-verbatim-directive>
**【实施阶段L1 MD文件的质量控制】**

- **适用范围**: 仅对spec/目录下非_前缀的MD文件生效（排除_开头的目录和文件）
- **长度控制**: 400-500行限制，超出按模块拆分
- **补丁保护**: 修改后检查基础完整性要求，核心一致性保护
- **质量预防**: 基础信息密度监控，结构清晰保持，术语统一验证
- **阶段特异**: TDD策略完整性，测试场景开发指导有效性

**自检清单**:
  - □ 内容组织是否简洁清晰？
  - □ 文档结构是否便于快速理解？
  - □ TDD策略是否完整可执行？
  - □ BDD场景是否能有效指导开发实现？

- **修正触发**: 发现问题立即停止，然后让Human-in-the-loop，建议审查、整理和修复
</stage-verbatim-directive>
</craft-implementation-req4-l1>
