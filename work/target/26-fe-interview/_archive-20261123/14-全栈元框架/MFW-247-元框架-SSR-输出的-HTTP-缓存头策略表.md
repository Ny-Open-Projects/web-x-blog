---
title: [MFW-247] SSR 产物 HTTP 缓存头策略表
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-247：SSR 缓存头策略表

**答**:
- 策略表（按内容类型）：静态产物 immutable,max-age=31536000 / ISR 页 s-maxage=60,stale-while-revalidate=300（CDN 层 SWR——旧页立回+后台刷新）/ SSR 动态页 no-store 或 private,max-age=0（个人化禁共享缓存）/ API GET 视数据（s-maxage+tag 失效）
- 关键区分：private（浏览器可缓存）vs 无指令（完全动态）——登录后页面用 private 让回退键可用且不跨用户串
- CDN 协同：s-maxage 与 surrogte-key（Fastly）/Cache-Tag（Cloudflare）配合 → 按域失效（与 revalidateTag 双轨——应用层与边缘层各失效各的）
- 验证：线上响应头采集比对策略表（curl 脚本进发布检查——头配错是缓存事故直接原因）

```text
策略表速查：
静态产物  → immutable,1y
ISR 页    → s-maxage=60,SWR=300
个人化 SSR → private,no-cache（或 0）
API GET   → s-maxage + surrogate-key
```
