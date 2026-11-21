---
title: [MFW-154] Edge Runtime 的限制清单有哪些？哪些代码会在 Edge 上翻车？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-154：Edge Runtime 的限制清单有哪些？哪些代码会在 Edge 上翻车？
**答**：
- 运行时限制：无 TCP/UDP socket（`pg`/`redis`/`mysql` 直连全挂）、部分 Node 内置模块缺失（fs/net/child_process）、无文件系统持久写、CPU 时间与内存上限（Worker 约 10~50ms CPU/128MB 量级）、无长驻连接池。
- API 语义差异：Node crypto 与 WebCrypto 子集不同；`process.env` 注入时机不同（构建期 vs 运行时）；setTimeout 可用但无进程常驻语义。
- 翻车三件套：① ORM 直连 DB（Prisma 经典坑——要用 Accelerate/Driver Adapters）；② 依赖里有 native binding；③ 需要长计算（PDF 生成、大图处理）超 CPU 配额。
- 工程对策：依赖审计（模块级拆分 Node/Edge runtime）、HTTP 协议数据服务（Neon driver/PlanetScale HTTP）、重任务投递队列由中心 worker 消费。

```ts
// 判别清单：这段代码能不能跑在 Edge？

// ❌ 1. TCP 直连
// import { Pool } from 'pg';              // net.Socket —— Edge 不支持

// ❌ 2. 文件系统
// import fs from 'fs';                    // 只读挂载都没有，构建期资源用 import 内联

// ✅ 3. HTTP 数据服务
const { rows } = await fetch('https://db-proxy.example.com/sql', {
  method: 'POST',
  body: JSON.stringify({ sql: 'SELECT * FROM products WHERE id = $1', args: [id] }),
}).then((r) => r.json());

// ✅ 4. WebCrypto（而非 node:crypto 全量）
const key = await crypto.subtle.importKey('raw', secret, 'HMAC', false, ['sign']);

// ❌ 5. 重计算
// await generatePdf(500);                  // CPU 超 50ms 配额 -> 被杀

// 工程上：runtime 按路由声明隔离
// export const runtime = 'edge';   // 轻路由
// export const runtime = 'nodejs'; // 重路由
```
