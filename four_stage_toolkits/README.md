# Four Stage Toolkits - AI Agent质量工具包

> **🎯 目标**: AI Agent在使用GUIDE时的强制执行质量工具
> **📍 位置**: 被GUIDE文件动态加载，提供>>命令响应
> **🔧 设计**: 上下文驱动，专注质量保障而非功能开发
> **📦 迁移说明**: Build_Spec_Exec_Master_Plan 系列文件已迁移至 `../agentic_coding/` 目录

## 🚀 核心成就

- **✅ 完整TOOLKIT体系**: L1/L2/L3三级×4阶段=12个工具文件创建完成
- **✅ >>协议验证**: 100%触发率，AI Agent严格按文件执行
- **✅ SOLID原则**: 职责分离，按需加载，简洁设计验证成功
- **✅ 模板集成**: 4个STAGE模板统一支持，多级别路径标准化
- **✅ 差异化设计**: L1快速迭代、L2标准流程、L3严格控制特色鲜明

## 📁 文件结构

```
four_stage_toolkits/
├── README.md                        # 本文件
├── TOOLKIT_L1_REQUIREMENTS.md       # L1需求阶段质量工具
├── TOOLKIT_L1_DESIGN.md             # L1设计阶段质量工具
├── TOOLKIT_L1_IMPLEMENTATION.md     # L1实现阶段质量工具（TDD主场）
├── TOOLKIT_L1_TASK_PLANNING.md      # L1任务规划阶段质量工具
├── TOOLKIT_L2_REQUIREMENTS.md       # L2需求阶段质量工具
├── TOOLKIT_L2_DESIGN.md             # L2设计阶段质量工具
├── TOOLKIT_L2_IMPLEMENTATION.md     # L2实现阶段质量工具（TDD主场）
├── TOOLKIT_L2_TASK_PLANNING.md      # L2任务规划阶段质量工具
├── TOOLKIT_L3_REQUIREMENTS.md       # L3需求阶段质量工具
├── TOOLKIT_L3_DESIGN.md             # L3设计阶段质量工具
├── TOOLKIT_L3_IMPLEMENTATION.md     # L3实现阶段质量工具（TDD主场）
└── TOOLKIT_L3_TASK_PLANNING.md      # L3任务规划阶段质量工具
```

> **📦 注**: Build_Spec_Exec_Master_Plan_L[1-3].md 文件已迁移至 `../agentic_coding/` 目录，
> 该目录专门存放AI Agent执行计划生成器，与质量工具包职责分离。

## 🎯 设计原理

### 上下文驱动架构
- **加载时机**: 只有当用户在对应GUIDE中使用>>命令时才被读取
- **上下文确定**: 文件加载时已知阶段(REQUIREMENTS/DESIGN/IMPLEMENTATION/TASK_PLANNING)和级别(L1)
- **智能路由**: 支持具体命令(>>req_scan_l1)和通用命令(>>检查)

### 职责分离原则
- **CRAFT文件**: 推敲指导（建议式、启发式）→ `four_stage_crafting/`
- **CONSTRAINT文件**: 质量门禁（声明式、标准式）→ `four_stage_constraints/`  
- **TOOLKIT文件**: 质量工具（操作式、过程式）→ `four_stage_toolkits/` ✅

## 🔧 完整工具矩阵 (L1/L2/L3)

### L1-STREAMLINED 工具矩阵
| 阶段 | 扫描工具 | 修复工具 | 特殊性 |
|------|----------|----------|---------|
| **REQUIREMENTS** | req_scan_l1 | req_fix_l1 | 快速迭代，基本检查 |
| **DESIGN** | design_scan_l1 | design_fix_l1 | 架构基础检查 |
| **IMPLEMENTATION** | impl_scan_l1 | impl_fix_l1 | TDD主场增强50% |
| **TASK_PLANNING** | task_scan_l1 | task_fix_l1 | 基本执行计划 |

### L2-BALANCED 工具矩阵
| 阶段 | 扫描工具 | 修复工具 | 特殊性 |
|------|----------|----------|---------|
| **REQUIREMENTS** | req_scan_l2 | req_fix_l2 | 标准化检查，结构化修复 |
| **DESIGN** | design_scan_l2 | design_fix_l2 | ADR决策记录，系统化架构 |
| **IMPLEMENTATION** | impl_scan_l2 | impl_fix_l2 | TDD主场增强75% |
| **TASK_PLANNING** | task_scan_l2 | task_fix_l2 | 项目管理标准流程 |

### L3-RIGOROUS 工具矩阵
| 阶段 | 扫描工具 | 修复工具 | 特殊性 |
|------|----------|----------|---------|
| **REQUIREMENTS** | req_scan_l3 | req_fix_l3 | 形式化验证，INVEST原则，BDD严格 |
| **DESIGN** | design_scan_l3 | design_fix_l3 | 4+1视图，架构治理，合规性 |
| **IMPLEMENTATION** | impl_scan_l3 | impl_fix_l3 | TDD主场增强90%，变异测试≥85% |
| **TASK_PLANNING** | task_scan_l3 | task_fix_l3 | PMBOK标准，项目治理，审计就绪 |

## 📋 通用>>命令协议

### 精确命令格式

#### L1-STREAMLINED 命令
```bash
>>req_scan_l1      # 需求快速扫描
>>req_fix_l1       # 需求一键修复
>>design_scan_l1   # 设计快速扫描  
>>design_fix_l1    # 设计一键修复
>>impl_scan_l1     # 实现快速扫描
>>impl_fix_l1      # 实现一键修复
>>task_scan_l1     # 任务规划快速扫描
>>task_fix_l1      # 任务规划一键修复
```

#### L2-BALANCED 命令  
```bash
>>req_scan_l2      # 需求标准扫描
>>req_fix_l2       # 需求结构化修复
>>design_scan_l2   # 设计标准扫描
>>design_fix_l2    # 设计结构化修复
>>impl_scan_l2     # 实现标准扫描
>>impl_fix_l2      # 实现结构化修复
>>task_scan_l2     # 任务规划标准扫描
>>task_fix_l2      # 任务规划结构化修复
```

#### L3-RIGOROUS 命令
```bash
>>req_scan_l3      # 需求严格扫描
>>req_fix_l3       # 需求形式化修复
>>design_scan_l3   # 设计严格扫描
>>design_fix_l3    # 设计形式化修复
>>impl_scan_l3     # 实现严格扫描
>>impl_fix_l3      # 实现形式化修复
>>task_scan_l3     # 任务规划严格扫描
>>task_fix_l3      # 任务规划形式化修复
```

### 通用兼容命令
```bash
>>检查             # 自动路由到当前阶段的xxx_scan_l1
>>修复             # 自动路由到当前阶段的xxx_fix_l1
>>L1验收           # 统一验收命令，读取对应CONSTRAINT文件
```

## 🎯 L1-STREAMLINED设计原则

### 核心约束
- **输入灵活**: 支持目录和文件作为输入上下文
- **问题优先级**: 只关注🔴阻塞性问题，忽略🟡🟢
- **修复深度**: MVP修复，让项目"基本可用"即可
- **容错性**: 允许不完美，优先速度和可用性

### 目录结构约定
- **spec/requirements/**: 需求文档存放
- **spec/design/**: 设计文档存放
- **spec/implementation/**: 实现策略文档存放
- **spec/tasks/**: 任务规划文档存放

## 🔍 质量检查分级

### 🔴 阻塞性问题（必须修复）
- 影响项目基本可用性的关键问题
- L1工具会自动修复的问题类型
- 例如：文档缺失、测试框架缺失、任务列表缺失

### 🟡 警告问题（L1可忽略）
- 影响项目质量但不阻塞进展的问题
- L1级别容忍的不完美
- 例如：格式不规范、描述不够详细

### 🟢 建议优化（L1跳过）
- 锦上添花的优化建议
- L1级别直接跳过的问题
- 例如：高级模式、性能优化、深度重构

## 🧪 TDD主场特殊处理

### IMPLEMENTATION阶段增强
- **检查重点**: 测试框架配置 + 核心功能测试用例 + 代码可运行性
- **修复策略**: 测试优先原则，确保基本TDD循环能运行
- **L1简化**: "基本可测试"原则，不追求高测试覆盖率

### TDD主场标识
```
🧪 TDD重点：确保基本测试能够运行
🎯 **TDD主场特别说明**：IMPLEMENTATION是测试驱动开发的核心阶段
```

## 🎓 验证成果与学习收获

### Phase 1.2验证结果 ✅
- **✅ >>协议触发率**: 3/3 (100%) - AI Agent严格按TOOLKIT文件执行
- **✅ 防绕过机制**: 100%有效 - 无内置知识绕过行为
- **✅ 向后兼容**: >>检查→req_scan_l1映射正常工作  
- **✅ TDD主场**: IMPLEMENTATION特殊处理机制验证成功

### 关键设计教训
- **💡 SOLID原则**: 职责分离胜过功能集中，按需加载比提前暴露更有效
- **💡 简洁设计**: 相对路径比绝对路径更清晰 (four_stage_toolkits/xxx.md)
- **💡 命令发现**: AI Agent从文件中自然发现命令，而非模板预定义列表

### 未来L2/L3扩展
```
four_stage_toolkits/
├── TOOLKIT_L1_*.md              # L1-STREAMLINED工具包 ✅
├── TOOLKIT_L2_*.md              # L2-BALANCED工具包（Phase 2）
└── TOOLKIT_L3_*.md              # L3-RIGOROUS工具包（Phase 3）
```

## 📊 验证指标达成

### Phase 1.2实际验证结果
- **✅ 命令响应一致性**: 100% - 标准响应模板格式完全合规
- **✅ 协议触发可靠性**: 100% - 所有>>命令100%触发TOOLKIT文件读取
- **✅ 防绕过机制**: 100% - AI Agent零绕过行为，严格按文件执行
- **✅ 向后兼容性**: 100% - >>检查/>>修复兼容命令正常工作

### Phase 1.3待验证指标
- **问题检出准确性**: 目标>80%阻塞性问题检出率
- **修复成功率**: 目标>90%自动修复成功率  
- **用户学习成本**: 目标快速掌握>>命令使用

## 🔗 集成方式

### GUIDE模板集成
```markdown
## 🔧 质量工具包（{{SPEC_PRJ_LEVEL}}）
📂 **工具包文件**: `four_stage_toolkits/TOOLKIT_{{SPEC_PRJ_LEVEL_CODE_UPPER}}_{{STAGE}}.md`
🤖 **AI Agent注意**: 用户使用>>命令时，请立即读取上述工具包文件并严格按文件内容执行
```

### 集成覆盖范围
- ✅ **STAGE_1_REQUIREMENTS_TEMPLATE** - 已集成
- ✅ **STAGE_2_DESIGN_TEMPLATE** - 已集成  
- ✅ **STAGE_3_IMPLEMENTATION_TEMPLATE** - 已集成（TDD主场标识）
- ✅ **STAGE_4_TASK_PLANNING_TEMPLATE** - 已集成

---

**文档版本**: v1.2  
**适用级别**: L1-STREAMLINED  
**最后更新**: 2025-01-13  
**验证状态**: ✅ Phase 1.2完成，协议验证成功，模板集成完成