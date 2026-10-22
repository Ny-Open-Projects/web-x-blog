# 73. 什么是 AI Agent：定义、感知-计划-行动循环与记忆/长链技术

## 纲要

- **定义**：Agent=代理，代替人操作，让 LLM 自检输出是否最优/正确，不对就重试——弥补 LLM 自身"每层算力相同、输错无法改前置"的缺陷。
- **与 LLM 区别**：LLM 一次性输出、输错不能回溯修改；Agent 模拟人类"拆分→修正"的循环，强调自主性与主动性。
- **核心循环（4 阶段）**：Perception 感知（输入进记忆体）→ Planning 计划（拆步骤，如查加州人口→查阿拉斯加→除法）→ Policy 决策（是否终止/达标）→ Action 操作（两路径：完成 / 未实现需补接口）。
- **Action 最复杂**：LLM 自身无能联网等，需调用外部 tools（解释器/计算器/日历/搜索），相当于给模型"装手脚"。
- **Agent 内部结构**：state 状态（用户问题/背景）、memory 记忆（感觉/短期/长期）、experiences 经验、reflection 反应、world knowledge。
- **长链技术 long-chain**：把 LLM 输出拆分并链接，用向量数据库存储，后续提取关联内容；prompt template 特定结构，核心是 **ReAct 原则**（reason+act 交错：thought 想法 / action 执行 / observation 观察）。
- **多 agent 协同** multi-agent；当前受限：伦理 + 算力（全球算力不足以支撑每天持续迭代）。

> 本章按课程口径重构；产品名已规范化（LLM/Agent/ReAct）；剥离营销与课程群引流。

## 一、Agent 定义与与 LLM 差异

- Agent=代理，代替人操作并让 LLM 自检/重试，弥补 LLM 输错不可回溯的缺陷。
- LLM 每层算力相同、输出后无法改前置；Agent 循环模拟人类拆分+修正。

## 二、感知-计划-行动循环

- Perception 感知 → Planning 计划（拆步骤）→ Policy 决策（终止/达标）→ Action 操作（完成 or 调外部接口）。
- Action 是链路最复杂部分：LLM 自身无能联网，planning 中的"搜索人口"需调外部 tools。

## 三、记忆与长链技术

- 内部：state/memory（感觉/短期/长期）/experiences/reflection/world knowledge。
- 注意：memory 非对话上下文长度，指模型规模增大可存更多信息 + 训练微调记录信文关系（长期记忆）。
- 长链 long-chain：拆分输出并链接，向量库存储，后续提取关联；prompt template 用 ReAct（thought/action/observation 交错）。

## 四、ReAct 与多 Agent

- ReAct：先提任务→LLM 执行→对结果评判（交 LLM），类 CoT 提准。
- multi-agent：多个代理协同合作；受限主因伦理与算力。

## 五、FAQ

**Q1：Agent 与 LLM 本质区别？**
LLM 一次性输出且输错不可改；Agent 循环拆分+重试，自主修正。

**Q2：Agent 循环哪段最难？**
Action：LLM 自身无能联网/执行，需调外部 tools（解释器/搜索等）。

**Q3：长链技术解决什么？**
拆分 LLM 输出并链接存储，后续提取关联内容，突破单次上下文。

**Q4：ReAct 三要素？**
thought 想法、action 执行、observation 观察，交错循环。

## 六、面试高频问答

**1. Agent 的核心循环阶段？**
Perception 感知 → Planning 计划 → Policy 决策 → Action 操作（两路径）。

**2. 为什么 Agent 需要 tools？**
LLM 自身无能联网/执行代码，需外部工具扩展能力（装手脚）。

**3. memory 与上下文长度的区别？**
memory 指模型规模带来的长程信息存储与训练关系压缩，非对话上下文窗口。

**4. ReAct 原则是什么？**
reason+act 交错（thought/action/observation），让 LLM 边思考边验证提准。

## 七、ops 提示（增效）

> **Agent=循环+工具**：脱离 tools 的"Agent"只是 LLM 包装。
>
> **ReAct 提准**：拆 thought/action/observation 比一次性输出更稳。
>
> **长链靠向量库**：拆分存储+关联提取是突破上下文的关键。

