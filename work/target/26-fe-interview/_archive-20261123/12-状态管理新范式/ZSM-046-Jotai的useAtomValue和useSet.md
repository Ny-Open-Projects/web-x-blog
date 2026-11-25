---
title: [ZSM-046] Jotai 的 useAtomValue/useSetAtom/useAtom 有什么区别？怎么减少不必要的重渲染？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-046：Jotai 的 useAtomValue/useSetAtom/useAtom 有什么区别？怎么减少不必要的重渲染？
**答**：
- `useAtom` 返回 [value, setter]；`useAtomValue` 只要值；`useSetAtom` 只要 setter。
- 关键优化：useSetAtom 的返回值是稳定引用，**atom 值变化不触发持有 setter 的组件重渲染**——「控制器组件」模式的基础。
- 值组件拆分：展示值用 useAtomValue，写操作抽到子组件/工具栏用 useSetAtom，读写分离后重渲染范围最小化。
- setter 稳定引用意味着把它传给 memo 子组件、放进事件回调都不会导致更新失效。

```javascript
function Counter() {        // 只显示：值变才渲染
  const n = useAtomValue(countAtom)
  return <b>{n}</b>
}
function Controls() {       // 只写：永远不因 countAtom 变化而渲染
  const set = useSetAtom(countAtom)
  return <button onClick={() => set(c => c + 1)}>+1</button>
}
// useAtom(countAtom) 的 setter 同样稳定，但解构值会让本组件订阅值
```
