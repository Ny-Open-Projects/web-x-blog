---
title: [DP-202] 源码识别：React Hooks 源码中的备忘录与链表结构？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-202：源码识别：React Hooks 源码中的备忘录与链表结构？
**答**：
- 备忘录（memoization）：useMemo/useCallback/memo 都是备忘录模式——以依赖数组为"输入指纹"，命中即返回缓存值。React.memo 是组件级备忘录。
- 状态机/命令：useState 的 update 对象（action 存在 fiber hook 链表里）是命令模式变体——更新被封装为对象排队，渲染时统一执行。
- 链表与游标：hooks 按调用顺序存进 fiber.memoizedState 单向链表，dispatch 游标（hookIndex）在 render 时重置——"顺序即身份"，这是 hooks 不能放 if 里的根源。
- 识别要点：能画 hook 链表 + 解释 update 队列为什么用环形单向链表（中断恢复时从当前位置继续）。

```javascript
// React hooks 简化模型
function fiberWithHooks() {
  const hooks = []; let cursor = 0;                  // 链表 + 游标
  function useState(initial) {
    const i = cursor++;
    hooks[i] ??= { memoizedState: initial, queue: [] };   // 首次初始化
    const q = hooks[i].queue;
    // 执行更新队列（命令模式：action 对象排队）
    q.forEach(action => { hooks[i].memoizedState =
      typeof action === 'function' ? action(hooks[i].memoizedState) : action; });
    hooks[i].queue = [];
    const setState = action => q.push(action);        // 排队而非立即执行
    return [hooks[i].memoizedState, setState];
  }
  function useMemo(fn, deps) {
    const i = cursor++;
    const h = hooks[i] ??= { deps: null, value: undefined };
    if (!h.deps || deps.some((d, k) => d !== h.deps[k])) h.value = fn();  // 备忘录：指纹比对
    h.deps = deps;
    return h.value;
  }
  return { useState, useMemo, reset: () => { cursor = 0; } };   // render 开始重置游标
}
```
