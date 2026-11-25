---
title: [ZSM-570] 用 Chrome Performance 面板定位「状态驱动的卡顿」的完整路径
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-570：用 Chrome Performance 面板定位「状态驱动的卡顿」的完整路径

**答**：
- 路径五步：1) 录制用户操作轨迹（Performance 面板 + 开启 Screenshots），找长任务（Main > 50ms 的红色块）和 FPS 谷底；2) 展开长任务看调用栈，确认耗时落在 React commit（commitRoot）还是用户 setState 回调；3) React 侧：勾选 React Developer Tools 的 Profiler trace（「Record why each component rendered」），重叠时间段分析重渲次数；4) 状态侧：对照状态 tracer 日志，把 setState 时间点与长任务对齐——通常发现「一次交互触发了 N 个 store 的连环 set」；5) 归因输出：哪个 action、改了什么字段、触发多少组件、单次提交耗时。
- 常见结论模式：`setState → selector 重算 → 通知 → 渲染` 的链路里，时间大头一般在渲染，但「通知风暴」（一个 set 触发几百个 listener）和「selector 全量重算」也常见——Performance 面板里看 `store.subscribe` 或 selector 函数的自用时间。
- 对齐技巧：tracer 日志用 `performance.now()` 与 Performance 面板同一时间基线；给关键 action 打 `performance.mark(actionName)`，火焰图上直接可见命名标记。
- 验证修复：同一轨迹重录对比「长任务数量与总阻塞时长」（TBT 口径），不要只看 FPS 观感。
- 追问钩子：INP（Interaction to Next Paint）是生产侧的对应指标——每次交互最慢的渲染帧，状态优化最终要落在 INP 改善上。

```javascript
// 用 performance API 给状态变更打标记（与 Performance 面板联动）
function instrumentWithMarks(storeApi, actionNames) {
  const origSet = storeApi.setState
  storeApi.setState = (updater, replace, name) => {
    const mark = `state:${name ?? 'anonymous'}`
    performance.mark(mark)
    const t0 = performance.now()
    origSet(updater, replace, name)
    performance.measure(mark, mark)   // 火焰图上的 User Timing 区块
    // 长变更打 warning
    const dur = performance.now() - t0
    if (dur > 16) console.warn(`[perf] ${mark} took ${dur.toFixed(1)}ms`)
  }
}

// 录制后用 JS 解析 performance entries（自动化对比）
const measures = performance.getEntriesByType('measure')
  .filter((m) => m.name.startsWith('state:'))
  .map((m) => ({ name: m.name, duration: m.duration }))
const slowest = measures.sort((a, b) => b.duration - a.duration)[0]
console.log('最慢的状态变更:', slowest)
```
