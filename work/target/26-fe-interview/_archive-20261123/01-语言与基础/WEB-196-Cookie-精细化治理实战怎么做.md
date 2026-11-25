---
title: [WEB-196] Cookie 精细化治理实战怎么做？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-196：Cookie 精细化治理实战怎么做？
**答**：
- 盘点：用 DevTools Application 面板或脚本枚举全站 Cookie，按"业务必需 / 可删 / 有泄漏风险"三色标记。
- 收敛方向：静态资源用独立裸域不带业务 Cookie；每个 Cookie 显式 Domain/Path/Expires/SameSite，禁止裸 name=value。
- 安全加固：敏感会话用 __Host- 前缀 + HttpOnly + Secure；第三方嵌入场景评估 Partitioned 分区 Cookie。
- 上线保障：Cookie 变更走灰度；CI 里对 Set-Cookie 头做断言，防止依赖清单悄悄膨胀。

```javascript
// Cookie 审计脚本：控制台跑一遍，输出问题项清单
// 注意 document.cookie 读不到 HttpOnly 的 Cookie，完整盘点要结合 DevTools 或服务端头
[...document.cookie.split('; ')].forEach((c) => {
  const [name] = c.split('=');
  console.warn(`cookie: ${name}, size: ${c.length}`);
});
// 治理示例：安全会话 Cookie 的理想形态（服务端设置）
// Set-Cookie: __Host-sid=xxx; Secure; HttpOnly; SameSite=Lax; Path=/; Max-Age=604800
// 静态域剥离 Cookie：静态资源统一走 sstatic.example.com，业务 Cookie 永不设置到该域
```
