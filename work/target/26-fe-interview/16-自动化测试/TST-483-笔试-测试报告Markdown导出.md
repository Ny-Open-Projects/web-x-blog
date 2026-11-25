---
title: [TST-483] 笔试：测试结果导出为可读 Markdown 周报。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-483：笔试：测试结果导出为可读 Markdown 周报。
**答**：输入本周多次运行统计 `[{date, total, failed, flaky}]`。输出：趋势表、环比变化（失败数）、flaky 榜 top3、一句话结论（失败率上升/下降/平稳，±20% 阈值）。

```javascript
function weeklyReport(runs, flakyByTest) {
  const first = runs[0], last = runs[runs.length - 1];
  const delta = first.failed ? (last.failed - first.failed) / first.failed : 0;
  const trend = delta > 0.2 ? '失败率上升' : delta < -0.2 ? '失败率下降' : '平稳';
  const top3 = Object.entries(flakyByTest).sort((a, b) => b[1] - a[1]).slice(0, 3);
  return {
    table: runs.map(r => `| ${r.date} | ${r.total} | ${r.failed} | ${r.flaky} |`).join('\n'),
    trend, top3: top3.map(([n, c]) => `${n}(${c}次)`),
  };
}

```

**评分点**：
- 趋势表渲染（日期行）。
- 环比计算（首尾对比）。
- flaky 榜聚合排序。
- 结论阈值判定（±20%）。
