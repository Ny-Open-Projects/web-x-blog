---
title: [HW-146] 手写 Web Locks 资源协调——跨标签页互斥任务（清理/同步/选主）与锁泄漏防护
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-146：手写 Web Locks 资源协调——跨标签页互斥任务（清理/同步/选主）与锁泄漏防护
**答**：跨标签页互斥（只有一页做清理/同步）：navigator.locks.request({ifAvailable}) 非阻塞抢锁（抢不到立即返回 false——多数场景"跳过"比"排队"正确）；持锁心跳（长任务中锁持有者崩溃，浏览器自动释放——但任务要幂等可重入）；steal 模式（forceRelease 语义用 steal: true 抢死锁）。

```javascript
async function exclusiveTask(name, task, { ifAvailable = true, timeout = 30000 } = {}) {
  return navigator.locks.request(name, { ifAvailable }, async (lock) => {
    if (!lock) return { skipped: true };                  // 抢不到：另一页在做，直接跳过
    const started = Date.now();
    try {
      const result = await task();                        // 任务必须幂等可重入（持锁者崩溃后重跑安全）
      return { done: true, ms: Date.now() - started, result };
    } catch (e) {
      if (Date.now() - started > timeout) console.warn(`[lock:${name}] 超时释放`);
      throw e;
    }
  });
}
// 用法：跨标签页的本地缓存清理（PER-321 选主模式）
setInterval(async () => {
  const r = await exclusiveTask('cache-cleanup', async () => {
    await cleanupLRU(); return freedMB;
  }, { ifAvailable: true });
  if (r.skipped) return;                                  // 其他标签页已做：跳过
  report({ type: 'cleanup', ...r });
}, 10 * 60000);
// 语义对比：
// ifAvailable: true —— 抢不到跳过（清理/预取类：重复执行无意义）
// ifAvailable: false —— 排队等待（写共享存储类：必须都执行，按序）
// steal: true —— 抢占死锁持有者（滥用会破坏互斥，仅死锁恢复用）
```

**评分点**：
- ifAvailable 非阻塞抢锁语义（跳过 vs 排队的场景选择说清）。
- 任务幂等可重入要求（持锁者崩溃后浏览器自动释放，任务重跑安全）。
- 超时告警与 steal 模式的风险边界。
- 与 BroadcastChannel 选主的对比（Locks 更简单可靠——浏览器管理锁生命周期）。
