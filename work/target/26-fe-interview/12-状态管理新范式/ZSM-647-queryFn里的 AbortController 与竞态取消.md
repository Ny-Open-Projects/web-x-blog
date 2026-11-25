---
title: [ZSM-647] queryFn 里的 AbortSignal：请求取消与竞态防御的完整接法
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-647：queryFn 里的 AbortSignal：请求取消与竞态防御的完整接法

**答**：
- signal 的来源链：Query.fetch 创建 AbortController → retryer 透传 signal → queryFn 的 `({ signal, queryKey })` 接收。取消时机：组件卸载（该 observer 独占时）、queryKey 变化、invalidate 的 cancelRefetch、手动 `cancelQueries`。
- 完整接法三层：1) fetch 层传 signal（浏览器原生取消连接，省流量）；2) **axios 要显式配置** `axios.get(url, { signal })`；3) queryFn 内的「后处理」也要响应取消——signal.aborted 检查，避免取消后又跑昂贵的格式化。
- 竞态防御本质：key 切换（如搜索词变化）→ 旧请求取消 → 旧响应即使到达也**不写缓存不通知**（retryer 已标 cancel）——这就是 TanStack Query 比「useEffect + 手写 AbortController」安全的核心。
- 未接 signal 的后果：旧请求继续消耗带宽，虽然结果不进缓存（v5 会比对 queryKey），但服务端做了无用功；且长连接场景（SSE/fetch 流）必须 abort 才能真正断开。
- 追问钩子：`isCancelledError` 与真实错误的区分——取消不算 error 不触发 retry/错误 UI；onError 里要过滤取消类 rejection。

```javascript
// 完整接法示例
useQuery({
  queryKey: ['search', kw],
  queryFn: async ({ signal }) => {
    // ① fetch 原生取消
    const res = await fetch(`/api/search?q=${encodeURIComponent(kw)}`, { signal })
    if (!res.ok) throw new Error('failed')
    const data = await res.json()
    if (signal.aborted) throw new DOMException('aborted', 'AbortError')   // ② 后处理前检查
    return expensiveFormat(data)     // 取消后不会执行到这里
  },
  // ③ axios 等价写法
  // queryFn: ({ signal }) => axios.get('/api/search', { params: { q: kw }, signal })
})

// 手动取消场景
queryClient.cancelQueries({ queryKey: ['search'] })   // 离开搜索页时

// 错误处理区分取消
useQuery({
  ...opts,
  retry: (count, error) => {
    if (error.name === 'AbortError' || error.name === 'CanceledError') return false   // 取消不重试
    return count < 3
  },
})

// 不接 signal 的自查
// queryFn: () => fetch(url)   // ✗ 没接 signal：旧请求白跑，流式请求根本断不开
```
