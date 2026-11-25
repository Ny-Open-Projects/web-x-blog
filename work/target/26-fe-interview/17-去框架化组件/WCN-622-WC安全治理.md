---
title: [WCN-622] Shadow DOM 能否防御 XSS？WC 体系下有哪些安全新面（CSS 注入 / DOM Clobbering）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-622：Shadow DOM 能否防御 XSS？WC 体系下有哪些安全新面（CSS 注入 / DOM Clobbering）？

**答**：
- 结论：Shadow DOM 提供样式/结构隔离，但不是安全边界——innerHTML 注入照样执行脚本风险，且 CSS 注入可外传数据（属性选择器窃密）。
- 风险面：① 属性拼接进 innerHTML 导致 XSS ② 外部可控 CSS 用 [value^=a] 选择器 + 背景请求做数据外泄 ③ DOM Clobbering 用 name/id 覆盖 window 属性。
- 追问钩子：如何防？textContent 代替 innerHTML、CSS sanitize（禁用 url()/attr()）、不用 name/id 直接映射全局——考察纵深防御。

```javascript
// 反例：属性拼接进 innerHTML → XSS
// this.shadowRoot.innerHTML = `<div>${this.getAttribute('name')}</div>`;
// 正例：文本节点写入
class DsUser extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' });
    const div = document.createElement('div');
    div.textContent = this.getAttribute('name') || ''; // 不解析 HTML
    this.shadowRoot.appendChild(div);
  }
}
// CSS 注入防护：过滤危险构造
function sanitizeCss(css) {
  return css.replace(/url\s*\(/gi, '').replace(/attr\s*\(/gi, '');
}
customElements.define('ds-user', DsUser);
```
