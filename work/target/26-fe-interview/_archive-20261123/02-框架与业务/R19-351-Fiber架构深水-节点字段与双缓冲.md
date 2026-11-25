---
title: [R19-351] Fiber 架构深水：节点字段与双缓冲树
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Fiber]
type: 面试题
---

## R19-351：Fiber 架构深水：节点字段与双缓冲树

**答**：
- Fiber 节点是链表结构：child（第一个子节点）/sibling（兄弟）/return（父）——递归树改为链表遍历，遍历可中断（保存 currentFiber 游标即可恢复）
- 双缓冲（alternate）：current（屏幕上）与 workInProgress（内存中构建）两棵树——commit 后 workInProgress 变为新的 current，切换是 O(1) 指针交换
- 关键字段：flags（Placement/Update/Deletion 副作用标记，向上冒泡到 effectList）、lanes（优先级，替代 expirationTime）、stateNode（DOM 实例）
- effectList 的变迁：React 18 起 effectList 从单向链表改为「commit 阶段遍历 subtree flags」——渲染阶段结束时根节点带 subtreeFlags 汇总
- 面试表达：画出「render 阶段（可中断）→ commit 阶段（同步）」的分界，标注双缓冲切换点在 commit 完成时

```text
render 阶段: workInProgress 构建, 可中断可恢复 (beginWork/completeWork)
commit 阶段: 同步不可中断 (beforeMutation→mutation→layout)
双缓冲: current ↔ workInProgress 指针交换
flags 冒泡: 子树副作用汇总到根 (subtreeFlags)
```
