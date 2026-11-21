---
title: [MFW-420] 笔试：手写 ISR 再生成 Worker
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-420：ISR Worker
**需求**：实现 `createRegenWorker(store, render, { concurrency = 3 } = {})`：1) 队列消费：失效事件（tag/key）→ 去重合并 → 并发 ≤3 再生成；2) 单飞跨请求（同 key 在途共享——后续失效登记 dirty 不重复排队，完成后检查 dirty 决定是否再排一轮——不丢最末变更）；3) 失败保留旧页（渲染异常→不上架新产物——旧版继续服务+告警计数）；4) 写入原子（临时 key+rename——RBL-344）；5) 观测 { queueLen, inFlight, failStreak }（连续失败 ≥3 熔断该域——防坏数据源打爆循环）。

```javascript
export function createRegenWorker({ store, renderOne, { conc = 3, failCap = 3 } = {}) {
  const q = new Set(), inflight = new Map(), dirty = new Map()
  let failures = 0

  function invalidate(key) {
    if (inflight.has(key)) { dirty.set(key, true); return }       // 在途：记最末变更
    if (q.has(key)) return
    q.add(key); pump()
  }
  async function pump() {
    while (inflight.size < conc && q.size) {
      const key = firstOf(q); q.delete(key)
      const p = (async () => {
        try {
          const html = await renderOne(key)
          await putAtomic(store, key, html)                       // tmp+rename
          failures = 0
        } catch (e) {
          if (++failures >= failCap) circuitOpen(domainOf(key))   // 域级熔断
          report('isr.fail', { key, n: failures })                // 旧页保留：不写=仍服务
        } finally {
          inflight.delete(key)
          if (dirty.get(key)) { dirty.delete(key); thisModule.(key) }   // 追最末变更
          pump()
        }
      })()
      inflight.set(key, p)
    }
  }
  return { invalidate, stats: () => ({ q: q.size, run: inflight.size, failStreak: failures }) }
}
```
**评分点**：
- 在途 dirty 追踪（完成后再排一轮——合并窗口内的最末变更不丢）
- 失败保留旧页（不上架坏产物——ISR 可用性优先语义）+ 域级熔断（坏源打爆循环防护）
- 原子上架（tmp+rename——读方永远见完整页）
- 去重队列（同 key 多次失效一次成本）
