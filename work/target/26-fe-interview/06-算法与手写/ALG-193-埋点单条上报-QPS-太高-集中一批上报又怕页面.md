---
title: [ALG-193] 埋点单条上报 QPS 太高，集中一批上报又怕页面关闭丢失。如何设计"批量 + 去重 + 定时冲刷 + 离开兜底"的上报队列？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-193：埋点单条上报 QPS 太高，集中一批上报又怕页面关闭丢失。如何设计"批量 + 去重 + 定时冲刷 + 离开兜底"的上报队列？
**答**：四个机制协同：① 内存去重——事件唯一 key（id + ts）进 Set，重复丢弃；② 双阈值——队列达到 size 上限立即冲刷，否则由定时器周期性冲刷，兼顾延迟与吞吐；③ 冲刷用 `navigator.sendBeacon`（异步、页面卸载也能送达、不阻塞）；④ `visibilitychange` 到 hidden 时强制冲刷一次兜底（这是移动端最后可靠的时机，beforeunload 不可靠）。冲刷 O(队列长度)。

```javascript
class Tracker {
  constructor({ size = 20, interval = 5000 } = {}) {
    this.queue = [];
    this.seen = new Set();         // 内存去重
    this.size = size;
    this.timer = setInterval(() => this.flush(), interval); // 定时冲刷
    // 兜底：页面进后台（或卸载）前强制冲刷，beforeunload 在移动端不可靠
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) this.flush();
    });
  }
  track(event) {
    const key = `${event.id}:${event.ts}`;
    if (this.seen.has(key)) return;         // 去重：同一事件只入队一次
    this.seen.add(key);
    this.queue.push(event);
    if (this.queue.length >= this.size) this.flush(); // 批量阈值触发
  }
  flush() {
    if (!this.queue.length) return;
    const batch = this.queue.splice(0);     // 取空队列
    this.seen.clear();
    navigator.sendBeacon('/api/track', JSON.stringify(batch)); // 卸载也能送达
  }
}
```
