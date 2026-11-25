---
title: [AIC-470] 笔试：实现 flaky 用例隔离区管理（自动进出）。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-470：笔试：实现 flaky 用例隔离区管理（自动进出）。
**答**：状态 `tests: {id: {results: boolean[], quarantined}}`。隔离条件：最近 10 次中出现 ≥ 2 次失败且非连续通过；回归条件：隔离后连续 20 次通过自动解除。实现 `record(id, passed)` 与 `status(id)`。

```javascript
function makeQuarantine() {
  const tests = new Map();
  return {
    record(id, passed) {
      const t = tests.get(id) ?? { results: [], quarantined: false, greenStreak: 0 };
      if (t.quarantined) {
        t.greenStreak = passed ? t.greenStreak + 1 : 0;
        if (t.greenStreak >= 20) { t.quarantined = false; t.results = []; t.greenStreak = 0; }
      } else {
        t.results.push(passed);
        if (t.results.length > 10) t.results.shift();
        const fails = t.results.filter(x => !x).length;
        if (t.results.length === 10 && fails >= 2) t.quarantined = true;
      }
      tests.set(id, t);
    },
    status(id) {
      const t = tests.get(id);
      if (!t) return { quarantined: false, failRate: 0 };
      const win = t.results.slice(-20);
      return { quarantined: t.quarantined,
        failRate: win.length ? +(win.filter(x => !x).length / win.length).toFixed(2) : 0 };
    },
  };
}
const q = makeQuarantine();
for (let i = 0; i < 8; i++) q.record('t', true);
q.record('t', false); q.record('t', false);
console.log(q.status('t').quarantined); // true（10 次内 2 败）

```

**评分点**：
- 隔离判定用最近 10 次窗口统计失败次数。
- 回归计数从隔离时点起算（连续通过计数器）。
- 解除后历史窗口重置（防旧数据反复触发隔离）。
- status 返回 {quarantined, failRate20}。
