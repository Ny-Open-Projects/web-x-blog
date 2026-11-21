---
title: [WCN-052] WC 如何与浏览器原生平台能力（Popover、Dialog、CustomState、Anchor）融合？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-052：WC 如何与浏览器原生平台能力（Popover、Dialog、CustomState、Anchor）融合？

**答**：
- 平台方向是"把框架能力标准化"：Popover API 替代下拉/菜单组件的显隐管理、`<dialog>` 替代模态、`@starting-style` 替代入场动画库、CSS Anchor Positioning 替代浮层定位计算、CustomStateSet（ElementInternals.states）替代 data-attribute 状态暴露。
- WC 的定位变化：组件越来越薄——只做组合与业务语义，交互原语尽量交还平台；这让"去框架化"组件的体积和 bug 面大幅缩小。
- 融合实践：影子树内放 `popover` 元素（top layer 生效于整个视口，不局限影子树）；`popovertarget` 也可以跨影子树引用（button 在 light DOM 指向 shadow 内 id 需要同树——因此常把 trigger 也放影子树内）。
- CustomState：组件状态（loading/open/disabled）用 `states.add` 暴露为 `:--loading` 伪类，比 attribute 更高效且可参与选择器组合。
- 兼容策略：这些 API 均需渐进增强——存在性检测 + 行为降级实现同一对外接口。

```javascript
class Tooltip extends HTMLElement {
  #i = this.attachInternals?.();
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style>
        :host { position: relative; }
        #tip { position: fixed; inset: auto; margin: 4px; padding: 4px 8px;
               border-radius: 6px; background: #111827; color: #fff; font-size: 12px; }
      </style>
      <span id="trigger"><slot></slot></span>
      <div id="tip" popover>提示内容</div>`;
    const trigger = root.getElementById('trigger');
    trigger.addEventListener('mouseenter', () => this.#show(true));
    trigger.addEventListener('mouseleave', () => this.#show(false));
  }
  #show(on) {
    const tip = this.shadowRoot.getElementById('tip');
    if (on) { tip.showPopover?.() ?? (tip.hidden = false); this.#i?.states.add('open'); }
    else { tip.hidePopover?.() ?? (tip.hidden = true); this.#i?.states.delete('open'); }
  }
}
customElements.define('x-tooltip', Tooltip);
```
