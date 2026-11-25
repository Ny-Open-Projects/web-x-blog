---
title: [MFW-157] SSR 应用容器化部署要注意什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-157：SSR 应用容器化部署要注意什么？
**答**：
- 镜像：多阶段构建 + standalone/自包含产物，只拷贝运行必需文件（node_modules 按 trace 裁剪），alpine/slim 基底；镜像里带 `NODE_ENV=production`。
- 进程：**单容器单进程**（K8s 副本数管扩容），禁用容器内多 worker；优雅退出要处理 SIGTERM（停止接新请求 → 排空在途请求 → 退出），否则滚动更新会掐断请求。
- 健康检查：liveness（进程活着）/readiness（依赖就绪，DB ping）分离；就绪探针不过不接流量。
- 配置：env 注入 + 构建期静态资源与运行时配置分离（Next 的 NEXT_PUBLIC 是构建期内联，容器化时注意区分）。
- 资源：SSR CPU 密集，limits 按 QPS 压测定；设置 `max old space` 与内存 limit 对齐防 OOMKilled 循环。

```dockerfile
# Dockerfile —— Next.js standalone
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build   # output: 'standalone'

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production PORT=3000
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public
EXPOSE 3000
# SIGTERM 优雅退出：node 默认不处理，用 tini 或启动脚本捕获
CMD ["node", "server.js"]
```

```yaml
# k8s 片段
# livenessProbe:  { httpGet: { path: /api/health, port: 3000 }, periodSeconds: 10 }
# readinessProbe: { httpGet: { path: /api/ready, port: 3000 }, periodSeconds: 5 }
# lifecycle:
#   preStop: { exec: { command: ["sh", "-c", "sleep 5"] } }  # 给 LB 摘流量留窗口
# terminationGracePeriodSeconds: 30
```
