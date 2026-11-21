---
disableNunjucks: true
title: 8-9 JManus的文件架构以及Prompt提交入口
date: 2026-10-24 10:22:00
categories: [多Agent与SpringAI]
tags: [AI Agent, SpringAI, AgentScope, 多Agent与SpringAI]
---

## 【学习目标】
- 列举 JManus 的核心包（Agent / LLM / tool / Planning / Dynamic 等）及其职责。
- 定位用户提交 Prompt 的代码入口：`ManusController.askQuery`。
- 理解 planId 与 memoryId 在后续计划创建与记忆关联中的作用。

## 【正文】
JManus 是 OpenManus 的 Java 复刻版，二者架构思路完全一致，区别仅在语言栈，OpenManus 用 Python，JManus 基于 Spring Boot 与 Spring AI Alibaba。要自定义其内部逻辑并嵌入自有系统，必须先摸清它的代码结构。

Manus 的两大骨架（全局规划 + 基层执行）与两个 AI 自循环（每步结果验证反思、整体计划执行后评估调整）在 JManus 中均被保留；工具驱动（含 MCP）与多 Agent 模块化同样延续。JManus 的价值在于：我们并非用其可视化界面手动操作，而是改写内部代码、打包后作为接口嵌入自有程序，由自有系统调用这套多智能体能力。

**核心包布局**：项目源码按职责分包，名称即语义。

```mermaid
flowchart LR
    subgraph 框架层
        A[Agent] -->|智能体属性与创建|
        C[Config] -->|配置|
        E[Exception] -->|异常|
        I[i18n] -->|国际化|
        L[LLM] -->|大模型调用|
        T[tool] -->|工具箱|
        W[Workflow] -->|工作流|
        P[Prompt] -->|提示词|
        APP[JManusSpringBootApplication] -->|启动入口|
    end
    subgraph 业务核心
        EV[Event] -->|任务事件|
        R[Recorder/Entity] -->|实体类|
        D[Dynamic] -->|自定义Agent/MCP/Prompt|
        PL[Planning] -->|计划协调核心|
    end
```

`tool` 是工具箱，自定义工具放入即可被 Agent 取用；`Recorder` 内含 `Entity` 实体类；`Dynamic` 存放用户自定义的 Agent、MCP 与 Prompt；`Planning` 是整个架构的核心，后续课程会聚焦其中。`JManusSpringBootApplication` 即 Spring Boot 启动类。

**Prompt 提交入口**：用户需求经 `Planning` 包下的 `ManusController` 提交，关键方法是 `askQuery`。该方法以 `@PostMapping("/execute")` 接收 POST 请求，先用 `Input` 读取用户 Prompt，再生成 `planId`（计划标识，供后续创建计划使用）与 `memoryId`（记忆标识，后续计划、执行等记忆均与其关联）。此外，`@GetMapping("/details/{planId}")` 通过 `planExecutionRecorder` 获取指定计划的详细执行记录，异常处理则经 `exceptionCache` 抛出。

```mermaid
flowchart TD
    U[用户提交 Prompt] --> M[ManusController.askQuery]
    M -->|@PostMapping /execute| I[Input 读取 Prompt]
    I --> P[生成 planId]
    I --> R[生成 memoryId]
    P --> F[PlanningFactory 创建计划]
    R --> F
    M -.->|@GetMapping /details/{planId}| D[planExecutionRecorder 取执行记录]
```

## 【易错点 / 面试题】
1. JManus 与 OpenManus 的关系？答：同一架构思路的跨语言复刻，OpenManus 用 Python、JManus 用 Java + Spring AI Alibaba，核心骨架（规划/执行、工具驱动、多 Agent）一致。
2. 为什么 `memoryId` 要在提交入口就生成？答：记忆需与计划、执行全过程关联，越早绑定标识，后续各阶段才能用同一 ID 串联上下文。
3. `Planning` 包为何是核心？答：计划创建、任务分配、执行协调均落在其中，是 JManus 多 Agent 编排的枢纽。

## 【小结】
JManus 以清晰的职责分包承载多 Agent 架构，用户请求统一由 `ManusController.askQuery` 进入，借 `planId`/`memoryId` 串联计划与记忆。完整离线可跑的多 Agent 编排示例见 `981-demo/src/main/java/com/travel/agent/agent/SupervisorAgent.java`（以 AgentScope 离线桩复刻『主管调度成员』范式，与本章 JManus/Manus 思路同源，但栈不同）。

（技术前瞻：Spring AI 2.1 的 Message Parts 与渐进披露将进一步简化 Agent 间上下文与工具的标准化传递，但 JManus 当前的 Planning 编排范式不变。）
