---
title: [AGT-697] 手写 quarantine：方差检测、观察区隔离、恢复判定、关键用例确定性化？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-697：手写 quarantine：方差检测、观察区隔离、恢复判定、关键用例确定性化

**需求与边界**：
- 实现 flakyGuard(history)：history 为用例近 N 次判定序列。
- 边界要求：① 方差/翻转率超阈值标 flaky 并隔离到观察区（不阻断门禁）；② 隔离期间仍跑但不计分；③ 连续 M 次稳定后恢复；④ critical 用例 flaky 时不隔离而是强制确定性化（温度0+规则判定），做不到则降级判据。

**答**：
```javascript
function flipRate(verdicts) {
  let flips = 0;
  for (let i = 1; i < verdicts.length; i++)
    if (verdicts[i] !== verdicts[i - 1]) flips++;
  return flips / (verdicts.length - 1 || 1);
}
function flakyGuard(item, { flipThresh = 0.3, stableN = 5 } = {}) {
  const fr = flipRate(item.recentVerdicts);
  if (fr <= flipThresh) return { state: item.state };
  if (item.critical) {                             // 关键用例特殊处理
    const det = determinizable(item);
    return det ? { state: 'active', action: 'determinize',
      patch: { temperature: 0, judge: 'rules' } }
      : { state: 'active', action: 'relax-rubric',
        note: '关键用例不允许隔离，降级到可确定性判据' };
  }
  return { state: 'quarantined',                   // 普通：隔离
    resume: `连续 ${stableN} 次稳定后恢复`,
    note: '隔离期间照跑但不计分不门禁' };
}
function resumeCheck(item, stableN = 5) {
  const last = item.recentVerdicts.slice(-stableN);
  return new Set(last).size === 1;                 // 连续一致才恢复
}
```

**评分点**:
- 翻转率量化 flaky；隔离语义正确（照跑不计分不门禁）。
- critical 用例不隔离而是确定性化/降级判据（安全门禁不失守）。
- 恢复条件明确（连续稳定 N 次）。

