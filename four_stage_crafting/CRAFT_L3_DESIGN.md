# CRAFT_L3_DESIGN L3严格控制指导文档

> 🎯 **系统执行指令**: 架构设计分析场景→DESIGN阶段关联复杂度严格控制指导，完整追溯体系导向
> 📊 **核心聚焦**: 设计架构关联复杂度控制 - 完整追溯体系→系统理解复杂设计追溯→实现质量提升
> 📁 **级别特征**: L3-RIGOROUS (适量专业文档，完整追溯体系，严格控制偏好，适用于任意规模团队)
> 🔧 **协作模式**: C3-LEAD模式("我要控制") - 用户主导制定标准→严格执行→用户最终审批
> ⚡ **体系定位**: 创意激发者，支撑脚手架生产+后期推敲，验收标准由four_stage_constraints定义
> 🏗️ **文档架构**: MD+XML混合设计，核心指导内容全部封装在XML标记内，支持LLM精确提取和Level间无缝切换
## 🔗 命名规范权威引用

> - 核心概念定义见 `../agentic_spec/SPEC_ARTIFACT_NAMING_CORE_CONCEPTS.md` (PREFIX, SN, Front Matter, 追溯链字段)
> - L3 级别执行要求见 `../agentic_spec/SPEC_ARTIFACT_NAMING_L3_AUTHORITY.md` (必填 artifacts, 严格模式, 验收标准)

## 🔗 AICodingAgent规范权威引用

> - **ACA宪法**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md` - 不变量与契约定义 (I1-I4, C1-C3, PDCA)
> - **L3宪章**: `../agentic_spec/SPEC_ACA_L3_CHARTER.md` - L3质量标准 (10-15检查点, 通过率≥95%, 三层追溯)

## 🎯 XML标记体系说明

### 第一级标记 (craft-design-req[1-4]-l3)
**目的**: 包含L3级别DESIGN阶段的**完整指导内容**，作为LLM提取和Level切换的**整体单位**

### 第二级标记 (完整说明)

#### 6个标准维度子标签 (所有阶段通用 - 要求1):
1. `<document-organization>` - **文档组织架构策略**: 该级别需要多少文档、如何配置文档结构、基本协作约束、目录结构展示
2. `<directory-hierarchy>` - **目录层级组织**: 文件夹结构、层级深度控制、文件布局规范、导航方式设计  
3. `<categorization-granularity>` - **分类粒度策略**: 如何分类设计内容、分类细度控制、组织逻辑设计
4. `<interconnection-complexity>` - **关联复杂度管理** [DESIGN主攻]: 文档间引用关系、依赖复杂度、交叉引用策略
5. `<content-depth>` - **内容深度策略**: 每个文档写多少内容、详细程度把握、充实度标准定义
6. `<formalization-level>` - **形式化程度**: 模板规范度、结构严格性、执行技巧、认知要点集成

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

> 📋 **专业工程原则**: L3-RIGOROUS严格控制策略必须建立完整追溯体系，确保专业工程实践
> 🚫 **追溯完整约束**: 避免设计细节缺乏追溯体系，追溯记录需完整系统，支持第三方审计验证
> 💼 **知识沉淀导向**: 平衡专业规范度与可操作性，确保完整追溯体系服务知识系统化沉淀
> 🎯 **专业实践表达**: 使用专业工程实践标准格式，确保追溯记录便于理解和验证

## ⚠️ 重要原则澄清

> 🎯 **维度本质 > 表面形式**: L1/L2/L3的核心是约束复杂度的不同维度，不是具体的文件组织形式
> 📁 **文件/目录是表现**: 文件数量、目录结构只是维度的外在表现，重点是背后的指导价值和复杂度控制
> 🚫 **避免表面约束**: 不要被"血缘追溯网络"、"11个文档"等表面描述约束，关注L3严格专业的维度本质
> ✨ **指导性优先**: CRAFT是创意激发者，松耦合高内聚的指导性存在，而非行为约束者

<craft-design-req1-l3>
**精工设计_要求1_文档体系** L3严格控制：

<document-organization>
**📋 受众定位约束**（DESIGN阶段质量标准）：
- **主要读者**: 技术主管/架构师/PM（理解业务+技术概念）
- **语言要求**: 80%业务语言 + 20%技术概念
- **可读性标准**: PM能理解"做什么"，技术主管能理解"怎么做的思路"
- **L3严格控制**: PM/架构师/开发者都会参与设计讨论，需要业务价值清晰

**🚫 严格禁止的过度技术化内容**：
- **过程式代码**（函数调用、类方法、执行步骤） ← ⚠️ 硬性约束
- 具体技术参数（JWT配置细节、数据库字段类型、端口号、Redis TTL值）
- 框架API调用示例（AuthService.authenticate()、bcrypt.hash()、express.Router()）
- 技术命令和工具（npm命令、bash脚本、SQL语句、Docker命令）
- 过度技术化的架构图（UML类图、时序图、ER图）
- 实现层面的技术细节（线程池大小、内存配置、GC参数）

**✅ 推荐的技术概念表达**：
- 高层架构概念（前后端分离、微服务架构、三层架构、模块化设计）
- 业务组件划分（用户管理模块、任务处理模块、权限控制系统）
- 数据流向描述（用户请求→系统验证→业务处理→结果返回）
- 技术选择理由（从业务角度解释为什么选择某技术栈）
- **声明式代码**（接口契约、数据结构定义、配置文件模板） ← ✅ 容许使用
- 业务友好的技术术语（登录状态、数据存储、消息通知、缓存优化）

**⚖️ 平衡原则**：
- 技术术语必须配业务解释
- 设计决策必须说明业务价值
- L3严格控制中，设计文档需建立完整追溯链条和审计依据
- **技术术语密度 ≤ 20%**（DESIGN阶段约束）

🎯 **核心维度特征**（必须遵循）：
L3必须体现"严格控制，完整追溯"的本质特征
- **复杂度控制**：完整追溯体系，系统化决策记录
- **协作特征**：支持C3-LEAD模式("我要控制")，严格质量控制偏好，专业工程实践
- **质量标准**：决策追溯完整，知识系统化沉淀，第三方可审计，形式规范专业

📋 **推荐实施方案**（可参考调整）：
**⭐ L3-RIGOROUS 设计文档组织架构 - 创建design时的核心指导**：
```
design/                         # 设计文档根目录（完整追溯体系）
├── [architecture_file]           # 系统架构设计（严格标准架构治理）
├── [api_design_file]                   # API设计规范（严格标准交互标准）
├── [data_model_file]            # 数据模型设计（严格标准数据治理）
├── [component_design_file]      # 传统组件架构设计与组件责任边界定义（严格标准决策追溯体系）
├── [interface_contracts_file]   # 交互契约理念（严格标准契约治理）
├── [deployment_design_file]     # 部署架构设计（严格标准环境治理）
├── [system_integration_file]    # 系统集成设计（严格标准集成治理）
├── [security_design_file]       # 安全架构设计（严格标准安全治理）
├── [performance_design_file]    # 性能设计规范（严格标准性能治理）
├── [decision_records_file]      # 架构决策记录（严格标准决策治理）
└── [monitoring_design_file]     # 监控设计架构（严格标准监控治理）
```

**文档组织建议**：适量核心文档（参考范围8-12个），具体数量取决于维度覆盖需要
**策略定位**：严格标准设计完整性，专业工程实践全覆盖，建立完整追溯体系，支持第三方审计验证
**严格控制指导**：适量核心文档，涵盖严格标准设计全维度，建立完整的专业工程追溯体系，包含基础设计文档[architecture_file]、[api_design_file]、[data_model_file]、其中[component_design_file]作为传统组件设计中心，协作治理文档[interface_contracts_file]、[deployment_design_file]，专业工程文档[system_integration_file]、[security_design_file]、[performance_design_file]、[decision_records_file]、[monitoring_design_file]
**质量标准**：专业工程完整性原则，严格标准标准全面覆盖，完整追溯体系，C3-LEAD模式专业深度体验
**灵活性说明**：可根据项目特点调整专业工程文档类别，但需保持完整追溯体系的特征
**多角色协作约束**：L3-RIGOROUS严格控制策略重点确保PM/BA/Dev/Test/Ops/Architect各角色在AI Coding环境下的专业需求，建立完整知识沉淀体系，避免设计细节缺乏追溯，采用AI辅助的专业工程实践标准确保第三方可验证，优先体现完整追溯价值和审计能力，技术细节服务于知识系统化沉淀目标，重点使用各角色都能理解的AI Coding术语，确保完整追溯体系关联复杂度控制清晰可执行

**L3核心理念**：L3不是关于团队大小或公司规模，而是关于：决策追溯（每个决策的来龙去脉）、完整记录（知识的系统化沉淀）、可审计性（第三方可验证）、形式规范（专业的工程实践）

📁 **核心文档组织维度说明** (L3-RIGOROUS特征): 以下帮助理解占位符背后的文件组织思考维度，具体文件组织可灵活适配项目需要

**文档组织原则**:
- **维度优先**: 必需的是覆盖核心维度，文件组织形式灵活
- **完整追溯**: 建立完整决策追溯体系，支持第三方审计
- **专业工程**: 采用专业工程实践标准，支持知识系统化沉淀
- **质量标准**: 适量核心文档（8-12个范围，推荐11个），覆盖设计全维度，建立完整追溯体系

**维度1: 系统架构设计维度 (必需)**
- **对应占位符**: `[architecture_file]`
- **参考示例**: `architecture_design.md` 或 `system_architecture.md`
- **维度职责**: 记录系统架构决策，建立架构ADR体系，支持完整追溯
- **文档组织方式**:
  - 单文件形式: `architecture_design.md` (集成所有架构决策)
  - 分层形式: `architecture_overview.md`, `architecture_decisions.md` (分离概览和决策)
  - 视图分离形式: `architecture_c4_context.md`, `architecture_c4_container.md`, `architecture_c4_component.md` (按C4模型分层)
  - 目录结构形式: `architecture/overview/`, `architecture/decisions/`, `architecture/views/` (专业分类)
- **内容要求**: 系统分层设计、架构决策ADR格式、完整追溯矩阵、SOLID原则应用
- **L3特征**: 架构决策完整ADR记录，建立架构-组件-API追溯链，支持第三方审计验证

**维度2: API设计规范维度 (必需)**
- **对应占位符**: `[api_design_file]`
- **参考示例**: `api_design.md` 或 `api_specifications.md`
- **维度职责**: 定义API设计规范，建立API契约和版本演进追溯
- **文档组织方式**:
  - 单文件形式: `api_design.md` (集成所有API规范)
  - 模块分离形式: `api_auth.md`, `api_business.md`, `api_admin.md` (按业务模块)
  - RESTful分层形式: `api_resources.md`, `api_endpoints.md`, `api_contracts.md` (按API层次)
  - 目录结构形式: `api/resources/`, `api/contracts/`, `api/versioning/` (专业分类)
- **内容要求**: RESTful/GraphQL规范、API契约定义、版本演进策略、与数据模型追溯关系
- **L3特征**: API-需求-数据模型双向追溯矩阵，版本演进影响分析，支持契约测试

**维度3: 数据模型设计维度 (必需)**
- **对应占位符**: `[data_model_file]`
- **参考示例**: `data_model.md` 或 `database_design.md`
- **维度职责**: 定义数据模型设计，建立数据血缘追溯体系
- **文档组织方式**:
  - 单文件形式: `data_model.md` (集成所有数据模型)
  - 领域分离形式: `data_model_user.md`, `data_model_order.md` (按领域模型)
  - 分层形式: `data_model_conceptual.md`, `data_model_logical.md`, `data_model_physical.md` (三层模型)
  - 目录结构形式: `data_model/domains/`, `data_model/relations/`, `data_model/migrations/` (专业分类)
- **内容要求**: 实体关系图、数据字典、迁移策略、数据变更影响追溯
- **L3特征**: 数据变更完整影响追踪，数据血缘专业审计，支持数据治理

**维度4: 组件设计维度 (必需)**
- **对应占位符**: `[component_design_file]`
- **参考示例**: `component_design.md` 或 `component_architecture.md`
- **维度职责**: 定义组件架构和责任边界，建立Story-组件-实现追溯链
- **文档组织方式**:
  - 单文件形式: `component_design.md` (集成所有组件设计)
  - 层次分离形式: `components_presentation.md`, `components_business.md`, `components_data.md` (按架构层次)
  - 模块分离形式: `components_auth.md`, `components_order.md` (按业务模块)
  - 目录结构形式: `components/frontend/`, `components/backend/`, `components/shared/` (专业分类)
- **内容要求**: 组件责任定义、SOLID原则应用、组件依赖矩阵、US→DES→CMP追溯
- **L3特征**: 组件架构完整定义，US→DES→CMP追溯矩阵，支持TDD测试策略
- **L3 Front Matter格式示例**:
  ```yaml
  # DES (Design Document) - 设计文档
  ---
  id: DES-AUTH-010
  sn: AUTH
  status: approved
  owner: @architect-team
  version: v1.0.0
  source_us: US-AUTH-002
  related_adr: [ADR-AUTH-025]
  related_cmp: [CMP-AUTH-015]
  related_api: [API-AUTH-020]
  ---
  
  # Design Document: 认证系统架构设计
  
  ## 1. 架构概述
  基于 US-AUTH-002 的需求，设计无状态认证架构...
  ```
  
  ```yaml
  # ADR (Architecture Decision Record) - 架构决策记录 (L3核心特性)
  ---
  id: ADR-AUTH-025
  sn: AUTH
  status: accepted
  owner: @architect-lead
  version: v1.0.0
  date: 2025-01-15
  decision: 采用JWT进行无状态认证
  alternatives:
    - Session-based认证
    - OAuth 2.0
  consequences:
    - 优势: 无状态、可扩展、跨域支持
    - 劣势: Token过期管理复杂
    - 影响: 需要Redis存储黑名单
  related_des: [DES-AUTH-010]
  # 注：ADR↔DES双向追溯，L3审计级特性
  ---
  ```
  
  ```yaml
  # CMP (Component Specification) - 组件规格
  ---
  id: CMP-AUTH-015
  sn: AUTH
  status: active
  owner: @dev-team-auth
  version: v1.2.0
  source_des: DES-AUTH-010
  related_api: [API-AUTH-020]
  ---
  ```
  
  ```yaml
  # API (API Specification) - API规格
  ---
  id: API-AUTH-020
  sn: AUTH
  status: active
  owner: @api-team
  version: v1.1.0
  source_des: DES-AUTH-010
  related_cmp: [CMP-AUTH-015]
  ---
  ```

**维度5: 接口契约维度 (必需)**
- **对应占位符**: `[interface_contracts_file]`
- **参考示例**: `interface_contracts.md` 或 `api_contracts.md`
- **维度职责**: 定义接口契约规范，建立契约-API-组件追溯关系
- **文档组织方式**:
  - 单文件形式: `interface_contracts.md` (集成所有契约)
  - 系统分离形式: `contracts_internal.md`, `contracts_external.md` (内外部分离)
  - 协议分离形式: `contracts_rest.md`, `contracts_grpc.md`, `contracts_graphql.md` (按协议)
  - 目录结构形式: `contracts/internal/`, `contracts/external/`, `contracts/schemas/` (专业分类)
- **内容要求**: 契约Schema定义、版本兼容策略、契约变更影响分析
- **L3特征**: 契约-API-组件完整追溯矩阵，契约变更版本演进血缘，支持契约测试

**维度6: 部署架构设计维度 (必需)**
- **对应占位符**: `[deployment_design_file]`
- **参考示例**: `deployment_architecture.md` 或 `infrastructure_design.md`
- **维度职责**: 定义部署架构，建立部署-组件映射追溯关系
- **文档组织方式**:
  - 单文件形式: `deployment_architecture.md` (集成所有部署设计)
  - 环境分离形式: `deployment_dev.md`, `deployment_staging.md`, `deployment_prod.md` (按环境)
  - 层次分离形式: `deployment_infrastructure.md`, `deployment_containers.md`, `deployment_orchestration.md` (按层次)
  - 目录结构形式: `deployment/infrastructure/`, `deployment/environments/`, `deployment/ci_cd/` (专业分类)
- **内容要求**: 基础设施定义、容器编排策略、环境配置管理、部署-组件映射关系
- **L3特征**: 部署架构-组件完整映射，基础设施变更影响血缘，支持环境一致性验证

**维度7: 系统集成设计维度 (必需)**
- **对应占位符**: `[system_integration_file]`
- **参考示例**: `system_integration.md` 或 `integration_architecture.md`
- **维度职责**: 定义系统集成策略，建立外部依赖双向追溯关系
- **文档组织方式**:
  - 单文件形式: `system_integration.md` (集成所有集成设计)
  - 系统分离形式: `integration_payment.md`, `integration_auth.md`, `integration_notification.md` (按外部系统)
  - 模式分离形式: `integration_sync.md`, `integration_async.md`, `integration_batch.md` (按集成模式)
  - 目录结构形式: `integration/external_systems/`, `integration/adapters/`, `integration/protocols/` (专业分类)
- **内容要求**: 外部系统依赖、适配器设计、集成协议定义、集成变更影响分析
- **L3特征**: 外部系统双向血缘追溯，集成变更影响传播路径，支持专业审计验证

**维度8: 安全架构设计维度 (必需)**
- **对应占位符**: `[security_design_file]`
- **参考示例**: `security_architecture.md` 或 `security_design.md`
- **维度职责**: 定义安全架构，建立安全设计-架构-数据追溯体系
- **文档组织方式**:
  - 单文件形式: `security_architecture.md` (集成所有安全设计)
  - 层次分离形式: `security_authentication.md`, `security_authorization.md`, `security_encryption.md` (按安全层次)
  - 威胁分离形式: `security_threat_model.md`, `security_mitigation.md`, `security_compliance.md` (按威胁-缓解)
  - 目录结构形式: `security/authentication/`, `security/authorization/`, `security/compliance/` (专业分类)
- **内容要求**: 认证授权架构、威胁模型评估、安全合规标准、安全决策追溯
- **L3特征**: 安全设计-架构-数据血缘追溯，威胁模型完整来龙去脉，支持安全审计

**维度9: 性能设计规范维度 (必需)**
- **对应占位符**: `[performance_design_file]`
- **参考示例**: `performance_design.md` 或 `performance_architecture.md`
- **维度职责**: 定义性能设计策略，建立性能需求-架构追溯关系
- **文档组织方式**:
  - 单文件形式: `performance_design.md` (集成所有性能设计)
  - 维度分离形式: `performance_caching.md`, `performance_scalability.md`, `performance_optimization.md` (按性能维度)
  - 层次分离形式: `performance_application.md`, `performance_database.md`, `performance_infrastructure.md` (按架构层次)
  - 目录结构形式: `performance/strategies/`, `performance/metrics/`, `performance/tuning/` (专业分类)
- **内容要求**: 性能优化策略、缓存架构设计、扩展性设计、性能指标追溯
- **L3特征**: 性能需求-架构设计血缘追溯矩阵，性能优化决策影响传播，支持性能基准验证

**维度10: 架构决策记录维度 (必需)**
- **对应占位符**: `[decision_records_file]`
- **参考示例**: `architecture_decision_records.md` 或 `adr_index.md`
- **维度职责**: 统一记录架构决策ADR，建立决策关联网络和影响追踪
- **文档组织方式**:
  - 单文件形式: `architecture_decision_records.md` (ADR索引和记录)
  - 决策分离形式: `adr_001_database_choice.md`, `adr_002_api_protocol.md` (按ADR编号)
  - 类别分离形式: `adr_architecture.md`, `adr_technology.md`, `adr_process.md` (按决策类别)
  - 目录结构形式: `adr/architecture/`, `adr/technology/`, `adr/superseded/` (专业分类)
- **内容要求**: ADR标准格式、决策背景、备选方案、影响分析、决策关联网络
- **L3特征**: 统一ADR决策记录格式，决策间关联网络和影响追踪，支持决策历史检索

**维度11: 监控设计架构维度 (必需)**
- **对应占位符**: `[monitoring_design_file]`
- **参考示例**: `monitoring_architecture.md` 或 `observability_design.md`
- **维度职责**: 定义监控架构，建立监控-系统架构追溯关系
- **文档组织方式**:
  - 单文件形式: `monitoring_architecture.md` (集成所有监控设计)
  - 维度分离形式: `monitoring_metrics.md`, `monitoring_logging.md`, `monitoring_tracing.md` (三支柱分离)
  - 层次分离形式: `monitoring_application.md`, `monitoring_infrastructure.md`, `monitoring_business.md` (按监控层次)
  - 目录结构形式: `monitoring/metrics/`, `monitoring/logging/`, `monitoring/alerting/` (专业分类)
- **内容要求**: 可观测性三支柱设计、指标定义、告警策略、监控-架构追溯
- **L3特征**: 监控设计-系统架构血缘追溯，监控策略决策依据，支持可观测性验证
</document-organization>

<directory-hierarchy>**策略定位**：完整追溯体系支撑4层深度目录体系和专业化引用网络导航
**严格控制指导**：4层目录深度，支持专业化引用网络和导航，追溯记录体系支撑深层设计文档体系
**质量标准**：目录结构专业规范，便于完整追溯和专业审计，支持完整追溯的深度层级管理</directory-hierarchy>

<categorization-granularity>**设计架构核心定位**：完整追溯体系 - 用系统化决策记录实现设计追溯管理→建立完整决策记录→实现质量提升（核心工作做专业），C3-LEAD模式下严格按照用户制定的决策追溯标准执行，"我要控制" - 用户主导制定决策追溯规范，重点在专业工程实践而非简化妥协

**L3分类粒度策略**：采用完整追溯体系组织设计要素，支持决策记录和知识沉淀，便于第三方审计和专业工程实践，建立全链路影响分析能力

**需求承接策略**：基于REQUIREMENTS阶段的传统设计响应：基于需求细粒度分类的传统追溯设计体系，建立全链路需求→组件→设计传统追踪矩阵；
**L3追溯矩阵格式**: US → AC/DES → CMP/API → [Implementation阶段] (DESIGN阶段止于CMP/API，符合../agentic_spec/SPEC_ARTIFACT_NAMING_L3_AUTHORITY.md)；
**分层追踪管理**：需求变更→设计决策传播分析→组件影响识别→实施策略风险评估→分阶段应对计划

**完整决策追溯（决策来龙去脉记录）精工设计原则**：建立决策追溯的完整记录体系，通过系统化知识沉淀确保每个设计决策的来龙去脉可审计。复杂度控制机制：采用分阶段实施、标准化模板和专业分工，确保第三方可验证的可操作性

**精工设计建议**：
- **[architecture_file]**: 系统架构设计中心化决策追溯 - 建立架构决策的完整ADR记录，追踪每个架构选择的来龙去脉，引用[component_design_file]、[api_design_file]、[system_integration_file]建立血缘追溯链，支持第三方审计验证
- **[api_design_file]**: API设计规范完整决策追踪 - 建立API与需求、数据模型的双向追溯矩阵，记录API版本演进的影响分析，引用[data_model_file]和[interface_contracts_file]确保契约追溯完整
- **[data_model_file]**: 数据模型设计决策基础 - 建立数据变更的完整影响追踪记录，追踪数据结构变更对API和服务的传播路径，支持数据血缘的专业审计
- **[component_design_file]**: 传统组件架构设计+组件责任边界定义 - 核心功能：User Story→组件责任传统转化体系，建立完整的组件架构定义和设计原则（单一责任原则、高内聚低耦合），支持传统架构模式选择，追踪组件与故事、架构、实现的完整决策关系，支持专业审计标准
- **[interface_contracts_file]**: 接口契约决策追溯 - 建立接口契约与API设计、组件实现的追溯矩阵，记录契约变更的影响分析和版本演进血缘
- **[deployment_design_file]**: 部署架构决策追溯 - 建立部署架构与系统组件的完整映射关系，追踪基础设施变更对应用服务的影响血缘
- **[system_integration_file]**: 系统集成决策追溯 - 建立外部系统依赖的双向血缘追溯，记录集成变更的影响传播路径，支持专业审计验证
- **[security_design_file]**: 安全架构决策追溯 - 建立安全设计与架构、数据的血缘追溯，记录安全决策的完整来龙去脉和影响分析
- **[performance_design_file]**: 性能设计决策追溯 - 建立性能需求与架构设计的血缘追溯矩阵，记录性能优化决策的影响传播
- **[decision_records_file]**: 架构决策追溯中心 - 统一的ADR决策记录格式，建立决策间的关联网络和影响传播追踪
- **[monitoring_design_file]**: 监控架构决策追溯 - 建立监控设计与系统架构的血缘追溯，记录监控策略的决策依据和影响分析

**L3特异性检查**：是否包含完整的11个专业文档？是否建立了每个文件的决策追溯体系？是否实现了项目类型智能适配和专业工程能力？是否实现了知识系统化沉淀和全链路审计能力？是否支持C3-LEAD模式专业规范管理和第三方可验证标准？

**与其他维度协同**：
- **文档组织协同** (L3: 专业文档集合)：每个引用网络节点聚焦核心设计维度，通过思考深度而非数量优势体现L3价值，支持血缘追溯规模管理
- **目录层级协同** (L3: 深层规范目录体系)：血缘记录网络支撑深层设计文档体系，4层目录深度，支持专业化引用网络和导航  
- **分类粒度协同** (L3: 细粒度分类)：细粒度分类建立完整的血缘记录网络，引用矩阵支持全链路追溯和影响分析
- **内容深度协同** (L3: 完整详尽内容，深度掌握)：每个引用节点提供完整详尽的专业内容，血缘追溯内容深度支持专业团队深度掌握
- **形式化程度协同** (L3: 规范化，含元数据、版本、审批流)：血缘记录采用高度规范化的格式，包含元数据、版本控制、审批流程的血缘追溯规范

**策略定位**：用完整追溯体系专业化组织实现设计血缘管理，C3-LEAD模式下严格按照用户制定的血缘追溯标准执行
**精工设计指导**：全景引用网络，层级关联管理，支持血缘追溯规范？追踪矩阵，完整追溯，全链路影响分析？网状引用管理，影响传播，版本兼容性？
**质量标准**：完整追溯体系清晰可审计，每个设计决策来龙去脉可验证，支持C3-LEAD模式的用户主导专业规范管理</categorization-granularity>

<interconnection-complexity>**策略定位**：采用完整追溯体系组织设计要素，支持决策记录和知识沉淀，便于第三方审计和专业工程实践，建立全链路影响分析能力

**业务引用原则**：
- 文档间引用使用业务术语，避免纯技术ID
- 示例："基于[用户登录功能]的设计" 而非 "基于API-AUTH-001"
- 引用说明需包含业务上下文和业务价值
- L3完整追溯体系需保持业务可读性，支持第三方审计理解

**具体操作指导**：
- **L3追溯矩阵格式**: US → AC/DES → CMP/API → [Implementation阶段] (L3标准artifacts)
- **L3追溯网络建立**（DESIGN阶段范围）:
  * **需求层**: US-AUTH-002 ↔ 用户故事业务需求定义
  * **验证层**: AC-AUTH-005 ↔ 验收标准
  * **设计层**: DES-AUTH-010 ↔ ADR架构决策记录
  * **组件层**: CMP-AUTH-015 ↔ 组件架构和责任定义
  * **接口层**: API-AUTH-020 ↔ API规格
  * **下游阶段**: → [Implementation阶段BDD测试场景] (未来生成)
- **L3组件追溯示例**（止于DESIGN阶段）:
  * US-AUTH-002/用户登录 → DES-AUTH-010/认证架构(+ADR-AUTH-025) → CMP-AUTH-015/组件 + API-AUTH-020/接口 → [下游Implementation阶段]
- **完整追溯操作流程**:
  1. **需求变更触发**: 识别变更范围和影响边界
  2. **一级影响识别**: 直接关联的设计决策和组件
  3. **二级传播分析**: 间接影响的实现和测试策略
  4. **风险评估矩阵**: 变更风险等级和应对策略
  5. **分阶段应对计划**: 按影响程度制定实施步骤
- **决策审计标准**: 每个决策都有完整的来龙去脉记录，支持第三方独立验证
- **专业工程实践**: 采用业界标准的ADR格式，包含决策背景、备选方案、影响分析、决策原因
- **知识沉淀机制**: 建立决策知识库，支持历史决策的检索和复用

**执行检查点**：
1. 是否建立了完整的11文档血缘追溯网络？
2. 四层追溯网络是否覆盖需求→设计→实现→验证？
3. 决策记录是否支持第三方审计验证？
4. 血缘追溯是否具备专业工程实践标准？
5. 知识沉淀机制是否有效运作？

**质量标准**：决策追溯完整性检验通过，删除引用后仍可追溯80%决策来源，关联逻辑清晰可审计，支持C3-LEAD模式专业规范理解和第三方验证</interconnection-complexity>

<content-depth>**策略定位**：每个决策追溯节点提供完整详尽的专业内容
**精工设计指导**：完整详尽，深度掌握，每个文档支撑专业工程实践，决策追溯内容深度支持专业团队深度掌握，重点关注技术调研工作充实度的完整记录。协同建议：每个决策追溯节点提供完整详尽专业内容
**质量标准**：技术调研的可审计性比文档数量更重要，决策血缘追溯的完整性比结构完美更关键</content-depth>

<formalization-level>**策略定位**：决策记录采用高度规范化的格式，包含元数据、版本控制、审批流程
**精工设计指导**：规范化，含元数据版本审批流，高度规范的决策追溯格式确保专业工程实践。协同建议：决策记录采用高度规范化格式
**质量标准**：专业规范性比便利性更重要，格式标准化支持专业协作效率和第三方审计验证

**⭐ Artifact ID分配**: 保持现有artifact ID不变(确保引用完整性)，仅对新增artifact扫描宿主文件同PREFIX+SN，取max序号+1分配新ID

**L3精工设计执行技巧**：
1. **血缘追溯架构理解** - 全景引用网络，层级关联管理，支持血缘追溯规范→建立架构-详细-决策-集成四层引用网络，确保血缘追溯一致性
2. **血缘关联定义** - 追踪矩阵，完整追溯，全链路影响分析→引用矩阵标准模板，覆盖变更影响和依赖传播
3. **复杂关联考虑** - 网状引用管理，影响传播，版本兼容性→专业化血缘记录体系，缓解措施，应急预案
4. **质量门禁机制** - 核心检查点：血缘记录体系完整→追踪矩阵完善→决策来龙去脉可审计，协作流程：用户主导制定血缘追溯标准→严格按照执行→用户多维审批验证血缘追溯完整性→分阶段确认→专业规范化生产，执行流程：用户主导制定血缘记录标准→严格执行→用户审批后进入IMPLEMENTATION阶段，通过标准："血缘记录体系是否完整？追踪矩阵是否完善可操作？决策来龙去脉是否清晰可审计？"

**认知补强要点**：C3-LEAD模式协作精髓"我要控制" = 用户主导制定血缘追溯标准(适度深度参与) + 严格按标准记录决策来龙去脉 + 用户多维审批验证可审计性，L3核心特征对齐：质量控制偏好（严格控制，完整追溯每个决策）、协作风格（主导标准制定，深度参与质量把控）、交付节奏（确保质量，不妥协追溯完整性）、适用场景（任意规模团队，偏好极致质量控制），血缘追溯网络核心价值：血缘追溯（每个决策来龙去脉）、完整记录（知识系统化沉淀）、可审计性（第三方验证）、形式规范（专业工程实践），L3级专业工程哲学：质量为王，追溯完整胜过便利，系统沉淀胜过快速交付，血缘追溯网络支撑专业实践，选择L3的适用场景：任意规模团队，偏好极致质量控制的用户的最佳选择

**结构准确性检查**：是否采用L3标准的11文档决策追溯网络结构？是否包含完整的11个专业文档：[architecture_file]、[api_design_file]、[data_model_file]、[component_design_file]、[interface_contracts_file]、[deployment_design_file]、[system_integration_file]、[security_design_file]、[performance_design_file]、[decision_records_file]、[monitoring_design_file]？</formalization-level>

**⚡ 执行技巧集成**
**L3精工设计执行技巧**：
1. **血缘追溯架构理解** - 全景引用网络，层级关联管理，支持血缘追溯规范→建立架构-详细-决策-集成四层引用网络，确保血缘追溯一致性
2. **血缘关联定义** - 追踪矩阵，完整追溯，全链路影响分析→引用矩阵标准模板，覆盖变更影响和依赖传播
3. **复杂关联考虑** - 网状引用管理，影响传播，版本兼容性→专业化血缘记录体系，缓解措施，应急预案
4. **质量门禁机制** - 核心检查点：血缘记录体系完整→追踪矩阵完善→决策来龙去脉可审计，协作流程：用户主导制定血缘追溯标准→严格按照执行→用户多维审批验证血缘追溯完整性→分阶段确认→专业规范化生产，执行流程：用户主导制定血缘记录标准→严格执行→用户审批后进入IMPLEMENTATION阶段，通过标准："血缘记录体系是否完整？追踪矩阵是否完善可操作？决策来龙去脉是否清晰可审计？"

**认知补强要点**：C3-LEAD模式协作精髓"我要控制" = 用户主导制定血缘追溯标准(适度深度参与) + 严格按标准记录决策来龙去脉 + 用户多维审批验证可审计性，L3核心特征对齐：质量控制偏好（严格控制，完整追溯每个决策）、协作风格（主导标准制定，深度参与质量把控）、交付节奏（确保质量，不妥协追溯完整性）、适用场景（任意规模团队，偏好极致质量控制），血缘追溯网络核心价值：血缘追溯（每个决策来龙去脉）、完整记录（知识系统化沉淀）、可审计性（第三方验证）、形式规范（专业工程实践），L3级专业工程哲学：质量为王，追溯完整胜过便利，系统沉淀胜过快速交付，血缘追溯网络支撑专业实践，选择L3的适用场景：任意规模团队，偏好极致质量控制的用户的最佳选择
</craft-design-req1-l3>

<craft-design-req2-l3>
**精工设计_要求2_架构表达** L3精工设计：

<architecture-structure>**架构组织策略**：集成SOLID+KISS+DRY原则的系统架构决策记录和完整追溯体系
**执行要点**：
- SOLID架构原则：系统架构遵循单一职责、开闭原则、依赖倒置等核心原则
- KISS原则：架构复杂度可控，避免过度设计和不必要的抽象层
- DRY原则：消除架构中的重复设计，建立可复用的架构组件和模式
- 决策追溯体系：每个架构决策都有完整的来龙去脉记录
**方法论基础**：传统DDD战术设计(完整领域模型设计)、传统C4模型(四层完整架构视图+动态视图)、标准ADR架构决策记录体系、SOLID+KISS+DRY传统原则体系、传统设计模式最佳实践
**质量标准**：架构严格遵循SOLID+KISS+DRY原则，决策追溯完整可审计，支持专业工程实践</architecture-structure>

<component-definition>**组件定义策略**：严格遵循SOLID+KISS+DRY原则的组件边界划分和职责定义
**执行要点**：
- 单一职责严格化：每个组件仅有一个明确的变更理由
- 开闭原则保证：组件概念框架支持扩展但不允许修改现有功能
- 里氏替换严格：组件接口实现可完全替换且行为一致
- 接口隔离强制：严格按客户需求分离接口，禁止臃肿接口
- DRY组件复用：建立可复用组件库，消除重复设计

**L3传统组件设计机制**：
**User Story→组件责任转化体系**：
- **转化原则**：按业务流程分解+组件责任边界+接口定义验证+SOLID原则遵循
- **组件设计标准格式**：
  ```
  CMP-ID: CMP-<SN>-NNN (如：CMP-AUTH-015) - L3标准格式
  Name: 组件名称
  source_des: 关联的Design Document [DES-<SN>-NNN] - L3标准字段
  Responsibility: 组件核心责任定义
  Interface: 对外接口定义和约束  
  Dependencies: 依赖的其他组件
  Implementation_Pattern: 推荐的设计模式
  Quality_Attributes: 性能、安全等质量属性
  Testing_Strategy: 测试策略和验证方法
  ```
- **粒度控制标准**：每个组件应该遵循单一责任原则，具有清晰的边界和接口
- **质量验证**：每个组件必须可独立测试，支持传统TDD测试策略

**L3传统架构模式适配机制**：
- **前端GUI项目传统组件特征**：
  - UI组件：展示组件(Presentational)和容器组件(Container)分离
  - **⭐ 逻辑+视觉混合规格标准**：严格按SOLID原则定义前端GUI组件的逻辑功能与视觉设计统一规格（L3严格审计）
  - **逻辑规格标准**：组件功能、状态管理、事件处理、数据流转的严格边界定义，支持审计追溯
  - **视觉规格标准**：布局结构、样式设计、交互效果、视觉状态变化的技术栈无关严格标准，可第三方验证
  - 状态管理组件：遵循Flux/Redux传统模式
  - 路由组件：单一责任的导航和权限管理
  - 前端信息传递：组件设计→IMPLEMENTATION的组件测试基础
- **后端项目传统组件特征**：
  - 业务服务组件：遵循领域驱动设计(DDD)的服务边界
  - 数据访问组件：Repository模式和DAO模式的传统实现
  - 集成组件：适配器模式和防腐层设计
  - 后端信息传递：组件设计→IMPLEMENTATION的单元测试和集成测试基础

**L3严格标准协作增强**：
- **组件依赖矩阵**：建立清晰的组件依赖关系图，支持团队并行开发
- **跨团队接口契约**：与[interface_contracts_file]的标准化关联
- **组件版本管理**：支持组件独立版本演进和影响分析

**L3专业工程实践增强**：
- **决策追溯体系**：component_design_file的完整ADR决策记录格式
- **审计支持**：第三方可验证的传统组件设计决策链
- **追溯矩阵**：建立组件与US、DES的追溯矩阵(US→DES→CMP/API) - L3标准，下游连接Implementation阶段
- **专业规范**：严格遵循SOLID原则和传统软件工程最佳实践

**质量标准**：组件完全符合SOLID+KISS+DRY传统原则，责任边界清晰可测试，实现传统架构模式适配和专业工程能力，决策追溯完整可审计</component-definition>

<interface-design>**接口设计策略**：基于SOLID+KISS+DRY原则的API设计和契约规范，支持专业工程实践
**执行要点**：
- SOLID接口设计：全面应用单一职责、开闭原则、接口隔离等原则
- KISS原则：接口设计简洁直观，避免复杂的嵌套和多态结构
- DRY原则：建立统一的API模式和可复用的契约组件
- 全链路追溯：建立API与需求、数据模型的完整追溯链路
- 版本演进策略：支持向后兼容的API版本演进和影响分析
**质量标准**：API严格符合SOLID+KISS+DRY原则，契约清晰可测试，追溯关系完整可审计</interface-design>
</craft-design-req2-l3>

<craft-design-req3-l3>
**精工设计_要求3_技术决策** L3精工设计：

<decision-framework>**决策框架策略**：基于SOLID+KISS+DRY原则的专业化技术决策框架，支持第三方审计验证
**执行要点**：
- SOLID导向决策：所有技术选型必须支持SOLID原则，优先选择设计原则友好的技术
- KISS复杂度控制：防止过度工程化，在功能性与简洁性间找到平衡
- DRY原则应用：消除技术栈中的重复方案，建立统一的技本标准
- 专业审计支持：每个决策都有完整的ADR记录和第三方可验证的依据
**质量标准**：决策框架严格符合设计原则，每个决策都可审计可验证，支持专业工程实践</decision-framework>

<alternative-evaluation>**方案评估策略**：系统化备选方案评估，支持专业审计验证
**执行要点**：
- SOLID兼容性评估：评估每个方案对五个SOLID原则的支持程度和实施难度
- KISS复杂度对比：量化各方案的学习曲线、维护成本和认知负荷
- DRY效益分析：评估各方案对重复代码消除和可复用性的支持能力
- 第三方审计：所有评估结果必须可被独立第三方验证和重现
- 量化指标：使用可量化的指标来比较方案优劣
**质量标准**：方案评估全面系统，符合设计原则，评估过程可审计可重现</alternative-evaluation>

<constraint-management>**约束管理策略**：基于SOLID+KISS+DRY原则的专业化约束管理，平衡设计原则与项目约束
**执行要点**：
- SOLID原则不可妥协：在任何情况下都不允许违背五个SOLID原则
- KISS与DRY平衡：在简单性和可复用性间找到适当平衡点
- 约束分级管理：技术约束、业务约束、资源约束、时间约束分级管理
- 首先原则排序：SOLID>业务需求>KISS>DRY>其他约束
- C3-LEAD模式严格审批：用户主导制定所有约束管理标准
**质量标准**：约束管理严格规范，权衡决策有据可查，支持第三方审计验证</constraint-management>
</craft-design-req3-l3>

<craft-design-req4-l3>
**精工设计_要求4_质量标准** L3精工设计：

<design-coherence>**连贯性检查要点**：L3的11个专业文档是否完整？决策记录体系是否完整？追踪矩阵是否完善可操作？决策来龙去脉是否清晰可审计？架构一致性、设计原则统一、逻辑连贯，采用L3标准的11文档决策追溯网络结构：包含基础设计、协作治理、专业工程全维度文档。</design-coherence>

<quality-assurance>**质量保证机制**：血缘追溯网络关联复杂度策略是否具体可执行？"精工设计_要求2_架构表达"标准是否正确实施？设计审查、质量门禁、验收标准，C3-LEAD模式多维检查点验证，血缘追溯规范审批机制，用户主导标准制定协作流程。

**演进支持整合内容**：关联复杂度（主攻维度）的L3精工设计策略是否明确？血缘追溯网络（交叉矩阵，完整追溯）策略是否专业可操作？扩展性设计、维护友好性、演进策略，体现L3-RIGOROUS血缘追溯专业特征，建立完整的血缘记录网络和追溯矩阵，支持C3-LEAD模式规范化管理和深度掌握。提供的血缘追溯记录体系方案具体可执行，L3级执行要点便于实际应用。</quality-assurance>

<stage-verbatim-directive>
**【设计阶段L3 MD文件的质量控制】**

- **适用范围**: 仅对spec/目录下非_前缀的MD文件生效（排除_开头的目录和文件）
- **长度控制**: 600-800行限制，按专业工程模块拆分
- **补丁保护**: 修改后确保完整详尽完整性要求，严格标准一致性保护
- **质量预防**: 严格信息密度专业管理，专业规范结构控制，术语严格标准化
- **阶段特异**: 架构连贯性，技术决策完整追溯，设计决策可审计性

**自检清单**:
  - □ 内容组织是否严格规范专业？
  - □ 文档结构是否支持第三方审计？
  - □ 架构设计是否建立完整追溯体系？
  - □ 技术决策是否来龙去脉清晰可审计？

- **修正触发**: 发现问题立即停止，然后让Human-in-the-loop，建议审查、整理和修复
</stage-verbatim-directive>
</craft-design-req4-l3>
