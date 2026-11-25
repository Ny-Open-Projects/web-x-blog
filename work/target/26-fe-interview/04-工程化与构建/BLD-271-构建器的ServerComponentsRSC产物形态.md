---
title: [BLD-271] RSC（Server Components）的产物形态怎么处理？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-271：RSC 产物形态怎么处理？
**答**：
- 双产物形态：server 组件只在服务端执行（编译到 Node bundle，产物不发浏览器）；client 组件双端——构建器按 'use client' 指令拆分模块归属（图分割）。
- 序列化产物：RSC payload（组件树 → 可序列化流——组件引用替换为 client reference ID）——构建器生成 client manifest（client 组件 ID 映射到 chunk）。
- 边界规则：server→client 只能传可序列化 props（函数/类实例不可传——构建期静态检查可捕获部分）。
- 追问钩子：为什么 client reference manifest 是 RSC 构建的核心——服务端渲染时遇到 client 组件只输出「引用 ID + props」占位，浏览器按 ID 从 manifest 找到对应 chunk 加载执行——manifest 的正确性直接决定「服务端占位与客户端实现能否对上」，错位就是 hydration 失败。

```javascript
// 'use client' 指令 → 图分割
// server.bundle: 服务端组件树（Node target）
// client.manifest: { ClientButton: 'chunks/button-abc.js' }
// RSC payload: {"$":"L1","props":{...}}  ← client reference
```
