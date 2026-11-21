---
title: [PER-058] DOM 型 XSS 有哪些隐蔽的 sink？innerHTML 之外还有哪些容易漏防的点？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-058：DOM 型 XSS 有哪些隐蔽的 sink？innerHTML 之外还有哪些容易漏防的点？

**答**：
- 隐蔽 sink 清单：`innerHTML/outerHTML`、`document.write`、`location.href = 'javascript:...'` 等伪协议、`<a href>`/`<iframe src>` 接收用户输入、`setAttribute('onclick', ...)`、jQuery 的 `$(html)`、`eval/setTimeout` 字符串、`insertAdjacentHTML`。
- DOM 型 XSS 的特点是**全程不经过服务端**，WAF 和后端转义都拦不住，只能靠前端约定 + CSP 兜底。
- URL 类 sink 必须校验协议白名单（http/https/mailto），否则 `javascript:alert(1)` 能穿透普通转义。
- 防御原则：能用 `textContent` 不用 `innerHTML`；必须插 HTML 时走统一的安全渲染入口；URL 一律先 `URL` 构造器解析再校验协议。

```javascript
// 危险 sink 示例与对应的安全写法
const userInput = location.hash.slice(1); // 例如 "#javascript:alert(document.cookie)"

// 危险 1：innerHTML —— 用户输入被解析为 HTML
// el.innerHTML = userInput;                      // 禁止
el.textContent = userInput;                      // 安全：按纯文本插入

// 危险 2：伪协议跳转
// location.href = userInput;                    // javascript: 协议直接执行
function safeNavigate(url) {
  const u = new URL(url, location.origin);       // 先解析
  if (!['http:', 'https:'].includes(u.protocol)) {
    throw new Error('blocked protocol: ' + u.protocol); // 协议白名单
  }
  location.href = u.href;
}
safeNavigate('https://example.com');             // 通过
safeNavigate(userInput);                         // javascript: 被拦截

// 危险 3：字符串形式的内联事件
// btn.setAttribute('onclick', "track('" + name + "')"); // 引号逃逸即 XSS
btn.addEventListener('click', () => track(name));       // 闭包传参，无拼接
```
