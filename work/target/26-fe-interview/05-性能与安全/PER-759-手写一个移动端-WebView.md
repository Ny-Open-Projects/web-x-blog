---
title: [PER-759] 手写一个移动端 WebView 缓存配额守护：Storage 用量监控、超限清理与清理白名单
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-759：手写一个移动端 WebView 缓存配额守护：Storage 用量监控、超限清理与清理白名单

**答**：
- 配额监控：`navigator.storage.estimate()` 定期查询（usage/quota），超 80% 触发清理；分桶清理按缓存域（离线包/图片缓存/数据缓存/日志），白名单（登录态/用户设置）不动。
- 要点：清理顺序按价值/体积比"（日志最先清、离线包按最后使用时间、图片缓存 LRU）；清理后复查（仍未达标提示用户或降级为无缓存模式）；estimate 不可用（老 WebView）降级为按条数清理。
- 边界：清理是异步批量（不阻塞主线程，分片执行）；清理动作与结果上报（运维要知道配额分布）。
- 评分点：价值比清理顺序与分片执行。

```javascript

class StorageQuotaGuard {
  constructor({ threshold = 0.8, whitelist = ['auth', 'settings'] } = {}) {
    this.threshold = threshold; this.whitelist = new Set(whitelist);
    setInterval(() => this.check(), 60000);
  }
  async check() {
    if (!navigator.storage?.estimate) return this.fallbackClean();  // 老内核降级
    const { usage, quota } = await navigator.storage.estimate();
    if (usage / quota < this.threshold) return { ok: true, usageMB: +(usage / 1048576).toFixed(0) };
    const report = await this.clean(usage, quota);
    report('storage-clean', report);
    return report;
  }
  async clean(usage, quota) {
    const freed = { logs: 0, imgCache: 0, offline: 0 };
    freed.logs = await purgeOldest('logs', Infinity);           // 1. 日志全清（价值最低）
    if (usage - freed.logs > quota * this.threshold)
      freed.imgCache = await purgeLRU('img-cache', quota * 0.3); // 2. 图片 LRU 清到 30%
    if (usage - freed.logs - freed.imgCache > quota * this.threshold)
      freed.offline = await purgeStalePackages('offline-pkgs', this.whitelist); // 3. 离线包按最后使用
    return { freedMB: Object.values(freed).reduce((s, v) => s + v, 0) / 1048576, ...freed };
  }
  fallbackClean() { return purgeByCount('img-cache', 100); }    // 按条数清理
}
// 清理本身分片异步：purgeOldest 内部按 50 条/批，批间 await idle
```
