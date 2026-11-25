---
title: [SCN-1165] SCADA 大屏的 SPC 统计过程控制（控制图）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1165：SCADA 大屏的 SPC 统计过程控制（控制图）

**答**：
- 控制图：X-bar/R 图（均值+极差），UCL/LCL 控制限（±3σ），超限/连串判异。
- 判异：Western Electric 规则（连续 7 点同侧/趋势）自动判异标注。
- 处置：判异触发质量异常处置流程。

```javascript
// SPC 控制图
function spcChart(samples, { subgroup = 5 } = {}) {
  const means = chunkMeans(samples, subgroup);
  const cl = avg(means);
  const r = avg(ranges(samples, subgroup));
  const ucl = cl + 2.66 * r, lcl = cl - 2.66 * r;
  return { cl, ucl, lcl,
    violations: westernElectric(means, cl, ucl, lcl),  // 判异规则
  };
}
function chunkMeans(s, n) { const out = []; for (let i = 0; i < s.length; i += n) out.push(avg(s.slice(i, i + n))); return out; }
function ranges(s, n) { const out = []; for (let i = 0; i < s.length; i += n) out.push(Math.max(...s.slice(i, i + n)) - Math.min(...s.slice(i, i + n))); return out; }
function avg(a) { return a.reduce((x, v) => x + v, 0) / (a.length || 1); }
function westernElectric(m, cl, ucl, lcl) {
  const out = [];
  for (let i = 6; i < m.length; i++) {
    const win = m.slice(i - 6, i + 1);
    if (win.every(v => v > cl)) out.push({ at: i, rule: '连续 7 点同侧' });
  }
  return out;
}
```
