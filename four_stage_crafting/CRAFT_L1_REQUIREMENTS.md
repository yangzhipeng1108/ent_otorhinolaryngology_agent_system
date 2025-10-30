# CRAFT_L1_REQUIREMENTS 需求精研指导文档

> 🎯 **系统执行指令**: 需求收集分析场景→REQUIREMENTS阶段需求工作充实引导(L1)，快速交付导向
> 📊 **核心聚焦**: 需求收集工作充实指导 - 业务理解深化→需求挖掘全面→设计质量提升
> 📁 **级别特征**: L1-STREAMLINED (3±2核心文件，平面结构，轻量快速，快速迭代偏好，适用于任意规模团队)
> 🔧 **协作模式**: C1-CONFIRM模式("你看着办") - 系统提供思考框架→用户主导需求判断→快速确认执行
> ⚡ **体系定位**: 创意激发者，支撑脚手架生产+后期推敲，验收标准由four_stage_constraints定义
> 🏗️ **文档架构**: MD+XML混合设计，核心指导内容全部封装在XML标记内，实现LLM精确提取和Level间无缝切换
> 🔗 **命名规范权威引用**:
> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L1 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` (必填 artifacts, 灵活模式, 验收标准)
>
> 🔗 **AICodingAgent规范权威引用**:
> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L1宪章**: `../agentic_spec/SPEC_ACA_L1_CHARTER.md` - L1质量标准 (4-6检查点, 通过率≥95%, 单层追溯)

## 🎯 XML标记体系说明

### 第一级标记 (craft-requirements-req[1-4]-l1)
**目的**: 包含L1级别REQUIREMENTS阶段的**完整指导内容**，作为LLM提取和Level切换的**整体单位**

### 第二级标记 (完整说明)

#### 6个标准维度子标签 (所有阶段通用 - 要求1):
1. `<document-organization>` - **文档组织架构策略**: 该级别需要多少文档、如何配置文档结构、基本协作约束、目录结构展示，User Story业务需求为核心
2. `<directory-hierarchy>` - **目录层级组织**: 文件夹结构、层级深度控制、文件布局规范、导航方式设计  
3. `<categorization-granularity>` - **分类粒度策略** [REQUIREMENTS主攻]: 如何分类需求内容、分类细度控制、组织逻辑设计，User Story业务需求为核心
4. `<interconnection-complexity>` - **关联复杂度管理**: 文档间引用关系、依赖复杂度、交叉引用策略
5. `<content-depth>` - **内容深度策略**: 每个文档写多少内容、详细程度把握、充实度标准定义
6. `<formalization-level>` - **形式化程度**: 模板规范度、结构严格性、AI执行技巧、认知要点集成

#### REQUIREMENTS阶段专项子标签:
**要求2_需求格式** (3个子标签):
- `<requirement-structure>` - **需求结构组织方式**: 用户故事格式、验收标准格式、需求分组方法
- `<format-standards>` - **格式标准和模板规范**: 模板设计、标题规范、文档格式要求  
- `<expression-quality>` - **表达质量控制**: 表达清晰度、完整性检查、质量把关方法

**要求3_验收标准** (3个子标签):
- `<validation-approach>` - **验证方法和策略**: 如何验证需求、验证时机、验证流程设计
- `<acceptance-criteria>` - **验收标准定义**: 简单描述性验收条件、完成定义
- `<testing-alignment>` - **测试对齐机制**: 与测试用例对齐、可测试性保证、TDD准备

**要求4_质量标准** (3个子标签):
- `<completeness-control>` - **完整性控制**: 需求遗漏检查、覆盖度验证、全面性保证
- `<consistency-check>` - **一致性检查**: 需求间一致性、术语统一、逻辑一致
- `<stage-verbatim-directive>` - **逐字传递指令**: 对下一阶段的逐字传递与接口要求

## 🤝 多角色协作约束

> 📋 **快速原型原则**: L1-STREAMLINED需求精研策略必须支持快速迭代，确保原型友好和迭代效率
> 🚫 **基础简洁约束**: 避免过度复杂的需求分类，分类细度需适度简化，支持快速理解
> 💼 **原型导向平衡**: 平衡需求完整性与收集简洁性，确保基础分类粒度服务快速原型开发
> 🎯 **基础化表达**: 使用简洁清晰的基础术语，确保基础分类粒度便于理解和实现

## ⚠️ 重要原则澄清

> 🎯 **维度本质 > 表面形式**: L1/L2/L3的核心是约束复杂度的不同维度，不是具体的文件组织形式
> 📁 **文件/目录是表现**: 文件数量、目录结构只是维度的外在表现，重点是背后的指导价值和复杂度控制
> 🚫 **避免表面约束**: 不要被"平面结构"、"3±2文件"等表面描述约束，关注L1快速简洁的维度本质
> ✨ **指导性优先**: CRAFT是创意激发者，松耦合高内聚的指导性存在，而非行为约束者

## 🎯 统一命名权威标准
**⭐ 以下为权威引用基准，确保系统一致性**

> 💡 **维度理解**: 以下文档结构描述重点体现L1维度特征(快速、简洁、基础)，具体文件组织可灵活适配项目需要

<craft-requirements-req1-l1>
**需求精研_要求1_文档体系** L1需求精研：

<document-organization>
> **⭐ 权威来源**:
> - Artifact定义、PREFIX清单及标准托管文件: `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` Section 1.6
> - L1级别推荐托管映射: `../agentic_spec/SPEC_ARTIFACT_NAMING_L1_AUTHORITY.md` Section 3.2
>
> 以下为L1-REQUIREMENTS阶段的标准维度定义和文档组织指引

**📋 受众定位约束**（REQUIREMENTS阶段质量标准）：
- **主要读者**: PM/BA/客户（业务背景，无技术假设）
- **语言要求**: 100%业务语言，绝对避免技术术语
- **可读性标准**: 任何非技术背景人员都能理解文档内容

**🚫 严格禁止的技术术语**：
- 技术实现细节（数据库、API、前后端、服务器）
- 技术指标（响应时间<1s、性能参数、吞吐量）
- 技术术语（CRUD、Token、Session、JWT、接口、认证）
- 框架名称（React、Vue、Node.js、Express）
- 技术格式（JSON、HTTP、REST、请求/响应）
- **过程式代码**（函数调用、执行步骤、控制流程） ← ⚠️ 硬性约束

**✅ 推荐的业务语言**：
- 业务功能（用户可以登录、查看任务、添加信息）
- 业务流程（用户输入信息后看到确认消息）
- 业务概念（界面、系统、信息、状态）
- 业务价值（提高效率、方便管理、节省时间）

**技术术语密度 = 0%**（REQUIREMENTS阶段硬性要求）

🎯 **核心维度特征**（必须遵循）：
L1必须体现"快速简洁，独立关联"的本质特征
- **复杂度控制**：最小化依赖，独立文档设计，基础分类组织
- **协作特征**：支持C1-CONFIRM模式("你看着办")，快速迭代偏好
- **质量标准**：MVP价值优先，避免过度工程化

📋 **推荐实施方案**（可参考调整）：

**📊 L1 REQUIREMENTS 标准结构** - L1-STREAMLINED 需求文档组织架构 - 创建requirements时的核心指导：

**🎯 标准模式（US → AC 路径）**
```
requirements/                    # 需求文档根目录（基础分类组织）
├── [user_stories_file]              # User Story传统角色视角（必需，业务需求基础层）
├── [acceptance_criteria_file]        # Acceptance Criteria验收标准（必需，验收US的业务需求）
└── [constraints_file]               # 约束条件（必需）
```

**文档组织标准**：核心维度必须覆盖（US + AC + Constraints），具体文件组织可灵活适配
- **标准模式**: User Story + Acceptance Criteria + Constraints（3个核心维度，通常对应3个文档）
- **可选扩展**: 可增加业务目标或利益相关方维度（视项目需要）

**策略定位**：每个基础分类对应1个专门文档，US为业务需求基础，AC为业务验收标准
**核心artifacts**：
- **必需**: User Story（US）+ Acceptance Criteria（AC）+ Constraints
- **派生关系**: AC从US派生（source_us字段必填）
- **受众定位**: PM/BA主导，使用业务语言，避免技术化

**质量标准**：文档组织控制在合理范围内，分类逻辑最清晰，避免文档冗余
**多角色协作约束**：L1-STREAMLINED策略重点确保PM/BA能够快速掌握需求收集要点，使用平易近人的业务术语，采用直观的工作指导，优先体现MVP价值和核心用户场景，重点使用PM/BA都能理解的实用方法

**📋 文档生产次序**：[user_stories_file]（获得US ID） → [acceptance_criteria_file]（填写source_us，验收US的业务需求） → [constraints_file]（全局约束）
**次序原因**：数据依赖（source_us字段）+ 方法论纪律（AC验收业务需求，由PM定义业务验收标准更科学）

📁 **核心文档组织维度说明** (L1-STREAMLINED特征): 以下帮助理解占位符背后的文件组织思考维度，具体文件组织可灵活适配项目需要

**文档组织原则**:
- **维度优先**: 必需的是覆盖核心维度，文件组织形式灵活
- **按阶段分目录**: requirements/design/implementation/task_planning
- **按粒度分层**: 核心文档放根目录，细节文档可放子目录或拆分文件
- **命名规范**: snake_case，语义化文件名
- **关联管理**: 使用相对路径引用，保持文档间关联清晰
- **灵活适配**: 内容少时合并文档，内容多时拆分文件（如`xxx_part1.md`），复杂时建子目录

**维度1: User Story角色视角维度 (必需 - 业务需求基础)**
- **对应占位符**: `[user_stories_file]`
- **参考示例**: `user_stories.md`
- **维度职责**: 提供平易近人的角色功能视角，作为业务需求的基础层
- **文档组织方式**:
  - 单文件形式: `user_stories.md`（推荐）
  - 合并文档形式: 整合到`requirements.md`的主要章节
- **内容要求**:
  - Front Matter包含id + sn
  - As a [角色], I want [功能], So that [价值]格式
  - 平易近人，一般人容易明白的表述，使用业务语言
- **受众定位**: PM/BA主导，避免技术术语
- **L1特征**: 必需文档，优先单文件形式

**维度2: Acceptance Criteria验收标准维度 (必需 - 业务验收)**
- **对应占位符**: `[acceptance_criteria_file]`
- **参考示例**: `acceptance_criteria.md`
- **维度职责**: 验收US的业务需求完成度，由PM定义业务验收标准
- **文档组织方式**:
  - 单文件形式: `acceptance_criteria.md`（推荐）
  - 合并文档形式: 整合到`user_stories.md`的验收章节
  - 分组文件形式: `acceptance_auth.md`, `acceptance_business.md`（多域项目）
- **内容要求**:
  - Front Matter包含id + sn + source_us（派生来源，必填）← ⭐ source_us字段验收US业务需求
  - Given-When-Then格式验证业务需求完成度
  - 简单描述性验收条件，使用业务语言，避免技术细节
- **追溯链**: 从US派生（source_us字段建立1:多父子关系）
- **受众定位**: PM定义业务验收标准（非技术验收）
- **L1特征**: 优先单文件或合并到US文档

**维度3: 约束边界维度 (必需)**
- **对应占位符**: `[constraints_file]`
- **参考示例**: `constraints.md`
- **维度职责**: 明确需求边界和实现限制
- **文档组织方式**:
  - 单文件形式: `constraints.md`
  - 合并文档形式: 作为需求文档的"约束条件"章节
  - 分类文件形式: `tech_constraints.md`, `business_rules.md`
- **内容要求**: 技术约束、业务规则、用户体验约束
- **L1特征**: 优先单文件或合并

**维度4: 业务目标维度 (可选，0-2个扩展之一)**
- **对应占位符**: `[business_goals_file]`
- **参考示例**: `business_goals.md`
- **维度职责**: 业务价值和目标文档
- **文档组织方式**: 单文件或合并到其他文档
- **L1特征**: 通常合并到用户故事或单独简单文件

**维度5: 利益相关方维度 (可选，0-2个扩展之一)**
- **对应占位符**: `[stakeholder_file]`
- **参考示例**: `stakeholders.md`
- **维度职责**: 干系人和角色文档
- **文档组织方式**: 单文件或合并到其他文档
- **L1特征**: 通常合并或省略
</document-organization>

<directory-hierarchy>
**策略定位**：平面目录支持基础分类的简单组织  
**需求精研指导**：[requirements_dir]/直接存放核心文件，无子目录，保持扁平化结构  
**质量标准**：目录层级保持简洁，文件组织一目了然，便于快速定位
</directory-hierarchy>

<categorization-granularity>
**分类策略**：基础文档分类，3个核心文件覆盖需求要素，避免过度分层，专注快速交付

**🎯 标准模式（3个核心文件）**：
- User Story业务需求：按业务域分组（SN划分），平面结构，无复杂层次
- Acceptance Criteria验收标准：按US分组，每个US对应1个或多个AC，用Given-When-Then表达
- 约束条件基础分类：技术约束、业务规则、用户体验

**💡 应用集成识别**（条件触发）：
- 思考：用户需要入口访问功能吗？（Web/移动/桌面/CLI）
- 如需要：创建导航US描述用户如何访问各项功能

**执行要点**：
- US组织原则：每个US保持独立，使用业务语言，平易近人
- AC派生原则：每个AC明确标注source_us，建立1:多父子关系，验收US业务需求
- PM/BA主导：使用业务术语，避免技术化，由PM定义业务验收标准
- 避免复杂的层次嵌套关系，保持平面结构

**质量标准**：分类简单明确，追溯链清晰，业务语言表达，便于PM/BA快速理解
</categorization-granularity>

<interconnection-complexity>
**策略定位**：基础分类文档间保持独立，通过ID追溯链关联，避免复杂交叉引用

**🔗 L1追溯链关系**：
- `[user_stories_file]` ← 追溯基准，业务需求基础层
- `[acceptance_criteria_file]` → 引用 `[user_stories_file]`（通过source_us字段派生）
- `[constraints_file]` ← 独立文档，可被其他文档引用

**需求精研指导**：
- **派生链（1对多）**: AC从US派生，使用source_us字段，验收US业务需求
- **业务验收定位**: AC由PM定义，使用业务语言，避免技术细节
- 引用关系简单明确，通过Front Matter的ID字段实现
- 避免循环引用，保持单向依赖

**质量标准**：文档间依赖关系清晰，追溯链完整，引用数量控制在必要范围内
</interconnection-complexity>

<content-depth>
**策略定位**：每个分类保持核心内容，避免冗余  
**需求精研指导**：每个文档控制篇幅，核心信息突出，重点关注需求收集工作充实度：核心用户识别是否全面、业务痛点理解是否深入、验收标准是否可测试  
**质量标准**：内容扎实比格式完美更重要，宁可内容扎实文档简单，也不要格式完美内容空洞

**业务语言强制要求**：
- 每个需求描述必须用业务语言表达
- 技术实现方式严禁出现在需求文档中
- PM/BA/客户可读性是第一质量标准
</content-depth>

<formalization-level>
**形式化策略**：简洁模板，标准格式，保持结构清晰但避免复杂化

**执行要点**：
- 统一模板和标题规范，Markdown自由格式
- 核心执行技巧：业务理解→验收定义→边缘考虑→质量门禁
- C1-CONFIRM模式："你看着办"，AI提供框架，用户快速确认

**质量标准**：格式简单完整，3个核心文档，平面结构，便于快速执行

**⭐ Artifact ID分配**: 保持现有artifact ID不变(确保引用完整性)，仅对新增artifact扫描宿主文件同PREFIX+SN，取max序号+1分配新ID
</formalization-level>

</craft-requirements-req1-l1>

<craft-requirements-req2-l1>
**需求精研_要求2_需求格式** L1需求精研：

<requirement-structure>**组织策略**：User Story为业务需求基础，角色功能优先

**🎯 主线组织：User Story业务需求**：
- 按业务功能分组(3-5个核心业务域)
- 每个US使用As-Want-So格式，表达角色需求和业务价值
- 保持用户故事的独立性和完整性
- 平面结构，无复杂层次嵌套

**执行要点**：
- 优先思考"什么角色需要什么功能"(User Story - 平易近人的业务需求基础层)
- 使用业务语言，避免技术术语，PM/BA主导
- 支持向后续阶段传递：User Story → AC验收 → VS设计(DESIGN) → BDD场景(IMPLEMENTATION)

**方法论基础**：
- 角色功能模式(User Story驱动)
- 业务价值优先，避免技术化
- 支持BDD场景映射和测试驱动开发

**质量标准**：
- 核心角色识别完整(3-5个)
- 每个US的业务价值明确
- US与AC对应关系清晰
- 确保需求覆盖全面，业务链路完整</requirement-structure>

<format-standards>**格式策略**：User Story为主格式，Acceptance Criteria作为验收标准，快速业务需求描述

**🎯 L1核心格式：User Story标准（快速模式）**：

**Front Matter（必填元数据）**：
```yaml
---
id: US-<SN>-NNN      # 例如: US-MAIN-001, US-AUTH-001
sn: <SN>             # 例如: MAIN, AUTH (业务域标识)
---
```

**User Story 内容结构**：
```markdown
## US-MAIN-001: 用户登录

**As a** 注册用户
**I want** 输入用户名密码后进入系统
**So that** 访问我的账户和使用应用功能

**业务场景**：
- 用户打开登录界面
- 输入用户名和密码
- 点击登录按钮
- 系统确认身份后进入主界面

**业务价值**：
- 安全访问个人账户
- 使用系统核心功能
```

**📋 补充格式：Acceptance Criteria（验收标准）**：

**Front Matter（必填元数据）**：
```yaml
---
id: AC-<SN>-NNN      # 例如: AC-MAIN-005, AC-AUTH-010
sn: <SN>             # 例如: MAIN, AUTH (必须与source_us的SN一致)
source_us: US-<SN>-NNN  # 派生来源（必填）：标识该AC派生自哪个User Story
---
```

**Acceptance Criteria 内容结构**：
```markdown
## AC-MAIN-005: 登录成功验收

**Given** 用户已注册且账号密码正确
**When** 用户输入用户名密码并点击登录
**Then** 用户成功进入系统主界面

**验收要点**：
- 登录操作快速完成（用户感觉流畅）
- 系统记住用户登录状态
- 主界面信息正确显示
```

**执行要点**：
- User Story优先，描述角色需求和业务价值
- AC必须派生自US（使用source_us字段）
- 支持BDD场景映射，便于后续IMPLEMENTATION阶段转换
- 保持格式简洁，避免过度复杂化

**质量标准**：
- User Story的业务价值清晰可验证
- As-Want-So格式完整
- AC的source_us正确指向US
- 业务语言表达，便于团队理解</format-standards>

<expression-quality>**质量策略**：内容完整性优先，格式从简，专注需求本质
**执行要点**：用简单自然的语言描述需求，避免复杂格式要求，突出需求收集完整性
**质量标准**：需求表达清晰易懂，内容充实准确，格式简单实用</expression-quality>

</craft-requirements-req2-l1>

<craft-requirements-req3-l1>
**需求精研_要求3_验收标准** L1需求精研：

<validation-approach>**验证策略**：每个US都有明确可验证的AC标准，覆盖正常和异常场景
**执行要点**：验收文档精简集中，简单目录结构，组织扁平避免层级（AC支持BDD场景映射的结构化表达）
**质量标准**：验证方法明确，便于查找和执行</validation-approach>

<acceptance-criteria>**标准策略**：功能点简单分组，用简单描述性语言表达验收要求，可测试性优先
**执行要点**：验收条件用自然语言具体描述，易于理解和验证，覆盖主要功能和关键场景
**质量标准**：描述清晰具体，核心验收要求明确，便于理解和验证</acceptance-criteria>

<testing-alignment>**对齐策略**：User Story天然支持BDD场景映射，AC验收标准与测试场景直接对应

**🔗 L1追溯链关系图**：

```
REQUIREMENTS阶段追溯链结构：

US-MAIN-001 (User Story - 业务需求)
  ├─[派生]→ AC-MAIN-005 (Acceptance Criteria)  ← source_us: US-MAIN-001
  └─[派生]→ AC-MAIN-006 (Acceptance Criteria)  ← source_us: US-MAIN-001

派生链（1对多）：US → AC （使用source_us字段）
```

**🎯 User Story → BDD映射机制**：
- As-Want-So → Feature描述(角色需求和业务价值)
- 业务场景 → Scenario步骤(业务操作路径)
  - 业务流程 → Given前置条件/When用户操作
  - 业务价值 → Then成功状态验证

**📋 Acceptance Criteria验收机制**：
- AC从US派生（source_us字段建立1:多父子关系）
- AC使用Given-When-Then格式验证业务需求完成度
- 每个US可派生1个或多个AC（覆盖不同验收场景）

**执行要点**：
- User Story的业务场景直接指导BDD场景编写
- AC必须使用source_us建立派生链（确保追溯完整）
- AC验证US的业务价值实现
- 支持向DESIGN阶段的VS技术设计和IMPLEMENTATION阶段的BDD测试场景无缝转换

**质量标准**：
- User Story可转换为完整BDD场景(Feature+Scenario+Steps)
- AC的source_us正确指向US，建立清晰派生链
- AC验收标准可测试、可验证
- 测试对齐机制清晰，便于后续阶段使用</testing-alignment>

</craft-requirements-req3-l1>

<craft-requirements-req4-l1>
**需求精研_要求4_质量标准** L1需求精研：

<completeness-control>**完整性策略**：全面识别用户角色，周全考虑业务场景，清晰需求边界
**执行要点**：质量文档精简控制，检查清单简单结构，组织扁平便于检查
**质量标准**：关注核心质量要求，避免规范过多复杂
**ID规范强制要求**：每个User Story必须包含Front Matter，包括id字段（格式：US-<SN>-NNN，如US-MAIN-001）和sn字段，作为全流程追溯基准
**SN说明**：Story Namespace业务域标识，单域项目可用MAIN或CORE，多域项目按业务划分（如AUTH, PAY等）</completeness-control>

<consistency-check>**一致性策略**：基础分类覆盖核心质量要素，充实度优先
**执行要点**：内容扎实重于格式，实用可行重于全面，依赖关系最小化
**质量标准**：检查清单简洁，避免复杂交叉依赖

**变更管理整合内容**：C1-CONFIRM模式单检查点，快速确认工作充实度
**变更执行要点**：基础Markdown格式，确认机制简单，支持快速评估确认
**变更质量标准**：核心检查点明确，重点确保需求收集工作充实度</consistency-check>

<stage-verbatim-directive>
**【需求阶段L1 MD文件的质量控制】**

- **适用范围**: 仅对spec/目录下非_前缀的MD文件生效（排除_开头的目录和文件）
- **长度控制**: 400-500行限制，超出按模块拆分
- **补丁保护**: 修改后检查基础完整性要求，核心一致性保护
- **质量预防**: 基础信息密度监控，结构清晰保持，术语统一验证
- **阶段特异**: 业务价值完整性，需求覆盖度充分

**自检清单**:
  - □ 内容组织是否简洁清晰？
  - □ 文档结构是否便于快速理解？
  - □ 业务需求理解是否充分？
  - □ 验收标准是否可测试？

- **修正触发**: 发现问题立即停止，然后让Human-in-the-loop，建议审查、整理和修复
</stage-verbatim-directive>
</craft-requirements-req4-l1>

---

*CRAFT_L1_REQUIREMENTS.md - L1-STREAMLINED级别的需求分类粒度需求精研权威指导文档*
