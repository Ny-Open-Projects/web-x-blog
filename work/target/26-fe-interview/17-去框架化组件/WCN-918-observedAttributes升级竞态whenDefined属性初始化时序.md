---
title: [WCN-918] observedAttributes 更新时机与框架渲染时序冲突（升级竞态）怎么处理
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-918：observedAttributes 更新时机与框架渲染时序冲突（升级竞态）怎么处理

**答**：
- 结论先行：自定义元素的升级（upgrade）是异步的——元素先以 HTML 形式解析出来、属性和子节点已存在，但类构造函数和 connectedCallback 还没跑，此时框架若直接读 property 会拿到 undefined。
- 用 `customElements.whenDefined('ds-x')` 等待定义完成再操作；WC 内部在 constructor 里从已存在的 attributes 读初始值（attributeChangedCallback 在升级时会补触发）。
- 框架侧「元素升级前设 property」会丢：因为升级后 constructor 可能覆盖实例字段；解决是把初始值都放 attribute，property 只作为升级后的运行态。
- 属性更新顺序：升级时会按 attributeChangedCallback 对每个已存在属性依次调用，顺序按文档顺序，不要在单个回调里依赖其他属性已就绪。
- 追问钩子：面试官问「SSR 输出带属性的 WC 在客户端升级会不会闪一下」——答：用 `display` 默认样式 + `:defined` 伪类做升级前隐藏，升级后再显示，避免 FOUC。

```javascript
// 等待升级 + 从 attribute 读初始值
const el = document.createElement('ds-price');
el.setAttribute('value', '99'); // 升级前先写 attribute
// 此时 property 可能尚未就绪：
console.log(el.value); // undefined（未升级）
customElements.whenDefined('ds-price').then(() => {
  console.log(el.value); // 99（升级后从 attribute 初始化）
});
class DsPrice extends HTMLElement {
  static get observedAttributes() { return ['value']; }
  constructor() { super(); this._value = null; }
  connectedCallback() { this._value = this.getAttribute('value'); }
  attributeChangedCallback(n, o, v) { if (n === 'value') this._value = v; }
  get value() { return this._value; }
}
customElements.define('ds-price', DsPrice);
```
