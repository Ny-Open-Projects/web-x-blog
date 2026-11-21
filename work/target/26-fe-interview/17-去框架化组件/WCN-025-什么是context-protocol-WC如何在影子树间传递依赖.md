---
title: [WCN-025] 什么是 Web Components 的 Context Protocol？影子树之间如何传递依赖而不必逐层传 props？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-025：什么是 Web Components 的 Context Protocol？影子树之间如何传递依赖而不必逐层传 props？

**答**：
- 问题：Shadow DOM 阻断 DOM 继承，React 的 Context、Vue 的 provide/inject 在原生 WC 里没有对应物，深层组件要靠层层 attribute 传递。
- Context Protocol（WICG 提案）：`new ContextProvider()` / `contextcast` 思路——用自定义事件 `contextrequest` 沿 DOM 树向上冒泡（composed），祖先 Provider 捕获并回传值；避免逐级透传。
- 实现要点：请求事件必须 composed 冒出接收方影子树，回应走直接引用（不冒泡）或由 Provider 写到请求者的公开属性上。
- 兜底方案：全局 registry（如 `@lit/context`）或框架包装层把 React Context 的值作为 attribute/property 注入 WC。
- 适用场景：主题 token、i18n 实例、当前用户、设计系统配置这类"环境依赖"，不适合高频变化的数据（事件风暴）。

```javascript
// Provider：监听冒泡上来的 contextrequest
class AppProvider extends HTMLElement {
  #ctx = { theme: 'dark', i18n: { t: (k) => ({ 'btn.ok': '确定' })[k] ?? k } };
  connectedCallback() {
    this.addEventListener('contextrequest', (e) => {
      if (e.detail.key === this.#ctx) {  // key 用引用/字符串均可
        e.detail.value = this.#ctx;
        e.preventDefault();               // 表示已处理
        e.stopPropagation();
      }
    });
  }
}
customElements.define('app-provider', AppProvider);

// Consumer：深处组件向上请求
function requestContext(el, key) {
  return new Promise((resolve) => {
    const ev = new CustomEvent('contextrequest', {
      bubbles: true, composed: true,
      detail: { key, value: null, },
    });
    el.addEventListener('contextrequest', (e) => resolve(e.detail.value), { once: true });
    // 自身不消费：先在自身触发前移除自身监听（此处简略）
    el.dispatchEvent(ev);
  });
}
```
