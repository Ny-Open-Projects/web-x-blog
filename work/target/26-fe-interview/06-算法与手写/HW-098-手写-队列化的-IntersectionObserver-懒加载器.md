---
title: [HW-098] 手写懒加载调度器——IO 观察优先级队列、加载节流与失败重试
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-098：手写懒加载调度器——IO 观察优先级队列、加载节流与失败重试
**答**：图片/组件懒加载的工程化封装：单例 IO 只负责"进入视口"事件，把真正加载丢进**并发受限的加载队列**（防止弱网下同时发起 50 张图挤爆带宽），支持优先级（首屏图高优先）、失败重试与占位保布局。

```javascript
class LazyLoader {
  constructor({ concurrency = 4, rootMargin = '200px', retry = 1 } = {}) {
    Object.assign(this, { concurrency, retry });
    this.queue = []; this.active = 0;
    this.io = new IntersectionObserver((es) => {
      for (const e of es) if (e.isIntersecting) {
        this.io.unobserve(e.target);
        this.enqueue(e.target, e.target.dataset.priority === 'high' ? 10 : 0);
      }
    }, { rootMargin });
  }
  observe(el) { this.io.observe(el); }
  enqueue(el, priority) {
    this.queue.push({ el, priority, tries: 0 });
    this.queue.sort((a, b) => b.priority - a.priority);   // 高优先级先加载
    this.#drain();
  }
  #drain() {
    while (this.active < this.concurrency && this.queue.length) {
      const { el, tries } = this.queue.shift();
      this.active++;
      this.#load(el).catch(() => {
        if (tries < this.retry) this.queue.push({ el, priority: 0, tries: tries + 1 });  // 重试回队
        else el.dispatchEvent(new CustomEvent('load-failed'));
      }).finally(() => { this.active--; this.#drain(); });
    }
  }
  #load(el) {
    return new Promise((resolve, reject) => {
      const src = el.dataset.src;
      const img = new Image();
      img.onload = () => { el.src = src; el.classList.add('loaded'); resolve(); };
      img.onerror = reject;
      img.src = src;                                       // 预加载成功再赋值，避免半图
    });
  }
}
// 用法：<img data-src="a.avif" data-priority="high"> 全部 loader.observe(img)
// 弱网下并发 4、首屏 high 优先、失败重试 1 次 —— 占位（aspect-ratio CSS）防 CLS
```

**评分点**：
- 单例 IO + 并发受限加载队列（弱网不挤爆带宽），这是工程化核心。
- 优先级排序（首屏 high 先行）；重试有限次且回队保持调度。
- 预加载成功后再赋值 src（避免半渲染图）；失败派发自定义事件供 UI 反馈。
- rootMargin 提前量；unobserve 防重复触发。
