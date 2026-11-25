---
title: [MFW-848] 流式渲染早期 flush 的 script 何时能执行，和 HTTP/2 优先级什么关系
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-848：流式渲染早期 flush 的 script 何时能执行，和 HTTP/2 优先级什么关系

**答**：
- 结论：早期 flush 的 script 必须等其依赖的 DOM/资源就绪才安全执行；HTTP/2 优先级决定资源到达顺序，但 script 还需浏览器解析到该标签才执行。
- 落地：关键 JS 用 preload 提优先级并尽早 flush，非关键 JS 放到流尾，用 async/defer 控制执行时机。
- 追问钩子：为什么流式下 script 执行更脆弱？——DOM 持续到达，script 可能操作尚未存在的节点。

```javascript
// shell 阶段：关键资源 preload + 尽早 flush 引导脚本
res.write(`<head>
  <link rel="preload" as="script" href="/critical.js">
  <script defer src="/critical.js"></script>
</head>`);
res.flush();                                       // 浏览器立即开始解析/下载

// 洞阶段：DOM 就绪后再写依赖它的脚本
res.write('<div id="cart"></div>');
res.write('<script>initCart(document.getElementById("cart"))</script>');
res.flush();

// HTTP/2 优先级：critical.js 权重高，先于非关键资源到达
```
