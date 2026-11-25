---
title: [WCN-547] Signals 的「可观察调试」：如何用 Effect 日志与依赖时间戳定位「为什么这个 effect 又跑了」？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-547：Signals 的「可观察调试」：如何用 Effect 日志与依赖时间戳定位「为什么这个 effect 又跑了」？

**答**：
- 结论：给每次写打时间戳与来源标签，effect 重跑时记录「触发链」——哪个写 → 哪些 computed 标脏 → 本 effect。
- 依赖时间戳：computed 记录自身与依赖的最后变更时间，effect 比较后可知是哪个依赖变晚。
- 日志环形缓冲保留最近 N 条，避免内存无限增长。
- 追问：生产问题如何复现？（答：开启采样日志上报 + 用同一序列重放）

```javascript
const LOG = []; const MAX = 200;
function logWrite(sig, value, at = performance.now(), src = 'user') {
  LOG.push({ type: 'write', sig: sig.name, value, at, src });
  if (LOG.length > MAX) LOG.shift();
}
function logEffect(effect, dirtyDeps) {
  LOG.push({ type: 'effect', name: effect.name, at: performance.now(),
    cause: dirtyDeps.map(d => ({ name: d.name, lastChange: d.lastChange })) });
}
function explain(effectName) { return LOG.filter(l => l.name === effectName || l.type === 'write').slice(-20); }
```
