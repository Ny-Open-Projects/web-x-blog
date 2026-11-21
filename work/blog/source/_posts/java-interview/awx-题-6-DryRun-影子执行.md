---
title: "题 6：DryRun 影子执行"
date: 2026-11-18
categories: [Java面试, Agent笔试]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 6：DryRun 影子执行

### 题目（15 分钟）

给 AgentExecutor 增加 **dryRun 模式**：① 构造时传入 `boolean dryRun`（或 AgentConfig）② dryRun 下工具调用不真实执行，返回按工具声明生成的**模拟结果**（ToolSpec 声明示例返回值）③ 产出完整"计划轨迹"（每步记录：本应调用什么工具/参数/模拟结果），供人工审阅 ④ dryRun 与正常模式代码路径尽量复用（不复制循环）。场景：新 Agent 上线前人工审计划（AD-104 plan-approve-execute）。

### 评分细则

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | 执行层拦截（dryRun 时跳过真实调用）✓｜模拟结果生成（按 spec）✓｜计划轨迹完整产出 ✓ | 40 |
| 边界处理 20% | dryRun 与真实模式代码路径复用（不复制循环）✓｜模拟结果标注"模拟"防误用 ✓ | 20 |
| 工程质量 20% | 拦截在执行器层（非循环层 if）✓｜配置驱动（非硬编码）✓ | 20 |
| 并发与安全 20% | dryRun 无副作用保证（写工具也不执行）✓｜计划轨迹脱敏意识 ✓ | 20 |

### 参考实现

```java
public class DryRunAwareExecutor implements ToolExecutor {
    private final ToolExecutor realExecutor;
    private final boolean dryRun;

    @Override
    public ToolMessage execute(ToolCall call, ToolSpec spec) {
        if (dryRun) {
            // 模拟结果：按 spec 的示例返回值生成（声明驱动，AD-372）
            String simulated = spec.simulatedResult(); // spec 声明 exampleOutput
            return ToolMessage.of(call.id(),
                "[DRY-RUN 模拟] " + simulated + "（真实执行将调用 " + call.name() + "）");
        }
        return realExecutor.execute(call, spec); // 真实模式
    }
}
// 循环完全复用（不复制）：AgentExecutor 只依赖 ToolExecutor 接口（题 1 结构不变）
// 计划轨迹 = dryRun 的完整轨迹（每步"本应做什么"），供 plan-approve-execute（AD-104）
```

### 追问清单

1. 为什么拦截在执行器层而不是循环层加 if？→ 执行器层拦截让循环完全复用（JA-723 插件思想），循环层 if 是复制代码
2. 模拟结果怎么保证"贴近真实"？→ spec 声明 exampleOutput（AD-169 mock 保真），或录制真实结果回放（AD-350 快照）
3. dryRun 对写操作工具（发邮件）的保证？→ 拦截在执行器层，写工具同样不触达（副作用零）
4. 计划轨迹人工审完后如何"批准执行"？→ 同一轨迹切真实模式重放（AD-104 plan-approve-execute）
5. dryRun 与影子执行的区别？→ dryRun 是单任务计划预览，影子是生产流量双跑对比（AD-371/234）

### 常见错误

循环里加 if(dryRun)（复制循环）｜写工具在 dryRun 也执行了｜模拟结果没有"模拟"标注（误用为真实）｜计划轨迹不含参数（审不完整）。
