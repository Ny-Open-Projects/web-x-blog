---
title: [ZSM-047] Jotai 的 write-only atom 怎么当 action 用？跨 atom 联动怎么实现？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-047：Jotai 的 write-only atom 怎么当 action 用？跨 atom 联动怎么实现？
**答**：
- `atom(null, (get, set, payload) => ...)` 第一参读函数给 null 即 write-only，语义等同 action/reducer。
- 在写函数里可以 set 任意 atom、get 任意 atom，一次动作级联多个状态（如「提交订单」同时改购物车、清表单、加日志）。
- 异步 action：写函数可以 async，await 接口后再 set；失败分支回滚用前面 get 的快照。
- 相比 Zustand：action 与状态同在 atom 图里，派生与联动都在声明式依赖中，不易出现「忘了同步另一个切片」的 bug。

```javascript
const cartAtom = atom([])
const formAtom = atom({ title: '' })
const logsAtom = atom([])

// write-only action：一次提交联动三个 atom
const submitAtom = atom(null, (get, set) => {
  const items = get(cartAtom)
  if (!items.length) return
  set(logsAtom, l => [...l, `submit ${items.length}`])
  set(cartAtom, [])            // 清购物车
  set(formAtom, { title: '' }) // 重置表单
})
```
