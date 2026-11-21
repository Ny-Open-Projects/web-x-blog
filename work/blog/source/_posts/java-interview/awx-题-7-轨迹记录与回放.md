---
title: "题 7：轨迹记录与回放"
date: 2026-11-18
categories: [Java面试, Agent笔试]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 7：轨迹记录与回放

### 题目（20 分钟）

实现 Agent 轨迹基建两件：
① `TrajectoryRecorder`：每步（模型调用/工具调用/终止）异步追加 JSON Lines 文件（一行一步），主循环只入队不阻塞；队列满时丢弃策略可配置（丢调试保审计 AD-106 分级）
② `TrajectoryReplayer`：从轨迹文件重建消息序列（重放给 mock 模型可复现 Agent 行为），支持失败任务回放调试（AD-093）。
要求：轨迹条目结构化（时间戳/类型/内容摘要/token），异步不丢审计级事件。

### 评分细则

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | 异步队列+消费线程 ✓｜JSON Lines 逐条落盘 ✓｜重放重建消息序列正确 ✓ | 40 |
| 边界处理 20% | 队列满分级丢弃（审计级不丢）✓｜损坏行跳过不崩 ✓ | 20 |
| 工程质量 20% | 记录器与主循环解耦（观察者/队列）✓｜格式版本化（字段演进）✓ | 20 |
| 并发与安全 20% | 消费线程优雅停机（ drains 队列）✓｜轨迹脱敏钩子 ✓ | 20 |

### 参考实现

```java
public class AsyncTrajectoryRecorder implements TrajectoryRecorder, AutoCloseable {
    private final BlockingQueue<String> queue = new LinkedBlockingQueue<>(10_000);
    private final Thread consumer;
    private final PrintWriter writer;
    private final DropPolicy dropPolicy; // AUDIT_SAFE：审计级事件不丢

    public AsyncTrajectoryRecorder(Path file, DropPolicy policy) throws IOException {
        this.writer = new PrintWriter(Files.newBufferedWriter(file, StandardCharsets.UTF_8));
        this.dropPolicy = policy;
        this.consumer = Thread.ofPlatform().daemon().name("trajectory-writer").start(this::drain);
    }

    @Override
    public void record(TrajectoryEntry entry) { // 主循环只入队（不阻塞 AD-040）
        String line = entry.toJson();
        if (entry.level() == Level.AUDIT) {      // 审计级：满了也等待写入（不丢）
            queue.offer(line);
        } else if (!queue.offer(line)) {          // 调试级：满了按策略丢
            dropPolicy.handle(entry);
        }
    }

    private void drain() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                String line = queue.poll(1, TimeUnit.SECONDS);
                if (line != null) writer.println(line);
                writer.flush();
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            queue.forEach(writer::println);       // 停机前 drain 残余（AD-307）
            writer.close();
        }
    }

    @Override public void close() { consumer.interrupt(); }
}

public class TrajectoryReplayer {
    /** 从轨迹重建消息序列（重放给 mock 模型复现行为 AD-093） */
    public List<Message> rebuild(List<TrajectoryEntry> entries) {
        List<Message> messages = new ArrayList<>();
        for (TrajectoryEntry e : entries) {
            switch (e.type()) {
                case "model" -> messages.add(Message.assistant(e.content()));
                case "tool"  -> messages.add(Message.tool(e.toolCallId(), e.content()));
                case "user"  -> messages.add(Message.user(e.content()));
            }
        }
        return messages;
    }
}
```

### 追问清单

1. 为什么异步而不是同步写？→ 同步 IO 阻塞主循环（JA-207 管线），异步队列解耦（AD-276）
2. 队列满了为什么审计级不丢？→ 审计事件是合规要求（JA-383），丢审计=违规；调试级可采样（JA-231）
3. 重放为什么要按消息序列重建而不是直接跑代码？→ 精确复现决策上下文（AD-093），mock 模型按序返回
4. 轨迹文件的字段演进怎么办？→ 版本头（schema_version 首行）+读取端兼容（AD-246 格式设计）
5. 停机时如何保证不丢日志？→ drain 残余（interrupt 后 flush），与优雅停机（AD-307）联动

### 常见错误

同步写阻塞主循环（每步 fsync）｜队列满直接抛异常（应分级）｜重放不还原 tool_call_id 关联（AD-063）｜停机丢尾部日志。
