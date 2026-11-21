---
title: [ZSM-090] 为什么 TanStack Query 要求 queryFn 是「不吞错」的 Promise？吞错的 fetch 会导致什么诡异现象？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-090：为什么 TanStack Query 要求 queryFn 是「不吞错」的 Promise？吞错的 fetch 会导致什么诡异现象？
**答**：
- Query 靠 Promise rejection 识别失败并驱动 retry/isError；queryFn 内 try/catch 吞掉错误或 `fetch` 后手动 return undefined，会被当成「成功返回 undefined」。
- 诡异现象：isError 永远 false、retry 不触发、data 为 undefined 但 status 是 success，渲染层判空逻辑全部失效。
- fetch 不抛 HTTP 错误（只有网络层才 reject），必须检查 `res.ok` 手动抛——这是最高频的吞错源头。
- 封装规范：统一 api 层抛出带 status 的 Error，queryFn 只负责调用，不做兜底转换。

```javascript
async function request(url) {
  const res = await fetch(url)
  if (!res.ok) {                          // 关键：HTTP 错误手动抛
    const err = new Error(await res.text())
    err.status = res.status
    throw err                              // 让 Query 正确进入 error/retry 流
  }
  return res.json()
}
// 反例：queryFn: async () => { try { return await api() } catch { return [] } } ← 吞错
```
