---
title: [V3-378] SSR 下 cookie/session 怎么传递？有哪些坑？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-378：SSR 下 cookie/session 怎么传递？有哪些坑？
**答**：
- 服务端：从请求头解析 cookie（Nuxt 用 useRequestHeaders(['cookie'])），转发给 API 或解析 session，把用户态放进 payload 下发。
- 客户端：登录后写 cookie（HttpOnly 由服务端 Set-Cookie），客户端渲染读非敏感态即可，敏感数据不进 payload。
- 坑一：SSR 缓存页面带用户态 → 会串号；用户相关页面禁 HTML 缓存或用边缘个性化（ESI/客户端注入）。
- 坑二：请求头透传不全（UA、语言）导致服务端渲染的 UA 分支与客户端不一致，产生 hydration mismatch。
- 坑三：cookie 的 SameSite/Domain 与跨域 API 不匹配，SSR 服务端发请求带不了 cookie——需要网关信任内网 token 方案。
```javascript
const headers = useRequestHeaders(['cookie'])
const { data: user } = await useFetch('/api/me', { headers })
```
