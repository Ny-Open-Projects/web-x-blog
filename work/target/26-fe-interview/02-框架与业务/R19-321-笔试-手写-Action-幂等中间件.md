---
title: [R19-321] 笔试：手写 Server Action 幂等去重中间件
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-321：笔试：手写 Server Action 幂等去重中间件
**题**：实现 `withIdempotency(handler)`：从 formData 取 requestId；用 Map/Redis 记录「进行中」与「已完成结果」（TTL 5 分钟）；同 requestId 重入返回首次结果（不重复执行）；进行中重复请求返回 { code: 'PENDING' }。

```javascript
const inflight = new Map()
const done = new Map()
export function withIdempotency(handler) {
  return async (prevState, formData) => {
    const requestId = formData.get('requestId')
    const TTL = 5 * 60_000
    const doneHit = done.get(requestId)
    if (doneHit && Date.now() - doneHit.t < TTL) return doneHit.result
    if (inflight.has(requestId)) return { ok: false, code: 'PENDING' }
    inflight.set(requestId, true)
    try {
      const result = await handler(prevState, formData)
      done.set(requestId, { result, t: Date.now() })
      return result
    } finally {
      inflight.delete(requestId) // 解锁；done 不删（供重入）
    }
  }
}
// 用法：export const createOrder = withIdempotency(async (prev, fd) => { /* 下单 */ })
```
**评分点**：
- inflight 锁防并发重复执行（finally 解锁）。
- done 结果缓存 + TTL（重试网络失败时拿到首次结果）。
- PENDING 语义返回而非阻塞等待。
- 提示生产用 Redis + setnx 过期，内存 Map 仅单实例。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-1cd03a74-aafb-414e-b0f2-7c337b793852-cwd'; fi
exit "$__zcode_status"
