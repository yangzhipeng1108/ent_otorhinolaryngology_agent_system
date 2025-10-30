# CRAFT_L1_DESIGN 精工设计指导文档

> 🎯 **系统执行指令**: 架构设计分析场景→DESIGN阶段关联复杂度精工设计激发，基础关联导向
> 📊 **核心聚焦**: 设计架构关联复杂度控制 - 基础组件关联→系统理解基础架构→实现质量提升
> 📁 **级别特征**: L1-STREAMLINED (3±2核心文件，平面目录，基础简洁，快速原型偏好，适用于任意规模团队)
> 🔧 **协作模式**: C1-CONFIRM模式("你看着办") - 系统主导方案设计→用户确认接受→快速推进策略
> ⚡ **体系定位**: 创意激发者，支撑脚手架生产+后期推敲，验收标准由four_stage_constraints定义
> 🏗️ **文档架构**: MD+XML混合设计，核心指导内容全部封装在XML标记内，支持系统精确提取和Level间无缝切换
> 🔗 **命名规范权威引用**:
> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L1 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` (必填 artifacts, 灵活模式, 验收标准)
>
> 🔗 **AICodingAgent规范权威引用**:
> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L1宪章**: `../agentic_spec/SPEC_ACA_L1_CHARTER.md` - L1质量标准 (4-6检查点, 通过率≥95%, 单层追溯)

## 🎯 XML标记体系说明

### 第一级标记 (craft-design-req[1-4]-l1)
**目的**: 包含L1级别DESIGN阶段的**完整指导内容**，作为系统提取和Level切换的**整体单位**

### 第二级标记 (完整说明)

#### 6个标准维度子标签 (所有阶段通用 - 要求1):
1. `<document-organization>` - **文档组织架构策略**: 该级别需要多少文档、如何配置文档结构、基本协作约束、目录结构展示
2. `<directory-hierarchy>` - **目录层级组织**: 文件夹结构、层级深度控制、文件布局规范、导航方式设计
3. `<categorization-granularity>` - **分类粒度策略**: 如何分类设计内容、分类细度控制、组织逻辑设计
4. `<interconnection-complexity>` - **关联复杂度管理** [DESIGN主攻]: 文档间引用关系、依赖复杂度、交叉引用策略
5. `<content-depth>` - **内容深度策略**: 每个文档写多少内容、详细程度把握、充实度标准定义
6. `<formalization-level>` - **形式化程度**: 模板规范度、结构严格性、系统执行技巧、认知要点集成

#### DESIGN阶段专项子标签:
**要求2_架构表达** (3个子标签):
- `<architecture-structure>` - **架构结构组织方式**: 系统分层设计、模块划分方法、组件关系定义
- `<component-definition>` - **组件概念和边界划分**: 组件职责理念、边界清晰化、交互原则
- `<interface-design>` - **交互设计和契约理念**: API设计思路、数据契约理念、通信协议指导

**要求3_技术决策** (3个子标签):
- `<decision-framework>` - **决策框架和评估方法**: 技术选型原则、评估标准、决策流程
- `<alternative-evaluation>` - **备选方案分析对比**: 方案对比分析、优缺点评估、选择依据
- `<constraint-management>` - **约束管理和权衡取舍**: 技术约束识别、权衡决策、妥协管理

**要求4_质量标准** (3个子标签):
- `<design-coherence>` - **设计连贯性保障**: 架构一致性、设计原则统一、逻辑连贯
- `<quality-assurance>` - **质量保证和检查机制**: 设计审查、质量门禁、验收标准
- `<evolution-support>` - **演进支持和可维护性**: 扩展性设计、维护友好性、演进策略

## 🤝 多角色协作约束

> 📋 **快速原型原则**: L1-STREAMLINED精工设计策略必须支持快速迭代，确保原型友好和迭代效率
> 🚫 **基础简洁约束**: 避免过度复杂的设计分类，关联控制需适度简化，支持快速理解
> 💼 **原型导向平衡**: 平衡架构清晰度与策略简洁性，确保基础关联复杂度服务快速原型开发
> 🎯 **基础化表达**: 使用简洁清晰的基础术语，确保基础关联复杂度便于理解和策略制定

## ⚠️ 重要原则澄清

> 🎯 **维度本质 > 表面形式**: L1/L2/L3的核心是约束复杂度的不同维度，不是具体的文件组织形式
> 📁 **文件/目录是表现**: 文件数量、目录结构只是维度的外在表现，重点是背后的指导价值和复杂度控制
> 🚫 **避免表面约束**: 不要被"平面结构"、"2层目录"等表面描述约束，关注L1快速简洁的维度本质
> ✨ **指导性优先**: CRAFT是创意激发者，松耦合高内聚的指导性存在，而非行为约束者

## 术语口径（中文 → English）
- 架构设计（Architecture Design）
- 组件接口（Component Interface）
- 数据模型（Data Model）
- 技术选型（Technology Selection）
- KISS原则（Keep It Simple, Stupid） - 保持简单直接的设计理念，避免不必要的复杂性
- C4模型（C4 Model） - 软件架构可视化框架：Context-Container-Component-Code四层次架构描述
- Function Point（功能点） - 基于Vertical Slice分解的设计单元，连接需求与架构

---

## 🎯 统一命名权威标准
**⭐ 以下为权威引用基准，确保系统一致性**

> 💡 **维度理解**: 以下文档结构描述重点体现L1维度特征(快速、简洁、基础)，具体文件组织可灵活适配项目需要

<craft-design-req1-l1>
**精工设计_要求1_文档体系** L1精工设计：

<document-organization>
> **⭐ 权威来源**:
> - Artifact定义、PREFIX清单及标准托管文件: `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` Section 1.6
> - L1级别推荐托管映射: `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` Section 3.2
>
> 以下为L1-DESIGN阶段的标准维度定义和文档组织指引

**📋 受众定位约束**（DESIGN阶段质量标准）：
- **主要读者**: 技术主管/架构师/PM（理解业务+技术概念）
- **语言要求**: 80%业务语言 + 20%技术概念
- **可读性标准**: PM能理解"做什么"，技术主管能理解"怎么做的思路"

**🚫 严格禁止的过度技术化内容**：
- **过程式代码**（函数调用、类方法、执行步骤） ← ⚠️ 硬性约束
- 具体技术参数（JWT配置、数据库字段类型、端口号）
- 框架API调用示例（AuthService.authenticate()、express.Router()）
- 技术命令和工具（npm命令、bash脚本、SQL语句）
- 过度技术化的架构图（UML类图、时序图）

**✅ 推荐的技术概念表达**：
- 高层架构概念（前后端分离、微服务架构、三层架构）
- 业务组件划分（用户模块、任务模块、权限系统）
- 数据流向描述（用户请求→系统处理→结果返回）
- 技术选择理由（从业务角度解释为什么选择某技术）
- **声明式代码**（接口契约、数据结构、配置文件） ← ✅ 容许使用

**⚖️ 平衡原则**：
- 技术术语必须配业务解释
- 设计决策必须说明业务价值
- **技术术语密度 ≤ 20%**（DESIGN阶段约束）

🎯 **核心维度特征**（必须遵循）：
L1必须体现"快速简洁，独立关联"的本质特征
- **复杂度控制**：最小化依赖，独立文档设计，少量交叉引用
- **协作特征**：支持C1-CONFIRM模式("你看着办")，快速决策优先
- **质量标准**：MVP价值优先，轻量级表达，避免过度复杂结构

📋 **推荐实施方案**（可参考调整）：
**⭐ L1-STREAMLINED 设计文档组织架构 - 创建design时的核心指导**：
```
design/                         # 设计文档根目录（独立文档少量关联）
├── [vertical_slice_file]           # Vertical Slice定义（DESIGN起点）
├── [technical_acceptance_file]     # Technical Acceptance技术验收
├── [function_point_file]           # Function Point功能点分解（VS→FP转化）
├── [architecture_file]             # 系统架构
├── [api_design_file]              # API设计
├── [data_model_file]              # 数据模型
└── [component_design_file]         # 组件概念框架（智能适配：前端→UI组件，后端→服务组件）
```

**文档组织标准**：适量核心文档（通常对应7个维度），具体数量取决于维度覆盖需要
**L1阶段对比说明**：
- REQUIREMENTS/IMPLEMENTATION/TASK_PLANNING：通常对应3-4个核心维度
- DESIGN：通常对应7个核心维度 - 因需VS+TAC+FP+architecture+api+data+component完整覆盖端到端设计链路与追溯链
- 合理性：DESIGN作为需求到实现的转换枢纽，需要更完整的维度覆盖支撑追溯链（US→VS→TAC→FP→COMP）
**策略定位**：每个独立文档对应核心设计关注点
**核心七文档**：[vertical_slice_file]、[technical_acceptance_file]、[function_point_file]、[architecture_file]、[api_design_file]、[data_model_file]、[component_design_file]（其中component_design_file实现项目类型智能适配）
**质量标准**：文档组织最优化，关联逻辑最清晰，避免过度复杂结构
**可选扩展**：可增加[deployment_file]或合并策略（保持独立文档少量关联特征）
**多角色协作约束**：L1-STREAMLINED精工设计策略重点确保PM/Dev能够快速理解设计意图，减少沟通成本，避免复杂技术术语，采用直观的设计表达便于快速决策和执行，优先体现快速原型价值和MVP场景，技术细节服务于快速交付目标，重点使用PM和Dev都能理解的简洁术语，确保独立文档关联复杂度控制清晰可执行

**📋 文档生产次序**：[vertical_slice_file] → [technical_acceptance_file] → [function_point_file] → [architecture_file] → [api_design_file] → [data_model_file] → [component_design_file]
**次序原因**：Vertical Slice优先生产，Technical Acceptance验收VS技术路径，Function Point基于VS分解功能点（source_vs引用VS-<SN>-NNN），后续架构/API/数据/组件设计基于FP展开

📁 **核心文档组织维度说明** (L1-STREAMLINED特征): 以下帮助理解占位符背后的文件组织思考维度，具体文件组织可灵活适配项目需要

**维度总述**：
- **7个必需维度**：维度1-7（VS/TAC/FP/Architecture/API/Data/Component）是L1-DESIGN的核心维度，必须覆盖
- **1个可选维度**：维度8（Deployment）根据项目需要选择，可合并到Architecture
- **泛化原则**：维度是思考框架，文件数量/组织形式灵活适配（单文件/多文件/目录/合并）

**文档组织原则**:
- **维度优先**: 必需的是覆盖核心维度，文件组织形式灵活
- **按阶段分目录**: requirements/design/implementation/task_planning
- **按粒度分层**: 核心文档放根目录，细节文档可放子目录或拆分文件
- **命名规范**: snake_case，语义化文件名
- **关联管理**: 使用相对路径引用，保持文档间关联清晰
- **灵活适配**: 内容少时合并文档，内容多时拆分文件（如`xxx_part1.md`），复杂时建子目录

**维度1: Vertical Slice维度 (必需)**
- **对应占位符**: `[vertical_slice_file]`
- **参考示例**: `vertical_slices.md` 或 `value_paths.md`
- **维度职责**: 从User Story提炼用户成功状态，定义端到端价值路径（前端交互/数据流转/后端处理/结果反馈）
- **文档组织方式**:
  - 单文件形式: `vertical_slices.md`
  - 多文件形式: `vertical_slices_part1.md`, `vertical_slices_part2.md` (VS多时)
  - 目录结构形式: `vertical_slices/core.md`, `vertical_slices/auxiliary.md`
  - 合并文档形式: 作为需求响应文档的"价值切片"章节
- **内容要求**: VS Front Matter（id/sn/source_us）、user_success、value_path四向度
- **L1特征**: 优先单文件，聚焦核心价值切片
- **追溯链关键**: VS通过source_us字段引用US-<SN>-NNN，建立REQUIREMENTS→DESIGN桥梁

**维度2: Technical Acceptance维度 (必需)**
- **对应占位符**: `[technical_acceptance_file]`
- **参考示例**: `technical_acceptance.md` 或 `tech_criteria.md`
- **维度职责**: QA/架构师视角验收VS技术实现质量，关注性能/安全/可靠性
- **文档组织方式**:
  - 单文件形式: `technical_acceptance.md`
  - 多文件形式: `technical_acceptance_part1.md`, `technical_acceptance_part2.md` (TAC多时)
  - 目录结构形式: `technical_acceptance/performance.md`, `technical_acceptance/security.md`
  - 合并文档形式: 作为vertical_slice文档的"技术验收"章节
- **内容要求**: TAC Front Matter（id/sn/source_vs）、Given-When-Then格式、技术指标
- **L1特征**: 优先单文件或合并到VS文档
- **追溯链关键**: TAC通过source_vs字段引用VS-<SN>-NNN，验证技术路径

**维度3: Function Point维度 (必需)**
- **对应占位符**: `[function_point_file]`
- **参考示例**: `function_points.md` 或 `feature_breakdown.md`
- **维度职责**: 基于VS的value_path分解功能点，建立VS→FP追溯链
- **文档组织方式**:
  - 单文件形式: `function_points.md`
  - 多文件形式: `function_points_part1.md`, `function_points_part2.md` (FP多时)
  - 目录结构形式: `function_points/core.md`, `function_points/auxiliary.md`
  - 合并文档形式: 作为vertical_slice文档的"功能点分解"章节
- **内容要求**: FP Front Matter（id/sn/source_vs）、value_path_mapping、core_logic、input_output
- **L1特征**: 优先单文件，聚焦核心功能点
- **追溯链关键**: FP通过source_vs字段引用VS-<SN>-NNN，为IMPLEMENTATION阶段提供基础

**维度4: 系统架构维度 (必需)**
- **对应占位符**: `[architecture_file]`
- **参考示例**: `architecture.md` 或 `system_design.md`
- **维度职责**: 记录系统整体架构和技术选型
- **文档组织方式**:
  - 单文件形式: `architecture.md`
  - 多文件形式: `architecture_part1.md`, `architecture_part2.md` (内容多时)
  - 目录结构形式: `architecture/overview.md`, `architecture/tech_stack.md`
  - 合并文档形式: 作为设计总览文档的"架构"章节
- **内容要求**: 系统分层、技术栈、部署架构
- **L1特征**: 优先单文件，保持简洁清晰

**维度5: API设计维度 (必需)**
- **对应占位符**: `[api_design_file]`
- **参考示例**: `api_design.md` 或 `api_spec.md`
- **维度职责**: 记录系统接口设计和契约定义
- **文档组织方式**:
  - 单文件形式: `api_design.md`
  - 多文件形式: `api_design_part1.md`, `api_design_part2.md` (接口多时)
  - 目录结构形式: `api/rest_api.md`, `api/graphql.md`
  - 合并文档形式: 作为架构文档的"API"章节
- **内容要求**: 接口列表、请求响应格式、错误码
- **L1特征**: 优先单文件或合并到架构文档

**维度6: 数据模型维度 (必需)**
- **对应占位符**: `[data_model_file]`
- **参考示例**: `data_model.md` 或 `database_schema.md`
- **维度职责**: 记录数据结构和实体关系
- **文档组织方式**:
  - 单文件形式: `data_model.md`
  - 多文件形式: `data_model_part1.md`, `data_model_part2.md` (实体多时)
  - 目录结构形式: `data_model/entities.md`, `data_model/relationships.md`
  - 合并文档形式: 作为架构文档的"数据模型"章节
- **内容要求**: 实体定义、字段说明、关系映射
- **L1特征**: 优先单文件或合并

**维度7: 组件设计维度 (必需)**
- **对应占位符**: `[component_design_file]`
- **参考示例**: `component_design.md` 或 `ui_components.md` (前端) / `module_design.md` (后端)
- **维度职责**: 记录组件/模块的概念框架和职责划分
- **文档组织方式**:
  - 单文件形式: `component_design.md`
  - 多文件形式: `component_design_part1.md`, `component_design_part2.md` (组件多时)
  - 目录结构形式: `components/ui.md`, `components/business.md`
  - 合并文档形式: 作为架构文档的"组件设计"章节
- **内容要求**: 组件列表、职责说明、交互关系
- **L1特征**: 优先单文件或合并，概念层级即可
- **项目类型适配**: 前端GUI项目→UI组件设计，后端项目→模块设计，全栈项目→前后端组件

**维度8: 部署设计维度 (可选)**
- **对应占位符**: `[deployment_file]`
- **参考示例**: `deployment.md`
- **维度职责**: 记录部署架构和运维策略
- **文档组织方式**: 单文件或合并到架构文档
- **L1特征**: 通常合并到架构文档或简单单文件
</document-organization>
<directory-hierarchy>**策略定位**：平面目录支持独立文档的简单组织
**精工设计指导**：design/直接存放核心文件，无子目录，平面结构或单层目录支持独立文档快速组织和导航
**质量标准**：目录结构简洁清晰，便于快速定位和理解，支持独立文档的基础分类</directory-hierarchy>  
<categorization-granularity>**设计架构核心定位**：独立文档少量关联 - 用独立文档少量关联的清晰组织实现设计管理→AI快速决策最简关联方案→设计质量提升（核心工作做简洁），C1-CONFIRM模式下AI快速决策最简关联方案，用户信任确认即可，"你看着办" - 用户信任AI的关联决策，重点在快速交付而非完美关联

**L1分类粒度策略**：粗分类文档间保持独立，少量交叉引用
- **追溯链引用**：[vertical_slice_file]→source_us引用US，[technical_acceptance_file]→source_vs引用VS，[function_point_file]→source_vs引用VS
- **技术设计引用**：[architecture_file]引用[api_design_file]/[component_design_file]/[function_point_file]，[api_design_file]引用[data_model_file]，[component_design_file]基于[function_point_file]展开
- **智能适配**：[component_design_file]实现项目类型智能适配（前端→UI组件，后端→服务组件）

**需求承接策略**：基于REQUIREMENTS阶段的设计响应：基于User Story和Vertical Slice的快速设计体系，建立US→VS→TAC→FP→组件概念框架链路；
**简化追踪格式**："US-<SN>-NNN/User Story → VS-<SN>-NNN/Vertical Slice → TAC-<SN>-NNN/Technical Acceptance → FP-<SN>-NNN/Function Point → COMP-<SN>-NNN/组件概念框架 [端到端价值追踪]"；
**快速管理**：US变更→VS快速调整→TAC技术验收→FP设计更新→组件概念框架直接更新

**精工设计建议**：
- **[vertical_slice_file]**: Vertical Slice定义文档 - 从User Story提炼用户成功状态，定义value_path（VS的价值路径四向度：Value Path Four Dimensions，包含前端交互/数据流转/后端处理/结果反馈），端到端价值切片跨层穿透技术栈，是DESIGN阶段的起点和核心；文档组织：可按功能模块分组或单文件列表，每个VS独立成块；参考下方"L1 Vertical Slice生产机制"
- **[technical_acceptance_file]**: Technical Acceptance Criteria技术验收文档 - QA/架构师视角验收VS技术实现，使用Given-When-Then格式关注性能/安全/质量指标，区别于REQUIREMENTS的AC业务验收；文档组织：与VS对应，可合并到vertical_slice_file或独立文档；参考下方"L1 Technical Acceptance Criteria生产机制"
- **[function_point_file]**: Function Point功能点分解文档 - 基于VS的value_path分解功能点，建立VS→FP追溯链，为IMPLEMENTATION阶段提供实施基础；文档组织：可按模块分组或单文件列表，每个FP包含value_path_mapping；参考下方"L1 Function Point转化机制"
- **[architecture_file]**: 系统架构独立描述 - 快速理解导向，系统整体架构独立说明（最多3-4个核心组件），使用PM和Dev都能理解的简洁术语；简化引用："详见[api_design_file]接口定义"、"参考[data_model_file]数据结构"、"组件概念框架见[component_design_file]"、"功能点分解见[function_point_file]"，避免复杂技术术语；原型价值体现：突出MVP核心架构价值，避免复杂的组件间依赖图，保持架构清晰直观
- **[api_design_file]**: API设计独立规范 - API接口独立定义，避免过度引用架构细节，可简单说明与数据模型的对应关系，重点突出API的独立可用性和简洁性
- **[data_model_file]**: 数据模型独立定义 - 数据结构独立描述，便于后续开发参考，避免复杂的关联约束，保持模型简单直接，可被API文档简单引用，但本身保持独立完整
- **[component_design_file]**: 组件概念框架智能适配 - 根据项目类型智能适配内容：前端GUI项目→UI组件概念框架模板，后端项目→服务组件概念框架模板，保持设计独立性但与架构文件形成简单关联；组件设计基于FP功能点展开

**🎯 L1 Vertical Slice生产机制（US驱动）**：

**User Story→Vertical Slice转化体系**：
- **转化原则**：
  - 基于User Story的As-Want-So提炼用户成功状态（user_success）
  - 定义value_path（VS的价值路径四向度：Value Path Four Dimensions）：前端交互 + 数据流转 + 后端处理 + 结果反馈
  - 端到端价值切片，跨层穿透技术栈
  - 快速原型导向，聚焦MVP核心价值路径

- **Vertical Slice标准格式**：
  ```yaml
  ---
  id: VS-<SN>-NNN           # 例如: VS-MAIN-001, VS-AUTH-002
  sn: <SN>                  # 必须与source_us的SN一致
  source_us: US-<SN>-NNN    # 派生来源（必填）
  ---

  user_success: [用户成功状态 - 从US的"So that"提炼]
  value_path:
    - 前端交互: [用户界面操作和交互流程]
    - 数据流转: [前后端数据交换和传递]
    - 后端处理: [业务逻辑处理和状态变更]
    - 结果反馈: [用户可见结果和状态呈现]
  ```

- **转化示例**：US-AUTH-001 → VS-AUTH-001（user_success + value_path四向度）

**🎯 L1 Technical Acceptance Criteria生产机制（VS技术验收）**：

**Vertical Slice→TAC转化体系**：
- **转化原则**：
  - TAC是QA/架构师视角的技术验收标准（区别于AC的业务验收）
  - 验收VS的value_path（VS的价值路径四向度：Value Path Four Dimensions）技术实现质量
  - 使用Given-When-Then格式（技术视角，非用户视角）
  - 关注性能、安全、可靠性等技术指标

- **TAC标准格式**：
  ```yaml
  ---
  id: TAC-<SN>-NNN          # 例如: TAC-MAIN-001, TAC-AUTH-002
  sn: <SN>                  # 必须与source_vs的SN一致
  source_vs: VS-<SN>-NNN    # 派生来源（必填）
  ---

  Given [技术前置条件 - 架构组件就绪状态]
  When [技术操作 - value_path（VS的价值路径四向度：Value Path Four Dimensions）技术实现]
  Then [技术验收标准 - 性能/安全/质量指标]
  And [端到端技术一致性验证]
  ```

- **转化示例**：VS-AUTH-001 → TAC-AUTH-001（Given-When-Then技术验收）

**AC vs TAC 关键区别**：
- **AC (REQUIREMENTS阶段)**: PM/BA定义，业务验收，验证US业务需求满足度
  - 示例: "Given 用户在登录页，When 输入正确凭证，Then 成功登录并看到Dashboard"
- **TAC (DESIGN阶段)**: QA/架构师定义，技术验收，验证VS技术路径质量
  - 示例: "Given 认证服务就绪，When 触发认证流程，Then API响应<500ms且Token安全存储"

**🎯 L1 Function Point转化机制（Vertical Slice驱动）**：

**Vertical Slice→Function Point转化体系**：
- **转化原则**：
  - 基于Vertical Slice的value_path（VS的价值路径四向度：Value Path Four Dimensions）分解Function Point
  - 端到端价值切片驱动功能点识别
  - 快速原型导向，最小可行架构优先

- **Function Point标准格式**：
  ```yaml
  ---
  id: FP-<SN>-NNN           # 例如: FP-MAIN-001, FP-AUTH-002
  sn: <SN>                  # 必须与source_vs的SN一致
  source_vs: VS-<SN>-NNN    # 派生来源（必填）
  ---

  name: 功能点名称
  value_path_mapping:
    - 前端交互 → 前端组件需求
    - 数据流转 → 数据模型/API需求
    - 后端处理 → 业务逻辑组件需求
    - 结果反馈 → 状态管理/UI反馈需求
  core_logic: 核心业务逻辑
  input_output: 输入输出简述
  ```

- **转化示例**：
  ```yaml
  Vertical Slice "用户通过登录表单提交达成认证成功状态" (VS-MAIN-001)

  → Function Point:
  ---
  id: FP-MAIN-001
  sn: MAIN
  source_vs: VS-MAIN-001
  ---

  name: 用户认证功能点
  value_path_mapping:
    - 用户界面: 登录表单界面
    - 数据传递: 登录信息验证请求
    - 系统处理: 用户身份验证服务
    - 用户反馈: 状态记录与界面跳转
  ```

**快速原型导向**：Function Point精简只保留MVP核心要素，直接指导组件概念框架
**追溯原则**：FP通过source_vs字段建立与Vertical Slice的明确派生链，无需额外的related_us字段

**L1特异性检查**：是否避免了复杂的文档间依赖？是否用少量引用覆盖核心关联需要？是否便于快速理解和TDD准备？

**策略定位**：用独立文档少量关联的清晰组织实现设计管理，C1-CONFIRM模式下AI快速决策最简关联方案
**精工设计指导**：核心组件独立说明，简单关联，避免复杂依赖？接口独立定义，关键实体识别，关系简单分类？基础模型（核心/关联/辅助）简单管理？
**质量标准**：独立文档少量关联，每个设计决策来源清晰，支持C1-CONFIRM模式的用户快速信任确认</categorization-granularity>
<interconnection-complexity>**策略定位**：采用独立文档为主的清晰关联体系，每个文档最多2-3个引用点，避免过度依赖和交叉引用，专注快速设计价值交付

**具体操作指导**：
- **[architecture_file]引用规范**: "详见 [api_design_file] 第X节接口定义"、"参考 [data_model_file] 核心实体Y"、"组件概念框架见 [component_design_file]"、"功能点分解见 [function_point_file]"
- **[api_design_file]引用规范**: "基于 [data_model_file] 实体Z设计"、"映射到 [architecture_file] 组件A"
- **[data_model_file]引用规范**: "支撑 [api_design_file] 接口需求"、"对应 [architecture_file] 数据层"
- **[function_point_file]引用规范**: "基于 [vertical_slice_file] 的VS-<SN>-NNN分解"、"指导 [component_design_file] 组件设计"
- **[component_design_file]引用规范**: "基于 [architecture_file] 组件A设计"、"实现 [function_point_file] 功能点FP-<SN>-NNN"
- **引用密度控制**: 每个文档≤3个引用点，每个引用≤1行描述
- **独立性验证**: 删除引用后文档仍可理解80%内容

**🎯 端到端价值链一致性保障**：

**Vertical Slice → 架构设计映射**：
- **前端交互** → 前端组件设计(UI/UX组件)
- **数据流转** → API设计 + 数据模型设计
- **后端处理** → 业务逻辑组件/服务设计
- **结果反馈** → 状态管理 + 用户反馈机制设计

**一致性检查点**：
- [ ] 前端组件设计覆盖VS的"前端交互"需求
- [ ] API设计支持VS的"数据流转"需求
- [ ] 业务组件实现VS的"后端处理"逻辑
- [ ] 反馈机制满足VS的"结果反馈"要求

**L1策略**：减少中间转换层，VS→架构尽量直接映射；接口强类型；使用标准化数据格式。

**AI执行检查点**：
1. 引用格式是否统一简洁？
2. 文档独立性是否保持？  
3. 关联逻辑是否清晰可追踪？
4. VS的价值路径四向度（Value Path Four Dimensions）到架构组件的映射是否完整？

**质量标准**：独立性检验通过，关联逻辑清晰可传递，端到端价值链一致性明确，支持C1-CONFIRM模式快速理解

**业务引用原则**：
- 文档间引用使用业务术语，避免技术ID
- 示例："基于[用户登录功能]的设计" 而非 "基于API-AUTH-001"
- 引用说明需包含业务上下文
</interconnection-complexity>
<content-depth>**策略定位**：每个独立文档保持核心内容，避免冗余引用
**精工设计指导**：轻量级内容，概要了解（需满足端到端检查点的基础覆盖要求），每个文档控制篇幅，核心设计信息突出，重点关注技术调研工作充实度的完整记录。协同建议：每个独立文档保持核心内容，避免冗余引用
**平衡原则**：内容精简但检查点完整，用简洁表达确保VS的价值路径四向度（Value Path Four Dimensions）映射清晰
**质量标准**：技术调研的充分性比文档数量更重要，架构决策的合理性比结构完美更关键</content-depth>
<formalization-level>**策略定位**：独立文档结构化但引用格式简洁
**精工设计指导**：自由格式，基础Markdown，统一模板，标准标题，引用清晰但不复杂。协同建议：独立文档结构化但引用格式简洁
**⭐ Artifact ID分配**: 保持现有artifact ID不变(确保引用完整性)，仅对新增artifact扫描宿主文件同PREFIX+SN，取max序号+1分配新ID
**质量标准**：可用性比完美更重要，格式标准化支持协作效率和快速交付

**L1精工设计执行技巧**：
1. **架构设计** - 生成[architecture_file]，包含系统核心组件和简单引用关系，MVP导向
2. **API设计** - 生成[api_design_file]，按功能模块组织REST接口，包含请求响应示例
3. **数据模型** - 生成[data_model_file]，定义核心实体、字段和关系
4. **功能点分解** - 生成[function_point_file]，基于VS分解FP，建立追溯链
5. **质量门禁机制** - 核心检查点：独立关联复杂度控制→设计可行性→快速实施性，协作流程：AI分析设计需求→提出7文档独立关联方案→用户快速浏览确认核心设计思路→立即执行生产，通过标准："核心设计覆盖完整吗？7文档关联简单明确吗？追溯链完整吗？能立即启动TDD吗？"

**认知补强要点**：C1-CONFIRM模式协作精髓"你看着办" = AI主推独立关联方案 + 用户快速确认 + 高效执行，L1核心特征：快速迭代，聚焦核心价值交付，信任AI判断，减少反复确认，优先速度，容忍合理妥协，适用场景：任意规模团队，偏好快速验证想法，独立关联核心价值：零关联学习成本，零管理负担，最大效率覆盖核心设计关联要素，L1级快速交付哲学：速度为王，可用胜过完美，行动胜过分析，独立关联即可支撑，选择L1的适用场景：任意规模团队，偏好快速迭代验证想法的用户的最佳选择

**结构准确性检查**：是否采用L1标准的七文档独立关联结构？是否包含[vertical_slice_file]、[technical_acceptance_file]、[function_point_file]、[architecture_file]、[api_design_file]、[data_model_file]、[component_design_file]七个核心文档？是否建立完整的US→VS→TAC→FP→COMP追溯链？</formalization-level>

**⚡ 执行技巧集成**
**L1精工设计执行技巧**：
1. **架构设计理解** - [architecture_file]包含系统核心组件(3-4个)，简单引用[api_design_file]主要接口和[data_model_file]核心实体，重点突出MVP架构价值
2. **API设计规范** - [api_design_file]按功能模块组织REST接口，每个接口包含请求响应示例，引用[data_model_file]中的数据结构定义
3. **数据模型管理** - [data_model_file]定义核心实体、关联关系，包含字段类型和约束，为API设计提供数据结构支撑
4. **功能点分解** - [function_point_file]基于[vertical_slice_file]的VS分解FP，建立source_vs追溯，为IMPLEMENTATION提供基础
5. **质量门禁机制** - 核心检查点：7文档独立关联→追溯链完整→设计可行性→快速实施性，协作流程：AI分析设计需求→提出7文档独立关联方案→用户快速浏览确认核心设计思路（快速确认）→立即执行生产，通过标准："[vertical_slice_file]、[technical_acceptance_file]、[function_point_file]、[architecture_file]、[api_design_file]、[data_model_file]、[component_design_file]七文档覆盖完整？追溯链US→VS→TAC→FP→COMP完整？文档间关联简单明确？能立即启动TDD吗？"

**认知补强要点**：C1-CONFIRM模式协作精髓"你看着办" = AI主推7文档独立关联方案 + 用户快速确认 + 高效执行，L1核心特征对齐：质量控制偏好（快速迭代MVP，聚焦核心价值交付）、协作风格（信任AI判断，"够用就行"，减少反复确认）、交付节奏（优先速度，容忍合理妥协）、适用场景（任意规模团队，偏好快速验证想法），独立关联核心价值：零学习成本（[vertical_slice_file]→[technical_acceptance_file]→[function_point_file]→[architecture_file]→[api_design_file]→[data_model_file]→[component_design_file]简单引用链），零管理负担，最大效率覆盖核心设计要素+追溯链支撑，L1级快速交付哲学：速度为王，可用胜过完美，行动胜过分析，7文档独立关联+完整追溯链即可支撑TDD启动，选择L1的适用场景：偏好快速迭代验证想法的用户的最佳选择
</craft-design-req1-l1>

<craft-design-req2-l1>
**精工设计_要求2_架构表达** L1精工设计：

<architecture-structure>**架构组织策略**：基于KISS原则的简洁直观系统架构说明，3-4个核心组件快速原型验证
**执行要点**：
- KISS原则优先：保持架构/API简单直观，避免复杂抽象和过度设计
- 核心组件识别：专注MVP最小可行产品的核心架构价值
- 简单明了：使用PM和Dev都能理解的简洁术语
- 快速验证：架构设计支持快速原型开发和迭代
- 单一职责基础：每个组件专注一个明确的业务功能
**与Vertical Slice协同**：
- KISS约束主要针对架构层次和API接口设计
- Vertical Slice的value_path（VS的价值路径四向度：Value Path Four Dimensions）是需求维度，可映射到3-4个核心架构组件
- 示例：前端交互+结果反馈需求 → UI组件层(1个架构组件)
        数据流转+后端处理需求 → 业务逻辑层(1个架构组件)
**方法论基础**：KISS原则导向设计 + 基础C4模型(Context-Container简化视图)
**质量标准**：架构遵循KISS原则，清晰简洁，满足核心需求，支持快速迭代验证</architecture-structure>
<component-definition>**组件定义策略**：基于KISS原则和单一职责的简洁组件划分，边界清晰，接口简单直观
**执行要点**：
- KISS原则：组件概念框架保持简单，避免复杂的抽象层
- 单一职责基础：每个组件专注一个明确的业务功能
- 边界清晰可测试：组件边界明确，便于单元测试
- 简化引用：使用简单的文档引用，避免复杂关联
- 直观命名：组件和接口命名符合直觉，无需解释

**L1 Function Point集成组件概念框架**：
- **Function Point→组件直映射**：每个Function Point直接对应1个核心组件，最大化开发效率
- **项目类型智能适配**：
  - **前端GUI项目**：Function Point→UI组件 + 状态管理 → IMPLEMENTATION阶段交互指导
    - **⭐ 逻辑+视觉混合指导**：基于VS的value_path提供组件的功能逻辑与视觉设计统一描述（L1简化快速）
    - **逻辑指导**：组件核心功能、基础状态管理的简化描述
    - **视觉指导**：基础布局结构、核心交互效果的快速原型描述
  - **后端项目**：Function Point→服务组件 + API设计 → IMPLEMENTATION阶段测试指导
- **快速原型优化**：简化Function Point内容，直接指导组件实现

**质量标准**：组件概念框架简洁清晰，边界明确，支持快速开发和智能适配机制</component-definition>
<interface-design>**接口设计策略**：基于KISS原则的简洁直观API设计，支持快速原型开发和迭代
**执行要点**：
- 接口设计简洁直观，避免不必要的复杂性
- 专注MVP核心功能，优先实现关键价值
- 采用标准化设计模式和通用数据格式
- 提供基本的错误处理和状态反馈
- 保持单一职责，每个接口专注一个明确功能
**质量标准**：接口设计简单易用，文档清晰完整，支持快速集成和测试实现</interface-design>
</craft-design-req2-l1>

<craft-design-req3-l1>
**精工设计_要求3_技术决策** L1精工设计：

<decision-framework>L1决策框架和评估方法：技术选型原则、评估标准、决策流程，重点关注技术决策充实度：技术选型是否基于充分调研？关键决策是否有明确依据？技术方案是否考虑了主要风险？格式保持简单：核心技术选型说明，简单决策记录格式，避免复杂决策树便于快速执行。</decision-framework>
<alternative-evaluation>L1备选方案分析对比：方案对比分析、优缺点评估、选择依据，决策质量优先：技术选型的合理性比记录格式更重要，决策依据的充分性比文档完美更关键。保持简单的比较格式，重点突出技术选型的合理性和快速可行性。</alternative-evaluation>
<constraint-management>L1约束管理和权衡取舍：技术约束识别、权衡决策、妥协管理，重点关注设计工作充分性：技术调研是否足够支撑架构决策？设计方案是否能满足核心需求？关键技术风险是否已识别？确认机制保持简单：C1-CONFIRM模式的单检查点验证，"你看着办"的快速确认机制，快速浏览确认核心设计思路。</constraint-management>
</craft-design-req3-l1>

<craft-design-req4-l1>
**精工设计_要求4_质量标准** L1精工设计：

<design-coherence>**连贯性检查要点**：核心设计覆盖完整性，文档关联简单明确，架构一致性和逻辑连贯性，采用L1标准的核心文档独立关联结构。
**追溯强制要求**：Function Point必须包含source_vs字段（格式：VS-<SN>-NNN），建立与DESIGN阶段Vertical Slice的明确追溯链路</design-coherence>
<quality-assurance>**质量保证机制**：独立关联复杂度策略可执行性，架构表达标准实施质量，C1-CONFIRM模式的快速验证流程。

**演进支持整合内容**：关联复杂度管理的清晰策略，独立文件组织的实用方案，支持扩展性和维护友好性，体现L1快速交付特征。</quality-assurance>
<stage-verbatim-directive>
**【设计阶段L1 MD文件的质量控制】**

- **适用范围**: 仅对spec/目录下非_前缀的MD文件生效（排除_开头的目录和文件）
- **长度控制**: 400-500行限制，超出按模块拆分
- **补丁保护**: 修改后检查基础完整性要求，核心一致性保护
- **质量预防**: 基础信息密度监控，结构清晰保持，术语统一验证
- **阶段特异**: 架构连贯性，技术决策合理性

**自检清单**:
  - □ 内容组织是否简洁清晰？
  - □ 文档结构是否便于快速理解？
  - □ 架构设计是否连贯清晰？
  - □ 技术决策是否合理可行？

- **修正触发**: 发现问题立即停止，然后让Human-in-the-loop，建议审查、整理和修复
</stage-verbatim-directive>
</craft-design-req4-l1>
