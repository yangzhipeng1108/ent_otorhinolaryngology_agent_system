# Build_Spec_Exec_Master_Plan_L1.md

> 🎯 **定位**: L1级别执行计划生成引擎
> 📋 **用途**: 读取SPEC脚手架,生成AI Agent可执行的ProgressPlan体系
> 🧠 **本质**: 方法论指导文档,非机械脚本

> ⚠️ **执行契约**: 进入本文件 = 立即启动十二步工作流。从`Step 1`开始按顺序推进，禁止生成额外临时文档；分析草稿若确需暂存，只能放到`_scratch/`或沙箱并在进入`Step 5`前清理。

---

## 📖 Constitutional原则引用索引 (ACA宪法桥接)

> **核心依据**: `../agentic_spec/SPEC_ACA_CORE_PRINCIPLES.md`
> **桥接方式**: Constitutional-level公理 → L1级别具体实现

### 四大不变量 (Four Invariants)
- **I1-CanonicalLocationUniqueness**: 权威位置唯一性
  - L1应用: Constraints定义文件权威位置，N+4文件各有唯一Canonical位置
- **I2-CompletenessPrinciple**: 完整性原则
  - L1应用: MasterPlan/SubPlan/Constraints/Dashboard/Lessons各有完整性定义
- **I3-QualityVerificationTriple**: 质量验证三元组
  - L1应用: {Pre} AI_Create {Post: Verify} → Step 5/6/7/8/9/10/11验证清单
- **I4-DependencyChainIntegrity**: 依赖链完整性
  - L1应用: Constraints → MasterPlan → SubPlan → Dashboard → Lessons依赖链

### 执行协议 (Execution Protocols)
- **C2-PDCA**: Plan → Do → Check → Act
  - L1应用: ProgressPlan = PDCA的AI Agent实现，Lessons = Reflection持久化
- **C3-ProducerConsumerContract**: 生产者-消费者契约
  - L1应用: SubPlan = Producer，Dashboard = C3.2-Consumer
- **E1-EmergencyProtocol**: STOP → Report → Rollback → Fix → Verify → Resume
  - L1应用: 分级决策机制，Lessons问题案例库

### 本文档Constitutional桥接说明
本文档是Constitutional原则在L1-STREAMLINED级别的**具体实现指导**：
- Constitutional定义"必须遵守什么"（不变量和协议）
- 本文档定义"如何在L1级别执行"（方法论和模板）
- 引用格式: `(I1)` `(C2-PDCA)` `(E1)` 表示桥接Constitutional原则

---

## 📖 目录与快速导航

**🎯 首次阅读路径**: §0 文档概览 → §14 十二步执行流程 → 按需查阅§1-§13

**📚 章节功能分组**:
- **概览** (§0): 文档目的/ProgressPlan概念/HITL机制/执行次序/版本说明
- **方法论** (§1-§9): 引擎架构/文件识别/Phase划分/Round规划/上下文提炼/HITL设计/Plan更新
- **模板** (§10-§13): MasterPlan/SubPlan/Constraints/Dashboard生成指导
- **执行** (§14): 十二步工作流(Step 1-12) ⭐ AI Agent执行入口

---

## § 0. 文档概览与核心概念

### § 0.1 这个文档是什么

**元层次定位**: 生成ProgressPlan的ProgressPlan

**输入**: SPEC脚手架(spec/目录 + 4阶段文档)
**输出**: 5类可执行ProgressPlan文档 (遵循I1-CanonicalLocation原则)
  - **SpecExecMasterConstraints_L1.md** - 目录结构与命名约定 (~80-120行) (I1-Canonical定义器)
  - **SpecExecMasterPlan_L1.md** - 总控ProgressPlan (150-250行) (C3.1-Producer总控)
  - **SpecExecSubPlan_*.md** - 独立执行单元 (各400-800行) (C3.1-Producer执行单元)
  - **SpecExecMasterDashboard_L1.md** ⭐ - 进度Contract验证 (~200-300行) (C3.2-Consumer)
  - **SpecExecMasterLessons_L1.md** ⭐ - Reflection知识库 (~300-400行) (C2-PDCA + E1)

**生成过程**: 12步工作流 + Human-in-the-Loop决策点

**文档性质**: 方法论指导,强调AI Agent判断空间,灵活应用而非机械执行

### § 0.2 什么是ProgressPlan ⭐ Constitutional桥接

### Constitutional依据（SPEC_ACA_CORE_PRINCIPLES.md）

**C2-PDCA桥接** (Plan → Do → Check → Act):
- ProgressPlan = PDCA循环的AI Agent实现
- **Plan阶段**: 前置条件检查(C2.1-Plan) + 推理分析(目标/文档/产出)
- **Do阶段**: 执行创建 + 遵守Invariants(I1/I2/I3/I4)
- **Check阶段**: 后置条件验证(C2.3-Check) + Quality Gates
- **Act阶段**: 决策路径(继续|重试|升级|回滚) + Lessons记录

**E1-EmergencyProtocol桥接** (失败恢复机制):
- **Reflection机制** = Check阶段验证 + E1的Report步骤持久化
- **分级决策** = E1协议实现:
  - Level 1 (自主): 明确问题 → Fix → Verify → Resume
  - Level 2 (协商): 模糊问题 → Report(诊断) → HITL → Fix
  - Level 3 (升级): 架构问题 → STOP → Report → HITL → Rollback/Fix
- **Lessons记录** = E1的Report + Fix经验积累（持久化知识库）

**ProgressPlan vs 传统计划**:

| 维度 | 传统计划 | ProgressPlan (AI Agent) |
|------|---------|------------------------|
| 执行方式 | 瀑布式,预先固定 | 迭代式,动态调整 |
| 失败处理 | 回退重做 | Reflection+分级恢复 |
| 学习机制 | 无 | Lessons记录+经验积累 |
| 人机协作 | 人工控制 | HITL检查点+自信度评估 |
| 进度追踪 | 完成百分比 | Round状态+质量指标+反思记录 |

**Master-SubPlan架构价值** (I4-DependencyChain + C3-ProducerConsumer):
- **问题**: 单文件MasterPlan 1500-3000行臃肿，AI Agent上下文负担过重
- **解决**: I4依赖链 → Constraints → MasterPlan(总控) → SubPlan(执行单元)
- **职责分离** (C3):
  - MasterPlan (C3.2-Consumer): 只追踪SubPlan状态，不追踪Round细节
  - SubPlan (C3.1-Producer): 独立维护Round执行记录
  - Dashboard (C3.2-Consumer): 验证SubPlan产出，质量门禁判定
- **架构优势**: 150-250行总控 + N个400-800行SubPlan，清晰VS边界，支持并行协作

### § 0.3 Human-in-the-Loop协作机制

**HITL不是Bug,是Feature**:
- 本文档生成过程需要13-25轮Human-in-the-loop协作
- HITL是质量保障机制,非执行阻碍

**HITL触发场景**:

1. **技术栈识别不确定** (Step 1):
   - 罕见技术栈/架构选择矛盾/测试策略不明确
   - 触发条件: 自信度<50%

2. **Phase划分自信度<80%** (Step 2):
   - 依赖关系复杂/集成策略模糊/Phase数量难以判断

3. **文件已存在需要决策** (Step 5/6/7/8/9):
   - 现有文件备份后覆盖/保留现有/手动Review
   - 用户主导决策,AI提供上下文
   - 特别注意: Lessons/SubPlan包含宝贵经验,强烈建议保留现有

4. **Constraints约定不明确** (Step 5):
   - 目录结构不明/命名规则模糊/测试组织策略不确定

**HITL标准模板**:
```
🤝 需要您的决策 - [标题]

**背景**: [简要说明当前执行到哪个步骤]

**不确定项**:
- 来源: [哪个文档/哪个章节发现的问题]
- 问题: [具体不确定的点]
- 推测: [基于现有信息的初步判断]
- 选项: [可选方案A/B/C]

**影响范围**: [该决策会影响哪些后续步骤]
```

### § 0.4 执行次序速览

**十二步工作流** (Constitutional桥接):
```
Step 1: 读取脚手架 + 识别技术栈
         ↓
Step 2: Phase划分 (垂直切片驱动)
         ↓
Step 3: SubPlan划分 (Master-SubPlan架构)
         ↓
Step 4: Round规划 (C2-PDCA + TDD节奏)
         ↓
Step 5: 生成Constraints ⭐ (I1-Canonical第一优先级)
         ↓
Step 6: 生成完整Lessons ⭐ (C2-Reflection完整版)
         ↓
Step 7: 生成MasterPlan (C3.1-Producer总控)
         ↓
Step 8: 生成SubPlan×N (I4-依赖Constraints+MasterPlan)
         ↓
Step 9: 生成Dashboard完整版 (C3.2-Consumer验证)
         ↓
Step 10: 完善Lessons (GOAL挂靠)
         ↓
Step 11: 更新Dashboard (体系完成里程碑)
         ↓
Step 12: Git分阶段提交 ⭐ (I4-版本控制)
```

**核心依赖关系**:
- Step 1→2→3: 顺序执行,识别artifacts→Phase划分→SubPlan划分
- Step 4: 基于Step 3的SubPlan清单,为每个SubPlan规划Round
- Step 5: 基于Step 1的技术栈识别和Step 4的Round规划,生成Constraints
- Step 6: 基于Step 5的Constraints文件,生成Lessons初始框架 (C2-Reflection空结构) [信息依赖:Step 3分析结果]
- Step 7: 基于Step 5的Constraints和Step 6的Lessons框架,生成MasterPlan总控 (C3.1-Producer) [信息依赖:Step 3分析结果]
- Step 8: 基于Step 5的Constraints和Step 7的MasterPlan文件,生成每个SubPlan文件 (C3.1-Producer) [信息依赖:Step 4的Round规划]
- Step 9: 基于Step 7的MasterPlan和Step 8的SubPlan,生成Dashboard完整版 (C3.2-Consumer验证Producer产出)
- Step 10: 基于Step 7的MasterPlan和Step 8的SubPlan,完善Lessons内容 (C2-Reflection + E1)
- Step 11: 基于Step 8的SubPlan执行状态,更新Dashboard里程碑数据
- Step 12: 基于Git状态,执行阶段性提交和备份

**输出文件顺序**: Step 5→Constraints → Step 6→Lessons框架 → Step 7→MasterPlan → Step 8→SubPlan×N → Step 9→Dashboard完整版 → Step 10→Lessons完善 → Step 11→Dashboard更新 → Step 12→Git提交

**Git & Dashboard 节奏提示**:
- 每次生成或更新关键文档（MasterPlan/SubPlan/Constraints/Dashboard/Lessons）后，立即执行 `git add` → 小步提交（推荐信息如 `plan: add master plan skeleton`）
- Dashboard/Lessons 在 Step 9-11 会继续更新；若在执行阶段发现信息变动，也需同步更新 Dashboard 并再次提交
- 建议保持“一项改动一条 commit”，同时在 Dashboard 上记录进度/决策，确保 Producer-Consumer 合约可追踪

**依赖类型说明** (架构设计):
- **📁 文件依赖**: 需要检查前置步骤生成的文件存在性 (Step 5-11)
- **📋 信息依赖**: 需要前置步骤的分析结果 (Step 1-4产出,存在于AI Agent上下文)

**文件存在性检查** (阶段1-简化版):
- Step 5/6/7/8/9执行前检查文件依赖是否存在
- **文件不存在** → 直接生成
- **文件已存在** → HITL决策(A.备份后覆盖 / B.保留现有 / C.手动Review)
- **前置依赖验证**: 每步检查所需前置文件,缺失则阻塞返回对应Step
- **Dashboard更新**: Step 11/12 更新现有Dashboard文件,不检查存在性

**关键约束**: Constraints必须第一个生成,是所有文件创建的基础规范。Lessons/Dashboard完整版在Plan之前生成,为后续引用做好准备。MasterPlan为总控,SubPlan为执行单元。

### § 0.5 版本说明与迭代路线

**当前版本**: v2.0 - 阶段1基础版(2025-01)

**阶段1特征**: 
- 安全可靠的文件检查 + 用户主导HITL决策
- 简洁执行流程(~40-75行/Step)
- 版本号标准: v1.0.0(所有生成文件统一)

**未来演进计划**:
- **阶段2** [计划]: AI辅助分析 + 智能推荐(spec变化对比/变化摘要展示)
- **阶段3** [未来]: 自动化决策 + 增量更新(🟢🟡🔴自动分级/轻微变化自动执行)

**核心设计原则**:
- 每个阶段都是可工作的完整系统
- 基于实际使用反馈迭代
- 保持向后兼容

### § 0.6 步骤完成标准格式 ⭐ AI Agent交互规范

> **设计目标**：进度透明 + 连续执行 + 明确终点
> **核心原则**：Step 1-11禁止说"任务完成/任务结束/全部完成"，只有Step 12才能宣布"全部完成"

---

**分析步骤（Step 1-4）完成格式**:
```
🎯 进度：Step X/12 已完成 (YY%) - [步骤名称]
📋 已产出：[关键成果描述]
💡 **流程进行中**：整个工作流还有Z步未完成，请勿中断
⏭️ **继续执行**：即将自动进入 Step Y - [下步骤名称]
```

**示例**（Step 3完成）:
```
🎯 进度：Step 3/12 (25%) - SubPlan划分
📋 已产出：SubPlan清单(8个) + GOAL覆盖率(100%) + 执行序号分配
💡 **流程进行中**：整个工作流还有9步未完成，请勿中断
⏭️ **继续执行**：即将自动进入 Step 4 - Round规划
```

---

**生成步骤（Step 5-9）完成格式**:
```
🎯 进度：Step X/12 已完成 (YY%) - [步骤名称]
📁 **阶段性输出**：[文件名] (约XXX行) ⚠️ 这不是最终完成
📊 **文件进度**：已生成A/5个核心文件，还有B个待生成
💡 **流程进行中**：整个工作流还有Z步未完成，请勿中断
⏭️ **继续执行**：即将自动进入 Step Y - [下步骤名称]
💾 **建议操作**（可选）：git add [文件] && git commit -m "plan: add [描述]"
```

**示例**（Step 7完成）:
```
🎯 进度：Step 7/12 (58%) - MasterPlan生成
📁 **阶段性输出**：SpecExecMasterPlan_L1.md (约200行) ⚠️ 这不是最终完成
📊 **文件进度**：已生成3/5个核心文件（Constraints + Lessons框架 + MasterPlan），还有2个待生成（SubPlan + Dashboard）
💡 **流程进行中**：整个工作流还有5步未完成，请勿中断
⏭️ **继续执行**：即将自动进入 Step 8 - SubPlan批量生成
💾 **建议操作**（可选）：git add SpecExecMasterPlan_L1.md && git commit -m "plan: add master plan v1"
```

---

**更新步骤（Step 10-11）完成格式**:
```
🎯 进度：Step X/12 已完成 (YY%) - [步骤名称]
📊 **内容更新**：[更新对象] ([更新内容简述]) ⚠️ 这不是最终完成
💡 **流程进行中**：整个工作流还有Z步未完成，请勿中断
⏭️ **继续执行**：即将自动进入 Step Y - [下步骤名称]
💾 **建议操作**（可选）：git add [文件] && git commit -m "plan: update [描述]"
```

**示例**（Step 11完成）:
```
🎯 进度：Step 11/12 (92%) - Dashboard最终更新
📊 **内容更新**：SpecExecMasterDashboard_L1.md (体系状态: ✅已就绪) ⚠️ 这不是最终完成
💡 **流程进行中**：整个工作流还有1步未完成，请勿中断
⏭️ **继续执行**：即将自动进入 Step 12 - Git提交（**最后1步！**）
💾 **建议操作**（可选）：git add SpecExecMasterDashboard_L1.md && git commit -m "plan: sync dashboard completion"
```

---

**最后一步（Step 12）完成格式**
```
🎯 进度：Step 12/12 已完成 (100%)
✅ ProgressPlan 体系已就绪（所有核心文档已提交）
```

## § 1. 引擎作用与核心依赖 ⭐ Constitutional桥接
## § 1. 引擎作用与核心依赖 ⭐ Constitutional桥接

**Constitutional原则**:
- **I1-CanonicalLocation**: Constraints定义文件权威位置（唯一性保证）
- **I4-DependencyChain**: Constraints → MasterPlan → SubPlan → Dashboard/Lessons依赖链
- **C2.1-Plan**: Constraints必须第一个生成（前置条件检查）

**输入**: SPEC脚手架目录（spec/目录 + 三柱体系）

**输出**: 本引擎生成**N+4**个文件
- **Constraints文档** (1个): 目录结构与命名约定 (~80-120行) ⭐ **必须第一个生成** (I1)
- **MasterPlan文档** (1个): 总控Progress Plan (~150-250行) (C3.1-Producer总控)
- **SubPlan文档** (N个): 独立可执行Progress Plan (各~400-800行) (C3.1-Producer单元)
- **Dashboard文档** ⭐ (1个): 进度Contract验证 (~200-300行) (C3.2-Consumer)
- **Lessons文档** ⭐ (1个): Reflection知识库 (~300-400行) (C2-Reflection + E1)

**⚠️ 执行顺序关键约束** (I4-DependencyChain):
1. Constraints必须第一个生成 (I1-Canonical + C2.1-Plan前置条件)
2. MasterPlan → SubPlan → Dashboard/Lessons依赖链 (I4)
3. 依赖原因: I4要求∀ artifact ≠ root: ∃ parent，Constraints = root

**详细生成流程**: 参见§14十二步工作流

---

## § 2. L1特征

**L1核心**: 快速迭代(端到端打通) | 垂直切片优先 | TDD红绿重构(金字塔60%/30%/10%, 覆盖率≥80%) | 小步集成(每2-3个VS)  
**L1心态**: Done > Perfect - 容忍技术债但要记录

---

## § 3. 核心方法论依据

**遵循SPEC CRAFT精神**: 快速迭代、垂直切片、测试驱动(详见`four_stage_crafting/CRAFT_L1_*.md`)

---

## § 4. 文件发现与识别策略

| 分类 | 主要来源 | 关键字段 |
|------|-----------|-----------|
| US / AC | `requirements/` | `id/sn`、关联下游 |
| VS / TAC / FP | `design/` | `source_us`、value_path、组件映射 |
| 设计 artefact (API/CMP/DM/契约) | `design/` | 与 VS/FP 的引用关系 |
| BDD / Test Suite / Test Data | `implementation/` | `source_vs` 或 `source_fp`、质量门禁 |
| 项目结构 / TDD 策略 | `implementation/` | 目录布局、测试分层 |
| GOAL / Task artefact | `task_planning/` | `source_vs`、`related_sc`、任务序列 |

若 artefact 缺失，标记 "📌 待确认"；GOAL registry 必须完整。
## § 5. Phase划分方法（核心）

1. **VS/FP 为单元**：根据业务优先级和价值路径定位核心 Phase。
2. **集成节点**：每 2-3 个 Phase 安排一次集成/协调 Phase；结尾保留最终集成。
3. **依赖图**：生成技术层与业务层依赖图（ASCII 或 Mermaid），在 MasterPlan 中引用。
4. **序号命名**：Phase ID 与 SubPlan 序号保持一致，便于追溯。
5. **HITL 条件**：Phase <3 或 >15、依赖循环、集成窗口不明时暂停确认。
## § 6. Round规划方法（PDCA + TDD）

- **目标**：每个 SubPlan 覆盖 VS/FP 所需的 RED → GREEN → REFACTOR → Integration 轮次，并保留缓冲。
- **模板**：Plan（引用 VS/AC/BDD）、Do（实现与测试）、Check（门禁：覆盖率≥80%、集成≥95%）、Act（决策 + Lessons/Dashboard 更新 + git 小步提交）。
- **估算**：单 VS 4-6 轮；集成或风险场景 2-3 轮；超 18 轮需重新评估。
- **HITL**：value_path 缺失、门禁目标不明确、团队协调冲突等。
## § 7. 上下文提炼策略

**核心问题**: 避免上下文爆炸（100+条AC但Round只需3条）

**解决方案**: 精准引用，按需加载

#### 7.1 构建文档引用映射表

**映射类型**: US→AC映射 | US→架构组件映射(架构/API/数据模型) | US→BDD场景映射

#### 7.2 精准引用路径设计

**Round规划引用格式**: 定位关键词(搜索"US-XXX"/"AC-XXX"/章节名) + 读取范围 → 信任LLM能找到信息

## § 8. HITL检查点设计

#### 8.1 Phase边界强制检查点

每个Phase结束时强制HITL:

**检查内容**:
1. Phase目标达成情况（US完成？AC通过？功能可演示？）
2. 质量门禁达标（覆盖率≥80%？测试通过？）
3. Lessons & Learning总结（问题？调整？影响？）
4. 人工验证（功能可用性？质量满意？）

**决策选项**: ✅继续 / 🔄部分重做 / ⏸️暂停调整 / ⏭️跳过

#### 8.2 Round内智能触发

🔴阻塞性(立即HITL): 架构冲突/测试失败>30%/性能偏差>50% | 🟡警告性(询问): 覆盖率未达标/测试失败<10% | 🟢建议性(记录): 代码风格/优化机会

#### 8.3 Lessons & Learning结构

**核心章节**: 目标达成情况(✅/⚠️/❌) | 问题与解决方案 | 架构/设计调整 | 最佳实践 | 质量指标回顾 | 对后续Phase影响 | 计划调整建议

## § 9. 动态Plan更新策略

**核心理念**: 计划稳定优先，必要时更新

**触发条件**: 架构重大调整 | Phase执行偏差>50% | 新增/删除Phase  
**不触发**: Round微调±2轮 | 具体实现调整 | Lessons小问题

**更新流程**: Phase结束评估 → 生成更新建议 → HITL决策 → 更新文件+版本递增

---

## 模板使用说明

**占位符替换**: `{{SPEC_PRJ_NAME}}` `{{SPEC_PRJ_DESC}}` `{{SPEC_USER_COLLABORATION_MODE}}` `{{SPEC_PRJ_ROOT_DIR}}` `{{TIMESTAMP}}` `{{N/X/MIN/MAX}}`

**核心规则**: 
- `[使用§X的模板]` → 完整复制§X内容并填充占位符
- 多实例展开 → 每个Phase/Round完整复制模板，禁止"同上"或"参考"
- 映射关系 → 生成实际映射表，不留空占位符

---

## § 10. SpecExecMasterPlan_L1.md 生成指导 ⭐ 总控概览

**定位**: 总控 Progress Plan（约 180~250 行），记录 SubPlan 状态与 GOAL 覆盖。

**生成步骤**
1. 复制模板，填入项目元信息、Constraints 引用、版本号。
2. 导入 SubPlan 索引表（序号 / 文件 / 类型 / GOAL_ID / Phase / 预估 Round / 状态）。
3. 绘制 Phase 依赖图，标注集成点与风险缓冲。
4. 生成 GOAL 覆盖表：`id/sn/source_vs/related_sc/assigned_subplan/status`。
5. 汇总 HITL 检查点、风险恢复、Plan 变更历史、KPI 及 Dashboard/Lessons 引用。

**检查要点**: GOAL 覆盖 100%；依赖图无冲突；SubPlan 状态块完整；引用字段正确。
## § 11. SpecExecSubPlan_*.md 生成指导 ⭐ 执行单元

**定位**: 独立执行 Progress Plan（约 400~800 行），包含 Round PDCA 与协作信息。

**生成步骤**
1. 新建 `SpecExecSubPlan_{序号}_{GOAL或TYPE}_L1.md`（序号两位，GOAL SubPlan 使用 GOAL ID）。
2. 填写元信息、依赖索引、交接物声明。
3. 复写 GOAL_COVERAGE（GOAL SubPlan 必填）。
4. 嵌入 Round PDCA 规划，注明门禁指标与缓冲轮次，并明确测试资产建设/维护任务（fixtures、mock、测试数据、环境配置等）。
5. 建立进度追踪、Lessons 占位、完成 HITL 清单与风险恢复树，明示 Round 总数/已完成数与未完成任务（TODO/Triage）列表，确保 SubPlan 内部即可感知当前进度与待办。

**检查要点**: Round 规划完整；GOAL_COVERAGE 字段齐全；Lessons/Dashboard 引用存在；风险记录同步。
## § 12. SpecExecMasterConstraints_L1.md 生成指导

**定位**: 目录与命名约束（约 80~120 行）。

**生成要点**
- 文档头部 + 版本；强约束声明（位置、命名、禁止区域、引用方式）。
- 技术栈识别、目录结构（根/源码/测试）、命名规则、禁止区域、引用方式、变更日志。
- 细节参见 `CRAFT_L1_*` 指南，ProgressPlan 需补充 GOAL/SubPlan 命名规则。

**检查要点**: 目录与命名清晰；测试目录说明；禁止区域列出；变更日志记录。
## § 13. SpecExecMasterDashboard_L1.md 生成指导 ⭐ Consumer

**定位**: 进度 Contract 验证文档（约 200~300 行）。

**生成要点**
- 项目概览 KPI、SubPlan 状态总览、Round 汇总、预测分析、当前焦点、里程碑、质量指标、更新记录。
- `GOAL_STATUS` 表：`id/sn/source_vs/related_sc/assigned_subplan/status`。
- 数据来源于 MasterPlan/SubPlan/Lessons；Dashboard 不改写 Plan。

**检查要点**: GOAL 覆盖完整；SubPlan 状态同步；质量门禁判定使用 L1 阈值（覆盖率 ≥80%、集成 ≥95%）。
## § 14. 十二步工作流 ⭐ 执行契约摘要

- **连续执行**：除 HITL 外按 Step 1-12 顺序推进。
- **进度输出**：遵循 §0.6 模板，Step 1-11 不得宣称“全部完成”；播报时带上 SubPlan 完成度（{{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}）与 Round 规划/完成度（{{PLANNED_OR_DONE_ROUNDS}}/{{TOTAL_ROUNDS}}）。
- **Dashboard/TODO 维护**：MasterPlan/SubPlan/Lessons 每次调整后记录待同步项；Dashboard 自 Step 9 生成起立即刷新 TODO/Next Actions，Step 11 勾选完成项并播报最新状态。
- **HITL 场景**：文件冲突、技术栈不确定、Phase 依赖矛盾、GOAL 漏挂等；使用 §0.3 模板与用户协商。
- **工具提示**：针对 CLine/Cursor 等 Agent，暂停时需说明原因并指向下一步。
- **恢复机制**：若执行中断，先检查文件状态，再从中断的 Step 继续，可保留既有产物。

详细示例与输出样式请参阅各 Step 条目。
### Step 1 (预计3-4分钟): 读取脚手架 + 识别技术栈
- **输入**: `spec/` 目录树。
- **操作**: 依照 §4 表格核对 artefact（US/AC/VS/BDD 等），记录缺失；解析 `goal_breakdown.md` 生成 `GOAL_INDEX`；整理技术栈及项目类型。
- **输出**: artefact 清单、`GOAL_INDEX`、技术栈/项目类型。
- **进度提示**: `🎯 Step 1/12 (8%) — 分析产出，继续执行 Step 2`。

### Step 2 (预计3-5分钟): Phase 划分
- **输入**: Step 1 结果与 CRAFT L1 指南。
- **操作**: 以 VS/Story 优先级划分 Phase，标注集成窗口、风险缓冲。
- **输出**: Phase 列表、依赖图草案。
- **进度提示**: `🎯 Step 2/12 (17%) — 继续执行 Step 3`。

### Step 3 (预计2-4分钟): SubPlan 划分
- **输入**: Phase 结果、`GOAL_INDEX`。
- **操作**: 将 GOAL/VS 映射到 SubPlan；编号；记录前置依赖；统计 SubPlan 总数，供后续播报与 Dashboard TODO 使用。
- **输出**: SubPlan 索引表。
- **进度提示**: `🎯 Step 3/12 (25%) — 继续执行 Step 4（SubPlan 总数：{{TOTAL_SUBPLANS}}）`。

### Step 4 (预计3-6分钟): Round 规划
- **输入**: SubPlan 列表、VS/AC/BDD 信息。
- **操作**: 规划 RED/GREEN/REFACTOR/Integration 轮次，注明质量门禁与缓冲；统计全局 Round 总数以便播报；确保每个 SubPlan 至少包含测试资产建设/维护相关 Round（fixtures、mock、环境配置等）。
- **输出**: Round 规划明细。
- **进度提示**: `🎯 Step 4/12 (33%) — 继续执行 Step 5（Round 规划进度：{{PLANNED_ROUNDS}}/{{TOTAL_ROUNDS}}）`。

### Step 5 (预计3-5分钟): 生成 Master Constraints
- **输入**: Round 规划、技术栈信息。
- **操作**: 生成/更新 `SpecExecMasterConstraints_L1.md`，经 HITL 决策保留或覆盖。
- **输出**: Constraints 文件。
- **进度提示**: `🎯 Step 5/12 (42%) — 阶段性输出，继续执行 Step 6`。

### Step 6 (预计3-5分钟): 生成 Lessons 框架
- **输入**: SubPlan 列表、Constraints。
- **操作**: 生成/更新 `SpecExecMasterLessons_L1.md` 空框架，挂载 GOAL/SubPlan 占位符。
- **输出**: Lessons 框架文件。
- **进度提示**: `🎯 Step 6/12 (50%) — 阶段性输出，继续执行 Step 7`。

### Step 7 (预计4-6分钟): 生成 MasterPlan
- **输入**: Constraints、Lessons 框架、SubPlan/Phase 数据。
- **操作**: 生成 `SpecExecMasterPlan_L1.md`，填写索引表、依赖图、GOAL 覆盖等。
- **输出**: MasterPlan 文件。
- **进度提示**: `🎯 Step 7/12 (58%) — 阶段性输出，继续执行 Step 8`。

### Step 8 (预计6-10分钟): 生成 SubPlan×N
- **输入**: MasterPlan、Round 规划、`GOAL_INDEX`。
- **操作**: 为每个 SubPlan 生成/更新文件，包含 GOAL_COVERAGE 与 Round PDCA；显式安排测试资产建设/维护任务（fixtures、数据、mock、环境配置）；在 SubPlan 内部写入进度追踪小节（Round 总数/完成数 + TODO/Triage 列表）；记录已完成 SubPlan 数并在进度播报中注明；若 Dashboard/TODO 尚未生成，则在本步骤维护临时待办列表供 Step 9 写入；提醒 Round 完成时按 §6 Act 更新 Lessons、Dashboard 并执行 git commit。
- **输出**: `SpecExecSubPlan_*_L1.md`。
- **进度提示**: `🎯 Step 8/12 (67%) — 阶段性输出，继续执行 Step 9（SubPlan 已生成：{{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}）`。

### Step 9 (预计3-5分钟): 生成 Dashboard 完整版
- **输入**: MasterPlan、SubPlan、`GOAL_INDEX`。
- **操作**: 生成 `SpecExecMasterDashboard_L1.md`，填充 KPI、GOAL 覆盖、预测分析等；同步/刷新 TODO Checklist（或 Next Actions）并即时播报当前完成度。
- **输出**: Dashboard 文件。
- **进度提示**: `🎯 Step 9/12 (75%) — 阶段性输出，继续执行 Step 10（Dashboard 进度：SubPlan {{COMPLETED_SUBPLANS}}/{{TOTAL_SUBPLANS}}, Round {{COMPLETED_ROUNDS}}/{{TOTAL_ROUNDS}}）`。

### Step 10 (预计1-2分钟): Lessons 挂靠 GOAL
- **输入**: MasterPlan、SubPlan、Dashboard、`GOAL_INDEX`。
- **操作**: 将 GOAL/SubPlan 数据填入 Lessons 各章节，保持占位。
- **输出**: Lessons 更新。
- **进度提示**: `🎯 Step 10/12 (83%) — 内容更新，继续执行 Step 11（Lessons 已挂靠 GOAL：{{LESSONS_LINKED}}/{{TOTAL_GOALS}}）`。

### Step 11 (预计1-2分钟): Dashboard 更新里程碑
- **输入**: Dashboard、Lessons、最新 SubPlan 状态。
- **操作**: 更新 Dashboard 最终状态（体系就绪、时间戳），并勾选/清理 TODO Checklist 中已完成项。
- **输出**: Dashboard 更新。
- **进度提示**: `🎯 Step 11/12 (92%) — 内容更新，继续执行 Step 12（Dashboard 标记完成：里程碑 {{MILESTONES_DONE}}/{{TOTAL_MILESTONES}}）`。

### Step 12 (预计1-2分钟): Git 阶段提交
- **输入**: 所有 Progress Plan 文件。
- **操作**: 执行 git add/commit，小步记录生成的文档，确认无遗漏。
- **输出**: ProgressPlan 最终提交记录。
- **进度提示**: `🎯 Step 12/12 (100%) — ✅ ProgressPlan 体系已就绪`。
## § 15. SpecExecMasterLessons_L1.md 生成指导 ⭐ Constitutional桥接

**文档定位**: Reflection知识库文档 (典型300-400行), 实现C2-PDCA Reflection + E1-EmergencyProtocol案例库

**核心职责**: Round-by-Round实践记录 | 技术债务管理 | 问题解决案例库 | 最佳实践提炼 | 数据驱动分析

**与MasterPlan关系**: Lessons = C2-Reflection持久化 | SubPlan执行时边学边干 | 记录E1完整流程

**Constitutional原则**:
- **I1-CanonicalLocation**: 权威位置 `{{SPEC_PRJ_ROOT_DIR}}/SpecExecMasterLessons_L1.md`
- **I2-Completeness**: Lessons完整性=文档头部 ∧ 知识库概览 ∧ Round-by-Round记录 ∧ 技术债务管理 ∧ 问题解决案例库 ∧ 最佳实践提炼 ∧ 数据驱动分析 ∧ 更新记录表
- **C2-PDCA**: Lessons = Check阶段验证 + Act阶段Reflection持久化
- **E1-EmergencyProtocol**: 问题解决案例库记录E1完整流程 (STOP → Report → Rollback → Fix → Verify → Resume)
- **I4-DependencyChain**: Lessons记录 → Round执行 → SubPlan → Phase依赖链

---

**必需章节** (按顺序生成):

**1. 文档头部**:
- 标题: `# SpecExecMasterLessons_L1.md`
- 引用块 (markdown `>`格式): 项目名/Lessons类型(Reflection知识库)/生成时间
- Lessons版本: 初始1.0

**2. 知识库概览**:
- 表格格式 (2列: 指标|当前值)
- 必含: 总Round记录数/总技术债数量(H/M/L分级)/总问题案例数/最佳实践数量(A/B/C三级)/最后更新时间/知识库覆盖率
- 知识库覆盖率: (已记录Round / 总已完成Round) × 100%
- 替换变量: {{TOTAL_ROUND_RECORDED}} {{TOTAL_TECH_DEBT}} {{TOTAL_PROBLEM_CASES}} {{BEST_PRACTICES_COUNT}}

**3. Round-by-Round实践记录** ⭐ **C2-Reflection核心**:
- 组织方式: 按SubPlan分组，每个SubPlan一个章节
- **每个SubPlan章节结构**:
  ```markdown
  ### SubPlan_{{序号}}_{{TYPE}} - {{功能简称}}

  **SubPlan元信息**:
  - 执行序号: {{序号}}
  - 关联Phase: {{Phase名称}}
  - 总Round数: {{总数}}
  - 已记录Round数: {{已记录数}}

  **Round-by-Round记录**:

  #### Round {{X}}: {{Round目标}}

  **元信息**:
  - TDD阶段: RED/GREEN/REFACTOR/Integration
  - 实际耗时: {{时间}}
  - 状态: ✅已完成 / ❌失败 / ⏭️已跳过

  **Good Practices** ✅:
  - [实践1]: 具体描述
  - [实践2]: 具体描述

  **Watch Out** ⚠️:
  - [注意点1]: 问题 → 改进方向
  - [注意点2]: 问题 → 改进方向

  **Tools & Tricks** 🔧:
  - [工具1]: 工具名称 + 使用场景 + 效果
  - [技巧1]: 技巧描述 + 提效程度
  ```

**4. 技术债务管理**:
- 技术债清单表格(7列): ID|描述|优先级(H/M/L)|发现Round|责任SubPlan|预计解决时间|状态
- 状态图例: ⬜未解决 🔄解决中 ✅已解决 ⏭️已忽略
- 优先级说明:
  - H (High): 阻塞后续开发，必须立即解决
  - M (Medium): 影响质量，应尽快解决
  - L (Low): 优化项，可延后解决

**5. 问题解决案例库** ⭐ **E1协议记录**:
- 组织方式: 按问题类型分类
- 问题类型: 测试失败 (Test Failures) | 架构冲突 (Architecture Conflicts) | 依赖问题 (Dependency Issues) | 性能偏差 (Performance Deviations) | 集成错误 (Integration Errors)
- **每个案例结构**:
  ```markdown
  #### 案例{{ID}}: {{问题标题}}

  **问题类型**: {{类型}}

  **E1协议流程记录**:
  1. **STOP**: 问题发现时刻和现象
     - 时间: {{时间戳}}
     - 现象: {{具体现象描述}}
     - 影响范围: {{Round/SubPlan/Phase}}

  2. **Report**: 问题根因分析
     - 根因: {{根本原因}}
     - 诊断过程: {{如何定位的}}

  3. **Rollback**: 回滚操作（如有）
     - 回滚内容: {{回滚的代码/配置}}
     - 回滚原因: {{为什么回滚}}

  4. **Fix**: 修复方案
     - 修复方案: {{具体修复措施}}
     - 实施步骤: {{步骤列表}}

  5. **Verify**: 修复验证
     - 验证方法: {{如何验证}}
     - 验证结果: {{验证通过/失败}}

  6. **Resume**: 恢复执行
     - 恢复时间: {{时间戳}}
     - 后续影响: {{对后续Round的影响}}

  **经验教训**:
  - {{关键经验1}}
  - {{关键经验2}}

  **相关Round**: Round {{X}}, SubPlan_{{序号}}
  ```

**6. 最佳实践提炼**:
- 组织方式: A/B/C三级分类
- **A级实践** (必须遵守): 实践描述 | 适用场景 | 证据(哪些Round验证有效) | 影响
- **B级实践** (强烈推荐): 实践描述 | 适用场景 | 证据 | 影响
- **C级实践** (可选优化): 实践描述 | 适用场景 | 证据 | 影响

**7. 数据驱动分析**:
- Round平均耗时趋势: 图表/数据（学习曲线）
- 技术债累积趋势: 按时间轴统计
- 问题类型分布: 饼图/百分比
- 最常见问题TOP 5: 排序列表
- 最有效实践TOP 5: 基于应用频率排序

**8. Lessons更新记录表**:
- 表格(5列): 更新时间|更新人|变更内容|Round ID|备注
- 审计追踪: 每次Round.Act强制添加记录
- 初始记录: v1.0|AI Agent|初始生成|N/A|基于MasterPlan生成

---

**变量替换规则**:
- `{{SPEC_PRJ_NAME}}` `{{TIMESTAMP}}` 替换为实际值
- `{{TOTAL_ROUND_RECORDED}}` `{{TOTAL_TECH_DEBT}}` `{{TOTAL_PROBLEM_CASES}}` `{{BEST_PRACTICES_COUNT}}` 替换为统计值
- `{{序号}}` `{{TYPE}}` `{{功能简称}}` `{{Phase名称}}` `{{Round目标}}` `{{时间}}` `{{状态}}` 替换为SubPlan数据
- `{{ID}}` `{{问题标题}}` `{{类型}}` `{{时间戳}}` `{{描述}}` `{{经验}}` 替换为案例数据

**典型长度**: 300-400行 (小型200-300/大型500-600，随Round增加而增长)

**强制更新机制** (边学边干):
- **触发时机**: SubPlan Round.Act(全部通过✅) 或 Round遇到问题时
- **强制更新内容**:
  ```
  Round.Act(全部通过✅):
    1. Round-by-Round添加本Round记录 (C2-Reflection)
       - Good Practices: 本Round有效实践
       - Watch Out: 本Round注意事项
       - Tools & Tricks: 本Round使用的工具/技巧

    2. 如有技术债 → 添加到技术债务清单 (E1-Report)
       - 技术债描述/优先级(H/M/L)/预计解决时间/责任SubPlan

    3. 如有问题解决 → 添加到问题解决案例库 (E1完整流程)
       - 问题类型/E1流程记录/解决方案/经验教训

    4. 仪表盘同步 (C3.2-Consumer)
       - 立即更新 `SpecExecMasterDashboard_L1.md` Round进度、SubPlan状态与“最后更新”时间
       - 若MasterPlan/各SubPlan存在Round进度表，同步标记该Round完成

    5. Git 小步提交 (I4-版本控制)
       - 执行 `git add` & `git commit -m "round: <GOAL>/<Round> pass"` 形成可回溯节点
       - 与 Step 12 的阶段性提交配合，确保每轮通过后都有版本记录
  ```

**生成策略**:
- **新项目**: 基于MasterPlan的SubPlan索引表生成初始Lessons，所有章节为空结构
- **已有项目**: 读取Dashboard和SubPlan执行记录，同步已完成Round的Lessons
- **不确定时**: HITL（Round记录缺失/技术债优先级不明/问题案例分类模糊）

**数据来源**:
- 主要: 从各SubPlan的Round小结和Lessons & Learning章节提取
- 辅助: 从MasterPlan的SubPlan执行状态记录区提取
- 更新频率: Round完成时强制更新，边学边干

**生成要点**:
- Lessons是持久化知识库，记录随Round增加而增长
- Round-by-Round记录按SubPlan组织，保持追溯性
- E1案例库记录完整的6步流程（STOP→Report→Rollback→Fix→Verify→Resume）
- 技术债务管理提供H/M/L优先级分级
- 最佳实践提炼提供A/B/C三级分类

---

**End of Build_Spec_Exec_Master_Plan_L1.md**
