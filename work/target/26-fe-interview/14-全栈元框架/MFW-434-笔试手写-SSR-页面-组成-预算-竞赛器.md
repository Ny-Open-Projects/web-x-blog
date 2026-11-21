---
title: [MFM-434→MFW-434] 笔试：手写组合页预算竞赛器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFM→MFW-434：预算竞赛
**需求**：实现 `raceSegments(specs, { pageMs = 800 } = {})`（MFW-326/382 合一执行器）：1) 段声明 {name, fn, tier: 'core'|'boost'|'fill', ownMs}；2) 全局页预算分配：core 保底（pageMs×0.6 按数均分），boost 竞速剩余（先到先得——量入为出），fill 只用 idle（全部完成后仍剩预算才跑）；3) 每段结果三态 { data | fallback, usedMs, aborted }；4) 总钟到 → 未完成 boost/fill 全弃（页面准时出货——部分数据好于迟到整页）；5) 决策可解释输出（哪个段被谁挤掉——预算链审计）。

```javascript
export async function raceSpecs(specs, { pageMs = 800 } = {}) {
  const t0 = now(), out = {}, ledger = []
  const core = specs.filter(s => s.tier === 'core')
  const coreEach = Math.floor((pageMs * 0.6) / Math.max(core.length, 1))
  await Promise.allSettled(core.map((s) => bound(s, Math.min(s.ownMs, coreEach), out, ledger)))
  const left = pageMs - (now() - t0)
  await Promise.allSettled(boosts.map((s, i) =>           // boost 竞速剩余
    s.until = min(s.ownMs, left - reservedForAfter(i, boosts))))
  if (pageLeft() > 50) await Promise.allSettled(fill.map(s => bound(s, pageLeft(), ...)))  // idle 才跑
  return { out, ledger, onTime: now() - t0 <= pageMs + 50 }
}
function bound(s, ms, out, ledger) {
  const t0 = now()
  return Promise.race([s.fn(), at(ms, () => { throw 'budget' )])
    .catch(() => { ledger.push({ seg: s.name, cutBy: 'budget', atMs: ms }); return s.fallback?.() })
    .then((v) => { ledger.push({ seg: s.name, ms: now() - t0 }); out[s.name] = v })
}
```
**评分点**：
- 三档预算分配公式（core 均分保底/boost 竞速/fill 只用 idle——确定性与弹性兼得）
- 总钟硬截止（部分数据准时出货——整页 P95 可承诺）
- ledger 审计（谁被谁挤掉——预算链可解释，调参有据）
