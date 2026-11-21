---
title: "题 10.2.2：Function Calling / Tool Use 是什么？和 Agent 什么关系？"
date: 2026-11-18
categories: [Java面试, AI与Agent]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 10.2.2：Function Calling / Tool Use 是什么？和 Agent 什么关系？

**【参考回答（可背）】**
Function Calling：把工具的 JSON Schema 声明给模型 → 模型在需要时输出"调用哪个函数+参数"（结构化 JSON）→ **应用执行** → 结果回填 → 模型继续生成。模型不执行，只"决定调用"——执行永远在你手里（安全边界）。
这构成 Agent 的最小闭环：**感知（用户输入）→ 思考（模型决策）→ 行动（工具调用）→ 观察（结果回填）→ 循环直到完成** —— 即 ReAct（Reasoning + Acting）模式。
Java 实践：Spring AI 的 @Tool 注解 / FunctionCallback；把现有 Service 方法暴露为工具（查询订单、创建工单），加上参数校验与权限校验。

**【追问链】**
1. 工具太多怎么办？→ 工具检索（先选工具组再选工具）、分层路由（主 Agent 调度子 Agent，每个子 Agent 只带少量工具）。
2. 工具调用的安全边界？→ 白名单、权限继承用户身份（不能让 Agent 越权）、破坏性操作人工确认（human-in-the-loop）、审计日志全量。

**【P10 加分项】**
谈"Agent = 新的应用程序范式"：传统应用 = 确定性代码 + 数据；Agent 应用 = 概率性模型 + 工具生态 + 编排。工程含义：**测试方式（评测集替代单测的部分角色）、发布方式（灰度按效果指标）、监控方式（轨迹追踪 trace LLM 调用链）都要重做**——这是 Java 后端工程师最大的转型机会与冲击。

---
