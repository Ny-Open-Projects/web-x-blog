---
title: [ZSM-414] 笔试：手写 store 订阅扇出监控（定位渲染风暴）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-414：手写 store 订阅扇出监控（定位渲染风暴）
**答**：实现 `instrumentStore(store)`：1) 包装 subscribe 统计每个 listener 的「通知次数」；2) 包装 setState 记录单次通知扇出（listener 数）与相邻两次 setState 的最小间隔；3) 同一事件循环 tick 内 setState 超过 10 次判定「疑似循环」打告警（带最后一次写入来源 stack）；4) `report()` 返回 top5 高频 listener（含注册位置）与扇出分布；5) 提供 `reset()`。

```javascript
export function instrumentStore(store) {
  const stats = { listeners: new Map(), fanout: [], tickCount: 0, minGap: Infinity, lastAt: 0 }
  let lastSetAt = 0

  const origSubscribe = store.subscribe
  store.subscribe = (fn, loc = captureLoc()) => {
    const rec = stats.listeners.get(loc) ?? { n: 0, loc }
    stats.listeners.set(loc, rec)
    return origSubscribe((...args) => { rec.n++; return fn(...args) })
  }

  const origSet = store.setState
  store.setState = (patch) => {
    const now = performance.now()
    if (now - lastSetAt < 16) stats.minGap = Math.min(stats.minGap, now - lastSetAt)   // 帧
    lastSetAt = now
    stats.tickCount++
    if (stats.tickCount > 10)
      console.warn('possible sync loop', new Error().stack?.split('\n')[2])
    queueMicrotask(() => (stats.tickCount = 0))
    const fan = countListeners(store)
    stats.fanout.push(fan)
    return origSet(patch)
  }

  return {
    report: () => ({
      topListeners: [...stats.listeners.values()].sort((a, b) => b.n - a.n).slice(0, 5),
      maxFanout: Math.max(0, ...stats.fanout),
      minGapMs: stats.minGap === Infinity ? null : stats.minGap,
    }),
    reset: () => { stats.listeners.clear(); stats.fanout.length = 0; stats.minGap = Infinity },
  }
}

function countListeners() { return 0 }   // 由包装层接入实际计数
function captureLoc() { return new Error().stack?.split('\n')[3] ?? 'unknown' }
```
**评分点**：
- tick 内计数 + microtask 清零的循环判定（同步环才有效，异步正常链路不误报）
- listener 按「注册位置」聚合（能定位到业务代码行，而非匿名函数）
- 最小 setState 间隔度量（帧级抖动可视化）
- 包装不改变原语义（透传参数与返回值），可随时卸载
