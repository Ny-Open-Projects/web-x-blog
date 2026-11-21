---
title: [WCN-006] Shadow DOM 的 open 与 closed 模式有什么区别？closed 真的能"私有"吗？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-006：Shadow DOM 的 open 与 closed 模式有什么区别？closed 真的能"私有"吗？

**答**：
- `attachShadow({ mode: 'open' })`：外部可通过 `element.shadowRoot` 拿到影子根，方便调试与外部定制。
- `mode: 'closed'`：`element.shadowRoot` 返回 null，JS 引用不暴露，适合不希望外部随意改内部结构的组件。
- closed 不是真正私有：仍可被原型方法截获（包装 `Element.prototype.attachShadow` 记录返回值）、通过事件路径 `event.composedPath()` 在派发瞬间拿到内部节点。
- closed 的额外代价：浏览器 DevTools 里影子树仍可见，但外部生态（如 Testing Library 查询、popover 定位库）拿不到引用；无障碍工具同样可能读不到内部节点。
- 实践建议：设计系统组件一般用 open + `::part` 暴露定制点；closed 只用于强封装场景（如广告 SDK、水印组件）。

```javascript
// closed 模式的"逃逸"演示：包装 attachShadow 记录影子根
const orig = Element.prototype.attachShadow;
Element.prototype.attachShadow = function (init) {
  const root = orig.call(this, init);
  if (init.mode === 'closed') this.__root = root; // 拿到引用
  return root;
};
class Watermark extends HTMLElement {
  connectedCallback() { this.attachShadow({ mode: 'closed' }).textContent = '©internal'; }
}
customElements.define('x-watermark', Watermark);
const wm = document.createElement('x-watermark');
document.body.append(wm);
console.log(wm.shadowRoot);            // null
console.log(wm.__root?.textContent);   // ©internal（仅演示，非安全边界）
```
