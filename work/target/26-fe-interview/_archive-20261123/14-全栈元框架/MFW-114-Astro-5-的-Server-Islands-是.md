---
title: [MFW-114] Astro 5 的 Server Islands 是什么？和客户端岛有什么区别？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-114：Astro 5 的 Server Islands 是什么？和客户端岛有什么区别？
**答**：
- Server Islands：页面主体可以是**缓存able 的静态 HTML**，个别「个性化/实时」组件（登录态、购物车数、实时价格）标记为服务端岛，请求时单独从服务器渲染替换进静态页面。
- 解决的核心矛盾：静态页面想用 CDN 长缓存，但页面上有个性化内容——传统做法整页放弃缓存或全站 SSR。Server Islands 把个性化粒度缩到组件级，主体仍是 CDN 缓存的静态 HTML。
- 机制：构建期给岛的位置留占位符 + HTML 注释标记；请求命中静态页后，浏览器/CDN 对岛 URL 发起请求，服务端渲染该组件回填（带 `server-island-*` 协议头，Astro 内部处理）。
- 与客户端岛的分工：客户端岛省「交互 JS」，服务端岛省「个性化缓存」——两者可叠加（个性化组件同时交互化）。

```astro
---
// src/pages/index.astro —— 主体可被 CDN 缓存为静态 HTML
import CartCount from '../components/CartCount.astro'; // 个性化组件
---
<html>
  <head><title>商城首页</title></head>
  <body>
    <h1>今日精选</h1>
    <!-- 主体静态：商品列表构建期渲染，CDN 缓存 1 小时 -->

    <!-- 服务端岛：每请求实时渲染，不进静态缓存 -->
    <CartCount server:defer userId={Astro.cookies.get('uid')?.value} />
  </body>
</html>
```

```astro
---
// src/components/CartCount.astro —— 服务端岛组件
import { cookies } from 'astro:user'; // 请求级上下文
const uid = Astro.cookies.get('uid')?.value;
const count = uid ? await db.cart.count(uid) : 0;
---
<span id="cart-count">{count}</span>
```
