---
title: [ZSM-065] 排查题：Jotai 页面偶发「改了 atom 但界面没更新」，可能原因清单与排查步骤
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-065：排查题：Jotai 页面偶发「改了 atom 但界面没更新」，可能原因清单与排查步骤
**答**：
- 原因一（最常见）：mutate 引用未替换——改了对象内字段，Object.is 判定无变化。排查：devtools 看 atom 值，若值变了 UI 没动，基本锁定。
- 原因二：组件拿的是快照变量（解构出的对象）而不是重新 useAtomValue，闭包旧值。排查：检查渲染路径。
- 原因三：写错了 atom 实例——atomFamily 每次调用参数不稳定导致读写不同实例。排查：打印 atom 引用是否一致。
- 原因四：被 memo/React.memo 边界挡住且 props 引用没变，或 Provider 隔离——写的是另一个 store 的同名 atom。
- 步骤：先 devtools 确认值 → 再确认订阅组件挂对 store → 再查引用替换 → 最后查组件 memo 边界。

```javascript
// 反例：useMemo 缓存了 atom 值对象，又直接改它
const obj = useMemo(() => ({ count: 0 }), [])
setObjAtom(obj) // 传同一引用 → 不触发
// 修正：setObjAtom(prev => ({ ...prev, count: prev.count + 1 }))
```
