---
title: [AIC-746] AI 质量工程的可观测性需要采集哪些信号
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-746：AI 质量工程的可观测性需要采集哪些信号

**答**：
- 结论先行：AI 质量可观测性 = 把「生成→审查→上线→回滚」全链路的质量数据采出来，核心信号分四类：输入（prompt/上下文）、过程（重试/降级/耗时）、输出（质量分/采纳/返工）、结果（逃逸/回滚/SLA）。
- 采集要点：每条 AI 产出关联唯一 traceId，贯穿生成与后续事故；采样要覆盖「被拒的建议」而非只看采纳的（否则有幸存者偏差）。
- 用途：定位质量退化（哪个模型/哪类任务）、成本核算、事故归因；没有 traceId 就无法把线上 bug 关联回当时的生成上下文。
- 追问钩子：为什么必须采集「被拒绝的 AI 建议」？——只看采纳的会产生幸存者偏差，无法知道 AI 在哪里频繁出错，也就无法改进 prompt。

```javascript
// 质量可观测性：全链路 trace
function track(traceId, stage, data) {
  return { traceId, stage, ts: Date.now(), ...data };
}
const tid = 'tr-001';
const events = [
  track(tid, 'generate', { model: 'A', tokens: 500 }),
  track(tid, 'review', { decision: 'reject', reason: '缺边界' }), // 被拒建议也要采
  track(tid, 'regenerate', { model: 'B', tokens: 700 }),
  track(tid, 'accept', { quality: 0.9 }),
];
console.log(events.filter(e => e.decision === 'reject').length); // 1 → 改进线索
console.log(new Set(events.map(e => e.traceId)).size === 1);    // 全链路同一 trace
```
