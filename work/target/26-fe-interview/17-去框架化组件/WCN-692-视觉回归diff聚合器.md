---
title: [WCN-692] 笔试：实现视觉回归截图的 diff 聚合器（多基线对比 + 差异分级 + 忽略区域 + 报告生成）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-692：笔试：实现视觉回归截图的 diff 聚合器（多基线对比 + 差异分级 + 忽略区域 + 报告生成）

**答**：
- 需求：实现 aggregateDiff(cases)：cases 是 {name, baseline, current}[], 每项是像素数组；计算差异率并按级别（critical/major/minor）分类；支持 ignoreRegions；输出汇总报告与失败项。
- 思路：逐 case 比对（容差 + 忽略区域）；差异率阈值分级；critical 直接失败；生成按级别排序的报告。
- 边界：baseline 缺失标记为 new；长度不一致按差异处理；空数组返回通过。

```javascript
export function aggregateDiff(cases, opts = {}) {
  const { tolerance = 0.02, thresholds = { major: 0.05, critical: 0.2 } } = opts;
  const report = [];
  for (const c of cases) {
    if (!c.baseline) { report.push({ name: c.name, level: 'new' }); continue; }
    const a = c.baseline, b = c.current || [];
    const len = Math.max(a.length, b.length);
    let changed = 0;
    for (let i = 0; i < len; i++) {
      if (c.ignoreRegions?.some(r => i >= r[0] && i < r[1])) continue;
      if (Math.abs((a[i] ?? 0) - (b[i] ?? 0)) / 255 > tolerance) changed++;
    }
    const ratio = len ? changed / len : 0;
    const level = ratio >= thresholds.critical ? 'critical'
      : ratio >= thresholds.major ? 'major'
      : ratio > 0 ? 'minor' : 'pass';
    report.push({ name: c.name, ratio: +ratio.toFixed(3), level });
  }
  const order = { critical: 0, major: 1, minor: 2, new: 3, pass: 4 };
  report.sort((x, y) => order[x.level] - order[y.level]);
  return { report, failed: report.filter(r =>
    ['critical', 'major', 'new'].includes(r.level)).map(r => r.name) };
}
console.log(aggregateDiff([
  { name: 'Button', baseline: [1, 1, 1, 1], current: [1, 9, 1, 1] },
]));
```

**评分点**：
- 逐 case 比对含容差与忽略区域（ignoreRegions）。
- 差异按阈值分级 critical/major/minor（分级合理）。
- baseline 缺失标记 new，长度不一致按差异处理（边界完整）。
- 输出按严重度排序的报告与失败清单（便于 CI 门禁）。
