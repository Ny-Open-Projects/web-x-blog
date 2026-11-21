---
title: "题 8：多 Agent 主从编排"
date: 2026-11-18
categories: [Java面试, Agent笔试]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 8：多 Agent 主从编排

### 题目（25 分钟）

实现 `Orchestrator`（主 Agent 编排器）：
① `decompose(task)` 用 LLM 把任务拆解为子任务列表（含依赖声明：哪些子任务可并行）
② 按 DAG 拓扑执行：无依赖的子任务并行分发给 `SubAgent`（每个子 Agent 独立上下文与预算），有依赖的等前置完成
③ 聚合：子结果按声明合并为最终产出
④ 失败传播策略可配置：子失败→重试（1 次）→跳过并标注→整体失败，三档
要求：子 Agent 隔离（独立消息序列/预算），失败不传染（JA-373）。

### 评分细则

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | LLM 拆解子任务+依赖声明 ✓｜DAG 拓扑执行（并行/串行正确）✓｜聚合产出 ✓ | 40 |
| 边界处理 20% | 子失败三档传播策略 ✓｜跳过时结果标注"未完成部分" ✓｜拆解失败（LLM 返回不可解析）处理 ✓ | 20 |
| 工程质量 20% | 子 Agent 隔离（独立消息序列/预算池）✓｜DAG 数据结构清晰 ✓ | 20 |
| 并发与安全 20% | 并发子任务结果线程安全收集 ✓｜子预算独立（互相不挤占）✓ | 20 |

### 参考实现

```java
public class Orchestrator {
    private final ModelClient model;
    private final Function<SubTask, SubAgent> subAgentFactory; // 每子任务独立 Agent（JA-373 隔离）

    public record SubTask(String id, String description, List<String> dependsOn) {}
    public record SubResult(String taskId, String output, Status status) { // status: OK/SKIPPED/FAILED
        enum Status { OK, SKIPPED, FAILED }
    }

    public String run(String task, FailurePolicy policy) {
        // ① LLM 拆解（输出 JSON 子任务数组，含依赖）
        List<SubTask> plan = decompose(task);
        // ② DAG 拓扑执行（AL-024 拓扑序：入度为零先跑）
        Map<String, SubResult> results = new ConcurrentHashMap<>();
        List<SubTask> pending = new ArrayList<>(plan);
        while (!pending.isEmpty()) {
            List<SubTask> ready = pending.stream()
                .filter(t -> t.dependsOn().stream().allMatch(d ->
                    results.containsKey(d) && results.get(d).status() == SubResult.Status.OK))
                .toList();
            if (ready.isEmpty()) { // 剩余全被依赖阻断（前置失败）→ 按策略处理
                markBlockedAsSkipped(pending, results, policy); break;
            }
            // 并行执行无依赖子任务（AD-026），每个子 Agent 独立上下文+预算（JA-373）
            Map<String, CompletableFuture<SubResult>> fs = new HashMap<>();
            for (SubTask t : ready) {
                SubAgent agent = subAgentFactory.apply(t);
                String context = contextFor(t, results); // 只传依赖结果（最小化 AD-215）
                fs.put(t.id(), CompletableFuture.supplyAsync(() -> agent.execute(context)));
            }
            fs.forEach((id, f) -> {
                try {
                    results.put(id, f.get(60, TimeUnit.SECONDS));
                } catch (Exception e) {
                    results.put(id, policy.handle(id, e)); // 重试→跳过标注→失败（AD-133）
                }
            });
            pending.removeIf(t -> results.containsKey(t.id()));
        }
        // ③ 聚合（按计划顺序合并，标注 SKIPPED 部分）
        return aggregate(task, plan, results);
    }
}
```

### 追问清单

1. 子 Agent 之间能直接通信吗？→ 默认隔离（父中转），直接通信引入耦合（AD-032 协议化才可）
2. 拆解的 JSON 解析失败怎么办？→ 重试拆解/降级为单 Agent 直答（AD-133 传播）
3. 为什么子结果只传依赖结果而非全部？→ 上下文最小化（AD-215），泄露面与 token 双控
4. 聚合时两个子结论矛盾怎么办？→ 裁决机制（AD-462：投票/加权/裁判）
5. 并发子 Agent 的预算怎么管？→ 独立子池（AD-500 池隔离），总池兜底（AD-553）
6. 循环依赖（A 依赖 B、B 依赖 A）怎么办？→ 拆解校验（拓扑排序失败=LLM 拆解错误，重拆）

### 常见错误

子 Agent 共享父上下文（泄露+污染）｜DAG 判断遗漏（阻断死循环）｜失败整体失败（部分结果丢弃）｜并发结果 HashMap 竞态（应 ConcurrentHashMap）。
