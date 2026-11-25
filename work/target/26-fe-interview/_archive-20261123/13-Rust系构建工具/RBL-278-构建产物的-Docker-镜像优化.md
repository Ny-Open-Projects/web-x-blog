---
title: [RBL-278] 构建产物的 Docker 镜像优化
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-278：构建产物的 Docker 镜像优化

**答**:
- 多阶段构建：builder 阶段装全量依赖构建 → runtime 阶段只拷产物与运行依赖（node:alpine/或 nginx:alpine 静态）——镜像从 1GB 降到几十 MB
- 层缓存：package.json 先 COPY 再 install（依赖不变时层命中）；构建产物不进依赖层
- .dockerignore：node_modules/dist 排除（防止宿主污染构建上下文，上下文传输也快）
- 构建缓存进阶：BuildKit 的 cache mount（npm/pnpm store 缓存跨构建复用）——CI 里依赖安装时间砍半

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm i --frozen-lockfile
COPY . .
RUN pnpm build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
# .dockerignore: node_modules, dist, .git
```
