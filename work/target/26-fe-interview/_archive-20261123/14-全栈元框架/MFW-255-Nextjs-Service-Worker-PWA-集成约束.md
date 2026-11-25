---
title: [MFW-255] Next.js × PWA/SW 的集成约束
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-255：Next × PWA/SW

**答**:
- 语义冲突：SW 缓存与 Next 多层缓存（Router Cache/Data Cache/CDN）叠加——五层缓存互相覆盖，失效顺序成谜——SW 缓存范围必须最小化（只 precache 静态 hash 产物，SSR 路由 network-only）
- RSC Payload 不可 SW 缓存（与路由状态绑定，旧 payload + 新路由 = 水合错乱）——SW 对 RSC 请求直通
- 更新策略：新发版 → SW skipWaiting + 提示刷新（Router Cache 也随刷新清空——半新半旧状态避免）
- 落地清单：SW 只管 /_next/static 与 fonts；API 与页面直通；版本号对齐（SW precache manifest 由构建生成——与产物同原子发布）

```javascript
// workbox 路由策略（与 Next 缓存共存）
registerRoute(({url}) => url.pathname.startsWith('/_next/static'), new CacheFirst())   // 仅静态
registerRoute(/\/api\//, new NetworkOnly())
// SSR/RSC 路由：不注册 = network-only（直通）——五层缓存不叠
```
