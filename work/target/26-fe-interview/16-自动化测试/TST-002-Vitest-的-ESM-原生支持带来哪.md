---
title: [TST-002] Vitest 原生跑 ESM 带来了哪些实际收益？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-002：Vitest 原生跑 ESM 带来了哪些实际收益？
**答**：
- 语法零转换成本：import/export、顶层 await、动态 import 直接被 Node 原生 ESM 执行，esbuild 只做 TS/JSX 剥离，不做模块格式改写。
- 与源码一致：Vite 项目产物就是 ESM，测试环境和运行环境模块语义相同，避免了 Jest 里 CJS 模拟 ESM 的「interop」怪问题（default 互操作、命名导出丢失）。
- tree-shaking 语义保留：测试里按具名导出引入，不会因为 CJS 打包把整个库拉进来，mock 的粒度也更准。
- 依赖处理：Vitest 沿用 Vite 的 optimizeDeps 预构建，把 CJS 依赖转 ESM，`server.deps.inline` / `deps.optimizer` 解决特殊包。
- 代价（追问钩子）：部分 CJS-only 依赖在 ESM 下可能报「does not provide an export named」，需要 inline 或 alias 处理。

```javascript
// 源码直接用 ESM，测试无需任何转换配置
// src/request.ts
import axios from 'axios';
export const get = (url: string) => axios.get(url);

// src/request.test.ts
import { describe, it, expect, vi } from 'vitest';
import { get } from './request';              // 原生 ESM 加载
vi.mock('axios', () => ({ default: { get: vi.fn() } })); // 拦截的是同一份 ESM 模块

// 若某 CJS 包报命名导出缺失，可强制内联转换：
// vitest.config.ts
export default defineConfig({ test: { server: { deps: { inline: ['old-cjs-pkg'] } } } });
```
