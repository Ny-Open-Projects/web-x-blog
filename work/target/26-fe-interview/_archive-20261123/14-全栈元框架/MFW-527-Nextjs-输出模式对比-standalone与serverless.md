---
title: [MFW-527] Next.js 输出模式：standalone / serverless / export 的部署矩阵
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-527：Next.js 输出模式：部署矩阵三形态

**答**:
- 三形态：1) **standalone**（自包含 node server：node_modules 裁剪到运行时必需——Docker 镜像瘦身 RBL-681 的官方版：.next/standalone 目录）；2) **serverless**（Vercel 函数：每路由一个函数——冷启动与函数数量爆炸的权衡）；3) **export**（纯静态：无 server 能力——SSR/ISR/API routes 全禁用，只能 SSG+客户端功能）。
- 选型矩阵：自有 K8s → standalone（镜像 + K8s 编排）；Vercel → serverless；纯内容站 → export；混合（静态页 + 少量 API）→ export + 独立 API 服务。
- standalone 的产物结构：`.next/standalone/server.js`（入口）+ 静态资源外置（public/.next/static 需手动拷贝——镜像分层优化：代码层与静态层分离 RBL-681 层序）。
- serverless 的冷启动画像：每路由独立函数（shared：最大 bundle 冷启动重 vs 每路由：小 bundle 但函数多）——「函数数量 × 冷启动」是 serverless 架构的成本模型。
- 追问钩子：为什么 standalone 模式要「静态资源外置」？——静态资源走 CDN（immutable 缓存 RBL-618）而 node server 无缓存头意义；镜像里静态资源让每次代码发布都重传大镜像（静态层不变却重打包）；「部署单元的职责分离」：代码层（频繁变）与资产层（不变）分开——与 Docker 分层缓存（RBL-681）同一层序哲学。

```javascript
// standalone 构建
// next.config: output: 'standalone'
// 产物：.next/standalone/server.js + node_modules 裁剪版
// Dockerfile（RBL-681 模板）
// FROM node:20 AS builder
// COPY . .
// RUN pnpm build
// FROM node:20-slim
// COPY --from=builder /app/.next/standalone ./
// COPY --from=builder /app/.next/static ./.next/static    # 静态层分离
// COPY --from=builder /app/public ./public
// CMD ["node", "server.js"]
// serverless 函数画像
// 每路由函数：冷启动 ~100-300ms（bundle 小）
// shared lambda：冷启动重但函数少 —— Vercel 按路由自动拆
```
