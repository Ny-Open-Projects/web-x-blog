---
title: [ZSM-142] TanStack Query 里怎么真正取消一个请求？AbortController 和 cancelQueries 的关系是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-142：TanStack Query 里怎么真正取消一个请求？AbortController 和 cancelQueries 的关系是什么？
**答**：
- cancelQueries 只是「标记放弃」：让 Query 停止等待并重置状态；真正掐断网络连接要 queryFn 里接 signal——queryFn 第二参 `{ signal }` 把 AbortSignal 传给 fetch，取消时浏览器中止真实请求。
- 组件卸载/ key 变化时 Query 会自动 abort 传入的 signal，所以「切页取消旧请求」只需 signal 接上 fetch，一行多余代码都不用写。
- 检测取消：queryFn 里 catch 到 `error.name === 'AbortError'` 是正常流程不是错误，不要上报埋点；自定义 axios 的话传 `signal` 参数即可（axios 0.22+ 原生支持）。
- 注意：没接 signal 时 cancelQueries 只是不再把结果写进缓存，网络仍在跑，弱网用户多占带宽。

```javascript
function useGoods(id) {
  return useQuery({
    queryKey: ['goods', id],
    queryFn: ({ signal }) =>           // 关键：接收 signal
      fetch(`/api/goods/${id}`, { signal }).then(res => {
        if (!res.ok) throw Object.assign(new Error(), { status: res.status })
        return res.json()
      }),
    staleTime: 30_000,
  })
}

// 主动取消：搜索切换场景
function onKeywordChange(next) {
  queryClient.cancelQueries({ queryKey: ['search'] })   // 标记放弃旧查询
  setKeyword(next)                                      // key 变化自动 abort + 重取
}
// queryFn 内部：catch (e) { if (e.name === 'AbortError') return neverUpstream(e) }
```
