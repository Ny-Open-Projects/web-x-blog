---
title: [WCN-002] autonomous element 与 customized built-in element 有什么区别？为什么 Safari 拒绝后者？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-002：autonomous element 与 customized built-in element 有什么区别？为什么 Safari 拒绝后者？

**答**：
- autonomous element：`customElements.define('my-btn', Cls)`，是全新的标签名，只能通过 `is` 不存在的方式直接书写 `<my-btn>`。
- customized built-in：`customElements.define('my-btn', Cls, { extends: 'button' })`，增强原生元素，书写为 `<button is="my-btn">`，保留原生语义（可聚焦、可提交表单、可达性）。
- Safari 至今不支持 customized built-in（认为该方案设计复杂、收益不明），所以跨浏览器工程中应以 autonomous element + ARIA 角色模拟为主。
- 实践折衷：需要原生语义时，autonomous 元素内部可以渲染一个真实 `<button>` 作为根节点（shadow 内 `<button part="root"><slot></slot></button>`），兼顾兼容与可达性。
- 追问钩子：`document.createElement('button', { is: 'my-btn' })` 在 Safari 里只会得到普通 button，需做能力检测降级。

```javascript
// autonomous：全新标签
customElements.define('my-button', class extends HTMLElement {}, {});

// customized built-in：Chrome/Firefox 支持，Safari 不支持
if ('customBuiltInElements' in HTMLElement || false) {
  customElements.define('fancy-button', class extends HTMLButtonElement {}, { extends: 'button' });
}
// 探测方式实际用：是否识别 is 属性升级
const probe = document.createElement('button', { is: 'fancy-button' });
console.log(probe.outerHTML.includes('is')); // Safari: 行为不同，需另测
```
