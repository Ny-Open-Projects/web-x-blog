# 8-10 JManus 的核心：计划协调器

## 【学习目标】
- 说明 `PlanningCoordinator`（计划协调器）在 JManus 中的核心地位。
- 梳理「用户入口 → PlanningFactory → PlanningCoordinator 构造器」的创建链路。
- 解释 PlanCreator / PlanExecutorFactory / PlanFinalizer 如何覆盖计划全生命周期。

## 【正文】
沿 JManus 的设计骨干：用户提交请求 → 创建计划（高层规划）→ 执行任务。任务执行又按复杂度分叉，简单任务直接交由对应 Agent，复杂任务由主管级 Agent 再拆解后分派。这条骨干的枢纽就是计划协调器。

**用户入口的两步动作**：`ManusController` 中的请求入口方法（接收 `/execute`）先初始化 `ExecutionContext` 执行上下文，把 `planId`、`memoryId` 等属性写入其中；随后创建 `PlanningCoordinator` 计划协调器。协调器由 `PlanningFactory` 的 `createPlanningCoordinator` 方法创建，且必须把刚生成的 `ExecutionContext` 作为参数传入。

协调器一旦生成，便在异步线程中执行计划创建与任务执行，并立即向用户返回 OK，用户无需等待，后台异步完成后续全部工作：

```java
        // 生成内存ID
        memoryId = RandomStringUtils.randomAlphabetic(count: 8);

        // 设置上下文
        context.setMemoryId(memoryId);

        // 异步创建并执行计划
        CompletableFuture.supplyAsync(() -> {
            try {
                memoryService.saveMemory(new MemoryEntity(context.getMemoryId(), query));
                return planningFlow.executePlan(context);
            } catch (Exception e) {
                logger.error("Failed to execute plan", e);
                throw new RuntimeException("Failed to execute plan: " + e.getMessage());
            }
        });
```

异步返回 OK 的设计，让用户在提交 Prompt 后即可放手，由 JManus 后台自主完成「查库、读文件、调 API、生成计划、执行、汇总」的全流程。该异步块先持久化记忆，再触发 `planningFlow.executePlan(context)` 跑通整条生命周期。

**协调器的创建链路**：`createPlanningCoordinator` 并非静态方法，而是通过注入的 `PlanningFactory` 实例调用，`@Lazy` 延迟加载该工厂以提升性能：

```java
        @Autowired
        @Lazy
        private PlanningFactory planningFactory;
```

真正的协调器对象在其自身构造方法中 `new` 出来，构造需传入三个参数：`PlanCreator`（计划开始）、`PlanExecutorFactory`（计划执行）、`PlanFinalizer`（计划结束）。三者恰好对应计划的生命周期三段。

```mermaid
flowchart TD
    A[ManusController 入口方法] --> B[初始化 ExecutionContext]
    B --> C[PlanningFactory.createPlanningCoordinator]
    C --> D[@Lazy 注入 PlanningFactory]
    D --> E[PlanningCoordinator 构造器]
    E --> F1[PlanCreator 计划开始]
    E --> F2[PlanExecutorFactory 计划执行]
    E --> F3[PlanFinalizer 计划结束]
    E --> G[异步执行计划 + 返回 OK]
```

这层嵌套创建的意义在于：没有计划协调器，后续的任务执行、工具调用、Agent 分派都无从谈起。它通过持有 PlanCreator / PlanExecutorFactory / PlanFinalizer，把「意图理解 → 计划制定 → 计划执行 → 结果总结」整条生命周期统一管理，因而是 JManus 业务逻辑的核心。

## 【易错点 / 面试题】
1. 为什么计划协调器要异步执行？答：计划创建与执行可能耗时较长（涉及多轮大模型调用与工具调用），异步可在受理请求后立即返回，避免阻塞用户连接。
2. `PlanningFactory` 为何用 `@Lazy`？答：延迟初始化，减少启动期不必要的依赖加载，提升容器启动性能。
3. 协调器构造的三个参数是什么含义？答：PlanCreator 负责计划开始（意图分析+建计划），PlanExecutorFactory 负责计划执行，PlanFinalizer 负责计划收尾总结，合起来覆盖计划全生命周期。

## 【小结】
计划协调器是 JManus 的中枢，经「入口方法 → PlanningFactory → 自身构造器」三级创建，借 PlanCreator / PlanExecutorFactory / PlanFinalizer 统管计划全生命周期，并以异步执行解耦用户请求与后台编排。完整离线可跑的多 Agent 编排示例见 `981-demo/src/main/java/com/travel/agent/agent/SupervisorAgent.java`（以 AgentScope 离线桩复刻『主管调度成员』范式，与本章 JManus/Manus 思路同源，但栈不同）。

（技术前瞻：Spring AI Agents 方向将把「主管协调多成员」范式进一步标准化，但 JManus 当前以 PlanningCoordinator 自管生命周期的设计范式不变。）
