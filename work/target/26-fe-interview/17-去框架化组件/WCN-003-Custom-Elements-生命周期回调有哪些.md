---
title: [WCN-003] Custom Elements 有哪些生命周期回调？各自触发时机与典型用途？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-003：Custom Elements 有哪些生命周期回调？各自触发时机与典型用途？

**答**：
- `constructor`：元素实例化时调用，只做状态初始化与 shadow 挂载骨架，不能读 attribute、不能 append 到自身之外的 DOM。
- `connectedCallback`：插入文档后触发（可多次触发），做事件绑定、数据请求、渲染；此时才能安全访问 `this.shadowRoot` 与文档。
- `disconnectedCallback`：移出文档时触发，做事件解绑、定时器/observer 清理，注意不在里面做"销毁后不允许"的 DOM 操作。
- `attributeChangedCallback(name, old, new)`：仅在 `observedAttributes` 列出的 attribute 变化时触发，是外部配置入口。
- `adoptedCallback`：元素被 `document.adoptNode` / iframe 间迁移时触发，最少见。
- 追问钩子：`attributeChangedCallback` 可能在 `connectedCallback` 之前触发（HTML 解析时属性先就位），所以回调里要容忍"未连接"状态。

```javascript
class LiveClock extends HTMLElement {
  static observedAttributes = ['tz', 'format'];
  constructor() {
    super();
    this.timer = null;
    this.attachShadow({ mode: 'open' }).innerHTML = '<time></time>';
  }
  attributeChangedCallback(name, oldV, newV) {
    if (oldV !== newV && this.isConnected) this.render();
  }
  connectedCallback() { this.render(); this.timer = setInterval(() => this.render(), 1000); }
  disconnectedCallback() { clearInterval(this.timer); }
  adoptedCallback() { console.log('被迁移到新文档'); }
  render() {
    this.shadowRoot.querySelector('time').textContent =
      new Date().toLocaleTimeString('zh-CN', { timeZone: this.getAttribute('tz') || 'Asia/Shanghai' });
  }
}
customElements.define('live-clock', LiveClock);
```
