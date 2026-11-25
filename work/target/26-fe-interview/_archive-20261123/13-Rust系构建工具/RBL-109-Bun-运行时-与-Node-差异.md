---
title: [RBL-109] Bun 运行时与 Node.js 的核心差异有哪些？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-109：Bun 运行时与 Node.js 的核心差异有哪些？
**答**：
- 引擎差异：Bun 用 JavaScriptCore（Safari 引擎），Node 用 V8——JIT 策略与启动速度不同，Bun 启动快（冷启动约 4~5 倍于 node）。
- 语言实现：Bun 用 Zig 写核心，无 GC 停顿的 JS 端（JSC 有 GC，但宿主层无 V8 堆开销）。
- 原生集成：内置 SQLite（bun:sqlite）、内置编译器（TS/JSX 零配置运行）、内置 fetch/WebSocket、内置打包器与测试器。
- API 兼容：实现了大部分 Node API 与 npm 生态；差异点集中在 native addon（N-API 支持有但部分 C++ 扩展异常）、worker 线程细节、部分 stream 行为。
- 部署生态：Bun 单二进制可 `bun build --compile` 出独立可执行文件；Node 有更成熟的进程管理/调试（--inspect）生态。
- 追问钩子：生产迁移评估顺序——先脚本/工具类负载（低风险高收益），再服务端长驻进程（需要完整回归）。

```bash
# 零配置跑 TS：无需 ts-node/tsconfig 编译步骤
bun ./scripts/migrate.ts

# 内置 SQLite
# import { Database } from 'bun:sqlite';
# const db = new Database('app.db');

# 编译独立二进制
bun build --compile ./server.ts --outfile app
./app   # 无需 node/bun 环境
```
