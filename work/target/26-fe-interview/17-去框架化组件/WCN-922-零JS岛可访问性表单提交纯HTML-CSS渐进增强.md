---
title: [WCN-922] 零 JS 岛怎么保持可访问性与表单提交（纯 HTML + CSS 方案）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-922：零 JS 岛怎么保持可访问性与表单提交（纯 HTML + CSS 方案）

**答**：
- 结论先行：无框架 islands 的目标不是「全站零 JS」，而是让多数静态岛在 JS 失败时仍完整可用——靠语义化 HTML、原生表单、CSS 交互（:hover/:focus/:checked）兜底。
- 可访问性基线：用原生 button/a/input/label 而非 div，保证键盘可达、焦点可见、role/aria 正确；SSR 输出的语义 DOM 本身就是无障碍底座（不依赖水合后才可访问）。
- 表单提交：零 JS 岛用 `<form action method>` 走原生提交，JS 加载后渐进增强为 AJAX（拦截 submit）；禁用 JS 时仍能把数据送到服务端。
- CSS 交互：折叠面板用 `<details>/<summary>`、Tabs 用 radio + :checked、下拉用 :focus-within，零 JS 实现基础交互。
- 追问钩子：面试官问「动态校验怎么办」——答：用原生 `required/pattern/type=email` + `:invalid/:valid` 做浏览器原生校验，JS 只做增强体验。

```javascript
// 服务端输出的「零 JS 岛」HTML（含语义标签 + 原生校验 + CSS 交互）
const html = `
<details class="faq" open><summary>运费说明</summary><p>全场包邮。</p></details>
<form action="/api/subscribe" method="post">
  <label>邮箱 <input type="email" name="email" required
    pattern="[^@]+@[^@]+\.[^@]+"></label>
  <button type="submit">订阅</button>
</form>
<style>
  .faq summary { cursor: pointer; }
  input:invalid { border-color: #c00; }
  input:focus-visible { outline: 2px solid #1677ff; }
</style>`;
// 无 JS：form 走原生提交、details 原生展开、input 原生校验，页面完整可用。
// JS 加载后仅渐进增强：拦截 submit 改 AJAX。
document.addEventListener('submit', e => {
  e.preventDefault(); // JS 可用时增强；JS 失败则该监听不存在，回退原生提交
  fetch(e.target.action, { method: 'POST', body: new FormData(e.target) });
});
```
