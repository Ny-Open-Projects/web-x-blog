---
title: [MFW-207] Next.js 多租户：缓存体系的租户隔离怎么做
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-207：多租户的缓存隔离

**答**:
- 铁律：所有缓存 key 必须含租户标识——fetch cache（query string 含租户）、Data Cache（cacheKey 前缀）、Router Cache（按租户路由自然隔离）、静态产物（ISR 按租户 key）
- 事故模式：generateStaticParams 遗漏租户维度 → 租户 A 内容被租户 B 命中（全缓存层共用）——多租户上线前必须做「跨租户串数据」专项测试
- ISR 多租户：`generateStaticParams` 枚举租户 × 页面（数量爆炸时退按需 ISR + revalidateTag 按租户失效）
- 失效隔离：revalidateTag 按租户复合 tag（`tenant:${id}:page:home`）——不能全局失效（牵连所有租户）

```javascript
// 租户复合 tag
fetch(`/api/tenants/${tenantId}/home`, { next: { tags: [`tenant:${tenantId}`, `tenant:${tenantId}:home`] } })
// 按租户失效
revalidateTag(`tenant:${tenantId}:home`)      // 只影响一个租户
```
