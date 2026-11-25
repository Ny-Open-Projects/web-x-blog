---
title: [MFW-251] Next.js 与 WebSocket 长连接的共存架构
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-251：WebSocket 与 Next 共存

**答**:
- 约束：App Router/Serverless 目标不支持 WS 服务端（请求-响应模型）——WS 服务独立部署（Node 常驻/专用网关），Next 前端通过环境变量指向 WS 域
- 部署形态：同域反代（/ws → WS 服务——省跨域与 Cookie 共享）或独立子域（wss://ws.app.com——CDN 不支持 WS 时直连）
- 鉴权传递：WS 握手带 Cookie（同域反代自动带；子域需 CORS+credential）→ WS 服务校验 session——与主站同一鉴权源
- 状态一致性：WS 推送的数据写客户端 Query 缓存（setQueryData）——与 RSC/Action 数据流汇合到同一缓存（MFW-201 失效链复用）

```javascript
// next.config: 同域反代
async rewrites() { return [{ source: '/ws/:path*', destination: 'wss://ws-internal:8080/:path*' }] }
// 客户端
const ws = new WebSocket(`wss://${location.host}/ws/room/${id}`)   // Cookie 自动携带
ws.onmessage = (e) => qc.setQueryData(['room', id], merge(JSON.parse(e.data)))   // 汇入统一缓存
```
