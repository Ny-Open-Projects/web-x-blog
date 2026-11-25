---
title: [OPS-041] 前端项目的 Dockerfile 多阶段构建怎么写？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-041：前端项目的 Dockerfile 多阶段构建怎么写？
**答**：
- 阶段一 builder：装 Node、装依赖、npm run build，产出 dist；阶段二 runtime：只放 nginx/alpine 与 dist，Node、node_modules、构建工具全部不进最终镜像。
- 好处：最终镜像不含构建链（node_modules 动辄几百 MB），体积从 1GB 级降到 50MB 内，拉取快、攻击面小。
- 依赖安装与源码拷贝分层：先 COPY package*.json 再 npm ci，源码变更不触发依赖重装，吃满层缓存。
- nginx 基础镜像里带 SPA 配置与健康检查端点，ENTRYPOINT 保持前台运行。

```dockerfile
# 多阶段构建：构建与运行彻底分离
FROM node:22-alpine AS builder
WORKDIR /app

# 先拷贝依赖清单吃缓存：源码变了不重装依赖
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile

COPY . .
RUN pnpm build

# 运行阶段：只有 nginx 与静态产物
FROM nginx:1.27-alpine
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

# 健康检查端点 + 探活
RUN printf 'ok' > /usr/share/nginx/html/healthz
HEALTHCHECK --interval=15s --timeout=3s --retries=3 \
  CMD wget -qO- http://127.0.0.1/healthz || exit 1

EXPOSE 80
# nginx 镜像默认前台运行，无需额外 CMD
```
