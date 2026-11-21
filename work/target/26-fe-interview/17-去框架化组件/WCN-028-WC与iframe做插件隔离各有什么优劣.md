---
title: [WCN-028] WC 与 iframe 做插件/小组件隔离各有什么优劣？什么场景必须用 iframe？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-028：WC 与 iframe 做插件/小组件隔离各有什么优劣？什么场景必须用 iframe？

**答**：
- WC 隔离强度：DOM/样式通过 Shadow DOM 隔离；JS 与全局对象（window、document、localStorage）完全共享，插件代码可以任意访问主页面——隔离是"约定级"。
- iframe 隔离强度：独立 Window/Document/EventLoop（跨域 iframe 站点隔离），JS/存储/历史栈都隔离，且能用 `sandbox` 属性细粒度授权（allow-scripts、allow-same-origin 等）。
- WC 优势：同文档渲染、无额外通信成本、可主题化、可用 slot 让宿主内容投影、无 iframe 的弹层裁剪与滚动穿透问题。
- iframe 优势：第三方不可信代码、需要独立 CSP/独立域名 cookie、广告计量、需要嵌整页应用。
- 结论：可信生态（自己团队的设计系统、内部 SDK）用 WC；不可信/跨信任域（广告、支付脚本、在线文档）必须 iframe + sandbox。

```html
<!-- 不可信插件：iframe + sandbox 最小权限，禁止 top 导航与同源访问 -->
<iframe src="https://ads.example.com/widget"
        sandbox="allow-scripts"          <!-- 无 allow-same-origin：独立源、无法碰主页面存储 -->
        referrerpolicy="no-referrer"
        loading="lazy"
        title="推广位"></iframe>

<!-- 可信插件：WC，样式隔离 + token 主题化 -->
<style> .host { --plugin-primary: #2563eb } </style>
<trusted-widget class="host"></trusted-widget>
<script type="module" src="./trusted-widget.js"></script>
```
