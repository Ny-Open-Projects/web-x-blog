---
title: [WCN-875] 笔试：手写「编译产物体积 diff」可视化数据生成器（劣化告警）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-875：笔试：手写「编译产物体积 diff」可视化数据生成器（劣化告警）

**题目**：实现 `bundleDiff(before, after, { threshold = 0.05, topN = 5 })`，比较两次构建产物。输入为文件数组 `[{ path, size }]`（size 为字节数）。要求：① 按 path 配对，计算每个文件 `delta = after.size - before.size` 与 `pct = delta / before.size`（before 无该文件时 pct=1）；② 找出「新增文件」（after 有 before 无）与「删除文件」（before 有 after 无）；③ 总大小变化 totalDelta 与 totalPct；④ `alerts`：某文件增幅超过 threshold（默认 5%）或出现新增大文件（>10KB）时生成告警字符串；⑤ `top`：取增幅绝对值最大的 topN 个文件（含 delta/pct），按 delta 降序。边界：before.size=0 时 pct 特殊处理（新增视为 1，删除视为 -1）；空数组；结果要可视化友好（数字保留合适精度）。

**答**：

```javascript
function bundleDiff(before, after, { threshold = 0.05, topN = 5 } = {}) {
  const bMap = new Map(before.map(f => [f.path, f.size]));
  const aMap = new Map(after.map(f => [f.path, f.size]));
  const paths = new Set([...bMap.keys(), ...aMap.keys()]);
  const files = [], alerts = [];
  const added = [], removed = [];
  for (const p of paths) {
    const b = bMap.get(p), a = aMap.get(p);
    if (a === undefined) { removed.push(p); continue; }
    if (b === undefined) {
      added.push({ path: p, size: a });
      if (a > 10240) alerts.push(`新增大文件 ${p} (${(a / 1024).toFixed(1)}KB)`);
      files.push({ path: p, delta: a, pct: 1 }); continue;
    }
    const delta = a - b;
    const pct = b === 0 ? (delta > 0 ? 1 : delta < 0 ? -1 : 0) : delta / b;
    if (pct > threshold) alerts.push(`${p} 体积增长 ${(pct * 100).toFixed(1)}%`);
    files.push({ path: p, delta, pct: +pct.toFixed(4) });
  }
  const totalBefore = before.reduce((s, f) => s + f.size, 0);
  const totalAfter = after.reduce((s, f) => s + f.size, 0);
  const totalDelta = totalAfter - totalBefore;
  const totalPct = totalBefore ? +(totalDelta / totalBefore).toFixed(4) : 1;
  const top = files.sort((x, y) => y.delta - x.delta).slice(0, topN);
  return { added, removed, totalDelta, totalPct, alerts, top };
}
console.log(bundleDiff(
  [{ path: 'a.js', size: 1000 }, { path: 'old.js', size: 500 }],
  [{ path: 'a.js', size: 1400 }, { path: 'new.js', size: 20000 }],
));
```

**评分点**：
- 按 path 配对计算 delta/pct，正确识别新增/删除（数据正确性）。
- pct 分母为 0、新增/删除的特殊语义处理（边界）。
- 告警规则（增幅阈值 + 新增大文件）与 topN 增幅排序（业务价值：劣化告警）。
- 数值精度控制、可视化友好的输出结构（可用性）。
