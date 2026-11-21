---
title: [ZSM-041] Jotai 的 atom 是什么？派生 atom（derived atom）怎么工作？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-041：Jotai 的 atom 是什么？派生 atom（derived atom）怎么工作？
**答**：
- atom 是最小状态单元，`atom(init)` 创建；组件用 `useAtom` 读写，订阅粒度 = 单个 atom，天然无「整 store 重渲染」问题。
- 派生 atom：`atom(get => ...)` 只读派生，get 依赖其他 atom，自动建立依赖图，依赖变化才重算并通知订阅者。
- 可写派生 atom：`atom(read, (get, set, payload) => ...)`，写 action 时可级联更新多个 atom（类似 reducer + 多源联动）。
- 与 Zustand 的差异：Jotai 自下而上（原子组合成派生树），Zustand 自上而下（一个 store 拆 selector）；Jotai 适合「状态间有大量派生关系」的场景，如表单联动、图表配置。
- atom 创建是惰性的：值在首次读取时才计算，派生链没有订阅者时会被垃圾回收（可释放）。

```javascript
import { atom, useAtom } from 'jotai'

const priceAtom = atom(100)
const countAtom = atom(1)
const totalAtom = atom(get => get(priceAtom) * get(countAtom)) // 只读派生

const setBulkAtom = atom(null, (get, set, delta) => {
  set(countAtom, c => Math.max(0, c + delta))
  set(priceAtom, p => p + delta) // 可写派生：一次写多个
})
function Cart() {
  const total = useAtomValue(totalAtom) // 不拿 setter，避免无谓渲染
  const [, apply] = useAtom(setBulkAtom)
}
```
