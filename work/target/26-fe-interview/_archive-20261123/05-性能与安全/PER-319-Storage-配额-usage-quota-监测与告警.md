---
title: [PER-319] 笔试题：手写源存储用量监测器——estimate 采样 + 分层用量（IndexedDB/Cache 分开统计）+ 超限降级
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-319：手写源存储用量监测器——estimate 采样 + 分层用量 + 超限降级

**题目**：实现 `StorageMonitor`：① 每 10 分钟采样 `navigator.storage.estimate()`，内存中保留最近 24 个采样点；② 分层统计：IndexedDB 用量与 Cache 用量分开（estimate 只有总量，用 `performance.measureUserAgentSpecificMemory` 不行——改用 navigator.storage.estimate 的 usageDetails（Chrome 提供 byType））；③ 用量超过 quota 80% 触发降级回调 `onPressure`；④ 页面 hidden 时 flush 采样到上报。

**答**：estimate 的 `usageDetails`（Chrome）可拿到 indexedDB/cacheStorage/serviceWorkerRegistrations 分项；无此字段时退化用业务侧自记账（写入时累加字节）。

```javascript
class StorageMonitor {
  constructor({ interval = 600000, threshold = 0.8, onPressure } = {}) {
    Object.assign(this, { interval, threshold, onPressure });
    this.samples = [];
    this.timer = setInterval(() => this.sample(), interval);
    this.sample();
  }
  async sample() {
    if (!navigator.storage?.estimate) return null;
    const est = await navigator.storage.estimate();
    const point = {
      at: Date.now(),
      usage: est.usage ?? 0, quota: est.quota ?? 0,
      details: est.usageDetails ?? null,               // Chrome: {indexedDB, caches, serviceWorkerRegistrations}
    };
    this.samples.push(point);
    if (this.samples.length > 24) this.samples.shift();
    if (point.quota && point.usage / point.quota > this.threshold) {
      this.onPressure?.(point);                        // 超限降级：清缓存/通知用户
    }
    return point;
  }
  trend() {                                            // 最近趋势：每小时增长 MB
    if (this.samples.length < 2) return 0;
    const first = this.samples[0], last = this.samples.at(-1);
    const hours = (last.at - first.at) / 3600000;
    return hours > 0 ? +((last.usage - first.usage) / 1048576 / hours).toFixed(2) : 0;
  }
  flush() {
    navigator.sendBeacon?.('/rum/storage', JSON.stringify({ samples: this.samples, trend: this.trend() }));
    this.samples = [];
  }
  destroy() { clearInterval(this.timer); }
}
// 用法
const mon = new StorageMonitor({
  threshold: 0.8,
  onPressure: (p) => { clearOldCache(); toast(`本地存储空间紧张（${(p.usage / p.quota * 100).toFixed(0)}%），已清理旧缓存`); },
});
document.addEventListener('visibilitychange', () => document.visibilityState === 'hidden' && mon.flush());
```

**评分点**：
- estimate API 正确，usageDetails 分层兜底意识（无 details 时自记账）。
- 采样保留窗口（24 点）与趋势计算。
- 超限阈值触发 onPressure 降级，降级动作是"清缓存 + 用户提示"而不是默默失败。
- flush 绑 hidden + destroy 清定时器。
