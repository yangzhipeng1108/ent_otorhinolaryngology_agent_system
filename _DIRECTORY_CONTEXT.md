# 目录上下文定位说明

> **📍 用途**: AI Agent 路径导航 + 文件定位故障排除指南

---

## 🔍 锚定和搜索协议

**⚠️ 文件找不到时，本 MD 是故障排除指南**

### 标准锚定协议
**锚定文件**: `SPEC_ACA_CORE_PRINCIPLES.md` (唯一文件)
**验证特征**: 内容包含 "Constitutional Axioms"
**定位逻辑**: 该文件所在目录 = `agentic_spec/`，向上一级 = 工作根目录

### 搜索指令
```bash
# 方法1: 按文件名搜索
搜索目标: SPEC_ACA_CORE_PRINCIPLES.md

# 方法2: 按内容搜索  
搜索目标: 包含 "Constitutional Axioms" 的文件

# 验证: 确认找到正确文件
检查文件内容是否包含 "Design-by-Contract"
```

**定位后**: `agentic_spec/` 父目录 = 工作根目录

---

## 🗂️ 标准目录结构

```
./  ← 工作根目录
├── _DIRECTORY_CONTEXT.md           # 本文件
├── _docs/                          # 用户指南文档
├── _docs_authoring_guides/         # 框架作者指导文档
├── agentic_coding/                 # AI Agent执行计划生成器
├── agentic_spec/                   # 锚定目录
│   └── SPEC_ACA_CORE_PRINCIPLES.md # 锚定文件 ⭐
├── four_stage_crafting/            # CRAFT 推敲指导
├── four_stage_constraints/         # CONSTRAINT 质量门禁
├── four_stage_toolkits/            # TOOLKIT 质量工具
└── [spec/]                         # 仅推敲场景
```

---

## 🧭 路径引用规则

**兄弟目录使用相对路径**:
```markdown
✅ ../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md
❌ SPEC_PRACTICAL_DIRECT/agentic_spec/... (场景切换失效)
```

**为什么**: 生产场景 + 推敲场景通用

---

## ⚠️ 文件找不到时

1. **搜索锚定文件**: `SPEC_ACA_CORE_PRINCIPLES.md`
2. **验证内容特征**: "Constitutional Axioms"
3. **确定工作根目录**: 锚定文件向上一级
4. **重新引用**: 使用相对路径
