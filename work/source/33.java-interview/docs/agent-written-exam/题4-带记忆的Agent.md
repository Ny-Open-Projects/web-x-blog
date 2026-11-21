# 题 4：带记忆的 Agent

## 题目（20 分钟）

实现 `Memory` 接口与基于 `ConcurrentHashMap` 的实现，并集成到 Agent：
① `Memory` 接口：`write(userId, entry)` / `search(userId, query, topK)` / `delete(userId, memoryId)`
② Agent 每次任务结束后把"任务摘要+用户偏好"写入记忆
③ 新任务开始时按任务描述检索 topK=3 相关记忆注入 system 上下文
要求：写回有判据（不是所有对话都写）、用户间隔离（userId 维度严格隔离）。

## 评分细则

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | 接口三方法实现 ✓｜写回有判据（非全量写入）✓｜检索注入 system ✓｜userId 隔离严格 ✓ | 40 |
| 边界处理 20% | 无记忆时正常工作（空检索）✓｜delete 级联（用户删除权 AD-075）✓ | 20 |
| 工程质量 20% | 接口抽象（实现可换向量库 AD-290）✓｜写回判据声明式 ✓ | 20 |
| 并发与安全 20% | ConcurrentHashMap 线程安全 ✓｜跨用户隔离测试意识（JA-097 红线）✓ | 20 |

## 参考实现

```java
public interface Memory {
    void write(String userId, MemoryEntry entry);
    List<MemoryEntry> search(String userId, String query, int topK);
    void delete(String userId, String memoryId);
}

public class InProcessMemory implements Memory {
    // userId → 该用户的记忆列表（AD-072 隔离：结构即隔离）
    private final Map<String, List<MemoryEntry>> store = new ConcurrentHashMap<>();

    @Override
    public void write(String userId, MemoryEntry entry) {
        store.computeIfAbsent(userId, k -> new CopyOnWriteArrayList<>()).add(entry);
    }

    @Override
    public List<MemoryEntry> search(String userId, String query, int topK) {
        List<MemoryEntry> mine = store.getOrDefault(userId, List.of());
        // 简版相关性：关键词重叠计数（生产版换向量检索 AD-013）
        return mine.stream()
            .sorted((a, b) -> score(b, query) - score(a, query))
            .filter(e -> score(e, query) > 0)
            .limit(topK).toList();
    }

    @Override
    public void delete(String userId, String memoryId) { // 用户删除权（AD-075）
        store.getOrDefault(userId, new CopyOnWriteArrayList<>())
             .removeIf(e -> e.id().equals(memoryId));
    }
}

// Agent 集成：写回判据（AD-504 不是所有对话都写）
public void onTaskDone(String userId, String task, String result) {
    if (isWorthRemembering(task, result)) {  // 判据：含用户偏好/事实性结论才写
        memory.write(userId, MemoryEntry.of(task, summarize(result)));
    }
}
public List<Message> beforeTask(String userId, String task) {
    List<MemoryEntry> hits = memory.search(userId, task, 3);
    return hits.isEmpty() ? List.of()
        : List.of(Message.system("相关历史记忆：\n" + format(hits)));
}
```

## 追问清单

1. 为什么 userId 是隔离的第一道防线？→ 跨用户串号=数据泄露事故（JA-097 红线）
2. 生产环境记忆用什么存储？→ 向量库（语义检索）+KV（会话）+SQL（画像）三存储（AD-436）
3. 记忆会无限膨胀怎么办？→ 时效（AD-468）+合并（AD-469）+容量治理（AD-475）
4. 记忆写错了（污染）怎么办？→ 写回审计+异常检测+回滚（AD-504/173）
5. 用户要求"忘掉我说的 X"怎么实现？→ 主体权利 delete（AD-075），级联备份

## 常见错误

记忆全局共享（无 userId 维度）｜所有对话都写入（噪声记忆）｜检索无阈值（弱相关全注入）｜删除只删列表不删索引。
