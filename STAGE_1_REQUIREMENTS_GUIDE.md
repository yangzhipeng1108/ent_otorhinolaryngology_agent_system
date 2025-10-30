# STAGE 1 – REQUIREMENTS 精要指南

> **阶段边界**: 需求推敲阶段，仅处理业务语义与验收口径，**禁止**代码、框架或环境操作  
> **执行模式**: 哼将（创作）+ 哈将（验收）双轨协同，结果必须满足 ACA 宪章与 Lx 级别标准  
> **权威入口**: `four_stage_crafting/CRAFT_L2_REQUIREMENTS.md` · `four_stage_constraints/CONSTRAINT_L2_REQUIREMENTS.md`
> **ACA宪章**: `agentic_spec/SPEC_ACA_L2_CHARTER.md`

---

## 使用须知
- 先快速浏览本指南，锁定文档结构与质量门禁，再展开具体推敲  
- 任何详尽条文一律回看 CRAFT/CONSTRAINT 原文；本指南只保存高密度摘要  


## 项目概览
- **项目**: ent_otorhinolaryngology_agent_system_v2
- **约束级别**: L2-BALANCED
- **协作模式**: C2-PARTICIPATE
- **项目描述摘录**: 三甲医院耳鼻喉科智能问诊Agent系统，采用Python+FastAPI+PostgreSQL技术栈和分层架构+微服务设计，通过AI对话技术实现诊前智能导诊与辅助诊断，集成医学推理引擎和对话管理系统，支持Docker容器化部署和Kubernetes编排，提升诊疗效率和准确性，为患者提供24小时服务，减轻医生工作负担，支持HIS/LIS/EMR系统集成，符合医疗AI规范和等保三级要求
- **核心概念必须先读**: `four_stage_constraints/CONSTRAINT_CORE_CONCEPTS.md`

---

## 哼将要点速览（REQUIREMENTS）
> 详解请参阅 `four_stage_crafting/CRAFT_L2_REQUIREMENTS.md`

### Req-1 文档体系
- L2需求精研：5-8个核心维度，功能导向分类，支持团队协作。核心维度：用户故事、验收标准、业务规则、约束条件、接口需求，可选扩展：利益相关者、术语词汇表、非功能需求
- 功能导向分类支持平面或2层结构，组织清晰，支持团队协作
- 功能导向标准分类，用户故事采用Story-Feature混合组织，初步INVEST评价，业务术语分类
- 功能模块双向引用，用户故事↔业务规则↔验收标准形成清晰网络
- 标准化深度，支持团队系统理解业务需求，平衡各角色关注点
- 标准化模板格式，C2-PARTICIPATE模式协作，Feature-Story结构

### Req-2 需求格式
- 用户故事为核心，Story-Feature混合组织，按业务功能域分组，建立功能-角色-价值映射
- 用户故事模板+场景描述模板组合，统一格式标准，灵活平衡
- 内容+场景结构化平衡，适度规范，先理解业务功能再表达

### Req-3 验收口径
- 功能模块验收条件完整覆盖，考虑团队协作责任分工
- 功能模块对齐的标准组织，引入基础Given-When-Then场景描述
- 基础场景到测试用例映射，结构清晰，支持渐进式测试设计

### Req-4 质量基线
- 系统化梳理业务功能模块，平衡团队各角色需求关注点
- 功能模块标准分类，团队理解一致性优先，充实度重于流程完美
- 【需求阶段L2 MD文件的质量控制】- 长度控制：500-600行限制，按模块分段检查，补丁保护，质量预防，阶段特异：业务价值完整性，需求覆盖度充分

---

## 项目特定建议
🎯 针对ent_otorhinolaryngology_agent_system_v2项目REQUIREMENTS阶段的完整方向指导：三甲医院耳鼻喉科智能问诊系统需求复杂度高，建议采用L2-BALANCED标准流程，重点梳理患者端智能导诊、医生端辅助诊断、系统集成的业务需求，确保医疗合规性和用户体验的平衡，建立清晰的功能模块分类和验收标准体系。

---

## 哈将质量门禁（执行顺序）
1. 按 `four_stage_constraints/CONSTRAINT_L2_REQUIREMENTS.md` 的检查点完成逐项验收  
2. 验收报告须覆盖：对象清单 → 判定(✅/❌) → 证据(行号) → 通过率统计 → 结论  
3. 通过率 <0.95 或发现缺陷 → 触发 PDCA 真循环；三轮后仍失败，升级 Human-in-the-loop  
4. 禁止因业务压力跳过验收或降低门槛

---

## 数据流与追溯
- **输入**: 项目简述、协作偏好、spec/spec_variables.md 中的上下文  
- **产出**: `spec/requirements/` 下的用户故事、验收标准、约束文件（保持 SN + source_us 追溯链）  
- **配套登记**: 更新 `spec/spec_changelog.md` 记录关键决策，保持单句核心摘要；必要时同步进度仪表盘

---

## 🔧 质量工具包（L2-BALANCED）

📂 **工具包文件**: `four_stage_toolkits/TOOLKIT_L2_REQUIREMENTS.md`  
🤖 **AI Agent注意**: 用户使用>>命令时，请立即读取上述工具包文件并严格按文件内容执行

### >>命令机制
- 任何以 **>>** 开头的命令都会触发质量工具包
- 具体可用命令请查看上述工具包文件
