---
title: [WCN-919] WC 没有 Context：主题 / locale 怎么跨 shadow DOM 边界注入
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-919：WC 没有 Context：主题 / locale 怎么跨 shadow DOM 边界注入

**答**：
- 结论先行：shadow DOM 阻断了 CSS 与 React Context 的常规传递，跨边界注入主题/locale 靠三条路：CSS 变量继承、事件冒泡请求、全局 store 订阅。
- CSS 变量是首选：自定义属性（--ds-primary）会穿透 shadow boundary 继承，WC 内部用 `var(--ds-primary)` 即可响应宿主主题切换，零 JS（主题令牌场景）。
- 非样式上下文（locale/用户态）：用「冒泡请求事件」——WC 派发 `ds-context-request` 让祖先 Provider 响应并回填；或注入全局 signal store，WC 订阅对应 slice。
- 多实例隔离：同一页面多个微前端应用主题不同时，CSS 变量要在各自容器作用域声明，避免全局 :root 污染（设计系统中台多租户常见）。
- 追问钩子：面试官问「closed shadow root 还能注入吗」——答：closed 模式外部拿不到 shadowRoot，CSS 变量仍可继承，但 JS 查询不行，只能靠属性/事件协议，所以公开组件建议 open 模式。

```javascript
// 主题：CSS 变量穿透 + locale：冒泡请求
// 宿主：
document.body.style.setProperty('--ds-primary', '#1677ff');
// WC 内部样式使用变量：
class DsButton extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `<style>button{background:var(--ds-primary,#666)}</style>
                      <button><slot></slot></button>`;
    // 请求 locale 上下文
    this.dispatchEvent(new CustomEvent('ds-locale-request', {
      bubbles: true, composed: true,
      detail: { set: l => this.setAttribute('locale', l) },
    }));
  }
}
customElements.define('ds-button', DsButton);
// 祖先监听回填：
document.body.addEventListener('ds-locale-request', e => e.detail.set('zh-CN'));
```
