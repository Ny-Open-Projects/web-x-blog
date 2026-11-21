---
title: [ZSM-337] 状态库引入对包体积的影响怎么控制
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-337：状态库引入对包体积的影响怎么控制

**答**:
- 体积画像先行：zustand 核心 ~1KB、jotai ~2-4KB、valtio ~3KB、redux-toolkit ~12KB+；中间件与 devtools 是增量大头，按需 import
- tree-shaking 生效条件：sideEffects: false 的包 + ESM + 具名导入；`import { persist } from 'zustand/middleware'` 子路径导入比主入口干净
- devtools 类开发依赖用条件挂载（import.meta.env.DEV）让生产构建整体摇掉；不用的大中间件（immer/RxJS 适配）不引入
- 监控：bundle 分析（rollup-plugin-visualizer）把状态库占比纳入 PR 体积门禁，防止「顺手引个全家桶」

```javascript
// ✅ 按需 + 条件
import { create } from 'zustand'
import { persist } from 'zustand/middleware'   // 只在用到的模块引入
const dev = import.meta.env.DEV
export const useStore = create()(dev ? devtools(base) : base)
// ❌ import * as z from 'zustand' 全家桶进 bundle
```
