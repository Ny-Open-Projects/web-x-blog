---
title: [ENG-054] 前端应用如何用 Docker 部署？多阶段构建有什么好处？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-054：前端应用如何用 Docker 部署？多阶段构建有什么好处？
**答**：
- 前端产物是纯静态文件：第一阶段 node 镜像安装依赖并构建，第二阶段 nginx 镜像只拷贝 dist。
- 多阶段构建让最终镜像不含 node_modules 与源码，体积从上 GB 降到几十 MB。
- 镜像构建与 CI 解耦：Dockerfile 内固定 corepack/pnpm 版本保证可复现。
- 运行时通过 nginx 容器对外服务，配合健康检查滚动更新。

```bash
# Dockerfile 关键指令（多阶段构建）
# FROM node:22-alpine AS builder
# WORKDIR /app
# COPY package.json pnpm-lock.yaml ./
# RUN corepack enable && pnpm install --frozen-lockfile
# COPY . .
# RUN pnpm build
# FROM nginx:alpine
# COPY --from=builder /app/dist /usr/share/nginx/html

# 构建并运行
docker build -t my-spa:1.0.0 .
docker run -d -p 8080:80 --name my-spa my-spa:1.0.0

# 查看镜像体积，验证多阶段裁剪效果
docker images my-spa
```
