---
title: [WCN-493] 笔试：实现元素库的月度 ROI 计算（节省人力 vs 投入）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-493：笔试：实现元素库的月度 ROI 计算（节省人力 vs 投入）。
**答**：输入：各框架消费节省工时（对比各自自研维护）表 + 平台投入工时。输出月度净收益与累计 ROI 曲线数据点。

```javascript
function roiCurve(monthly) {
  let cum = 0; const points = [];
  let breakeven = null;
  monthly.forEach((m, i) => {
    const net = m.savedHours - m.platformHours;
    cum += net;
    points.push({ month: i + 1, net, cum });
    if (cum > 0 && breakeven === null) breakeven = i + 1;
  });
  return { points, breakeven,
    verdict: breakeven ? `第 ${breakeven} 个月回本` : '尚未回本' };
}
console.log(roiCurve([
  { savedHours: 10, platformHours: 40 }, { savedHours: 30, platformHours: 30 },
  { savedHours: 60, platformHours: 20 },
])); // breakeven 3

```

**评分点**：
- 节省 = Σ(框架自研维护工时 - 消费接入工时)。
- 净收益 = 节省 - 平台投入。
- 累计 ROI 序列（曲线数据）。
- 回本月标注（净收益首次转正）。
