---
title: [WEB-452] 子域 Cookie 作用域与域名收敛的安全考量
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-452：子域 Cookie 作用域与域名收敛的安全考量

**答**：
- Cookie 的 Domain 写父域（example.com）时所有子域共享：a.example.com 写的 b.example.com 能读
- 风险面：任何一个子域被 XSS（如弃用的营销子站、第三方托管页）都能偷走主域 Cookie——子域越多攻击面越大
- 治理思路：敏感 Cookie 尽量 Host-only（不设 Domain，仅当前子域可见）；业务子域做「域名收敛」，把动态用户内容收到统一 ugc 域
- Public Suffix List：避免把 Cookie 设到 `.com` 这类公共后缀，浏览器已防，但自有二级公网域（.github.io 类）要注意
- 排查工具：DevTools Application 面板按 Domain 过滤，梳理「哪些子域在往主域写 Cookie」

```javascript
// 仅当前子域可见（Host-only，不设置 domain）
document.cookie = 'sid=xxx; Secure; HttpOnly; SameSite=Lax; Path=/';
// 危险写法：主域共享，攻击面扩大
// document.cookie = 'sid=xxx; domain=.example.com; ...';
```
