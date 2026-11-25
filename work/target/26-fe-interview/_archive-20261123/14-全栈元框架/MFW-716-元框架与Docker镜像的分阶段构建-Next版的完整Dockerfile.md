---
title: [MFW-716] Next Docker 分阶段构建完整版
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-716：Next Docker 分阶段构建完整版

**答**:
- 完整的 Dockerfile（RBL-686/586 的 Next 特化）：1) **deps 阶段**（lockfile 缓存——pnpm install --frozen-lockfile）；2) **build 阶段**（pnpm build——生成 .next/standalone）；3) **runtime 阶段**（拷 standalone + static + public——最小镜像）；4) **健康检查**（HEALTHCHECK——容器编排的探针）；5) 非 root 用户（安全——USER node）。
- 体积优化链：alpine 基础镜像 + standalone（node_modules 裁剪）+ 静态分离 + .dockerignore（node_modules/.next 排除——上下文瘦身）。
- 多 app monorepo：standalone per app（apps/web/.next/standalone——turbo 编排的 Docker 多阶段）。
- 追问钩子：为什么「.dockerignore 排除 node_modules 和 .next」是体积与速度双赢？——node_modules 排除 = 避免宿主依赖进上下文（依赖安装由 Docker 内统一——版本一致性）；.next 排除 = 避免宿主构建产物干扰（Docker 内 clean build）；上下文传输速度（排除大目录 = build context 小——CI 构建加速）；「Docker 构建的第一课」：上下文瘦身是一切优化的前置。

```dockerfile
# .dockerignore
node_modules
.next
.git
*.md

# Dockerfile
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile

FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN corepack enable && pnpm build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup --system node && adduser --system node
COPY --from=builder --chown=node:node /app/.next/standalone ./
COPY --from=builder --chown=node:node /app/.next/static ./.next/static
COPY --from=builder --chown=node:node /app/public ./public
USER node
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:3000/api/health || exit 1
CMD ["node", "server.js"]
```
