# CRAFT_L3_REQUIREMENTS L3严格控制指导文档

> 🎯 **系统执行指令**: 需求收集分析场景→REQUIREMENTS阶段需求工作充实引导(L3)，细粒度完整追溯导向
> 📊 **核心聚焦**: 需求收集工作充实指导 - 业务理解深化→需求挖掘全面→设计质量提升
> 📁 **级别特征**: L3-RIGOROUS (适量专业文档，规范化目录体系，严格质量控制偏好，完整INVEST用户故事管理，适用于任意规模团队)
> 🔧 **协作模式**: C3-LEAD模式("我要控制") - 用户主导需求控制→系统提供专业建议→用户决策执行
> ⚡ **体系定位**: 创意激发者，支撑脚手架生产+后期推敲，验收标准由four_stage_constraints定义
> 🏗️ **文档架构**: MD+XML混合设计，核心指导内容全部封装在XML标记内，实现LLM精确提取和Level间无缝切换

## 🔗 命名规范权威引用

> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L3 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L3_AUTHORITY.md` (必填 artifacts, 严格模式, 验收标准)

## 🔗 AICodingAgent规范权威引用

> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L3宪章**: `../agentic_spec/SPEC_ACA_L3_CHARTER.md` - L3质量标准 (10-15检查点, 通过率≥95%, 三层追溯)

## 🎯 XML标记体系说明

### 第一级标记 (craft-requirements-req[1-4]-l3)
**目的**: 包含L3级别REQUIREMENTS阶段的**完整指导内容**，作为LLM提取和Level切换的**整体单位**

### 第二级标记 (完整说明)

#### 6个标准维度子标签 (所有阶段通用 - 要求1):
1. `<document-organization>` - **文档组织架构策略**: 该级别需要多少文档、如何配置文档结构、基本协作约束、目录结构展示, 用户故事为核心，简单需求平铺组织，中等复杂可用Feature分组，高度复杂可用Epic-Feature层次组织
2. `<directory-hierarchy>` - **目录层级组织**: 文件夹结构、层级深度控制、文件布局规范、导航方式设计  
3. `<categorization-granularity>` - **分类粒度策略** [REQUIREMENTS主攻]: 如何分类需求内容、分类细度控制、组织逻辑设计, 用户故事为核心，按需求复杂度选择：平铺 → Feature分组 → Epic-Feature层次
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
- `<acceptance-criteria>` - **验收标准定义**: 完整Gherkin场景格式、验收条件、完成定义
- `<testing-alignment>` - **测试对齐机制**: 与测试用例对齐、可测试性保证、TDD准备

**要求4_质量标准** (3个子标签):
- `<completeness-control>` - **完整性控制**: 需求遗漏检查、覆盖度验证、全面性保证
- `<consistency-check>` - **一致性检查**: 需求间一致性、术语统一、逻辑一致
- `<change-management>` - **变更管理机制**: 需求变更流程、影响分析、版本控制

## 🤝 多角色协作约束

> 📋 **严格质量控制原则**: L3-RIGOROUS严格控制策略适用于任意规模团队的严格质量控制偏好，确保专业完整性和可跟踪性
> 🚫 **完整INVEST约束**: 采用完整的INVEST评价体系，确保用户故事质量和项目成功率
> 💼 **专业项目实践**: 集成专业需求工程实践，支持标准化项目管理流程
> 🎯 **规范化表达**: 使用团队标准术语和规范化表达方式，确保项目成果可维护性

## ⚠️ 重要原则澄清

> 🎯 **维度本质 > 表面形式**: L1/L2/L3的核心是约束复杂度的不同维度，不是具体的文件组织形式
> 📁 **文件/目录是表现**: 文件数量、目录结构只是维度的外在表现，重点是背后的指导价值和复杂度控制
> 🚫 **避免表面约束**: 不要被"细粒度分类"、"10个文档"等表面描述约束，关注L3严格专业的维度本质
> ✨ **指导性优先**: CRAFT是创意激发者，松耦合高内聚的指导性存在，而非行为约束者

<craft-requirements-req1-l3>
**需求精研_要求1_文档体系** L3需求精研：

<document-organization>
**📋 受众定位约束**（REQUIREMENTS阶段质量标准）：
- **主要读者**: 审计人员/合规检查人员/第三方评审专家（需要验证业务逻辑和追溯链条）
- **语言要求**: 100%业务语言，绝对避免技术术语，强调完整追溯性
- **可读性标准**: 任何非技术背景审计人员都能理解业务逻辑和追溯关系
- **L3严格控制**: 审计人员/合规人员/评审专家需要验证需求完整性和追溯链条，必须确保业务逻辑清晰可审计

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
L3必须体现"严格控制，完整追溯"的本质特征
- **复杂度控制**：完整追溯体系，细分类别专业文档，血缘追溯网络
- **协作特征**：支持C3-LEAD模式("我要控制")，严格质量控制偏好
- **质量标准**：专业需求工程实践，项目成果可维护，第三方可审计

📋 **推荐实施方案**（可参考调整）：
## 📊 L3 REQUIREMENTS 标准结构
**⭐ L3-RIGOROUS 需求文档组织架构 - 创建requirements时的核心指导**：
```
requirements/                    # 需求文档根目录
├── [business_requirements_file]       # 业务需求（愿景+目标）
├── [user_stories_file]              # 用户故事（含完整INVEST评价）
├── [use_cases_file]                 # 用例文档
├── [acceptance_criteria_file]       # 验收标准
├── [performance_requirements_file]  # 性能需求
├── [security_requirements_file]     # 安全需求
├── [compliance_requirements_file]   # 合规需求
├── [constraints_file]               # 约束条件
├── [interfaces_file]                # 接口需求
└── [requirements_traceability_file] # 需求追溯矩阵
```

**文档组织建议**：适量核心文档（参考范围8-12个），具体数量取决于维度覆盖需要
**策略定位**：每个细分类别对应专业文档集合
**需求精研指导**：10±2个专业核心文档聚焦需求分析深度，通过思考维度的深度和广度体现L3特征，覆盖业务需求、用户故事、用例文档、验收标准、非功能需求核心类别
**质量标准**：适量核心文档覆盖需求全景，数量控制在合理范围，支持专业项目管理需要
**灵活性说明**：可根据项目特点调整非功能需求类别数量，但需保持细分类别的完整追溯特征
**多角色协作约束**：L3-RIGOROUS需求精研策略适用于任意规模团队的严格质量控制偏好，集成完整INVEST评价体系，确保用户故事质量和项目可跟踪性，采用专业需求工程实践，支持标准化项目管理，使用团队标准术语和规范化表达，确保项目成果可维护

📁 **核心文档组织维度说明** (L3-RIGOROUS特征): 以下帮助理解占位符背后的文件组织思考维度，具体文件组织可灵活适配项目需要

**文档组织原则**:
- **维度优先**: 必需的是覆盖核心维度，文件组织形式灵活
- **规范化分类**: 细分类别专业文档，支持完整追溯和审计
- **专业导航**: 目录结构清晰，支持团队协作和项目管理
- **质量标准**: 适量核心文档（8-12个范围，推荐10个），覆盖需求全景，支持企业级项目实践

**维度1: 业务需求维度 (必需)**
- **对应占位符**: `[business_requirements_file]`
- **参考示例**: `business_requirements.md` 或 `vision_and_objectives.md`
- **维度职责**: 记录项目愿景、业务目标、KPI体系，建立战略对齐
- **文档组织方式**:
  - 单文件形式: `business_requirements.md` (集成愿景+目标+KPI)
  - 分层形式: `vision.md`, `business_objectives.md`, `kpi_metrics.md` (分层管理)
  - 目录结构形式: `business/vision.md`, `business/objectives.md`, `business/kpi.md`
- **内容要求**: 项目愿景、SMART目标定义、KPI指标体系、成功标准，支持战略追溯
- **L3特征**: 战略对齐完整，量化指标明确，支持专业决策追溯和审计验证

**维度2: 用户故事维度 (必需)**
- **对应占位符**: `[user_stories_file]`
- **参考示例**: `user_stories.md` 或 `stories_with_invest.md`
- **维度职责**: 记录用户故事，集成完整INVEST评价，支持传统需求追溯
- **文档组织方式**:
  - 单文件形式: `user_stories.md` (含完整INVEST评价)
  - Epic分组形式: `stories_epic1.md`, `stories_epic2.md` (按Epic组织)
  - Feature分组形式: `stories_auth.md`, `stories_business.md` (按Feature组织)
  - 目录结构形式: `user_stories/epic1/`, `user_stories/epic2/` (多层次)
- **内容要求**: As a [角色] I want [功能] So that [价值]，完整INVEST六维评价，Story-Feature-Epic传统层次（按需引入）
- **L3特征**: 100%通过INVEST评价，传统层次组织清晰，支持完整项目追溯矩阵
- **L3 Front Matter格式示例**:
  ```yaml
  ---
  id: US-AUTH-002
  sn: AUTH
  status: active
  owner: @product-team
  version: v1.0.0
  related_ac: [AC-AUTH-005]
  related_des: [DES-AUTH-010]
  # 注：related_ac和related_des至少填写1个，可同时填写
  ---
  
  # User Story: 用户登录认证
  
  **As a** 注册用户  
  **I want** 通过用户名和密码登录系统  
  **So that** 我可以访问个人账户和受保护的功能
  
  ## INVEST 评价（L3审计级严格标准）
  
  - **I (Independent)**: ✅ 独立性 - 与其他Story无技术依赖
  - **N (Negotiable)**: ✅ 可协商 - 认证方式可调整（密码/生物识别）
  - **V (Valuable)**: ✅ 价值性 - 为用户提供安全访问能力
  - **E (Estimable)**: ✅ 可估算 - 3-5人日（含测试）
  - **S (Small)**: ✅ 小颗粒 - 单迭代可完成
  - **T (Testable)**: ✅ 可测试 - 有明确验收标准AC-AUTH-005
  ```

**维度3: 用例文档维度 (必需)**
- **对应占位符**: `[use_cases_file]`
- **参考示例**: `use_cases.md` 或 `use_case_specifications.md`
- **维度职责**: 详细记录用例规范，包含前置条件、主流程、异常流程、后置条件
- **文档组织方式**:
  - 单文件形式: `use_cases.md` (集成所有用例)
  - 功能模块形式: `use_cases_auth.md`, `use_cases_business.md` (按模块分类)
  - 目录结构形式: `use_cases/auth/`, `use_cases/business/` (专业分类)
- **内容要求**: 前置条件、主流程、异常流程、后置条件，与用户故事双向对齐
- **L3特征**: 规范化格式严格，与用户故事完整对齐，支持需求追溯矩阵

**维度4: 验收标准维度 (必需)**
- **对应占位符**: `[acceptance_criteria_file]`
- **参考示例**: `acceptance_criteria.md` 或 `gherkin_scenarios.md`
- **维度职责**: 定义验收标准，采用完整Gherkin语法或Given-When-Then格式
- **文档组织方式**:
  - 单文件形式: `acceptance_criteria.md` (集成所有验收场景)
  - Story对应形式: `acceptance_story001.md`, `acceptance_story002.md` (一对一)
  - Feature分组形式: `acceptance_feature_auth.md` (按Feature组织)
  - 目录结构形式: `acceptance/feature1/`, `acceptance/feature2/` (专业分类)
- **内容要求**: 完整Gherkin语法(Feature-Scenario-Given-When-Then)或简化格式，覆盖正常/异常/边界场景
- **L3特征**: 可选择完整Gherkin或简化格式，验证矩阵全覆盖，直接支持自动化测试转化
- **L3 Front Matter格式示例**:
  ```yaml
  ---
  id: AC-AUTH-005
  sn: AUTH
  status: active
  owner: @qa-team
  version: v1.0.0
  source_us: US-AUTH-002
  related_des: [DES-AUTH-010]
  related_sc: [SC-AUTH-030]
  ---
  
  # Acceptance Criteria: 用户登录认证验收标准
  
  ## Scenario 1: 有效凭证登录成功
  
  **Given** 用户已注册账户（用户名"testuser"，密码"Test@123"）  
  **And** 用户在登录页面  
  **When** 用户输入正确的用户名和密码  
  **And** 用户点击"登录"按钮  
  **Then** 系统验证凭证成功  
  **And** 用户被重定向到个人主页  
  **And** 系统显示"欢迎回来，testuser"消息
  
  ## Scenario 2: 无效凭证登录失败
  
  **Given** 用户在登录页面  
  **When** 用户输入错误的密码  
  **And** 用户点击"登录"按钮  
  **Then** 系统显示"用户名或密码错误"消息  
  **And** 用户停留在登录页面  
  **And** 登录尝试被记录（审计要求）
  ```

**维度5: 性能需求维度 (必需)**
- **对应占位符**: `[performance_requirements_file]`
- **参考示例**: `performance_requirements.md` 或 `nfr_performance.md`
- **维度职责**: 定义性能指标、响应时间、吞吐量、并发要求
- **文档组织方式**:
  - 单文件形式: `performance_requirements.md` (集成所有性能需求)
  - 分层形式: `performance_response_time.md`, `performance_throughput.md` (按指标分类)
  - 目录结构形式: `nfr/performance/` (NFR专业分类)
- **内容要求**: 量化性能指标、基准测试标准、性能边界条件，支持SLA定义
- **L3特征**: 量化指标明确，支持合规审查和专业验证

**维度6: 安全需求维度 (必需)**
- **对应占位符**: `[security_requirements_file]`
- **参考示例**: `security_requirements.md` 或 `nfr_security.md`
- **维度职责**: 定义安全要求、认证授权、数据保护、威胁模型
- **文档组织方式**:
  - 单文件形式: `security_requirements.md` (集成所有安全需求)
  - 分层形式: `security_authentication.md`, `security_data_protection.md` (按安全类别)
  - 目录结构形式: `nfr/security/` (NFR专业分类)
- **内容要求**: 认证授权策略、数据加密要求、威胁模型评估、安全合规标准
- **L3特征**: 安全威胁模型完整，支持安全审计和合规验证

**维度7: 合规需求维度 (必需)**
- **对应占位符**: `[compliance_requirements_file]`
- **参考示例**: `compliance_requirements.md` 或 `nfr_compliance.md`
- **维度职责**: 定义合规要求、法规标准、审计要求
- **文档组织方式**:
  - 单文件形式: `compliance_requirements.md` (集成所有合规需求)
  - 法规分类形式: `compliance_gdpr.md`, `compliance_hipaa.md` (按法规分类)
  - 目录结构形式: `nfr/compliance/` (NFR专业分类)
- **内容要求**: 法规标准要求、合规检查清单、审计验证标准
- **L3特征**: 法规标准完整，支持第三方合规审计和验证

**维度8: 约束条件维度 (必需)**
- **对应占位符**: `[constraints_file]`
- **参考示例**: `constraints.md` 或 `project_constraints.md`
- **维度职责**: 记录技术约束、资源约束、时间约束、外部依赖
- **文档组织方式**:
  - 单文件形式: `constraints.md` (集成所有约束)
  - 分类形式: `constraints_technical.md`, `constraints_resource.md` (按类型分类)
  - 目录结构形式: `constraints/technical/`, `constraints/resource/` (专业分类)
- **内容要求**: 技术栈约束、资源限制、时间要求、外部系统依赖
- **L3特征**: 约束分类清晰，影响分析完整，支持项目决策追溯

**维度9: 接口需求维度 (必需)**
- **对应占位符**: `[interfaces_file]`
- **参考示例**: `interface_requirements.md` 或 `external_interfaces.md`
- **维度职责**: 定义外部接口需求、API契约、集成要求
- **文档组织方式**:
  - 单文件形式: `interface_requirements.md` (集成所有接口需求)
  - 系统分类形式: `interfaces_payment.md`, `interfaces_auth.md` (按外部系统)
  - 目录结构形式: `interfaces/external/`, `interfaces/internal/` (专业分类)
- **内容要求**: API契约定义、数据格式规范、集成协议要求、错误处理策略
- **L3特征**: 接口规范详细，契约定义严格，支持集成测试和系统对接

**维度10: 需求追溯矩阵维度 (必需)**
- **对应占位符**: `[requirements_traceability_file]`
- **参考示例**: `requirements_traceability_matrix.md` 或 `traceability.md`
- **维度职责**: 建立需求追溯矩阵，支持完整的需求-设计-测试追溯
- **文档组织方式**:
  - 单文件形式: `requirements_traceability_matrix.md` (集中管理)
  - 分阶段形式: `traceability_req_to_design.md`, `traceability_req_to_test.md` (按追溯路径)
  - 目录结构形式: `traceability/req_design/`, `traceability/req_test/` (多维追溯)
- **内容要求**: EPIC-XXX→FEAT-XXX→STORY-XXX→TEST-XXX完整追溯链，变更影响分析，覆盖度验证
- **L3特征**: 传统追溯矩阵完整，变更影响可追踪，支持第三方审计和项目管理
</document-organization>
<directory-hierarchy>**策略定位**：规范化分类支撑专业需求文档体系
**需求精研指导**：平面目录结构支持专业分工协作，2层目录深度保持清晰导航
**质量标准**：目录层级简洁规范，支持专业团队的需求管理和项目跟踪</directory-hierarchy>  
<categorization-granularity>
**分类策略**：专业需求分类体系，集成完整INVEST用户故事管理，支持严格质量控制的项目跟踪

**💡 应用集成识别**（条件触发）：
- 思考：用户需要入口访问功能吗？（Web/移动/桌面/CLI）
- 如需要：创建导航US描述用户如何访问各项功能

**执行要点**：
- 业务需求清晰：愿景目标、成功指标建立对齐关系，支持项目决策跟踪
- 用户故事采用Story为中心的传统层次：Story是工作基本单位和价值载体，Feature作为Story分组工具（中等复杂度时引入），Epic作为Feature上级组织工具（高度复杂时引入）
- Epic定义原则：传统敏捷方法中的最高层主题组织工具，用于组织多个相关Feature，仅在高复杂度项目中使用，不承载具体工作内容
- Feature定义原则：传统敏捷方法中的功能域分组工具，用于组织多个相关Story，仅在中等复杂度及以上项目中使用，不承载具体工作内容
- Story核心原则：传统敏捷方法的核心工作单位，始终承载具体用户价值和工作内容，严格遵循INVEST六维评价标准，是唯一的实际工作载体
- 用例文档规范：前置条件+主流程+异常流程+后置条件，与用户故事双向对齐
- 非功能需求管理：性能、安全、合规需求分类管理，量化指标明确
- 验收标准体系：采用传统BDD/Gherkin完整语法（Feature-Background-Scenario-ScenarioOutline-Examples）或简化Given-When-Then格式，覆盖正常/异常/边界场景，支持直接转化为自动化测试
- 需求追溯管理：需求矩阵建立，变更影响可追踪，覆盖度检测
- 用户故事INVEST传统六维评价：
  • Independent(独立性): Story之间在技术和业务上保持独立，减少依赖
  • Negotiable(可协商): Story的范围和实现方式可以在开发过程中调整
  • Valuable(价值性): 每个Story都必须为用户或业务带来明确价值
  • Estimable(可估算): Story的工作量和复杂度可以被团队估算
  • Small(小颗粒): Story的大小适合在一个迭代周期内完成
  • Testable(可测试): Story包含明确的验收标准，可以验证完成情况

**质量标准**：专业分类体系完整，用户故事INVEST质量保证，项目追溯清晰可管

**L3业务语言分类原则 + 追溯体系**：
- 系统化分层组织必须使用业务术语
- 用户故事采用EPIC→FEAT→STORY三层追溯结构
- 每个Story必须有追溯ID（如EPIC-AUTH→FEAT-LOGIN→STORY-001）
- 避免技术模块命名（如"API层"、"数据层"）
- 分类名称审计人员/合规人员可理解
- 建立完整追溯矩阵，支持STORY→TEST映射
</categorization-granularity>
<interconnection-complexity>
**关联策略**：专业需求关联管理，支持项目追溯和变更影响分析
**执行要点**：
- 纵向追溯：业务目标→用户故事→验收标准→测试用例清晰链条
- 横向关联：用户故事与用例文档对齐，非功能需求关联映射
- 需求矩阵：需求-测试-验收三维对应，确保覆盖完整性
- 变更管理：影响分析和传播路径评估，支持项目控制
**质量标准**：需求关联清晰完整，项目追溯可管理，支持团队协作和变更控制

**向DESIGN阶段传递策略**：统一传递格式："[REQ-L3-VERSION]/[user_stories_file] → [DES-L3-VERSION]/[architecture_file] 架构设计决策 → [component_design_file] 组件设计"，传递清单包括用户故事INVEST评价结果、验收标准Given-When-Then格式、需求追溯矩阵（EPIC-XXX→FEAT-XXX→STORY-XXX），确保DESIGN阶段基于传统需求层次进行架构设计

**传统追溯机制**：
- **Story中心原则**：User Story是唯一的工作基本单位和价值载体，在INVEST评价时保持核心地位，Feature/Epic仅作上级组织工具
- **单向层次组织**：Epic→Feature→Story单向组织关系，简单项目用Story平铺，中等复杂引入Feature分组Story，高度复杂使用Epic分组Feature分组Story
- **验收标准对应**：确保Given-When-Then格式直接支持传统测试用例编写和BDD实践
</interconnection-complexity>
<content-depth>
**内容策略**：专业需求内容管理，支持严格质量控制的项目实践，集成INVEST质量保证
**执行要点**：
- 业务需求内容：项目愿景、SMART目标定义、KPI指标体系、成功标准
- 用户故事内容：每个故事包含INVEST完整评价，角色-需求-价值清晰映射
- 用例文档内容：前置条件、主流程、异常处理、后置条件，与用户故事对齐
- 非功能需求内容：性能指标、安全要求、合规检查，量化标准明确
- 验收标准内容：Given-When-Then测试场景，覆盖正常/异常/边界情况
**质量标准**：内容充实支持项目实践，INVEST质量全覆盖，需求追溯可管理

**业务语言强制要求 + INVEST严格评价**：
- 每个需求描述必须用业务语言表达，并附带追溯ID
- 每个Story必须通过严格INVEST六维评价（100%通过标准）
- 技术实现方式严禁出现在需求文档中
- 审计人员/合规人员可读性和追溯性是第一质量标准
- L3严格控制中，需求质量和追溯完整性直接影响审计就绪性
</content-depth>
<formalization-level>
**形式化策略**：专业规范化格式，集成INVEST评价流程，支持严格质量控制的项目管理
**执行要点**：
- L3需求精研执行技巧：业务需求理解(愿景对齐+KPI体系)→INVEST用户故事评价→验收标准定义→质量门禁(需求追溯完整性验证)
- C3-LEAD模式协作："我要控制"=用户主导设定项目标准→AI执行需求分析→用户验证项目成果
- 检查点设置：INVEST评价完整性→需求追溯可管理性→专业实践标准化
- 规范化模板：业务需求、用户故事、用例文档、验收标准统一格式
**质量标准**：需求追溯可管理性优先，规范化程度支持项目协作，专业工程实践标准化

**⭐ Artifact ID分配**: 保持现有artifact ID不变(确保引用完整性)，仅对新增artifact扫描宿主文件同PREFIX+SN，取max序号+1分配新ID

**结构准确性检查**：是否采用L3标准的专业需求分类体系？是否包含业务需求、用户故事、用例文档、验收标准、非功能需求五个核心类别？是否集成完整INVEST评价体系？
</formalization-level>

**⚡ 执行技巧集成**
**L3需求精研执行技巧**：
1. **业务需求理解** - 战略对齐，量化目标，KPI体系，血缘追踪深度→建立业务-功能-技术三层对齐，确保战略一致性
2. **验收标准定义** - 验证矩阵，测试场景库，全链路追溯→三维映射矩阵，自动化验收，质量指标追踪
3. **边缘情况考虑** - 威胁模型，合规风险，性能边界，异常处理→专业化风险评估，缓解措施，应急预案
4. **质量门禁机制** - 核心检查点：血缘追溯完整性→决策可审计性→专业实践规范性，协作流程：用户制定血缘追溯标准→AI执行→用户审批确认，执行流程：用户主导制定细粒度分类标准→严格按照执行→用户多维审批后进入DESIGN阶段，通过标准："分类体系是否完整？血缘追溯是否清晰？决策记录是否可审计？"

**认知补强要点**：C3-LEAD模式协作精髓"我要控制" = 用户制定血缘追溯标准 + AI记录决策来龙去脉 + 用户验证可审计性，L3核心特征对齐：质量控制偏好（严格控制，完整追溯每个决策）、协作风格（主导标准制定，深度参与质量把控）、交付节奏（确保质量，不妥协追溯完整性）、适用场景（任意规模团队，偏好极致质量控制），L3核心价值：血缘追溯（每个决策的来龙去脉）、完整记录（知识的系统化沉淀）、可审计性（第三方可验证）、形式规范（专业的工程实践），选择L3的适用场景：任意规模团队，偏好极致质量控制的用户的最佳选择，选择L3的核心标准：需要完整决策追溯、系统化知识沉淀、第三方审计验证和专业规范工程管理
</craft-requirements-req1-l3>

<craft-requirements-req2-l3>
**需求精研_要求2_需求格式** L3需求精研：

<requirement-structure>
**组织策略**：用户故事为核心的传统需求结构体系，Story始终是工作基本单位，Feature/Epic作为复杂度管理的组织工具，集成完整INVEST评价，按项目复杂度选择层次：简单项目Story平铺组织，中等复杂Story+Feature组织，高度复杂Story+Feature+Epic组织，支持传统项目管理和需求追溯
**执行要点**：
- 用户故事模板：As a [用户角色], I want [功能需求], So that [业务价值]
- 完整Gherkin格式选项：可选择Feature-Scenario-Given-When-Then完整结构，或根据需求复杂度降级使用
- 完整INVEST评价：每个用户故事必须通过Independent(独立性)、Negotiable(可协商)、Valuable(价值性)、Estimable(可估算)、Small(小颗粒)、Testable(可测试)六维评价
- 业务需求→功能需求对齐，项目目标可追溯，支持决策跟踪
**方法论基础**：用户故事映射(按需求复杂度选择层次体系)、场景化需求描述(完整场景覆盖+异常流程)、业务领域边界界定、需求追溯验证(完整INVEST评价)、完整项目追溯链管理
**质量标准**：用户故事100%通过INVEST评价，结构清晰完整，支持专业项目实践
</requirement-structure>
<format-standards>
**格式策略**：完整Gherkin语法规范+用户故事模板，支持灵活选择，集成元数据和版本控制
**执行要点**：
- 提供传统BDD/Gherkin完整语法模板：Feature-Background-Scenario-ScenarioOutline-Examples全语法支持
- Story中心的Gherkin集成：Story作为工作基本单位，每个Story对应具体Scenario，Feature作为相关Story的分组容器
- 传统Gherkin层次结构：
  • Feature: 功能域描述（可选，仅在复杂项目中使用）
  • Background: 公共前置条件（可选）
  • Scenario: 对应User Story的具体场景（必需）
  • Scenario Outline + Examples: 参数化测试（高级特性）
- 灵活选择机制：根据项目复杂度可选简化Given-When-Then格式或完整Gherkin语法
**质量标准**：格式选择灵活，Gherkin规范严格，支持专业项目管理和可追溯性
</format-standards>
<expression-quality>
**质量策略**：采用传统BDD严格规范，传统追溯矩阵优先，格式服务于传统质量控制需求
**执行要点**：根据需求复杂度选择Gherkin完整语法或Given-When-Then简化格式，但始终保持Story中心地位和传统追溯关系
**质量标准**：表达方式遵循传统软件工程规范，传统追溯矩阵完整，支持传统项目管理和质量控制
</expression-quality>
</craft-requirements-req2-l3>

<craft-requirements-req3-l3>
**需求精研_要求3_验收标准** L3需求精研：

<validation-approach>
**验证策略**：完整项目追溯验收标准，验证矩阵全覆盖，测试场景支持专业验证
**执行要点**：验收标准专业化管理，按验收类型组织，支持专业导航和项目验证
**质量标准**：验证方法系统完整，项目追溯清晰，支持团队协作验证
</validation-approach>
<acceptance-criteria>
**标准策略**：完整Gherkin验收场景+传统验收标准，多维体系支撑项目管理，全覆盖追溯质量指标
**执行要点**：可选择完整Feature-Scenario格式或基础Given-When-Then格式，按需求复杂度灵活选择
**质量标准**：验收场景规范完整，格式选择适配项目需求，直接指导专业验收测试
</acceptance-criteria>
<testing-alignment>
**对齐策略**：完整Gherkin直转自动化测试，专业验收标准制定，需求关联清晰的矩阵依赖
**执行要点**：Gherkin格式可直接转化为自动化测试脚本，传统验收标准转化为测试用例
**质量标准**：对齐机制专业规范，支持完整的自动化测试链条和项目追溯管理
</testing-alignment>
</craft-requirements-req3-l3>

<craft-requirements-req4-l3>
**需求精研_要求4_质量标准** L3需求精研：

<completeness-control>
**完整性策略**：业务战略对齐完整追溯，功能体系支撑专业审计，血缘追溯支持第三方验证
**执行要点**：
- 业务层完整性：战略目标对齐、功能需求体系完整、KPI指标监控全覆盖
- 非功能评估：性能、安全、合规要求达到严格质量控制标准，支持合规审查
- 质量管理体系：专业化文档管理，按质量类型深层组织，支持专业导航
- 血缘追溯体系：全链路可验证，决策来龙去脉可审计，支持独立第三方验证
**质量标准**：完整性检查严格全面，支持专业团队深度掌握，血缘追溯体系可审计

**应用集成需求识别**（⭐ 有用户交互界面的项目）：
- 💡 **思考点**：多功能应用如何让用户访问各项功能？
- 💡 **适用判断**：项目有用户交互界面（Web/移动/桌面/CLI）
- 💡 **验收标准**：用户能方便地发现和访问所有功能
- **审计要求**：导航/可用性需求的决策理由需完整记录，支持第三方验证
- **建议**：创建导航/可用性User Story（如US-NAV-001），建立完整的需求追溯链
</completeness-control>
<consistency-check>
**一致性策略**：专业质量标准分类，项目追溯完整性优先，实用性重于流程完美
**执行要点**：
- 专业术语统一：业务概念、技术名词、流程标准在项目文档中保持一致
- 逻辑一致性：业务目标→用户故事→验收标准逻辑链条清晰对应
- 需求关联一致：质量标准与需求、验收、INVEST评价全链路对齐，支持传统软件工程追溯需要
- 传统追溯一致性：用户故事的颗粒度与验收标准保持一致，支持EPIC-XXX→FEAT-XXX→STORY-XXX→TEST-XXX传统追溯矩阵
- 格式规范统一：模板结构、元数据格式、版本控制在所有文档中保持一致
**质量标准**：一致性检查严格全面，需求追溯网络可管理，支持团队协作和项目交付

**变更管理整合内容**：C3-LEAD模式多检查点，"我要控制"的项目追溯管理机制，用户主导的专业协作流程
**变更执行要点**：
- 规范化流程：文档元数据、版本控制、审批流程完整体系
- 专业检查点：INVEST评价完整性、需求追溯可管理性、专业实践标准化验证
- 用户主导标准：用户设定项目追溯标准→严格执行→用户验证项目成果
- 专业协作支持：支持专业团队严格质量评估和项目交付验收
**变更质量标准**：变更管理专业全面，质量检查严格，确保专业工程实践标准化
</consistency-check>
<stage-verbatim-directive>
**【需求阶段L3 MD文件的质量控制】**

- **适用范围**: 仅对spec/目录下非_前缀的MD文件生效（排除_开头的目录和文件）
- **长度控制**: 600-800行限制，严格分层次控制
- **补丁保护**: 修改后验证严格完整性要求，专业一致性保护
- **质量预防**: 严格信息密度控制，规范化结构管理，术语专业化
- **阶段特异**: 业务价值完整性，需求覆盖度充分

**自检清单**:
  - □ 内容组织是否专业完整？
  - □ 文档结构是否支持专业审计？
  - □ 业务需求理解是否充分？
  - □ 验收标准是否可测试？

- **修正触发**: 发现问题立即停止，然后让Human-in-the-loop，建议审查、整理和修复
</stage-verbatim-directive>
</craft-requirements-req4-l3>
