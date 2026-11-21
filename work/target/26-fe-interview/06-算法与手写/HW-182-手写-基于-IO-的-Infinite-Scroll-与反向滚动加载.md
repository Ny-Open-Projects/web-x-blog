---
title: [HW-182] 手写双向无限滚动——底部触发加载下一页 + 顶部反向加载历史（滚动锚定防跳动）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：聊天记录/邮件类双向滚动：底部 IO 触发 nextPage（追加）；顶部哨兵触发 prevPage（prepend）——prepend 后滚动位置补偿（保持视觉位置：加载前记录 scrollHeight，插入后 scrollTop += delta，PER-397 滚动锚定的手动版）。竞态防护（快速滚动双触发合并）与到底提示。

```javascript
class BiScroll {
  #loadingPrev = false; #loadingNext = false;
  constructor(container, { fetchPrev, fetchNext }) {
    Object.assign(this, { container, fetchPrev, fetchNext });
    const prev = document.createElement('div'), next = document.createElement('div');
    prev.style.cssText = next.style.cssText = 'height:1px';
    container.prepend(prev); container.append(next);
    const io = new IntersectionObserver((es) => {
      for (const e of es) {
        if (!e.isIntersecting) continue;
        if (e.target === next) this.#loadNext();
        if (e.target === prev) this.#loadPrev();
      }
    }, { root: container, rootMargin: '200px' });         // 提前 200px 触发（滚动连续性）
    io.observe(prev); io.observe(next);
  }
  async #loadNext() {
    if (this.#loadingNext || !this.hasNext) return;
    this.#loadingNext = true;
    try {
      const rows = await this.fetchNext();
      this.append(rows);                                  // 追加：自然无位移
      this.hasNext = rows.length > 0;
    } finally { this.#loadingNext = false; }
  }
  async #loadPrev() {
    if (this.#loadingPrev || !this.hasPrev) return;
    this.#loadingPrev = true;
    const c = this.container;
    const before = c.scrollHeight;
    try {
      const rows = await this.fetchPrev();
      c.prepend(...rows.map(render));                     // 前插
      c.scrollTop += c.scrollHeight - before;             // 补偿：视觉位置不变（防跳动核心）
    } finally { this.#loadingPrev = false; }
  }
}
// 补偿公式：scrollTop += 新 scrollHeight - 旧 scrollHeight —— prepend 后视觉位置零移动
// 双向防重入（loadingPrev/loadingNext 标志）防快速滚动双触发
// rootMargin 200px：提前加载（滚动到底才触发会闪加载态）
```

**评分点**：
- prepend 后 scrollTop += (newH - oldH) 位移补偿——本题核心。
- 双向防重入标志；IO rootMargin 提前量。
- hasNext/hasPrev 到头收敛（哨兵不再触发）。
- 追加方向无位移的说明（只有前插需要补偿）。
