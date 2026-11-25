---
title: [ZSM-642] 请求去重与 cancelRefetch：同 key 的并发请求怎么裁决
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-642：请求去重与 cancelRefetch：同 key 的并发请求怎么裁决

**答**：
- 默认去重：Query.fetch 发现「已在途的 fetch」时直接复用其 Promise——多个组件/多个 observer 触发的同 key 请求只发一次网络调用。这是「请求去重」的基础，也意味着 queryFn 必须可共享（无副作用）。
- cancelRefetch 语义：`fetch({ cancelRefetch: true })`（invalidate/refetch 默认开启）——放弃旧在途请求（AbortSignal 取消），发起新请求。场景：参数变了但 key 没变的强制刷新（如轮询叠加手动刷新）。
- 裁决规则总结：1) 在途 + 新请求同 key 同参数 → 复用（去重）；2) 在途 + invalidate/refetch 主动触发 → 取消旧的发新的（cancelRefetch 默认 true）；3) key 变化 → 旧请求 AbortSignal cancel（组件卸载或 key 切换时），新 Query 独立 fetch；4) retry 期间再触发 fetch → 归并为同一 retryer。
- 实战坑：`staleTime: 0` + 频繁 invalidate 会造成请求风暴——旧请求刚 cancel 又发新的；调 staleTime 或 debounce invalidate。
- 追问钩子：取消的请求服务端可能已执行——mutation 场景绝不 cancelRefetch（写操作不能取消重放），只对 query 用。

```javascript
// fetch 的裁决骨架（简化）
async function fetch(query, options) {
  const inFlight = query.#retryer
  if (inFlight && !options.cancelRefetch) {
    return inFlight.promise          // ① 去重：复用 Promise
  }
  if (inFlight && options.cancelRefetch) {
    inFlight.cancel({ silent: true })   // ② 取消旧的（AbortSignal.abort）
  }
  const retryer = createRetryer({ queryFn, signal: controller.signal })
  query.#retryer = retryer
  return retryer.promise
}

// 去重验证
const useA = useQuery({ queryKey: ['big'], queryFn: slowFetch })   // 请求 A
const useB = useQuery({ queryKey: ['big'], queryFn: slowFetch })   // 复用 A，网络面板只有一次

// cancelRefetch 实战
button.onclick = () => queryClient.refetchQueries({ queryKey: ['big'], type: 'active' })
// 手动刷新：默认 cancelRefetch=true → 放弃旧的立即拉新的

// 参数变化自动取消旧请求
const { data } = useQuery({
  queryKey: ['search', kw],        // kw 变化 → 新 Query，旧请求 signal cancel
  queryFn: ({ signal }) => fetch(`/api/search?q=${kw}`, { signal }).then((r) => r.json()),
})
// 旧响应到达时请求已取消 → 不写缓存不触发渲染（防旧结果覆盖新输入）
```
