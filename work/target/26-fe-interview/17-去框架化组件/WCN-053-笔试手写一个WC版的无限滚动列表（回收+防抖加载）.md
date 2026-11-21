---
title: [WCN-053] 笔试：手写一个 WC 版无限滚动列表（IntersectionObserver 哨兵 + 去重加载）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-053：笔试：手写一个 WC 版无限滚动列表

**题目**：`<infinite-list page-size="20" loader="/api/items">`：① 底部哨兵进入视口时请求下一页；② 加载中不重复触发（去重）；③ 无更多数据时显示"没有更多了"并停止观察；④ 失败可重试（点击"重试"）；⑤ 子项渲染为 `<item-row>` WC；⑥ disconnected 清理。

**答**：

```javascript
class InfiniteList extends HTMLElement {
  static observedAttributes = ['page-size', 'loader'];
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>ul{list-style:none;padding:0} .foot{padding:12px;text-align:center;color:#6b7280}</style>
        <ul id="list"></ul><div class="foot" id="foot"></div>`;
      this.#sentinel = this.shadowRoot.getElementById('foot');
      this.#io = new IntersectionObserver((ents) => {
        if (ents.some((e) => e.isIntersecting)) this.#load();
      }, { rootMargin: '400px' });
      this.#io.observe(this.#sentinel);
    }
  }
  #page = 0; #busy = false; #done = false; #io; #sentinel;
  disconnectedCallback() { this.#io?.disconnect(); }
  async #load() {
    if (this.#busy || this.#done) return;        // 去重 + 终止态
    this.#busy = true;
    const foot = this.shadowRoot.getElementById('foot');
    foot.textContent = '加载中…';
    try {
      const res = await fetch(`${this.getAttribute('loader')}?page=${this.#page + 1}&size=${this.getAttribute('page-size') | 0 || 20}`);
      const { items, hasMore } = await res.json();
      const frag = document.createDocumentFragment();
      for (const it of items) {
        const row = document.createElement('item-row');
        row.data = it;                            // property 传对象
        frag.append(row);
      }
      this.shadowRoot.getElementById('list').append(frag);
      this.#page++;
      if (!hasMore) { this.#done = true; this.#io.disconnect(); foot.textContent = '没有更多了'; }
      else foot.textContent = '';
    } catch {
      foot.textContent = '';
      const btn = document.createElement('button');
      btn.textContent = '加载失败，点击重试';
      btn.onclick = () => { btn.remove(); this.#load(); };
      foot.append(btn);
    } finally {
      this.#busy = false;
    }
  }
}
customElements.define('infinite-list', InfiniteList);
```

**评分点**：
- `#busy` 状态去重 + `#done` 终止态双重守卫；sentinel 加载后自动继续观察（IO 持续监听，不 disconnect）。
- 失败态可点击重试且 finally 里复位 busy（无论成败）。
- 文档碎片批量插入 + 子项走 property 传对象。
- disconnected 清理 observer；rootMargin 提前预加载。
