---
title: [RBL-035] Rspack 在 Docker 与 CI 中构建有哪些最佳实践？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-035：Rspack 在 Docker 与 CI 中构建有哪些最佳实践？
**答**：
- 镜像分层：依赖层（pnpm-lock 定死）与源码层分离，Rust 二进制（@rspack/core 的 native 包）随 node_modules 进缓存层，避免每次构建重下。
- CI 缓存：持久缓存目录（node_modules/.cache/rspack）挂 cache key = lockfile hash + 配置 hash，命中后增量构建秒级。
- 并行任务：typecheck、lint、build 三个 job 并行，build 只管打包（不背类型检查）。
- 内存与线程：容器要显式设置 CPU 限额，Rayon 线程数默认按宿主核数，容器核数受限时用环境变量对齐（避免线程过多互相挤压）。
- 复现性：固定 Rspack 版本（native 二进制版本与 JS 包必须匹配）、构建时间戳类字段不要进产物。
- 追问钩子：CI 慢的另一个常见根因是 npm registry 网络，用镜像源与依赖缓存先解决，再谈构建器。

```yaml
# Dockerfile 构建层
FROM node:20 AS build
WORKDIR /app
COPY pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile   # 依赖层（可缓存）
COPY . .
ENV RSPACK_THREADS=4
RUN pnpm build   # 源码层，命中 CI 缓存时秒级

# CI 缓存
# key: rspack-${{ hashFiles('pnpm-lock.yaml', 'rspack.config.js') }}
```
