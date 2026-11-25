---
title: [HW-202] 手写交互热力采集——按元素位置聚合交互延迟（x/y 网格化 + 热力图数据结构）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-202：手写交互热力采集——按元素位置聚合交互延迟（x/y 网格化 + 热力图数据结构）
**答**：交互热力图（哪个屏幕区域交互慢）：Event Timing 的 target 元素取 rect 中心 → 网格化（视口 8×8 桶）→ 桶内聚合 p75 duration 与样本数 → 上报桶矩阵（小 payload）→ 看板渲染热力图叠加页面。

```javascript
const GRID = 8;
const heat = new Map();                                  // "cx,cy" -> { total, count, max }
new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (e.interactionId == null || e.duration < 200) continue;
    const r = e.target?.getBoundingClientRect();
    if (!r) continue;
    const cx = Math.min(GRID - 1, Math.floor((r.left + r.width / 2) / (innerWidth / GRID)));
    const cy = Math.min(GRID - 1, Math.floor((r.top + r.height / 2) / (innerHeight / GRID)));
    const k = `${cx},${cy}`;
    const h = heat.get(k) ?? { total: 0, count: 0, max: 0 };
    h.total += e.duration; h.count++; h.max = Math.max(h.max, Math.round(e.duration));
    heat.set(k, h);
  }
}).observe({ type: 'event', durationThreshold: 200, buffered: true });
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState !== 'hidden') return;
  const cells = [...heat].map(([k, h]) => ({ k, p75: Math.round(h.total / h.count), count: h.count, max: h.max }));
  report({ type: 'interaction-heat', viewport: `${innerWidth}x${innerHeight}`, grid: GRID, cells });
  heat.clear();
});
// 桶矩阵 payload：64 个桶 × ~30B ≈ 2KB（对比逐样本上报省 90%+）
// 看板：热力图叠加截图 —— "右下角客服按钮区域交互 p75 480ms"一眼可见
// 判读价值：位置模式聚类的根因（某区域 = 某组件/某三方挂件的领地）
```

**评分点**：
- rect 中心网格化（8×8 桶）聚合 p75——本题核心。
- 桶矩阵 payload 的体积意识（2KB vs 逐样本）。
- viewport 尺寸随报（不同分辨率网格不可比）。
- 位置聚类到组件/三方领地的归因价值。
