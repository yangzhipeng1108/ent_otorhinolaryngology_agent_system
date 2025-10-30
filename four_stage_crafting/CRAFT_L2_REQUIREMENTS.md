# CRAFT_L2_REQUIREMENTS 需求精研指导文档

> 🎯 **系统执行指令**: 需求收集分析场景→REQUIREMENTS阶段分类粒度(L2)需求精研激发，功能导向分类
> 📊 **维度聚焦**: 需求信息分类粒度平衡 - 功能导向分类组织→系统理解业务逻辑→设计质量提升
> 📁 **级别特征**: L2-BALANCED (适量结构化文件，标准流程偏好，团队协作，适用于任意规模团队)
> 🔧 **协作模式**: C2-PARTICIPATE模式("我们一起商量") - 系统提供分类建议→用户参与讨论→共同确定方案
> **🤝 协作操作**: AI提供2-3个选项→用户表达偏好→共同讨论最终方案
> ⚡ **体系定位**: 创意激发者，支撑脚手架生产+后期推敲，验收标准由four_stage_constraints定义
> 🏗️ **文档架构**: MD+XML混合设计，核心指导内容全部封装在XML标记内，实现LLM精确提取和Level间无缝切换

## 🔗 命名规范权威引用

> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L2 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L2_AUTHORITY.md` (必填 artifacts, 严格模式, 验收标准)

## 🔗 AICodingAgent规范权威引用

> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L2宪章**: `../agentic_spec/SPEC_ACA_L2_CHARTER.md` - L2质量标准 (6-10检查点, 通过率≥95%, 双层追溯)

## 🎯 XML标记体系说明

### 第一级标记 (craft-requirements-req[1-4]-l2)
**目的**: 包含L2级别REQUIREMENTS阶段的**完整指导内容**，作为LLM提取和Level切换的**整体单位**

### 第二级标记 (完整说明)

#### 6个标准维度子标签 (所有阶段通用 - 要求1):
1. `<document-organization>` - **文档组织架构策略**: 该级别需要多少文档、如何配置文档结构、基本协作约束、目录结构展示, 用户故事为核心，需求简单时平铺组织，需求复杂时可用Feature分组用户故事
2. `<directory-hierarchy>` - **目录层级组织**: 文件夹结构、层级深度控制、文件布局规范、导航方式设计  
3. `<categorization-granularity>` - **分类粒度策略** [REQUIREMENTS主攻]: 如何分类需求内容、分类细度控制、组织逻辑设计, 用户故事为核心，简单需求直接组织，复杂需求可按Feature分组
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
- `<acceptance-criteria>` - **验收标准定义**: 基础场景描述格式、验收条件、完成定义
- `<testing-alignment>` - **测试对齐机制**: 与测试用例对齐、可测试性保证、TDD准备

**要求4_质量标准** (3个子标签):
- `<completeness-control>` - **完整性控制**: 需求遗漏检查、覆盖度验证、全面性保证
- `<consistency-check>` - **一致性检查**: 需求间一致性、术语统一、逻辑一致
- `<change-management>` - **变更管理机制**: 需求变更流程、影响分析、版本控制

## 🤝 多角色协作约束

> 📋 **团队协作原则**: L2-BALANCED需求精研策略必须平衡PM/BA/Dev/Test各角色需求，确保协作效率
> 🚫 **分类平衡约束**: 避免过度复杂的需求分类，需求细节需适度包装，支持团队共同理解
> 💼 **业务技术平衡**: 平衡业务价值表达与技术实现指导，确保需求分类粒度服务团队协作
> 🎯 **标准化表达**: 使用团队标准术语和模板化表达方式，确保功能导向分类关系清晰一致

## ⚠️ 重要原则澄清

> 🎯 **维度本质 > 表面形式**: L1/L2/L3的核心是约束复杂度的不同维度，不是具体的文件组织形式
> 📁 **文件/目录是表现**: 文件数量、目录结构只是维度的外在表现，重点是背后的指导价值和复杂度控制
> 🚫 **避免表面约束**: 不要被"功能导向分类"、"5个文档"等表面描述约束，关注L2标准协作的维度本质
> ✨ **指导性优先**: CRAFT是创意激发者，松耦合高内聚的指导性存在，而非行为约束者

<craft-requirements-req1-l2>
**需求精研_要求1_文档体系** L2需求精研：

<document-organization>
**📋 受众定位约束**（REQUIREMENTS阶段质量标准）：
- **主要读者**: PM/BA/客户（业务背景，无技术假设）
- **语言要求**: 100%业务语言，绝对避免技术术语
- **可读性标准**: 任何非技术背景人员都能理解文档内容
- **L2团队协作**: PM/BA/客户/技术主管都会阅读需求文档，需确保业务价值清晰

**🚫 严格禁止的技术术语**：
- 技术实现细节（数据库、API、前后端、服务器、中间件）
- 技术指标（响应时间<1s、性能参数、吞吐量、并发数）
- 技术术语（CRUD、Token、Session、JWT、接口、认证、事务）
- 框架名称（React、Vue、Node.js、Express、PostgreSQL、Redis）
- 技术格式（JSON、HTTP、REST、GraphQL、请求/响应）
- **过程式代码**（函数调用、执行步骤、控制流程） ← ⚠️ 硬性约束

**✅ 推荐的业务语言**：
- 业务功能（用户可以登录、查看任务、添加信息、管理数据）
- 业务流程（用户输入信息后看到确认消息，系统记录操作）
- 业务概念（界面、系统、信息、状态、权限、角色）
- 业务价值（提高效率、方便管理、节省时间、保证安全）

**技术术语密度 = 0%**（REQUIREMENTS阶段硬性要求）

🎯 **核心维度特征**（必须遵循）：
L2必须体现"标准协作，模块引用"的本质特征
- **复杂度控制**：标准化文档关联，功能导向分类，模块间引用网络
- **协作特征**：支持C2-PARTICIPATE模式("我们一起商量")，团队协作讨论
- **质量标准**：平衡业务价值与技术实现，标准术语统一

📋 **推荐实施方案**（可参考调整）：
## 📊 L2 REQUIREMENTS 标准结构
**⭐ L2-BALANCED 需求文档组织架构 - 创建requirements时的核心指导**：
```
requirements/                    # 需求文档根目录（功能导向分类）
├── [user_stories_file]              # 用户故事（含初步INVEST评价）
├── [business_rules_file]            # 业务规则
├── [acceptance_criteria_file]       # 验收标准
├── [constraints_file]               # 约束条件
└── [interfaces_file]                # 接口需求
```

**文档组织建议**：覆盖5-8个核心维度类型，支持复杂项目完整表达
**L2平衡决策机制**：
- **核心5维度**(基础覆盖): 用户故事、业务规则、验收标准、约束条件、接口需求
- **+1维度**(利益相关者): 增加利益相关者管理维度[stakeholder_file]
- **+2维度**(术语统一): 再增加术语词汇表维度[glossary_file]  
- **+3维度**(非功能需求): 增加非功能需求维度[nfr_file]，支持复杂项目
**选择依据**：
- 项目复杂度：基础项目→5维度 | 中等复杂→6-7维度 | 高复杂→7-8维度
- 协作需求：单团队→基础维度 | 多团队→扩展维度 | 跨组织→完整维度
**策略定位**：每个功能导向分类对应专门文档
**需求精研指导**：适量核心文件（标准规模），合适数量专项文件支撑团队协作讨论，包含[user_stories_file]、[business_rules_file]、[acceptance_criteria_file]、[constraints_file]、[interfaces_file]五个核心文档
**质量标准**：核心文档覆盖需求全貌，数量适中便于维护，文档组织控制在合理范围内
**灵活性说明**：可增加[stakeholder_file]或[glossary_file]，但需保持功能导向分类的模块引用特征
**多角色协作约束**：L2-BALANCED策略重点确保PM/BA/Dev/Test各角色需求平衡，避免过度复杂的需求分类，需求细节需适度包装支持团队共同理解，平衡业务价值表达与技术实现指导，确保需求分类粒度服务团队协作，使用团队标准术语和模板化表达方式确保功能导向分类关系清晰一致

📁 **核心文档组织维度说明** (L2-BALANCED特征): 以下帮助理解占位符背后的文件组织思考维度，具体文件组织可灵活适配项目需要

**文档组织原则**:
- **维度优先**: 必需的是覆盖核心维度，文件组织形式灵活
- **按阶段分目录**: requirements/design/implementation/task_planning
- **按粒度分层**: 核心文档放根目录，细节文档可放子目录或拆分文件
- **命名规范**: snake_case，语义化文件名
- **关联管理**: 使用相对路径引用，保持文档间关联清晰
- **灵活适配**: 内容少时合并文档，内容多时拆分文件（如`xxx_part1.md`），复杂时建子目录

**维度1: 用户故事维度 (必需)**
- **对应占位符**: `[user_stories_file]`
- **参考示例**: `user_stories.md` 或 `features.md`
- **维度职责**: 记录用户故事和功能需求，支持INVEST评价
- **文档组织方式**:
  - 单文件形式: `user_stories.md`
  - 多文件形式: `user_stories_epic1.md`, `user_stories_epic2.md` (按Epic分组)
  - 目录结构形式: `user_stories/epic1.md`, `user_stories/epic2.md`
  - 分模块形式: `user_stories_auth.md`, `user_stories_business.md` (按功能模块)
- **内容要求**: 用户故事+INVEST初步评价，支持团队共同理解
- **L2特征**: 支持多文件或目录结构，按Epic或功能模块分组

**维度2: 业务规则维度 (必需)**
- **对应占位符**: `[business_rules_file]`
- **参考示例**: `business_rules.md`
- **维度职责**: 记录业务规则和约束逻辑
- **文档组织方式**:
  - 单文件形式: `business_rules.md`
  - 多文件形式: `business_rules_part1.md`, `business_rules_part2.md`
  - 目录结构形式: `business_rules/core.md`, `business_rules/edge_cases.md`
  - 分类文件形式: `business_rules_pricing.md`, `business_rules_workflow.md`
- **内容要求**: 业务规则、决策表、业务流程
- **L2特征**: 支持按业务领域分类，标准化表达

**维度3: 验收标准维度 (必需)**
- **对应占位符**: `[acceptance_criteria_file]`
- **参考示例**: `acceptance_criteria.md`
- **维度职责**: 确保需求可验证、可测试，支持BDD映射
- **文档组织方式**:
  - 单文件形式: `acceptance_criteria.md`
  - 多文件形式: `acceptance_criteria_part1.md`, `acceptance_criteria_part2.md`
  - 目录结构形式: `acceptance/functional.md`, `acceptance/nfr.md`
  - 分组文件形式: `acceptance_auth.md`, `acceptance_business.md`
- **内容要求**: 功能验收条件+初步非功能需求验收
- **L2特征**: 结构化验收标准，支持BDD场景映射

**维度4: 约束条件维度 (必需)**
- **对应占位符**: `[constraints_file]`
- **参考示例**: `constraints.md`
- **维度职责**: 明确需求边界和实现限制
- **文档组织方式**:
  - 单文件形式: `constraints.md`
  - 多文件形式: `constraints_tech.md`, `constraints_business.md`
  - 目录结构形式: `constraints/technical.md`, `constraints/regulatory.md`
  - 分类文件形式: 按约束类型分文件
- **内容要求**: 技术约束、业务规则、合规要求
- **L2特征**: 分类清晰，支持多维度约束管理

**维度5: 接口需求维度 (必需)**
- **对应占位符**: `[interfaces_file]`
- **参考示例**: `interfaces.md` 或 `integration_requirements.md`
- **维度职责**: 记录系统间接口和集成需求
- **文档组织方式**:
  - 单文件形式: `interfaces.md`
  - 多文件形式: `interfaces_external.md`, `interfaces_internal.md`
  - 目录结构形式: `interfaces/rest_api.md`, `interfaces/messaging.md`
  - 分系统形式: 按集成系统分文件
- **内容要求**: 外部接口、集成点、数据交换需求
- **L2特征**: 标准化接口描述，支持团队协作

**维度6: 利益相关方维度 (可选，扩展之一)**
- **对应占位符**: `[stakeholder_file]`
- **参考示例**: `stakeholders.md`
- **维度职责**: 管理干系人和角色关系
- **文档组织方式**:
  - 单文件形式: `stakeholders.md`
  - 目录结构形式: `stakeholders/internal.md`, `stakeholders/external.md`
- **内容要求**: 干系人列表、角色职责、沟通计划
- **L2特征**: 支持多团队协作管理

**维度7: 术语词汇表维度 (可选，扩展之一)**
- **对应占位符**: `[glossary_file]`
- **参考示例**: `glossary.md` 或 `terminology.md`
- **维度职责**: 统一术语和概念定义
- **文档组织方式**:
  - 单文件形式: `glossary.md`
  - 分类文件形式: `glossary_business.md`, `glossary_technical.md`
- **内容要求**: 术语定义、缩写说明、领域概念
- **L2特征**: 支持团队术语统一，标准化表达

**维度8: 非功能需求维度 (可选，扩展之一)**
- **对应占位符**: `[nfr_file]`
- **参考示例**: `nfr.md` 或 `quality_attributes.md`
- **维度职责**: 记录非功能需求和质量属性
- **文档组织方式**:
  - 单文件形式: `nfr.md`
  - 分类文件形式: `nfr_performance.md`, `nfr_security.md`
  - 目录结构形式: `nfr/performance.md`, `nfr/security.md`
- **内容要求**: 性能、安全、可用性等质量需求
- **L2特征**: 结构化非功能需求管理
</document-organization>

<directory-hierarchy>
**策略定位**：功能导向分类支持平面或分层组织
**需求精研指导**：根据功能复杂度选择平面或2层结构，保持组织清晰，支持团队协作的目录结构
**质量标准**：目录层级适中，组织结构便于团队成员快速定位和协作
</directory-hierarchy>

<categorization-granularity>
**分类策略**：功能导向标准分类体系，5个核心文件按业务功能模块组织，支持团队协作理解

**💡 应用集成识别**（条件触发）：
- 思考：用户需要入口访问功能吗？（Web/移动/桌面/CLI）
- 如需要：创建导航US描述用户如何访问各项功能

**执行要点**：
- 用户故事采用Story-Feature混合组织：简单需求直接Story分组，复杂需求引入Feature层次对相关Story进行分组，应用初步INVEST评价
- Feature分组原则：当Story数量超过5-8个或存在明显业务功能域时，可引入Feature作为中间层次
- 业务规则按功能域分组（权限、数据、流程规则），建立双向引用关系
- 验收标准按功能模块组织，基础给定-当-那么场景格式，覆盖正常/异常/边界条件
- 约束条件四大分类：技术、业务、合规、性能约束，建立影响矩阵
- 接口需求三类：用户界面、系统接口、数据接口，明确输入输出规格
- 初步INVEST检查：Independent(独立性)、Negotiable(可协商)、Valuable(有价值)、Estimable(可估算)、Small(小颗粒)、Testable(可测试)

**质量标准**：功能模块覆盖全面，团队各角色理解分类逻辑，支持协作和系统理解

**L2业务语言分类原则**：
- 功能导向分类必须使用业务术语
- 用户故事分组基于业务领域（如"用户管理"、"任务处理"）
- 避免技术模块命名（如"API层"、"数据层"）
- 分类名称PM/BA/客户可理解
</categorization-granularity>

<interconnection-complexity>
**关联策略**：功能模块双向引用，用户故事↔业务规则↔验收标准形成清晰网络
**执行要点**：
- 用户故事引用相关业务规则，建立需求-规则双向链接
- 验收标准直接对应用户故事，确保验证完整性
- 接口需求与系统边界关联，明确输入输出依赖
- 约束条件影响矩阵，标识跨模块影响范围
**质量标准**：引用关系可追溯，模块依赖清晰，支持影响分析和团队协作
</interconnection-complexity>

<content-depth>
**内容策略**：标准化深度，支持团队系统理解业务需求，平衡各角色关注点
**执行要点**：
- 用户故事包含完整上下文，业务价值和验收条件清晰
- 业务规则覆盖核心逻辑，避免过度细节化
- 验收标准三层覆盖：正常流程、异常处理、边界条件
- 接口需求明确输入输出，数据格式和错误处理
**质量标准**：内容充实度支持开发理解，业务逻辑完整性优于文档完美

**业务语言强制要求**：
- 每个需求描述必须用业务语言表达
- 技术实现方式严禁出现在需求文档中
- PM/BA/客户可读性是第一质量标准
- L2标准流程中，需求质量直接影响后续设计和开发效率
</content-depth>

<formalization-level>
**形式化策略**：标准化模板格式，统一结构支持团队协作，平衡规范性与灵活性
**执行要点**：
- 核心执行技巧：业务理解→验收定义→边缘考虑→质量门禁
- C2-PARTICIPATE模式："我们一起商量"，AI建议+用户参与+共同决策
  - **3步协作流程**: (1)AI提供2-3个方案建议 → (2)用户评估并提出偏好 → (3)共同讨论形成最终方案
  - **决策机制**: 意见分歧时优先考虑用户偏好，AI提供风险提醒，追求"足够好"而非完美方案
  - **协作控制**: 保持高效讨论节奏，避免过度细节影响整体效率
- 功能模块模板化：Feature-Story结构，基础场景描述格式
- 5文档标准格式：用户故事、业务规则、验收标准、约束条件、接口需求

**📋 文档生产次序**：
**L2核心次序**：[user_stories_file] → [acceptance_criteria_file]（必须严格串行）
**L2推荐次序**（如使用）：US → AC → [constraints_file]/[interfaces_file]（约束条件/接口需求可选）

**次序说明**：
- **US优先原因**：US (User Story) 是L2核心，AC通过source_us派生，必须先生产US
- **L2特点**：无SB (Slice Brief)，保持REQUIREMENTS阶段简洁性
- **串行约束**：当前AI Coding平台限制，必须串行生产
- **推荐artifacts灵活性**：约束条件/接口需求等根据项目需要选择，但如使用需在US之后

**质量标准**：格式一致性支持协作，模板标准化提升开发效率

**⭐ Artifact ID分配**: 保持现有artifact ID不变(确保引用完整性)，仅对新增artifact扫描宿主文件同PREFIX+SN，取max序号+1分配新ID
</formalization-level>
</craft-requirements-req1-l2>

<craft-requirements-req2-l2>
**需求精研_要求2_需求格式** L2需求精研：

<requirement-structure>**组织策略**：用户故事为核心，采用Story-Feature混合组织模式，按业务功能域分组，建立功能-角色-价值映射，简单项目使用Story直接分组，复杂需求引入Feature层次对相关Story进行分组，集成初步INVEST评价
**执行要点**：
- 用户故事模板化表达：As a [用户角色], I want [功能需求], So that [业务价值]
- 基础场景描述：为重要用户故事添加简单的给定-当-那么场景说明
- 初步INVEST评价：每个用户故事检查Independent(独立性)、Valuable(价值性)、Estimable(可估算性)三个核心维度
- 功能模块系统化识别，建立角色-需求-价值清晰映射
**方法论基础**：用户故事映射(复杂需求可用Feature分组)、基础场景化描述、业务功能域识别、需求追溯验证(INVEST标准评价)
**质量标准**：用户故事符合初步INVEST标准，场景描述简单清晰，团队角色需求理解平衡</requirement-structure>

<format-standards>**格式策略**：用户故事模板+场景描述模板组合，统一格式标准，灵活平衡

**🎯 L2核心格式规范**：

**User Story 标准格式** (L2必须artifacts):
```yaml
---
id: US-AUTH-001
sn: AUTH
status: active
related_ac: [AC-AUTH-001, AC-AUTH-002]
---

# US-AUTH-001 用户登录功能

**As a** 系统用户
**I want** 使用邮箱和密码登录系统
**So that** 我可以访问个人专属功能

## 基础场景描述 (可选)
**Given** 用户在登录页面
**When** 用户输入正确的邮箱和密码
**Then** 系统应该允许用户成功登录并跳转到主页面

## INVEST评价 (初步)
- ✅ **Independent**: 独立的登录功能
- ✅ **Valuable**: 为用户提供安全访问价值
- ✅ **Estimable**: 可估算为中等复杂度
```

**Acceptance Criteria 标准格式** (L2必须artifacts):
```yaml
---
id: AC-AUTH-001
sn: AUTH
status: active
source_us: US-AUTH-001
---

# AC-AUTH-001 登录功能验收标准

## 基础验收条件
**Given** 用户在登录页面且具有有效账户
**When** 用户输入正确的邮箱和密码并点击登录
**Then** 系统应该验证凭据并跳转到用户主页面

### 正常流程
- 邮箱格式验证：必须符合标准邮箱格式
- 密码验证：密码长度至少8位
- 登录成功：显示欢迎消息并跳转

### 异常处理
- 邮箱不存在：显示"用户不存在"提示
- 密码错误：显示"密码错误"提示
- 账户被锁定：显示"账户已被锁定"提示

### 边界条件
- 连续失败3次：自动锁定账户5分钟
- 会话超时：30分钟无操作自动退出
```

**执行要点**：
- **US主线地位**: User Story是L2核心，所有AC通过source_us追溯到US
- **Front Matter必填**: id + sn 必填，status建议填写，追溯链字段按需添加
- **ID格式约束**: US-AUTH-001, AC-AUTH-001 (格式: US-<SN>-NNN, AC-<SN>-NNN)，SN不可省略
- **追溯链规范**: AC使用source_us指向US，US使用related_ac建立下游关联
- **阶段边界**: REQUIREMENTS阶段只涉及US/AC，FP属于DESIGN阶段
- 提供用户故事基础模板和可选的基础场景描述模板，支持渐进式结构化
- Feature组织时，使用简化Gherkin结构：Feature作为业务功能域标题，内含相关Story和基础场景描述
- Story-Feature混合格式：Feature [功能域名称] → Story集合 + 给定-当-那么基础场景

**质量标准**：格式清晰一致，便于团队协作，支持从简单到结构化的过渡，确保L2追溯链完整</format-standards>

<expression-quality>**质量策略**：内容+场景结构化平衡，适度规范，先理解业务功能再表达
**执行要点**：在保持内容完整的基础上，适度引入场景化描述，提升表达结构性
**质量标准**：需求表达清晰，场景描述简单易懂，团队理解一致</expression-quality>
</craft-requirements-req2-l2>

<craft-requirements-req3-l2>
**需求精研_要求3_验收标准** L2需求精研：

<validation-approach>**验证策略**：功能模块验收条件完整覆盖，考虑团队协作责任分工
**执行要点**：异常场景充分讨论，验收文档精简集中，按功能模块组织目录
**质量标准**：支持团队导航，避免验收规范过多分散</validation-approach>

<acceptance-criteria>**标准策略**：功能模块对齐的标准组织，引入基础Given-When-Then场景描述
**执行要点**：为重要用户故事提供基础给定-当-那么场景，可测试性优先，团队成员易于理解
**质量标准**：场景描述简单清晰，核心验收标准明确，便于理解和验证</acceptance-criteria>

<testing-alignment>**对齐策略**：基础场景到测试用例映射，结构清晰，支持渐进式测试设计
**执行要点**：基础给定-当-那么场景易于转化为测试用例，依赖关系适中，避免复杂引用
**质量标准**：场景描述可测试，支持团队测试实施和后续自动化</testing-alignment>
</craft-requirements-req3-l2>

<craft-requirements-req4-l2>
**需求精研_要求4_质量标准** L2需求精研：

<completeness-control>
**完整性策略**：系统化梳理业务功能模块，平衡团队各角色需求关注点
**执行要点**：
- 功能模块完整性：核心业务流程全覆盖，关键用户场景无遗漏
- 角色需求平衡：PM关注业务价值，BA关注流程逻辑，Dev关注技术约束，Test关注验收条件
- 业务边界共识：接口定义清晰，模块职责明确，团队理解一致
**质量标准**：功能模块系统完整，团队角色需求平衡覆盖，质量检查精简有效
</completeness-control>

<consistency-check>
**一致性策略**：功能模块标准分类，团队理解一致性优先，充实度重于流程完美
**执行要点**：
- 术语统一：业务概念、技术名词、流程描述保持一致
- 逻辑一致：用户故事与业务规则对应，验收标准与功能需求匹配
- 格式一致：模板化结构，标准化表达，便于团队协作
**质量标准**：需求理解团队一致，功能完整性优于文档规范，依赖关系简洁清晰

**变更管理整合内容**：C2-PARTICIPATE模式协作评审，"我们一起商量"的标准化变更流程
**变更执行要点**：
- 适度参与团队讨论：快速评估变更影响，达成共识决策
- **C2变更协作流程**: (1)AI分析变更影响并提供建议 → (2)用户评估业务优先级 → (3)共同制定变更计划
- **协作决策原则**: 用户主导业务判断，AI提供技术风险分析，平衡变更价值与实施成本
- 标准检查点：业务影响评估、技术可行性分析、测试影响范围
- 模板化变更：统一变更申请格式，标准化影响分析
- 团队评审机制：PM+BA+Dev+Test多角色参与，确保全面考虑
**变更质量标准**：变更影响可控，团队协作高效，质量评估精炼有效
**Level特异性检查**：是否体现L2-BALANCED团队协作特征？是否建立了合适的模块间引用关系？是否支持C2-PARTICIPATE模式协作和系统理解？
</consistency-check>

<stage-verbatim-directive>
**【需求阶段L2 MD文件的质量控制】**

- **适用范围**: 仅对spec/目录下非_前缀的MD文件生效（排除_开头的目录和文件）
- **长度控制**: 500-600行限制，按模块分段检查
- **补丁保护**: 修改后验证系统性完整性要求，标准一致性保护
- **质量预防**: 标准信息密度控制，层次结构管理，术语标准化
- **阶段特异**: 业务价值完整性，需求覆盖度充分

**自检清单**:
  - □ 内容组织是否标准规范？
  - □ 文档结构是否清晰可追溯？
  - □ 业务需求理解是否充分？
  - □ 验收标准是否可测试？

- **修正触发**: 发现问题立即停止，然后让Human-in-the-loop，建议审查、整理和修复
</stage-verbatim-directive>
</craft-requirements-req4-l2>


---

*CRAFT_L2_REQUIREMENTS.md - L2-BALANCED级别的需求分类粒度需求精研权威指导文档*
