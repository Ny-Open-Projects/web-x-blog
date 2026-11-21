---
title: [FRP-212] React 的删除操作在 commit 阶段怎么执行（副作用清单）？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-212：React 删除在 commit 阶段怎么执行？
**答**：
- render 阶段 diff 出 Deletion 标记的 fiber，挂到父级 deletions 数组（React 17 起按父 fiber 记录，不再全局 effectList）。
- commit mutation 阶段遍历 deletions：先递归执行子树的 componentWillUnmount/useEffect cleanup（commitDeletionEffects），再移除 DOM。
- ref 清理：删除前 detach ref（避免悬挂引用）。
- Suspense 子树删除有专门路径（隐藏而非卸载——offscreen 语义）。
- 顺序保证：子树 effect 清理先于 DOM 移除，防止 cleanup 读到已卸载 DOM 报错。
