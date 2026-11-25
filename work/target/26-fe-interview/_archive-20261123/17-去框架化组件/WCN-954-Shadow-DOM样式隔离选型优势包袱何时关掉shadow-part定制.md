---
title: [WCN-954] Shadow DOM 样式隔离在选型里是优势还是包袱：什么场景反而要关掉 shadow
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-954：Shadow DOM 样式隔离在选型里是优势还是包袱：什么场景反而要关掉 shadow

**答**：
- 结论先行：Shadow DOM 的强隔离在「多团队样式冲突」场景是优势，但在「需要全局主题穿透 / 外部样式定制 / 表单生态」场景是包袱，选型时按定制自由度决定用不用。
- 优势场景：微前端多子应用共存、第三方嵌入组件——避免 CSS 互相污染，token 通过 CSS 变量受控穿透即可。
- 关掉 shadow 的场景：① 组件需要被业务方用全局 CSS 深度定制（如白标产品换肤）；② 需要被外部 querySelector 操作 DOM；③ 依赖表单/polyfill 对 light DOM 的假设。
- 折中：用 open shadow + `part` 属性暴露可定制插槽（`::part(button)`），兼顾隔离与有限定制；或提供「light DOM 版本」双形态组件。
- 追问钩子：面试官问「closed shadow 能测试吗」——答：外部拿不到 shadowRoot，E2E 选择器失效，这也是公开组件库倾向 open 的原因，选型要考虑可测试性。

```javascript
// 开 shadow 并用 ::part 暴露定制点（隔离 + 有限定制）
class DsButton extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `<style>
      button { background: var(--ds-primary, #1677ff); }
    </style><button part="btn"><slot></slot></button>`;
  }
}
customElements.define('ds-button', DsButton);
// 业务方可定制：ds-button::part(btn){ border-radius:8px } —— 无需关 shadow
// 若需完全自由定制 -> 提供 light DOM 版本（不 attachShadow）
```
