---
id: US-TRIAGE-001
sn: TRIAGE
status: active
related_ac: [AC-TRIAGE-001, AC-TRIAGE-002]
---

# US-TRIAGE-001 智能导诊与预问诊功能

**As a** 患者
**I want** 通过多轮交互式问诊向系统描述我的症状
**So that** 系统能够智能推荐合适的就诊科室并收集完整的病情信息

## 基础场景描述
**Given** 患者访问智能导诊系统
**When** 患者通过语音或文字输入症状信息
**Then** 系统应该模拟医生临床思维进行多轮提问并推荐科室

## INVEST评价 (初步)
- ✅ **Independent**: 独立的导诊预问诊功能
- ✅ **Valuable**: 为患者提供精准分诊价值，提升就医效率
- ✅ **Estimable**: 可估算为高复杂度（涉及AI对话和医学推理）

---

---
id: US-DIAGNOSIS-001
sn: DIAGNOSIS
status: active
related_ac: [AC-DIAGNOSIS-001, AC-DIAGNOSIS-002]
---

# US-DIAGNOSIS-001 辅助诊断功能

**As a** 医生
**I want** 系统基于患者症状和病史提供初步诊断建议
**So that** 我可以获得诊断参考，提高诊断准确性和效率

## 基础场景描述
**Given** 医生查看患者的完整问诊记录
**When** 医生请求辅助诊断建议
**Then** 系统应该分析患者信息并生成初步诊断建议

## INVEST评价 (初步)
- ✅ **Independent**: 独立的辅助诊断功能
- ✅ **Valuable**: 为医生提供诊断决策支持价值
- ✅ **Estimable**: 可估算为高复杂度（涉及医学AI和数据分析）

---

## 功能模块组织

### Feature: 智能导诊模块
- US-TRIAGE-001: 智能导诊与预问诊功能

### Feature: 辅助诊断模块  
- US-DIAGNOSIS-001: 辅助诊断功能

> 📝 **文档状态**: 文档已搭建，等待后续设计完善
