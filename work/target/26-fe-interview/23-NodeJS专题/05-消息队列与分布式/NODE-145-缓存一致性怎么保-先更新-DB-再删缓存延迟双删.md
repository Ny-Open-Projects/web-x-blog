---
title: [NODE-145] 缓存一致性怎么保（先更新 DB 再删缓存？延迟双删）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-145：缓存一致性怎么保（先更新 DB 再删缓存？延迟双删）？
**答**：
- 主流方案是 **Cache-Aside**：读→miss 回填；写→**先更新 DB 再删缓存**（不是更新缓存——并发写会互相覆盖旧值）。
- 为什么还要双删：并发下读请求可能在 DB 更新**前**读了旧值，又在更新**后**把旧值回填缓存——脏数据活到 TTL；第二次延迟删除专门清这种回填。
- 延迟量 ≈ 主从同步延迟 + 一次读耗时（几百 ms 量级）；生产用延迟队列/定时任务实现，不用 `setTimeout`（进程重启即丢）。
- 终极方案：Canal 订阅 binlog 异步删缓存——业务零侵入、顺序有保证；任何方案都要给缓存带 TTL 做最后防线。

```javascript
async function updateProduct(id, patch) {
  const key = `product:${id}`;
  await redis.del(key);                                     // 删①：立即删，缩短脏窗口
  await db.product.update({ where: { id }, data: patch });  // 写库
  await delayQueue.push({ key, delayMs: 500 });             // 删②：延迟删，清并发旧读回填
}
```

```mermaid
sequenceDiagram
    participant U as 读请求 A
    participant W as 写请求 B
    participant R as Redis
    participant DB as MySQL
    participant Q as 延迟队列
    U->>R: 读缓存未命中
    U->>DB: 读到旧值
    W->>R: 第一次删除缓存
    W->>DB: 提交新值
    U->>R: 旧值回填缓存 脏数据出现
    W->>Q: 投递延迟删除任务
    Q-->>R: 延迟 500ms 后第二次删除
    Note over R: 脏窗口关闭 后续读到新值
```
