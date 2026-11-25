---
title: [ZSM-233] Jotai 异步 atom 怎么处理竞态与主动刷新
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-233：Jotai 异步 atom 怎么处理竞态与主动刷新

**答**：
- 异步 atom（read 函数返回 Promise）直接对接 Suspense；同 key 参数变化产生新依赖快照时，旧 Promise resolve 结果不会污染新读取（按依赖版本快照缓存）
- 主动刷新：write-only atom 里调用 `store.get(refreshableAtom)` 前先 `store.set(depAtom, ...)` 触发依赖变化，或用 jotai-utils 的 `atomWithRefresh` 内置 refresh 语义
- 竞态高发场景：搜索词 atom 变化触发异步 atom 重算，慢响应覆盖快响应——Jotai 的快照缓存天然按「本次依赖组合」隔离，不会串
- 错误处理：Promise reject 会抛给 Suspense 上层的 ErrorBoundary；需要局部降级用 loadable 包装

```javascript
import { atomWithRefresh } from 'jotai/utils'
const userAtom = atomWithRefresh(async (g) => fetchUser(g(userIdAtom)))   // 可 refresh
const reload = atom(null, (_g, s) => s(userAtom.refresh()))                // 主动刷新入口
```
