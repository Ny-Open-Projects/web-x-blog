---
title: [ENG-013] Vite 的环境变量机制是怎样的？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-013：Vite 的环境变量机制是怎样的？
**答**：
- .env 文件按环境命名：.env（全部）、.env.development、.env.production、.env.local（本地覆盖，默认 gitignore）。
- 只有 VITE_ 前缀的变量会暴露给客户端代码，通过 import.meta.env.VITE_XXX 读取。
- 自定义前缀用 envPrefix 配置；服务端专用变量不加前缀以防泄漏。
- TS 项目在 src/vite-env.d.ts 里扩展 ImportMetaEnv 获得类型提示。

```ini
# .env.development —— 仅 development 模式加载
VITE_API_BASE=http://localhost:3000/api
VITE_ENABLE_MOCK=true

# .env.production —— 生产构建时加载
VITE_API_BASE=https://api.example.com
VITE_ENABLE_MOCK=false

# 代码中通过 import.meta.env.VITE_API_BASE 读取
# .env.local 存放本地覆盖，默认被 gitignore，绝不提交
```
