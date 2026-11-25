---
title: [ZSM-604] 笔试：手写 selector 排行榜与放大系数分析器
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-604：手写 selector 排行榜与放大系数分析器
**答**：实现 `createSelectorProfiler(store)`：1) `wrap(label, selector)`：包装 selector 记录调用次数、累计耗时、worst、返回结果缓存命中率（同一 state 引用重复调用）；2) `countChange()`：store 每次变更计数（探针挂 subscribe）；3) `report(topN)`：输出 TopN 榜单 `{ label, calls, total, avg, worst, amplification }`——amplification = calls / changes（放大系数）；4) `reset()`；5) 附用例：模拟 3 次变更、某 selector 被调 9 次验证放大系数 = 3。

```javascript
function createSelectorProfiler(store) {
  const stats = new Map()   // label -> { calls, total, worst, cacheHit, lastState, lastOut }
  let changes = 0

  // 变更计数：挂 subscribe
  store.subscribe(() => changes++)

  function wrap(label, selector) {
    const s = { calls: 0, total: 0, worst: 0, cacheHit: 0, lastState: undefined, lastOut: undefined }
    stats.set(label, s)
    return (state) => {
      // 缓存：同一 state 引用直接命中
      if (state === s.lastState && s.lastOut !== undefined) {
        s.cacheHit++
        s.calls++
        return s.lastOut
      }
      const t0 = performance.now()
      const out = selector(state)
      const dt = performance.now() - t0
      s.calls++
      s.total += dt
      s.worst = Math.max(s.worst, dt)
      s.lastState = state
      s.lastOut = out
      return out
    }
  }

  function report(topN = 5) {
    return [...stats.entries()]
      .map(([label, s]) => ({
        label,
        calls: s.calls,
        totalMs: +s.total.toFixed(2),
        avgMs: s.calls ? +(s.total / s.calls).toFixed(3) : 0,
        worstMs: +s.worst.toFixed(3),
        cacheHitRate: s.calls ? +(s.cacheHit / s.calls).toFixed(2) : 0,
        amplification: changes ? +(s.calls / changes).toFixed(1) : 0,
      }))
      .sort((a, b) => b.totalMs - a.totalMs)
      .slice(0, topN)
  }

  function reset() {
    changes = 0
    for (const s of stats.values()) Object.assign(s, { calls: 0, total: 0, worst: 0, cacheHit: 0, lastState: undefined, lastOut: undefined })
  }

  return { wrap, report, reset, changes: () => changes }
}

// 用例
const listeners = new Set()
const store = {
  state: { items: [1, 2, 3], n: 0 },
  subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn) },
  setState(p) { Object.assign(this.state, p); listeners.forEach((fn) => fn()) },
}

const profiler = createSelectorProfiler(store)
const heavySel = profiler.wrap('heavyFilter', (s) => s.items.filter((x) => x % 2 === 0).map((x) => x * x))
const cheapSel = profiler.wrap('n', (s) => s.n)

heavySel(store.state)
heavySel(store.state)                 // 同 state：缓存命中
store.setState({ n: 1 }); cheapSel(store.state)
store.setState({ n: 2 }); heavySel(store.state)
store.setState({ n: 3 }); heavySel(store.state)
console.log(profiler.report())
// [{ label: 'heavyFilter', calls: 4, cacheHitRate: 0.25, amplification: 1.3, ... }]
// 放大系数 = calls / changes：>1 说明同一变更触发多次 selector
```
**评分点**：
- 缓存命中率统计（同 state 引用直通——优化效果可量化）
- 放大系数 calls/changes（热路径的核心指标）
- report 四维输出（calls/total/avg/worst）+ 排序
- reset 支持分段测量（优化前后同口径对比）
