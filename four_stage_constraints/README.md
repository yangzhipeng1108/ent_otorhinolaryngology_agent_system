# 约束体系目录导航

> 🎯 **核心概念权威定义**: [CONSTRAINT_CORE_CONCEPTS.md](CONSTRAINT_CORE_CONCEPTS.md)
> 📋 **文件关系**: 所有STAGE_*文件引用核心概念，避免重复定义
> ⚠️ **质量级别提示**: 目前仅 L1-STREAMLINED 处于稳定版本；L2-BALANCED 与 L3-RIGOROUS 文档仍在实验通道，结构已提供但执行器尚未全面验证，使用前请确认可接受额外人工校验。

## 📁 文件索引

### 🎯 核心概念定义
- **CONSTRAINT_CORE_CONCEPTS.md** - L1/L2/L3和协作模式权威定义

### 📋 分级约束应用文件

#### L1-STREAMLINED (快速迭代级)
- **CONSTRAINT_L1_REQUIREMENTS.md** - 需求阶段快速约束
- **CONSTRAINT_L1_DESIGN.md** - 设计阶段快速约束
- **CONSTRAINT_L1_IMPLEMENTATION.md** - 实施阶段快速约束
- **CONSTRAINT_L1_TASK_PLANNING.md** - 任务阶段快速约束

#### L2-BALANCED (标准流程级)
- **CONSTRAINT_L2_REQUIREMENTS.md** - 需求阶段标准约束
- **CONSTRAINT_L2_DESIGN.md** - 设计阶段标准约束
- **CONSTRAINT_L2_IMPLEMENTATION.md** - 实施阶段标准约束
- **CONSTRAINT_L2_TASK_PLANNING.md** - 任务阶段标准约束

#### L3-RIGOROUS (严格控制级)
- **CONSTRAINT_L3_REQUIREMENTS.md** - 需求阶段严格约束
- **CONSTRAINT_L3_DESIGN.md** - 设计阶段严格约束
- **CONSTRAINT_L3_IMPLEMENTATION.md** - 实施阶段严格约束
- **CONSTRAINT_L3_TASK_PLANNING.md** - 任务阶段严格约束

## 🔄 四阶段执行关系

```
需求澄清 → 设计文档 → 实施规划 → 任务执行
REQUIREMENTS → DESIGN → IMPLEMENTATION → TASK_PLANNING
     ↓           ↓          ⭐ TDD主场        ↓
  验收标准   →  技术方案  →   测试策略   →  声明式目标
```

### 阶段依赖关系
- **严格顺序**: 必须按1→2→3→4顺序执行，不可跳跃
- **输入输出**: 前阶段输出 = 后阶段输入，严格依赖
- **质量递进**: 每个阶段都有质量门禁，不通过不能进入下阶段
- **TDD中心**: 实施规划阶段是TDD策略制定的核心主场
- **⚠️ 计划为主**: 所有四阶段都是计划和文档制定，不涉及任何编码实现

### 文件层次和引用关系
```
CONSTRAINT_CORE_CONCEPTS.md (顶层：权威定义)
    ↓ 引用关系
├── CONSTRAINT_L1_REQUIREMENTS.md (L1需求约束应用)
├── CONSTRAINT_L1_DESIGN.md (L1设计约束应用)
├── CONSTRAINT_L1_IMPLEMENTATION.md (L1实施约束应用)
├── CONSTRAINT_L1_TASK_PLANNING.md (L1任务约束应用)
├── CONSTRAINT_L2_REQUIREMENTS.md (L2需求约束应用)
├── CONSTRAINT_L2_DESIGN.md (L2设计约束应用)
├── CONSTRAINT_L2_IMPLEMENTATION.md (L2实施约束应用)
├── CONSTRAINT_L2_TASK_PLANNING.md (L2任务约束应用)
├── CONSTRAINT_L3_REQUIREMENTS.md (L3需求约束应用)
├── CONSTRAINT_L3_DESIGN.md (L3设计约束应用)
├── CONSTRAINT_L3_IMPLEMENTATION.md (L3实施约束应用)
└── CONSTRAINT_L3_TASK_PLANNING.md (L3任务约束应用)
```

**引用规则**:
- **权威定义**: CONSTRAINT_CORE_CONCEPTS.md是唯一概念定义源
- **统一引用**: 所有CONSTRAINT文件必须引用核心概念，不得重复定义
- **职责分离**: 核心概念专注定义，CONSTRAINT文件专注该级别的具体约束指导
- **概念一致性**: L1/L2/L3和协作模式在所有文件中表述必须完全一致
- **哼哈二将配对**: 每个CONSTRAINT文件与对应CRAFT文件形成配对协作关系

## 🎯 使用指导

### ⚠️ 重要说明
**四阶段全部为计划制定阶段，不涉及编码**:
- 需求澄清：制定需求文档和验收标准
- 设计文档：制定技术架构和设计方案
- 实施规划：制定TDD测试策略和实施计划
- 任务规划：制定声明式目标和验收标准

**编码实现在四阶段全部完成后进行**，基于完整的计划文档体系执行。

### LLM使用方法
1. **读取核心概念**: 首先载入CONSTRAINT_CORE_CONCEPTS.md获取权威定义
2. **确定约束级别**: 基于项目SPEC_PRJ_LEVEL确定使用L1/L2/L3级别
3. **选择约束文件**: 根据当前阶段+约束级别选择对应CONSTRAINT_LN_STAGE.md文件
4. **制定计划文档**: 按照协作模式→约束级别映射，专注文档和计划制定
5. **严禁编码**: 任何阶段都不得生成实际代码，只制定计划

---

*约束体系目录 - 概念定义+应用指导+导航索引*
