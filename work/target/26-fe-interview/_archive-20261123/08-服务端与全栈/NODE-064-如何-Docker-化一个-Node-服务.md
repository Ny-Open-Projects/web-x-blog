---
title: [NODE-064] 如何 Docker 化一个 Node 服务？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-064：如何 Docker 化一个 Node 服务？
**答**：
- **多阶段构建**：builder 阶段装依赖+编译，runtime 阶段只拷 `node_modules`（`--omit=dev`）与产物，镜像从 1GB+ 缩到 150MB 级；基础镜像用 `node:22-alpine`（小但有 musl 兼容性注意）。
- 信号处理：容器 PID 1 不转发信号——要么 `docker run --init`，要么 `CMD ["node", "main.js"]` 直接以 node 为 PID 1（node 原生响应 SIGTERM）；**不要用 `npm start`**（npm 中间层吞信号）。
- 细节：`.dockerignore` 排除 node_modules/.git；非 root 用户运行；`NODE_ENV=production`；健康检查 HEALTHCHECK 或交给 K8s。

```dockerfile
# ---------- builder 阶段：装依赖 + 编译 TS ----------
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --registry=https://registry.npmmirror.com   # ci 严格按 lock 安装
COPY . .
RUN npm run build && npm prune --omit=dev               # 只留生产依赖

# ---------- runtime 阶段：最小运行环境 ----------
FROM node:22-alpine
ENV NODE_ENV=production
WORKDIR /app
RUN addgroup -S app && adduser -S app -G app             # 非 root 运行
COPY --from=builder --chown=app:app /app/dist ./dist
COPY --from=builder --chown=app:app /app/node_modules ./node_modules
COPY --from=builder --chown=app:app /app/package.json ./
USER app
EXPOSE 3000
# 直接以 node 为 PID 1：SIGTERM 直达进程，优雅退出生效
CMD ["node", "dist/main.js"]
```

```bash
# 构建与运行
docker build -t bff-server:1.0.0 .
docker run --init -d --name bff \
  -p 3000:3000 \
  --memory=512m --cpus=1 \
  --health-cmd="wget -qO- http://localhost:3000/healthz || exit 1" \
  --health-interval=15s \
  bff-server:1.0.0

# .dockerignore 内容：node_modules、.git、.env、dist、*.log、coverage
```
