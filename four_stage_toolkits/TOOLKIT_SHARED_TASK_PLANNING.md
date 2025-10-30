# 🔧 TOOLKIT_SHARED_TASK_PLANNING - 任务规划阶段跨Level共性工具

⚠️ **执行约束**：本文件为 AI Agent 的强制执行指令，所有共享命令必须遵循既定流程，不得以主观判断替代。

---

## 共性命令调用验证清单

在执行任何共享 `>>任务*` 命令前，AI Agent 必须确认：
- [ ] 用户显式调用了 `>>任务全景对齐` / `>>任务排期矩阵` / `>>任务执行拆解` / `>>任务收束写回` 之一
- [ ] 当前上下文处于 TASK_PLANNING 阶段（Stage-4），且 Level 与工具包一致
- [ ] 已完整读取本文件及对应 Level 的任务规划工具包配置
- [ ] 草稿工作区（参考 CRAFT 草稿命名，如 `spec/task_planning/_draft_<topic>/`）与版本文件（`draft_v{N}.md`）已建立或同步
- ℹ️ Level 具体治理要求由 `SPEC_PRJ_LEVEL`、对应的 `TOOLKIT_L{1|2|3}_TASK_PLANNING.md` 与 `CONSTRAINT_L{1|2|3}_TASK_PLANNING.md` 提供，本文件专注共享命令语义。

✅ 满足以上条件后方可执行命令；如参数缺失需先向用户确认。

---

## 共享命令总览（当前 4 个，持续扩充）

1. **>>任务全景对齐** — 汇总 GOAL 及项目上下文，明确 Stage-4 目标、关键里程碑与约束，建立主题草稿起点。
2. **>>任务排期矩阵** — 设计时间轴、里程碑、依赖矩阵与优先级策略，形成排期全景。
3. **>>任务执行拆解** — 拆解任务、分配责任、定义粒度与完成标准，确保执行可落地。
4. **>>任务收束写回** — 汇总推敲结果、质量门禁状态，并将确认内容写回 `spec/task_planning/` 正式资产。

> 若后续扩充命令，保持 `>>任务*` 前缀即可；各 Level 工具包引用“全部 `>>任务*` 命令”即可自动获得最新能力。

### Level 工具包挂载指引
- 各级别工具包需声明：引用本文件的全部 `>>任务*` 命令，执行前先读取本文件。
- Level 默认值由所在工具包决定；如用户显式传入 level 参数，须以用户指令为准。
- 新增命令需同步更新本文件与相关模板，保证跨 Level 一致性。

---

## 共性命令响应协议

### 通用起始段（四个命令统一）
```
🤖 检测到强制工具调用：>>任务{命令名}
📂 正在读取：TOOLKIT_SHARED_TASK_PLANNING.md + Level 配置
🎯 执行模式：{LEVEL} | 主题：{topic} | 版本：draft_v{N}
🗂️ 草稿工作区：遵循 CRAFT 草稿目录示例（如 `spec/task_planning/_draft_{topic}/draft_v{N}.md`）
[严格按工具包指令执行，不擅自扩展]
```

> 未提供 `topic` 或 `draft_v{N}` 时，需先向用户核实；禁止自行假设。

---

<!-- COMMAND_START:任务全景对齐 -->
## >>任务全景对齐 — 目标与上下文梳理

### 输出骨架
```
## 任务全景对齐（{LEVEL}）
- 项目上下文与 Stage-4 工作范围
- 关联 GOAL/US 清单与优先级摘要
- 关键里程碑 / 阶段目标 / 交付物概览
- 约束与假设：资源、时间、合规、协作边界
- 未决事项与澄清请求
- 草稿目录更新记录
```

### 操作要点
- 读取 `spec/task_planning/goal_breakdown.md` 中已确认 GOAL；缺失字段需列出澄清项。
- 建议生成 `spec/task_planning/_draft_{topic}/overview_v{N}_L{level}.md` 记录阶段全景。
- 将关键信息与需求 / 设计阶段的追溯号（US/ARCH）建立映射。
<!-- COMMAND_END:任务全景对齐 -->

---

<!-- COMMAND_START:任务排期矩阵 -->
## >>任务排期矩阵 — 时间轴与依赖编排

### 输出骨架
```
## 任务排期矩阵（{LEVEL}）
- 时间轴结构（迭代 / Sprint / 阶段）
- GOAL ↔ 里程碑 ↔ 交付物映射
- 任务依赖矩阵（含关键路径 / 阻塞项）
- 资源与容量约束（人力 / 时间 / 工具）
- 风险窗口与缓冲策略
- 自动化提醒 / 状态同步机制
```

### 操作要点
- 将排期成果写入草稿 `schedule_matrix_v{N}_L{level}.md`，并引用 GOAL ID。
- 排期细度与协同要求按照当前 Level 工具包 / 约束指南执行。
- 标记需要 Human-in-the-loop 确认的关键里程碑或资源决策。
<!-- COMMAND_END:任务排期矩阵 -->

---

<!-- COMMAND_START:任务执行拆解 -->
## >>任务执行拆解 — 任务颗粒与责任落实

### 输出骨架
```
## 任务执行拆解（{LEVEL}）
- 任务列表（含 GOAL 引用、责任人、优先级、估算）
- 完成定义（DoD/DOR）、验收方式
- 任务依赖与冲突解决策略
- 协作节奏与交付节奏（会议、汇报、同步机制）
- 风险 / 阻塞项与应对策略
- 数据更新：回写 task_breakdown.md / task_sequence.md 所需字段
```

### 操作要点
- 输出到 `task_plan_v{N}_L{level}.md`，并确保引用 GOAL ID 与相关文档。
- 任务颗粒与协作深度按当前 Level 工具包 / 约束指南执行。
- 引导记录 Human-in-the-loop 需要确认的重大任务决策。
<!-- COMMAND_END:任务执行拆解 -->

---

<!-- COMMAND_START:任务收束写回 -->
## >>任务收束写回 — 草稿收束与正式落地

### 输出骨架
```
## 任务收束写回（{LEVEL}）
- 本轮推敲摘要（覆盖执行命令）
- 进度与风险状态：里程碑完成度、阻塞、缓解措施
- 写回 `spec/task_planning/` 的文件/章节、Front Matter 更新
- 下一步动作：是否触发 >>task_scan_l{N}、是否需要 Human-in-the-loop
- 草稿目录处理：保留 / 归档 / 合并
- 待办事项与责任人
```

### 操作要点
- 明确写回对象（如 `goal_breakdown.md`、`task_sequence.md`、`milestones_timeline.md` 等）。
- 若写回受阻，记录原因、所需支持、目标时间。
- 建议输出是否需要执行对应 Level 的扫描命令验证正式成果。
<!-- COMMAND_END:任务收束写回 -->

---

## 草稿管理约定（topic-first + draft_v{N}.md）

- 草稿目录根路径：参考 CRAFT 草稿占位符（示例：`spec/task_planning/_draft_<topic>/`）
- 版本文件：`draft_v{N}.md`；可按命令拆分为 `overview/test/task/summary` 等子文件。
- 推荐结构示例：
  - `draft_dir/overview_v{N}_L{level}.md`
  - `draft_dir/schedule_matrix_v{N}_L{level}.md`
  - `draft_dir/task_plan_v{N}_L{level}.md`
  - `draft_dir/summary_v{N}_L{level}.md`
  - `draft_dir/artifacts/progress_v{N}.csv`
- Level 信息可写入文件名或 Front Matter，避免创建 L1/L2/L3 子目录造成碎片化。

---

## 级别控制（L1 / L2 / L3）

- 具体治理标准请参考 `TOOLKIT_L{1|2|3}_TASK_PLANNING.md` 与 `CONSTRAINT_L{1|2|3}_TASK_PLANNING.md`。
- 执行命令时需依据当前 Level 的质量门槛调整输出深度、粒度与追溯要求。

---

## 输入参数建议

- `topic`：主题名称（必填）
- `level`：L1 / L2 / L3（可选；缺省由工具包默认 Level 决定）
- `draft_version`：版本号 N（可选；默认按命令顺序自动 +1）
- `workspace_root`：草稿根路径（可选；未指定时沿用工具包上下文）

---

## 执行约束

- 不生成真实任务管理工具数据；仅输出任务规划文档内容。
- 禁止绕过草稿版控；正式写回必须通过 `>>任务收束写回` 明确声明。
- 输出需与草稿文件保持一致，确保追溯链条可验证。
- 若与 Level 工具包要求冲突，以更严格者为准。

---

## 错误处理与协作提醒

若出现以下情况需暂停并提示用户：
- GOAL 信息缺失或 `goal_breakdown.md` 尚未建立
- Stage-3 / Stage-2 未完成，导致任务规划缺乏输入
- Level 或资源约束不明确

> 建议采用 Human-in-the-loop 澄清后再继续执行；禁止擅自假设或创建未经确认的结构。

---

**文件版本**: SHARED-TASK-PLANNING v1.0  
**适用级别**: 跨 L1/L2/L3 通用  
**适用阶段**: TASK_PLANNING  
**最后更新**: 2025-05-xx  
**验证状态**: ✅ 已验证>>协议触发100%有效
