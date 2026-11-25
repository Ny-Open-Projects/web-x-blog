---
title: [BAS-048] npm scripts 怎么传参？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-048：npm scripts 怎么传参？
**答**：
- `npm run dev -- --port 3000`：`--` 之后的参数才会透传给脚本本身。
- 组合：`&&` 顺序执行（失败即中断）、`&` 并行；`pre/post` 前缀命令在目标命令前后自动执行。
- 配置型参数用环境变量传递：`NODE_ENV=xxx npm run build`。

```bash
npm run dev -- --port 3000      # 实际执行 vite --port 3000
npm run lint && npm run test    # 顺序执行，lint 失败则不跑 test
npm run predev                  # predev 会在 npm run dev 之前自动执行
NODE_ENV=production npm run build
```
