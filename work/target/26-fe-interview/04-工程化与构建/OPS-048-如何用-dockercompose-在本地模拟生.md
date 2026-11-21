---
title: [OPS-048] 如何用 docker-compose 在本地模拟生产环境？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-048：如何用 docker-compose 在本地模拟生产环境？
**答**：
- 目标：本地一条 `docker compose up` 起出"nginx 前端 + API 后端 + 依赖中间件"的完整拓扑，验证生产配置（反代、缓存、CORS）而不是只跑 vite dev。
- 前端容器直接复用生产 Dockerfile，保证"本地验证的配置 = 上线配置"。
- 用 healthcheck + depends_on condition 控制启动顺序，避免前端容器起来时后端未就绪导致联调误判。
- 数据与配置通过 volume 注入，容器无状态，随时重建。

```yaml
# docker-compose.yml：本地模拟生产拓扑
services:
  web:                       # 前端：生产同款镜像
    build:
      context: .
      dockerfile: Dockerfile
    ports: ["8080:80"]
    environment:
      API_BASE: http://api:3000
      APP_ENV: local-prod-sim
    depends_on:
      api: { condition: service_healthy }
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1/healthz"]
      interval: 10s

  api:                       # 后端：本地起真实服务而非 mock
    image: node:22-alpine
    working_dir: /srv
    command: sh -c "npm ci && node server.js"
    volumes: ["./backend:/srv"]
    environment:
      REDIS_URL: redis://redis:6379
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:3000/healthz"]
      interval: 10s

  redis:
    image: redis:7-alpine
    volumes: ["redis-data:/data"]

volumes:
  redis-data:
```

---

## 六、CI/CD 流水线（OPS-049 ~ OPS-058）

CI/CD 是"代码到生产"的自动化通道。考察重点：流水线设计的能力模型（阶段怎么分、卡点放哪、失败怎么办）、不同平台（GitHub Actions/GitLab CI/Jenkins）的落地写法、以及缓存与 Monorepo 视角的效率优化。与 ENG-040~043 的基础写法互补，本节聚焦发布链路与生产实践。

```mermaid
flowchart LR
  A["push 或 MR 触发"] --> B["lint 与类型检查"]
  B --> C["单元测试与覆盖率"]
  C --> D["构建产物"]
  D --> E["镜像构建与扫描"]
  E --> F{"发布审批"}
  F -- 通过 --> G["部署预发"]
  G --> H["预发自动化冒烟"]
  H --> I["部署生产灰度"]
  I --> J["生产冒烟与放量"]
  J --> K["全量并留存产物"]
  F -- 拒绝 --> L["终止并通知"]
```
