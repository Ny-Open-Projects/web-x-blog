---
title: [ZSM-030] Zustand 防闭包旧值：批量操作（连点、并发请求）怎么避免丢失更新？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-030：Zustand 防闭包旧值：批量操作（连点、并发请求）怎么避免丢失更新？
**答**：
- 丢失更新的根源：更新基于「快照旧值」而不是最新 state，两次并发写互相覆盖。
- 手段一：set 一律用函数形式 `set(s => ...)`，s 永远是最新合并前的 state，天然基于最新值计算。
- 手段二：不能进 set 的复杂计算用 `get()` 现取现算，不要缓存 state 到闭包/模块变量。
- 手段三：异步结果按请求序号（或 AbortController 取消旧请求）写入，只接受最新一次。
- 追问钩子：setState 两次同步调用会依次合并，渲染只触发一次（React 18 批处理），不用担心性能而改用「攒一批再 set」的 hack。

```javascript
const useCart = create((set, get) => ({
  count: 0,
  inc: () => set(s => ({ count: s.count + 1 })), // 连点安全
}))
let seq = 0
async function search(kw) {
  const my = ++seq
  const data = await api.search(kw)
  if (my !== seq) return            // 过期响应丢弃
  useSearch.setState({ list: data }) // 只写最新一次
}
```
