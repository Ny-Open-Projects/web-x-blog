---
title: "题 3：并行工具执行"
date: 2026-11-18
categories: [Java面试, Agent笔试]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 3：并行工具执行

### 题目（20 分钟）

模型一轮返回多个工具调用时，**无依赖的工具并行执行**（CompletableFuture.allOf），每个工具独立超时（5 秒），结果按 tool_call_id 顺序回填消息序列（与调用顺序一致）。任一工具失败不影响其他工具（失败转错误反馈）。实现 `ParallelToolExecutor.execute(List<ToolCall>) → List<ToolMessage>`。

### 评分细则

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | 并行提交（每工具一个 Future）✓｜allOf 等待全部 ✓｜结果按 id 对齐回填（不错位）✓ | 40 |
| 边界处理 20% | 单工具超时不影响其他（独立超时）✓｜单工具失败转错误消息（不整体失败）✓ | 20 |
| 工程质量 20% | 超时与取消传播（cancel(true)）✓｜执行器注入（线程池可控）✓ | 20 |
| 并发与安全 20% | 并行度上限（防打满下游）✓｜结果收集线程安全 ✓ | 20 |

### 参考实现

```java
public class ParallelToolExecutor {
    private final SafeToolExecutor delegate;   // 题 2 的容错执行器
    private final ExecutorService pool;        // 并行度由池大小控制（AD-053 隔离）
    private final Duration timeout;

    public List<ToolMessage> execute(List<ToolCall> calls) {
        // 逐个提交（并行），每个 Future 独立超时（AD-266）
        Map<ToolCall, CompletableFuture<String>> futures = new LinkedHashMap<>();
        for (ToolCall call : calls) {
            futures.put(call, CompletableFuture.supplyAsync(
                () -> delegate.executeQuietly(call), pool)  // 失败转错误文案（不抛出）
                .orTimeout(timeout.toMillis(), TimeUnit.MILLISECONDS)
                .exceptionally(ex -> "工具超时或执行失败：" + safeReason(ex)));
        }
        // allOf 等待全部完成（AD-008 并行）
        CompletableFuture.allOf(futures.values().toArray(new CompletableFuture[0])).join();
        // 按 calls 顺序回填（tool_call_id 对齐 AD-063，不错位）
        List<ToolMessage> out = new ArrayList<>();
        futures.forEach((call, f) -> out.add(ToolMessage.of(call.id(), f.join())));
        return out;
    }
}
```

### 追问清单

1. 两个工具有依赖（B 需要 A 的结果）怎么办？→ DAG 分层执行（AD-129），依赖串行、独立并行
2. 并行度如何控制？→ 线程池大小=并发上限（舱壁 AD-053），或信号量（JA-320）
3. 一个工具超时，为什么取消传播重要？→ 不中断则僵尸任务占资源（AD-302 cancel(true)）
4. 并行调用时 token 成本如何变化？→ 结果都回填上下文（AD-024 重发模型），并行省墙钟不省 token
5. 什么时候不该并行？→ 有依赖/有顺序副作用/下游限流严格（串行更稳）

### 常见错误

结果按完成顺序回填（id 错位）｜一个失败全部取消｜无独立超时（一个慢工具拖死全部）｜共享 SafeToolExecutor 的失败计数并发竞态（题 2 计数需并发安全化）。
