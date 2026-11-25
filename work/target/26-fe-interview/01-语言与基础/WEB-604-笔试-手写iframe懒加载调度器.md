---
title: [WEB-604] 笔试：手写第三方 iframe 懒加载调度器
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## WEB-604：笔试：手写第三方 iframe 懒加载调度器

**答**：实现 `IframeLazy`：① 页面中的占位元素带 `data-iframe-src`，进入视口（IntersectionObserver rootMargin 200px）才创建 iframe；② 同一时刻最多 2 个 iframe 在加载中（并发上限，避免第三方脚本集中抢主线程）；③ 加载完成（load 事件）或 8s 超时后释放并发额度；④ 失败/超时的 iframe 移除并记数；⑤ 重复 src 的占位只创建一次。写出核心实现。

```javascript
class IframeLazy {
  constructor(maxLoading = 2) {
    this.max = maxLoading; this.loading = 0; this.created = new Set(); this.failCount = 0;
    this.queue = [];
    this.io = new IntersectionObserver((ents) => {
      for (const e of ents) if (e.isIntersecting) {
        this.io.unobserve(e.target);
        this.queue.push(e.target);
        this._drain();
      }
    }, { rootMargin: '200px' });
  }
  observe(el) { if (!this.created.has(el.dataset.iframeSrc)) this.io.observe(el); }
  _drain() {
    while (this.loading < this.max && this.queue.length) {
      const el = this.queue.shift();
      const src = el.dataset.iframeSrc;
      if (this.created.has(src)) continue;
      this.created.add(src); this.loading++;
      const f = document.createElement('iframe');
      f.src = src; f.loading = 'lazy'; f.width = el.dataset.w || '300'; f.height = el.dataset.h || '150';
      const done = () => { this.loading--; this._drain(); };
      const timer = setTimeout(() => { f.remove(); this.failCount++; done(); }, 8000);
      f.addEventListener('load', () => { clearTimeout(timer); el.replaceWith(f); done(); });
      f.addEventListener('error', () => { clearTimeout(timer); this.failCount++; done(); });
    }
  }
}
```

**评分点**：
- IntersectionObserver 懒触发 + rootMargin 预加载带
- 并发上限控制进程/脚本集中启动风暴，超时/完成都释放额度
- 重复 src 去重 + 失败计数
- 超时清理定时器无泄漏
