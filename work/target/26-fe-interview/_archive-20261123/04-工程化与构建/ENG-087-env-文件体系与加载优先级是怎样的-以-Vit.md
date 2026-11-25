---
title: [ENG-087] .env 文件体系与加载优先级是怎样的（以 Vite/Next 为例）？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-087：.env 文件体系与加载优先级是怎样的（以 Vite/Next 为例）？
**答**：
- Vite 加载顺序（高到低，同名覆盖）：.env.[mode].local > .env.[mode] > .env.local > .env；.local 默认进 gitignore。
- 只有 VITE_ 前缀的变量会被注入客户端产物，其余留在 process.env 只供 vite.config 等服务端使用。
- Next.js 支持 .env/.env.local/.env.[env]，但值在 build 时内联进产物，运行时改 .env 不生效。
- 纪律：.env.example 提交字段模板并注明用途；真实 .env 不入库；mode 与 NODE_ENV 的映射要搞清（build --mode staging）。

```bash
# Vite 环境文件加载优先级（从高到低，高优先级覆盖低优先级）
# 1. .env.development.local
# 2. .env.development
# 3. .env.local
# 4. .env

# 检查：带 VITE_ 前缀的变量才会进客户端产物
cat .env.development
#   VITE_API_BASE=https://dev.example.com/api     <- 会注入 import.meta.env
#   DATABASE_URL=postgres://localhost/mydb        <- 无前缀，仅服务端可见

# 本地私密覆盖不入库
cat .gitignore | grep env
#   .env.local
#   .env.*.local

# staging 等自定义模式要显式指定
pnpm build --mode staging
```
