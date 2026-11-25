---
title: [V3-390] Nuxt 应用需要配置哪些安全 Headers？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-390：Nuxt 应用需要配置哪些安全 Headers？
**答**：
- 基础清单：CSP（script-src 白名单 + nonce）、HSTS、X-Content-Type-Options: nosniff、Referrer-Policy、Permissions-Policy、X-Frame-Options/frame-ancestors 防点击劫持。
- CSP 落地：Nuxt routeRules.headers 或 Nitro middleware 统一注入；内联脚本用 nonce（SSR 生成并透传到 payload），上报 report-uri 观察违例。
- SSR 特有：payload 序列化防 XSS（Vue 默认转义，避免 v-html 与 JSON-LD 直接拼接用户数据；必要时 sanitize）。
- Cookie 安全：HttpOnly + Secure + SameSite=Lax（登录态），客户端可见 cookie 只放非敏感展示态。
- 验证：securityheaders.com 扫描 A 级；CI 加 header 断言防回归。
