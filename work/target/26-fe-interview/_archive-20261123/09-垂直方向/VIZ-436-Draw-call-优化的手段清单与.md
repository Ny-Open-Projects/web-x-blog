---
title: [VIZ-436] Draw call 优化的手段清单与收益量级
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-436：Draw call 优化的手段清单与收益量级

**答**：
- 手段排序：实例化（358 万倍级）> 批处理合批（静态几何合并）> 纹理图集减少状态切换 > 多线程提交（WebGPU/worker）。
- 量级参考：桌面 3000 draw = 8ms CPU；合批到 300 = 1ms。
- 底线：先看 draw 数（Spector/自统计），超过 1000 再动手，避免过早优化。

```javascript
// draw 统计与合批判定
function drawAudit(draws) {
  const byGeo = {};
  for (const d of draws)
    byGeo[d.geoId] = (byGeo[d.geoId] ?? 0) + 1;
  const instancedCandidates = Object.entries(byGeo)
    .filter(([geo, n]) => n > 20).map(([geo, n]) => ({ geo, count: n }));
  return { total: draws.length,
    instancedCandidates,                                    // 优先实例化
    overThreshold: draws.length > 1000 };
}
```
