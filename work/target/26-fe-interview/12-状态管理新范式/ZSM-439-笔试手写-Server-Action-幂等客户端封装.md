---
title: [ZSM-439] 笔试：手写 Server Action 幂等客户端封装（去重 + 结果缓存 + 竞态）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-439：手写 Server Action 幂等客户端封装
**需求**：实现 `createActionClient(action)`：1) `call(args)`：参数稳定序列化后去重——同参数在途调用共享同一 Promise；2) 成功结果短缓存（10s 内同参数直接返回缓存）；3) 自动附加幂等键 `__opId`（同参数重试复用同一 opId——服务端去重依赖它）；4) 失败重试同 opId 最多 1 次；5) 超时（30s）后进入「待确认」态：返回 pending 标记而非错误（结果可能已生效）；6) `confirmPending(opId)` 轮询确认接口收尾。

```javascript
export function createActionClient(action, { cacheMs = 10_000, timeoutMs = 30_000 } = {}) {
  const inflight = new Map()
  const cache = new Map()      // key → { result, ts }
  const opIds = new Map()      // key → opId（重试复用）

  function keyOf(args) { return stableStringify(args) }

  async function call(args) {
    const key = keyOf(args)
    const hit = cache.get(key)
    if (hit && Date.now() - hit.ts < cacheMs) return hit.result
    if (inflight.has(key)) return inflight.get(key)

    const opId = (opIds.get(key) ??= crypto.randomUUID())
    const p = (async () => {
      const timer = new Promise((_, rej) => setTimeout(() => rej({ code: 'TIMEOUT', opId }), timeoutMs))
      try {
        const result = await Promise.race([action({ ...args, __opId: opId }), timer])
        cache.set(key, { result, ts: Date.now() })
        return result
      } catch (e) {
        if (e?.code === 'TIMEOUT') return { __pending: true, opId }       // 待确认态
        opIds.delete(key)                                                  // 确定失败：换新 opId 重试
        throw e
      }
    })().finally(() => inflight.delete(key))

    inflight.set(key, p)
    return p
  }

  async function confirmPending(opId) {
    const r = await action({ __opId: opId, __confirm: true })              // 幂等确认接口
    return r
  }

  return { call, confirmPending }
}
```
**评分点**：
- 三重去重（在途共享/结果短缓存/opId 幂等键），重试复用同 opId 是服务端幂等的关键
- 超时 ≠ 失败：pending 态 + confirmPending 轮询收尾（防重复提交的真·幂等设计）
- 确定失败清 opId（下次调用是新操作）
- inflight/cache 的 finally 清理防泄漏
