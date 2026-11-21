---
title: [RBL-163] Docker 化前端构建：层缓存与 BuildKit 缓存挂载
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-163：Docker 化前端构建：层缓存与 BuildKit 缓存挂载

**答**：
- 层缓存原则：变化频率从低到高排列 COPY——先 COPY lockfile 装依赖（低频），再 COPY 源码构建（高频），保证改代码不重装依赖。
- BuildKit cache mounts：把 pnpm store / Rust 工具缓存目录挂为 --mount=type=cache，缓存不进镜像层、跨构建复用，比纯 layer cache 更稳。
- 构建器内缓存：CI 上传/拉取 Docker 层缓存（buildx --cache-from/--cache-to type=registry），跨机器复用。
- 产物分离：构建 stage 与运行 stage 用 multi-stage，最终镜像只含 dist + 运行时，体积小且不受构建缓存污染。
- 追问钩子：Rust 工具（Rspack/Bun）都是单二进制，直接 COPY --from=构建镜像或官方镜像进去，不需要在最终镜像里装 node_modules 的编译依赖。

```dockerfile
# Dockerfile（BuildKit 语法）
FROM node:22-alpine AS deps
WORKDIR /app
COPY pnpm-lock.yaml ./
RUN corepack enable && pnpm fetch   # 只拉包不安装，lockfile 不变则此层永远命中

FROM deps AS build
COPY . .
RUN --mount=type=cache,id=pnpm-store,target=/root/.local/share/pnpm/store \
    pnpm install --frozen-lockfile --offline && \
    pnpm --filter @app/web build    # Rspack 构建，源码变更只重跑这层

FROM node:22-alpine AS runtime
WORKDIR /app
COPY --from=build /app/apps/web/dist ./dist
COPY --from=build /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]
```
