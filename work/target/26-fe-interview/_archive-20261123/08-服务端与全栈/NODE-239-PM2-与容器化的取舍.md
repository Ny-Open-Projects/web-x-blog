---
title: [NODE-239] PM2 与容器化的取舍？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-239：PM2 与容器化的取舍？
**答**:
- 容器环境不需要 PM2 做进程管理：K8s/云托管提供副本调度、健康检查、重启策略——进程管理职责上移。
- 容器内的 PM2 残余价值：单容器内多核利用（cluster 4 实例）+ reload 优雅滚动；但 K8s 水平扩副本更符合云原生（进程数交给 HPA）。
- 坑：PM2 daemon 在容器内 PID 1 问题（信号转发/僵尸进程回收）——需 --no-daemon 或 tini 作 init。
- 决策表：裸机/虚机 → PM2 全家桶；K8s → 单进程容器 + K8s 编排；Serverless → 无进程管理（平台冷启动）。

```dockerfile
# 容器内 PM2 的正确姿势
FROM node:22-alpine
RUN npm i -g pm2
COPY . /app
WORKDIR /app
CMD ["pm2-runtime", "ecosystem.config.js", "--env", "production"]
# pm2-runtime 前台运行（daemon 0），信号正确转发
# 或者完全去 PM2：CMD ["node", "dist/server.js"] + K8s replicas: N
```
