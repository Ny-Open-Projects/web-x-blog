---
title: [RBL-106] Bun 是什么？为什么说它是"一体化工具链"？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-106：Bun 是什么？为什么说它是"一体化工具链"？
**答**：
- Bun 是 Zig 编写的 JavaScript 运行时 + 一体化工具链：运行时（对标 Node）、包管理（bun install 对标 npm/pnpm）、打包器（bun build 对标 esbuild）、测试器（bun test 对标 jest）、转译器（内置 TS/JSX 支持），全部一个二进制。
- 一体化的价值：省去工具间胶水成本（安装、配置、兼容矩阵），共享同一套底层（解析/转译/缓存），整体链路快。
- 兼容面：兼容 Node API 大部分（fs/http/path 等）、npm 生态直接可用、CJS/ESM 混跑、npmrc 支持；但不完全兼容（部分 native addon、特定 API 行为）。
- 底层细节：Zig（非 Rust）、JSC 引擎（JavaScriptCore，非 V8）、内置 SQLite、文件路由的 HTTP server 等。
- 典型场景：脚本工具链、CI 安装提速、边缘函数运行时、单体仓库的快速 test。
- 追问钩子：Bun vs Node 的取舍不只是速度——生态成熟度、调试工具链、长期支持是团队迁移的真实考量。

```bash
# Bun 一体化命令面
bun install            # 包管理（替代 npm/pnpm，lockfile: bun.lockb）
bun run dev            # 跑 scripts
bun build ./src/index.ts --outdir dist --minify   # 打包（esbuild 级速度）
bun test               # 测试（jest 兼容 API）
bun ./server.ts        # 直接运行 TS（内置转译，无需 ts-node）
```
