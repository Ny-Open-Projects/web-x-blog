---
title: [TST-306] 开发期 mock 与契约漂移的问题如何根治？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-306：开发期 mock 与契约漂移的问题如何根治？
**答**：
- mock 从契约生成（如 Prism/OpenAPI 或 MSW+schema），人工手写 mock 即漂移之源。
- CI 校验 mock 响应过 schema 校验（mock 违约同样红）。
- 本地开发直接用契约生成器起 fake server（字段自动随机），不再维护 mock 文件。
- 契约即 mock、即类型、即文档——单一事实源的完整闭环。

```javascript
# OpenAPI → 本地 fake server（无需手写 mock）
npx prism mock ./openapi.yaml -p 4010
# 前端 vite proxy 指向 4010，字段自动按 schema 生成
r
```
