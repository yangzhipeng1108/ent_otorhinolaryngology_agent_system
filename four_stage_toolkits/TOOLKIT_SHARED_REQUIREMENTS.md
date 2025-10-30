# 🔧 TOOLKIT_SHARED_REQUIREMENTS - 需求阶段跨Level共性工具

⚠️ **执行约束**：本文件为AI Agent的强制执行指令，不可用AI自己的理解替代

## 共性命令调用验证清单

在执行任何共性>>命令前，AI Agent必须验证以下条件：
- [ ] 用户是否使用>>草稿创建、>>草稿推敲、>>草稿定稿格式命令？
- [ ] 用户是否在使用SPEC生成的GUIDE？
- [ ] 当前上下文是否为REQUIREMENTS阶段？
- [ ] 是否已完整读取本文件内容和对应Level配置？
- ℹ️ Level 具体要求由当前 `SPEC_PRJ_LEVEL`、对应的 `TOOLKIT_L{1|2|3}_REQUIREMENTS.md` 与 `CONSTRAINT_L{1|2|3}_REQUIREMENTS.md` 提供，本文件仅定义共享命令语义。

✅ **只有全部通过才能执行工具**

## 共性命令响应协议

**检测到>>草稿创建** → 执行draft_lifecycle：草稿全生命周期管理
**检测到>>草稿推敲** → 执行draft_analysis：草稿深度分析和优化
**检测到>>草稿定稿** → 执行draft_finalize：草稿正式化转换

---

<!-- COMMAND_START:draft_lifecycle -->
## >>草稿创建 - 草稿全生命周期管理

### 🤖 AI Agent标准响应模板
```
🤖 检测到强制工具调用：>>草稿创建
📂 正在读取：TOOLKIT_SHARED_REQUIREMENTS.md + Level配置
📋 执行草稿管理：{LEVEL}模式（依 Level 工具包 / CONSTRAINT 指南确定细度）
🔍 操作模式：智能判断（创建/更新/澄清）
[严格按TOOLKIT文件内容执行，不添加自己的理解]
```

### 智能操作判断逻辑

#### 🆕 创建模式（工作区不存在）
**触发**：`>>草稿创建:主题名` 且 requirements 草稿目录（参考 CRAFT 示意，如 `spec/requirements/_draft_{topic}/`）不存在
**操作**：创建工作区 → 生成initial_notes.md和draft_v1.md → 基于Level配置生成澄清问题 → 状态跟踪

#### 🔄 更新模式（工作区存在）
**触发**：`>>草稿创建:主题名 "新信息"` 且工作区存在
**操作**：版本管理(draft_v{N+1}.md) → 内容融合 → 变更追踪 → 澄清更新

#### ❓ 澄清模式（仅查看状态）
**触发**：`>>草稿创建:主题名` 且工作区存在但无新信息
**操作**：状态展示 → 澄清建议 → 下一步指导

### 草稿结构模板

#### initial_notes.md模板
```markdown
---
draft_id: draft_{timestamp}
title: "{主题名}"
status: active
created: {timestamp}
stakeholders: []
priority: medium
---

# 需求初始记录：{主题名}
## 🎯 原始描述
{用户的原始输入}

## 📝 初步理解
### 可能的用户角色
- 
### 核心功能猜测
- 
### 业务价值假设
- 

## ❓ 待澄清的关键问题
{基于当前 Level 工具包/质量约束生成的初始澄清问题}
```

### 澄清问题分类框架
**🔴 关键问题（必须澄清）**：用户角色和使用场景不明确、核心功能边界模糊、业务流程缺失关键步骤、与现有系统的集成点不清楚
**🟡 重要问题（建议澄清）**：非功能性需求、异常场景处理、数据来源和格式、用户权限和访问控制
**🟢 细节问题（可选澄清）**：用户界面偏好、数据展示格式、操作便利性优化、未来扩展可能性

### 输出格式
```
✅ 草稿操作完成：{操作类型}
📁 工作区：参考 CRAFT 草稿目录命名（示例：`spec/requirements/_draft_{topic_en}/`）
📄 当前版本：draft_v{N}.md
❓ 澄清问题：🔴{数量}个 🟡{数量}个 🟢{数量}个
💡 下一步建议：澄清关键问题 → >>草稿推敲:{主题名} → >>草稿定稿:{主题名}
```
<!-- COMMAND_END:draft_lifecycle -->

---

<!-- COMMAND_START:draft_analysis -->
## >>草稿推敲 - 草稿深度分析和优化

### 🤖 AI Agent标准响应模板
```
🤖 检测到强制工具调用：>>草稿推敲
📂 正在读取：TOOLKIT_SHARED_REQUIREMENTS.md + Level配置  
📋 执行推敲分析：{LEVEL}深度
🔍 分析范围：草稿完整性、一致性、可行性分析
[严格按TOOLKIT文件内容执行，不添加自己的理解]
```

### 推敲分析维度

**📋 完整性分析**：用户角色完整性、功能覆盖完整性、业务流程完整性、验收标准完整性
**🔗 一致性分析**：术语一致性、逻辑一致性、角色一致性、流程一致性
**⚡ 可行性分析**：技术可行性预警、业务可行性、资源可行性、时间可行性

### 输出格式
```
🔍 推敲分析完成：
📊 完整性评分：{score}/100 | 一致性评分：{score}/100 | 可行性评分：{score}/100

💡 优化建议：
1. {建议类型}：{具体建议}
2. {建议类型}：{具体建议}

🎯 推敲总结：总体质量{excellent/good/needs_improvement} | 关键问题{数量}个 | 建议优先级{high/medium/low}
💡 下一步建议：根据分析结果完善草稿内容，准备就绪后使用 >>草稿定稿:{主题名}
```
<!-- COMMAND_END:draft_analysis -->

---

<!-- COMMAND_START:draft_finalize -->
## >>草稿定稿 - 草稿正式化转换

### 🤖 AI Agent标准响应模板
```
🤖 检测到强制工具调用：>>草稿定稿
📂 正在读取：TOOLKIT_SHARED_REQUIREMENTS.md + Level配置
📋 执行定稿转换：{LEVEL}标准
🔍 转换范围：草稿→正式User Story + Acceptance Criteria
[严格按TOOLKIT文件内容执行，不添加自己的理解]
```

### 定稿转换流程

**📋 前置质量检查**：草稿完整性、澄清完成度、一致性检查、Level标准符合性

**🔄 格式标准化转换**：
- User Story生成：As-Want-So格式 + Front Matter(id/sn/title/status/priority/created/source_draft)
- Acceptance Criteria生成：Given-When-Then格式 + Front Matter(id/sn/source_us/title/status/created)

**🔗 追溯链建立**：SN一致性、派生关系(AC→US)、版本追溯(来源草稿draft_id)

**🧪 集成质量检查**：定稿完成后自动执行对应Level的扫描命令(L1:>>req_scan_l1, L2:>>req_scan_l2, L3:>>req_scan_l3)

### 工作区管理选项
完成后选项：1.保留工作区（如 `spec/requirements/_draft_{topic}/`）2.归档至 `_archive` 目录 3.删除工作区

### 输出格式
```
📋 定稿转换完成：
✅ 生成文档：📄 User Story: user_story_{主题名}.md (US-{id}) | 📋 Acceptance Criteria: acceptance_criteria_{主题名}.md (AC-{id1}, AC-{id2})
🔗 追溯链建立：SN: {semantic_number} | 派生关系: AC → US-{id} | 来源草稿: draft_{timestamp}
🧪 质量检查：{按当前 Level 工具包约定触发的扫描命令执行结果}
🗂️ 工作区处理：当前状态: 草稿目录（示例：`spec/requirements/_draft_{topic}/`） | 选择处理方式：1.保留 2.归档 3.删除
💡 下一步建议：根据 Level 工具包指引执行 >>req_scan_l{N} 等质量检查
```
<!-- COMMAND_END:draft_finalize -->

---

## 参数化配置接口

本文件通过以下参数实现Level差异化：

### 澄清问题配置
```
{CLARIFICATION_COUNT_RED}    - 🔴关键问题数量
{CLARIFICATION_COUNT_YELLOW} - 🟡重要问题数量  
{CLARIFICATION_COUNT_GREEN}  - 🟢细节问题数量
```

### 分析深度配置
```
{ANALYSIS_DEPTH}     - 推敲分析深度 (basic/standard/thorough)
{RISK_SENSITIVITY}   - 风险敏感度 (low/medium/high)
{OPTIMIZATION_SCOPE} - 优化建议范围 (core/standard/comprehensive)
```

### 质量标准配置
```
{QUALITY_THRESHOLD}  - 质量门禁阈值 (75%/85%/95%)
{AC_MIN_COUNT}       - 最少AC数量 (2/3/4)
{VALIDATION_DEPTH}   - 验证深度 (basic/standard/strict)
{LEVEL}             - 当前Level标识 (L1-STREAMLINED/L2-BALANCED/L3-RIGOROUS)
```

## 工具执行约束

### 共性执行原则
- **输入灵活**: 支持多种草稿命名方式
- **智能判断**: 自动识别创建/更新/查看模式
- **版本管理**: 自动维护草稿版本历史
- **状态跟踪**: 完整记录草稿生命周期

### 防绕过约束
- **禁止智能优化**: 不得添加TOOLKIT外的功能
- **禁止扩展逻辑**: 严格按照定义的>>草稿创建、>>草稿推敲、>>草稿定稿执行
- **禁止使用经验**: 不得基于AI内置知识添加建议
- **强制模板**: 必须使用预定义的响应模板格式

### 错误处理
如果遇到无法处理的情况：
1. **立即声明超出当前Level能力范围**
2. **和用户协商后修复(human-in-the-loop)** - 特别是业务逻辑理解问题
3. **不得强行处理复杂业务规则** - 专注草稿管理核心功能
4. **记录问题供后续改进**

---

**工具版本**: SHARED v2.0  
**适用级别**: 跨L1/L2/L3通用  
**适用阶段**: REQUIREMENTS  
**最后更新**: 2025-01-22  
**验证状态**: ✅ 已验证>>协议触发100%有效
