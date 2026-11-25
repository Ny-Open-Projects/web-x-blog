---
title: [R19-388] Hooks 链表与调用顺序约束的本质
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Fiber]
type: 面试题
---

## R19-388：Hooks 链表与调用顺序约束的本质

**答**：
- Hooks 存储：Fiber.memoizedState 是 hooks 单向链表——每个 Hook 节点按「调用顺序」挂链；渲染时按序读取 current 链、构建 workInProgress 链
- 顺序约束的本质：React 靠「调用顺序」对齐状态——条件调用会让链错位（第 N 个 hook 读到别的 hook 的状态）——所以「不能在条件/循环/嵌套函数里调 Hook」是架构约束不是风格
- Hook 节点结构：各 Hook 不同（useState 是 queue、useEffect 是 effect 对象、useMemo 是 [value, deps]）——deps 比较发生在「读取时」（Object.is 逐项）
- 并发下的双链：current 与 workInProgress 各一份链——中断恢复时「已处理的 hook」状态在新链保留（workInProgress hook 是复用/克隆）
- 理解应用：自定义 Hook 内的条件 Hook 同样违规——lint（eslint-plugin-react-hooks）在编译期拦

```text
Fiber.memoizedState:
  Hook1(useState) → Hook2(useEffect) → Hook3(useMemo) → ...
render: 按序遍历 current 链读取, 构建新链
条件调用: 链位错乱 → 状态串位 (架构层面禁止)
```
