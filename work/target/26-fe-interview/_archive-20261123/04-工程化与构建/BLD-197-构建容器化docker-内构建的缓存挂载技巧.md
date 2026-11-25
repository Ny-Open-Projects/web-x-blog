---
title: [BLD-197] 构建容器化：docker 内构建的缓存挂载技巧。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-197：构建容器化：docker 内构建的缓存挂载技巧。
**答**：
- 层缓存设计：**依赖层与源码层分离**——先 COPY package.json/pnpm-lock.yaml → install → 再 COPY 源码，lockfile 不变时 install 层直接命中；配合 BuildKit `--mount=type=cache` 把 pnpm store / node_modules / 构建缓存挂到宿主卷，**镜像层不膨胀且跨构建复用**。
- 构建缓存放哪：`node_modules/.cache`（webpack/vite/tsc）与 pnpm store 都用 cache mount；多阶段构建中 builder 阶段挂 cache，runtime 阶段只 COPY dist。
- 坑：cache mount 的内容不进镜像（正确），但 CI 弹性节点上宿主卷会消失——CI 侧要接"卷持久化"（云盘/remote cache 回补）；UID 不匹配导致 cache 目录权限问题（以固定 uid 运行）。
- 一致性：容器内构建要用固定 node 版本（镜像 tag 锁 digest）+ BUILD 参数不漂移，与 BLD-163 的可复现构建联动。

```dockerfile
# Dockerfile：BuildKit cache mount 的生产模板（多阶段）
# syntax=docker/dockerfile:1.7
FROM node:22.11.0-bookworm-slim AS builder
RUN corepack enable
WORKDIR /app
# ① 依赖层：先只复制清单文件，最大化层缓存命中
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
# ② pnpm store 挂 cache：跨构建复用下载缓存，不进镜像层
RUN --mount=type=cache,id=pnpm-store,target=/root/.local/share/pnpm/store \
    pnpm install --frozen-lockfile
# ③ 源码层（最高频变动放最后）
COPY . .
# ④ 构建缓存挂载：webpack/vite 的中间产物跨次构建复用（CI 卷持久化配合）
RUN --mount=type=cache,id=webpack-cache,target=/app/node_modules/.cache \
    pnpm build

# ── runtime：最小产物镜像（不含 node_modules/.cache）──
FROM nginx:1.27-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
# 校验产物清单（发布前一致性）
COPY --from=builder /app/dist/manifest.json /usr/share/nginx/html/
# 构建命令：
#   DOCKER_BUILDKIT=1 docker build --build-arg BUILDKIT_INLINE_CACHE=1 -t app:v1 .
# CI 弹性节点：cache 卷接持久盘，或构建前用 remote cache 预热
#   docker run --rm -v build-cache:/root/.local/share/pnpm/store ...
```
