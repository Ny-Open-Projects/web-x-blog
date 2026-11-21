---
title: [WCN-433] 笔试：实现元素的水合恢复（采用 DSD + 状态 + 不重建 DOM）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-433：笔试：实现元素的水合恢复（采用 DSD + 状态 + 不重建 DOM）。
**题目**：connectedCallback：① shadowRoot 已存在（DSD）则跳过模板注入 ② 读 data-state 恢复信号 ③ 只绑事件不重渲染。开发模式校验：恢复值与 DOM 文本一致。

```javascript
connectedCallback() {
  if (!this.shadowRoot) {   // polyfill 分支
    const tpl = this.querySelector('template[shadowrootmode]');
    this.attachShadow({ mode: 'open' }).append(tpl.content.cloneNode(true));
    tpl.remove();
  }
  const init = this.dataset.state && JSON.parse(atob(this.dataset.state));
  if (init) {
    restoreSignals(init);
    if (import.meta.env.DEV && this.shadowRoot.textContent.includes(String(init.sku)) === false)
      console.warn('[ds-goods] DSD 与状态不一致', init);
    this._hydrated = true;   // 不重渲染
  }
  this._bindEvents();
}

```

**评分点**：
- shadowRoot 存在性判断（原生 DSD 已解析）。
- polyfill 分支（模板手动 adopt）。
- 状态恢复 → 信号初始化 → no re-render。
- 一致性校验（dev：DOM 文本 vs 状态值）。
