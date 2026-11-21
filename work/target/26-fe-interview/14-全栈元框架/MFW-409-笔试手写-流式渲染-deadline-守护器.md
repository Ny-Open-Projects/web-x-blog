---
title: [MFW-409] 笔试：手写流式渲染 deadline 守护器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-409：deadline 守护器
**需求**：实现 `withRenderDeadline(renderFn, { totalMs = 3000, perDeps = {} })`：1) 总钟 + 每依赖子钟（AbortSignal.any 组合——MFW-361）；2) 超时段不炸整页——返回该段 fallback 数据并标记 degraded（页面完整、指标可信）；3) 剩余预算继承：子段超时消耗计入总钟（后续段预算 = total - elapsed）；4) 全部超时 → 快速失败（整页 504 + traceId——用户等 3s 得到错误好过 10s 白屏）；5) 观测每段 { ms, degraded }。

```javascript
export async function withDeadline(segments, { totalMs = 3000 } = {}) {
  const t0 = Date.now(), out = {}, degradedSegs = []
  const total = abortAtMs(totalMs)
  for (const [name, { fn, own, fallback, core }) of Object.entries(segments)) {
    const left = totalMs - (Date.now() - t0)
    if (left <= 0) { if (isCore) throw new TimeoutAllOut(traceId)      // 全超快速失败
      out[name] = fallback; degradedSegs.push(name); continue }
    try {
      out[name] = await fn(AbortSignal.any([ctl.signal, abortAtMs(Math.min(left, deps[name] ?? left)))))
    } catch { if (isCore(name)) throw new Error(`core ${name} timeout`)
      out[name] = fallback; degradedSegs.push(name) }
  }
  return { data: out, degraded: degradedSegs, took: Date.now() - t0 }
}
```
**评分点**：
- 核心/非核心分档（核心超时=整页失败；非核心=降级卡——可用性结构清晰）
- 剩余预算继承（后段用 total-elapsed——防尾部段各自满预算超总）
- 降级不静默（degraded 段进响应属性——可观测）
- 全超快速失败（3s 出错误好过 10s 白屏——体验经济学）
