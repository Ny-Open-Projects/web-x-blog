---
title: [PER-811] 手写一个 RN 图片预加载管理器：预取队列、命中率统计与内存约束
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-811：手写一个 RN 图片预加载管理器：预取队列、命中率统计与内存约束

**答**：
- 需求：实现 preload(urls, { concurrency, maxCount })：并发受控的预取队列；同一 URL 去重（进行中/已完成）；内存约束：已完成未消费的预取超过 maxCount 时暂停新预取（等待消费腾位）；统计命中率（预取后在页面被真实加载的比例）。
- 边界：重复 URL 只入队一次；预取失败记失败并允许重试一次；销毁时清空队列与统计。
- 评分点：并发控制；maxCount 反压；命中率统计口径。

```javascript
class ImagePreloader {
  constructor({ concurrency = 3, maxCount = 50 } = {}) {
    this.queue = []; this.running = 0;
    this.done = new Set(); this.pending = new Set(); this.fail = new Set();
    this.consumed = new Set(); this.max = maxCount;
    this.conc = concurrency;
  }
  preload(urls) {                              // 去重入队
    for (const u of urls)
      if (!this.done.has(u) && !this.pending.has(u) && !this.fail.has(u)) {
        this.pending.add(u); this.queue.push(u);
      }
    this.drain();
  }
  drain() {
    while (this.running < this.conc && this.queue.length) {
      if (this.done.size - this.consumed.size >= this.max) return;   // 反压：未消费满额
      const u = this.queue.shift();
      this.running++;
      Image.prefetch(u)
        .then(() => { this.pending.delete(u); this.done.add(u); this.drain(); })
        .catch(() => { this.pending.delete(u); this.fail.add(u); })   // 允许一次重试
        .finally(() => { this.running--; this.drain(); });
    }
  }
  consume(url) {                               // 页面真实加载时调用
    this.consumed.add(url);
    report('prefetch-hit', { hit: this.done.has(url) });
  }
  destroy() { this.queue = []; this.pending.clear(); this.fail.clear(); }
}
```
