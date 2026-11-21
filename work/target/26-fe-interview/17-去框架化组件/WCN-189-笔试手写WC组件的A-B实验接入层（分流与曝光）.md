---
title: [WCN-189] 笔试：手写 WC 组件的 A/B 实验接入层（分流 + 变体渲染 + 曝光归因）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-189：笔试：手写 WC 组件的 A/B 实验接入层

**题目**：实现 `<wc-ab experiment="cta-color">`：① 初始化时调用分流服务（SDK 或 fetch `/api/ab?exp=xxx&uid=...`）得到 variant（A/B/holdout）；② 根据变体渲染对应 slot（`<template slot="A">` 内容）或默认内容；③ 未返回前渲染默认（防阻塞）；④ 曝光归因：变体渲染完成后派发 `ab-expose`（detail: experiment/variant）；⑤ variant 持久化（同会话一致，sessionStorage）；⑥ 分流失败回落默认。

**答**：

```javascript
class WcAb extends HTMLElement {
  static observedAttributes = ['experiment'];
  async connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>:host{display:contents}</style><slot name="default" id="def"></slot>
        <slot name="A" hidden></slot><slot name="B" hidden></slot>`;
    }
    const exp = this.getAttribute('experiment');
    const variant = await this.#resolve(exp);
    this.#show(variant);
    this.dispatchEvent(new CustomEvent('ab-expose', {
      bubbles: true, composed: true, detail: { experiment: exp, variant },
    }));
  }
  async #resolve(exp) {
    const key = `ab:${exp}`;
    const cached = sessionStorage.getItem(key);
    if (cached) return cached;
    try {
      const res = await fetch(`/api/ab?exp=${encodeURIComponent(exp)}&uid=${getUid()}`,
        { signal: AbortSignal.timeout(800) });
      const { variant } = await res.json();
      sessionStorage.setItem(key, variant);
      return variant ?? 'default';
    } catch {
      return 'default';                     // 分流失败回落默认
    }
  }
  #show(variant) {
    const slotEl = this.shadowRoot.querySelector(`slot[name="${variant}"]`);
    if (slotEl && this.querySelector(`[slot="${variant}"]`)) {
      this.shadowRoot.querySelectorAll('slot').forEach((s) => (s.hidden = s !== slotEl));
    }
    // 无对应变体内容：保持 default slot（已在最前，hidden=false）
  }
}
customElements.define('wc-ab', WcAb);
// 用法：<wc-ab experiment="cta-color">
//   <button slot="default">默认按钮</button>
//   <button slot="A" style="background:#2563eb">蓝色按钮</button>
//   <button slot="B" style="background:#16a34a">绿色按钮</button>
// </wc-ab>
```

**评分点**：
- 变体持久化（sessionStorage）保证同会话一致（实验口径要求）。
- 默认内容先行渲染（分流不阻塞首屏），超时/失败回落。
- slot 切换实现变体渲染；ab-expose 事件带 experiment+variant（归因）。
- AbortSignal.timeout 防分流服务拖慢页面。
