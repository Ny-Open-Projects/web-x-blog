---
title: [WEB-164] Web Locks API 怎么保证多标签页一致性？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-164：Web Locks API 怎么保证多标签页一致性？
**答**：
- 问题：多标签页同源操作共享存储（IDB 清理、轮询去重、任务分发）会互相踩踏。
- Web Locks：navigator.locks.request(name, callback) 对命名锁排队，同一时刻只有一个持有者，标签页关闭自动释放——比 localStorage 抢锁健壮得多。
- 模式：独占（默认）与共享 { mode: 'shared' }；ifAvailable: true 抢不到就走降级逻辑，不排队。
- 典型用法：同一时刻只允许一个标签页做数据同步/过期清理/连接建立，其余标签页等待或复用结果。

```javascript
// 只让一个标签页执行过期缓存清理，其余直接跳过
navigator.locks.request('cache-gc', { ifAvailable: true }, async (lock) => {
  if (!lock) return;                       // 别的标签页在清理，跳过
  const stale = await findStaleEntries();
  await Promise.all(stale.map((k) => db.delete('cache', k)));
  console.log('gc done by this tab');
});
// 需要等待锁的场景（如初始化迁移）：不加 ifAvailable，自动排队
await navigator.locks.request('db-migrate', async () => {
  await runMigrationOnce();
});
```

## 二十七、性能采集与分析
