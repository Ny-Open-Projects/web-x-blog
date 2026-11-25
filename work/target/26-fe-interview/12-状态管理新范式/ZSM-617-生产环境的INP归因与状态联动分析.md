---
title: [ZSM-617] 生产环境的 INP 归因：怎么把慢交互和状态变更连起来
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-617：生产环境的 INP 归因：怎么把慢交互和状态变更连起来

**答**：
- INP（Interaction to Next Paint）：衡量交互响应性——每次交互从输入到下一帧渲染完成的耗时，取 p75。状态库导致的慢交互是 INP 恶化的最大嫌疑之一，但生产环境没有 Profiler，只能靠「事件对齐」归因。
- 对齐方案：1) 捕获交互入口——`document.addEventListener('pointerdown/keydown', capture)` 打 `performance.mark('input')`；2) 状态变更探针——每次 setState 打 mark 并带 action 名；3) 用 PerformanceObserver 的 `longtask`/`event` entry 拿到交互的实际耗时与 attribution；4) 上报时把「交互 → 距离最近的 N 条状态变更 → longtask」关联成一条链路。
- 归因结论形态：「搜索交互 INP p75 = 480ms，期间触发 cartStore.set 12 次 + 过滤 selector 重算 200ms」——有了 action 名就能直接定位代码。
- 采样与成本：归因探针只在 INP 候选交互（耗时 > 200ms）时激活细粒度记录，平时只记粗粒度计数——保证监控本身不拖慢页面。
- 追问钩子：修完验证也是生产闭环——同一交互的 INP p75 前后对比 + RUM 分位数迁移（p75 → p95 全线改善才算真修复）。

```javascript
// INP 归因探针
const recentChanges = []   // 最近状态变更环形缓冲

function trackStateChange(name) {
  recentChanges.push({ ts: performance.now(), name })
  if (recentChanges.length > 50) recentChanges.shift()
}

// 交互入口
['pointerdown', 'keydown'].forEach((ev) =>
  document.addEventListener(ev, (e) => {
    performance.mark('interaction-start', { detail: { target: e.target.tagName } })
  }, { capture: true, passive: true }))

// longtask 归因
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration < 200) continue
    // 找 longtask 期间的状态变更
    const involved = recentChanges.filter(
      (c) => c.ts >= entry.startTime - 50 && c.ts <= entry.startTime + entry.duration + 50
    )
    report({
      type: 'inp-attribution',
      duration: entry.duration,
      ts: entry.startTime,
      stateChanges: involved.map((c) => c.name),
      attr: entry.attribution?.[0]?.name,   // longtask 归属（script/react 等）
    })
  }
}).observe({ type: 'longtask', buffered: true })

// INP 候选触发细粒度记录
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (e.interactionId && e.duration > 200) {
      enableFineProbe(5000)   // 接下来 5 秒开启 selector 细粒度计时
    }
  }
}).observe({ type: 'event', buffered: true, durationThreshold: 200 })
```
