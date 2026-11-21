---
title: [TST-205] Playwright 容器化并发的要点（镜像/资源/显示）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-205：Playwright 容器化并发的要点（镜像/资源/显示）？
**答**：
- 用官方 mcr.microsoft.com/playwright 镜像（浏览器+依赖预装），版本必须与 @playwright/test 严格一致。
- 每容器 CPU/内存预算：单 worker 约 1 CPU + 1-2GB，超卖会导致超时假失败。
- headless 无需 X server；如需 headed 调试用 xvfb-run。
- shm 大小：--ipc=host 或 --shm-size=1g，否则 Chromium 多进程崩溃。

```javascript
# docker compose 片段
services:
  e2e:
    image: mcr.microsoft.com/playwright:v1.49.0
    ipc: host               # 关键：共享内存不足 Chromium 会崩
    environment:
      - SHARD_INDEX=${SHARD_INDEX}
    command: npx playwright test --shard=${SHARD_INDEX}/4
r
```
