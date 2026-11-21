---
title: "题 9：断点恢复 checkpoint"
date: 2026-11-18
categories: [Java面试, Agent笔试]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 9：断点恢复 checkpoint

### 题目（25 分钟）

实现 Agent 的断点恢复：
① `Checkpoint` 数据结构：消息序列+任务状态+预算余量+工具执行登记表（已完成步骤清单）
② `CheckpointStore` 接口：save(taskId, checkpoint) / load(taskId)，内存与文件两个实现
③ `AgentExecutor` 每步后自动 save，`resume(taskId)` 从最近 checkpoint 恢复继续执行
④ 讨论并实现：**工具幂等前提**（重放会重复执行工具，非幂等工具用"执行登记表"跳过已执行步骤）
要求：恢复后消息序列完整（不丢轮次），登记表让非幂等工具不重复执行。

### 评分细则

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | Checkpoint 含消息序列+登记表 ✓｜每步自动 save ✓｜resume 从 checkpoint 续跑且消息序列完整 ✓ | 40 |
| 边界处理 20% | 非幂等工具跳过（登记表）✓｜checkpoint 损坏容错（回退上一份）✓ | 20 |
| 工程质量 20% | Store 接口抽象（内存/文件可换）✓｜序列化格式版本化 ✓ | 20 |
| 并发与安全 20% | 同任务并发恢复的互斥 ✓｜checkpoint 含敏感数据加密意识 ✓ | 20 |

### 参考实现

```java
public record Checkpoint(String taskId, int step, List<Message> messages,
                         Set<String> executedToolKeys, // 工具执行登记表（幂等前提 AD-038）
                         long budgetUsed, Instant savedAt) {
    public String toJson() { /* 序列化：消息+登记表+预算 */ }
    public static Checkpoint fromJson(String json) { /* 反序列化，版本兼容 */ }
}

public interface CheckpointStore {
    void save(Checkpoint cp);
    Optional<Checkpoint> loadLatest(String taskId);
}

public class AgentExecutor { // 题 1 的扩展
    private final CheckpointStore store;

    public String runWithRecovery(String taskId, String task) {
        // 恢复或初始化
        Checkpoint cp = store.loadLatest(taskId).orElseGet(() -> initial(taskId, task));
        List<Message> messages = new ArrayList<>(cp.messages());
        BudgetCounter budget = BudgetCounter.restore(cp.budgetUsed());
        Set<String> executed = new HashSet<>(cp.executedToolKeys());
        int step = cp.step();

        for (; step < maxSteps; step++) {
            ModelResponse resp = model.chat(messages, tools.specs());
            messages.add(Message.assistant(resp));
            if (!resp.hasToolCalls()) return resp.content();
            for (ToolCall call : resp.toolCalls()) {
                String key = call.idempotencyKey(); // 工具+参数 hash（AD-057）
                ToolMessage msg;
                if (executed.contains(key)) {
                    msg = ToolMessage.of(call.id(), "[已执行，跳过] 结果见登记表"); // 非幂等保护（AD-038）
                } else {
                    ToolResult r = tools.execute(call.name(), call.args());
                    executed.add(key);
                    msg = ToolMessage.of(call.id(), r.content());
                }
                messages.add(msg);
            }
            // 每步后自动 checkpoint（消息序列完整保存 AD-037）
            store.save(new Checkpoint(taskId, step + 1, List.copyOf(messages),
                                      Set.copyOf(executed), budget.used(), Instant.now()));
        }
        return gracefulShutdown(messages);
    }
}
```

### 追问清单

1. 为什么恢复需要"工具执行登记表"？→ 重放会重复执行工具（发邮件两次），非幂等工具必须登记跳过（AD-038 红线）
2. 登记表的 key 怎么设计？→ 工具名+参数 hash（同参数同结果语义 AD-057 幂等键）
3. checkpoint 每步存还是每阶段存？→ 每步最安全（存储代价权衡 AD-037 粒度），阶段存恢复丢步
4. checkpoint 损坏怎么办？→ 保留最近 N 份（回退上一份 AD-642），损坏检测（校验和）
5. 恢复时模型上下文超窗怎么办？→ 恢复后先走裁剪管线（AD-023），恢复与裁剪正交
6. 多实例同时恢复同一任务？→ 恢复互斥（分布式锁或状态机 AD-058），双恢复=重复副作用

### 常见错误

只存任务状态不存消息序列（恢复后上下文断）｜登记表缺失（非幂等工具重复执行）｜恢复后步数从 0 重计｜checkpoint 无版本化（反序列化崩）。
