---
title: [MFW-158] 笔试：手写 Next.js 应用的生产 Dockerfile（多阶段 + 优雅退出）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-158：笔试：手写 Next.js 应用的生产 Dockerfile（多阶段 + 优雅退出）
**答**：为 Next.js（App Router + standalone 输出）写生产 Dockerfile：① 多阶段构建，镜像最小化；② 非 root 用户运行；③ 只监听 3000；④ 处理 SIGTERM 优雅退出（停止接新请求后排空）；⑤ 健康检查内置（HEALTHCHECK 或注释说明 K8s 探针）。

```dockerfile
# syntax=docker/dockerfile:1
# ===== 阶段 1：依赖 =====
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# ===== 阶段 2：构建 =====
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
# NEXT_PUBLIC_* 构建期内联，构建参数在此传入
ARG NEXT_PUBLIC_API_BASE
ENV NEXT_PUBLIC_API_BASE=$NEXT_PUBLIC_API_BASE
RUN npm run build

# ===== 阶段 3：运行 =====
FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production PORT=3000

# 只拷贝 standalone 产物（trace 裁剪过的 node_modules）
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public

# 非 root：alpine 的 node 用户
RUN chown -R node:node /app
USER node

EXPOSE 3000

# 容器级健康检查（K8s 场景用探针替代）
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
  CMD wget -qO- http://127.0.0.1:3000/api/health || exit 1

# 优雅退出：
# 1) tini 作为 PID 1，正确转发 SIGTERM 给 node
# 2) server.js 内监听 SIGTERM -> server.close() 排空在途请求 -> process.exit(0)
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["node", "server.js"]
```

```js
// server.js（standalone 产物外补丁或自定义启动层）
const server = require('./server.js');

process.on('SIGTERM', () => {
  console.log('SIGTERM: 停止接新请求，排空中…');
  server.close(() => process.exit(0)); // 等在途请求完成
  setTimeout(() => process.exit(1), 10000).unref(); // 排空超时兜底
});
```

**评分点**：
1. 三阶段划分正确，运行层只拷贝 standalone 产物（能说出为什么镜像小）。
2. USER node 非 root 运行 + chown 最小化授权。
3. SIGTERM 优雅退出链路完整：tini 转发信号 → server.close 排空 → 超时兜底强杀。
4. HEALTHCHECK/探针指向独立 /api/health，且 readiness 与 liveness 区分（口头补充）。
5. NEXT_PUBLIC 构建期内联意识（ARG 在 builder 阶段传）。
