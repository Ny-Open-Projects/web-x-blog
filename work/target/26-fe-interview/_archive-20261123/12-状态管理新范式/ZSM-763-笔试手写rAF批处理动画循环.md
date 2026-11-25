---
title: [ZSM-763] 笔试：手写 rAF 批处理动画循环（读写分离 + 帧预算监控 + 里程碑回调）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-763：手写 rAF 批处理动画循环（读写分离 + 帧预算监控 + 里程碑回调）
**需求**：实现 `createFrameLoop({ budgetMs })`：1) `read(el, fn)` / `write(el, fn)`：帧内先批量执行全部 read（单次 layout）再批量 write；2) 帧耗时监控：单帧 > budgetMs 告警（回调 onSlowFrame）并计数；3) `milestone(name, fn)`：里程碑任务——执行一次进 store（触发渲染），帧循环内标记去重；4) `stop()`；5) 附用例：读写在帧内分离执行、慢帧告警、里程碑去重。

```javascript
function createFrameLoop({ budgetMs = 8, onSlowFrame } = {}) {
  const reads = []
  const writes = []
  const milestones = new Map()     // name -> fn（标记去重）
  let raf = null
  let running = false
  let slowFrames = 0

  function read(el, fn) { reads.push({ el, fn }) }
  function write(el, fn) { writes.push({ el, fn }) }

  function milestone(name, fn) {
    milestones.set(name, fn)        // 每帧执行一次后清除
  }

  function tick() {
    if (!running) return
    const t0 = performance.now()
    // 1) 批量读：一次 layout
    const readResults = reads.map(({ el, fn }) => fn(el))
    reads.length = 0
    // 2) 批量写：一次 layout（读写分离避免 thrashing）
    writes.forEach(({ el, fn }, i) => fn(el, readResults[i]))
    writes.length = 0
    // 3) 里程碑：执行并清除（去重语义）
    for (const [name, fn] of milestones) {
      try { fn() } catch (e) { console.error('[milestone]', name, e) }
    }
    milestones.clear()
    // 4) 帧预算监控
    const frameMs = performance.now() - t0
    if (frameMs > budgetMs) {
      slowFrames++
      onSlowFrame?.(frameMs, slowFrames)
    }
    raf = requestAnimationFrame(tick)
  }

  function start() {
    if (running) return
    running = true
    raf = requestAnimationFrame(tick)
  }

  function stop() {
    running = false
    cancelAnimationFrame(raf)
  }

  return { read, write, milestone, start, stop, stats: () => ({ slowFrames, pendingReads: reads.length, pendingWrites: writes.length }) }
}

// 用例（jsdom 环境 mock rAF）
let rafQueue = []
globalThis.requestAnimationFrame = (fn) => { rafQueue.push(fn); return rafQueue.length }
globalThis.cancelAnimationFrame = () => { rafQueue = [] }

const slowEvents = []
const loop = createFrameLoop({ budgetMs: 0.01, onSlowFrame: (ms, n) => slowEvents.push({ ms, n }) })
loop.start()

// 读写分离：同帧内 read 先于 write
const ops = []
loop.read({}, () => ops.push('read1'))
loop.write({}, () => ops.push('write1'))
loop.read({}, () => ops.push('read2'))
loop.write({}, () => ops.push('write2'))

// 里程碑：进 store
let milestoneRuns = 0
loop.milestone('settle', () => { milestoneRuns++; useDrag.getState().settle({ x: 100 }) })

// 模拟两帧
rafQueue.splice(0).forEach((fn) => fn())
console.log(ops)                      // ['read1','read2','write1','write2']：读写分离
console.log(milestoneRuns)            // 1：里程碑执行一次
rafQueue.splice(0).forEach((fn) => fn())
console.log(milestoneRuns)            // 仍 1：去重（已清除）
console.log(loop.stats().slowFrames > 0)   // true：慢帧告警计数
loop.stop()
```
**评分点**：
- 读写分离（帧内全部 read 后全部 write，防 layout thrashing）
- 帧预算监控（慢帧计数 + 回调）
- 里程碑去重（Map 清除语义，动画结束只进一次 store）
- stop 清理（rAF 取消）
