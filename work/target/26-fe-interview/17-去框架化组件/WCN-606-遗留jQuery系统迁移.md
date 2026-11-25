---
title: [WCN-606] 遗留 jQuery 组件如何迁移为 Web Components，迁移路径与主要风险是什么？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-606：遗留 jQuery 组件如何迁移为 Web Components，迁移路径与主要风险是什么？

**答**：
- 结论：采用「包裹而非重写」——先把 jQuery 组件整体塞进 WC 的 Shadow DOM，统一对外契约，再逐步替换内部实现。
- 路径：① WC 做外壳并暴露属性/事件 ② 把全局 CSS 改造成 adoptedStyleSheets ③ 逐个替换 jQuery 插件为原生逻辑并删依赖。
- 追问钩子：风险点？jQuery 依赖全局 $ 与 document 选择器，需改造为 shadowRoot 作用域；事件委托与插件生命周期要在 disconnectedCallback 中销毁。

```javascript
class LegacyWrapper extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML =
      '<link rel="stylesheet" href="legacy.css"><div class="root"></div>';
    const root = this.shadowRoot.querySelector('.root');
    // 把原本 $(document) 的初始化收敛到 shadow 作用域
    this.instance = window.initLegacyWidget(root, {
      value: this.getAttribute('value'),
      onChange: (v) => this.dispatchEvent(
        new CustomEvent('ds-change', { detail: v, composed: true })
      ),
    });
  }
  disconnectedCallback() {
    this.instance?.destroy(); // 关键：销毁 jQuery 插件副作用
  }
}
customElements.define('ds-legacy-widget', LegacyWrapper);
```
