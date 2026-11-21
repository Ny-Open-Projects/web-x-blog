---
title: [MFW-229] TanStack Start 的部署目标适配（Nitro 魔层）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-229：TanStack Start 部署适配

**答**:
- 底座：Nitro（Unjs）统一服务端抽象——同一份代码编译到 Node/Cloudflare Workers/Vercel Edge/Netlify/Bun（target 由 preset 决定）
- 适配要点：运行时 API 差异被 Nitro 兜住（fetch 标准）、存储绑定（KV/R2/Blob 的 useStorage 统一面）、中间件语义对齐
- 实际差异仍存在：Edge CPU/内存限制（重 SSR 段超预算）、Node 专有依赖（pg 驱动）在 Edge 不可用——依赖审计按 target 做
- 选型建议：先确定部署目标再写代码（反向约束依赖选型）——「写完再选 Edge」是返工重灾区

```javascript
// nitro preset
export default defineConfig({
  server: { preset: 'cloudflare-pages' },   // 或 'node-server' / 'vercel-edge'
})
// 依赖审计：pg/redis 类 TCP 驱动在 Edge target 直接构建报错（早暴露好过线上炸）
```
