---
title: [MFW-721] 笔试：手写 TTI 分解分析器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-721：笔试：手写 TTI 分解

**答**：实现 `ttiBreakdown(metrics, { bandwidthKbps })`。metrics: `{ ttfbMs, htmlKB, jsKB, hydrationMs, deviceMultiplier? }`. 规则：1) 分解：ttfb（服务端）+ htmlTransfer（htmlKB × 8 / bandwidth × deviceMultiplier）+ jsDownload（jsKB × 8 / bandwidth × multiplier）+ hydration（hydrationMs × multiplier——设备算力影响水合时长）；2) total = 各段之和；3) 瓶颈识别：最大段 → bottleneck（每段的优化策略映射：TTFB → SSR/缓存；JS → code split；hydration → 优先级调度）；4) 返回 `{ breakdown: Record<segment, ms>, total, bottleneck, suggestion }`。边界：metrics 空（no-data）；bandwidth 极低（传输主导）；hydrationMs=0（纯静态——无水合段）。

```javascript
function ttiBreakdown(metrics = {}, { bandwidthKbps = 10000 } = {}) {
  if (!metrics.ttfbMs && !metrics.jsKB)
    return { noData: true, breakdown: {}, total: 0, bottleneck: null, suggestion: null };
  const mult = metrics.deviceMultiplier ?? 1;
  const transfer = (kb) => +(kb * 8 / bandwidthKbps * 1000 * mult).toFixed(0);
  const breakdown = {
    ttfb: metrics.ttfbMs ?? 0,
    htmlTransfer: transfer(metrics.htmlKB ?? 0),
    jsDownload: transfer(metrics.jsKB ?? 0),
    hydration: Math.round((metrics.hydrationMs ?? 0) * mult),
  };
  const total = Object.values(breakdown).reduce((s, v) => s + v, 0);
  const bottleneck = Object.entries(breakdown).sort((a, b) => b[1] - a[1])[0];
  const SUGGESTIONS = {
    ttfb: 'SSR 缓存/Edge 部署（RBL-520）',
    htmlTransfer: '压缩/CDN（RBL-702）',
    jsDownload: 'code split/树摇（RBL-686）',
    hydration: '水合优先级/选择性水合（RBL-710）',
  };
  return { breakdown, total, bottleneck: bottleneck[0], suggestion: SUGGESTIONS[bottleneck[0]] };
}

// 自测
// 3G 设备（带宽 1Mbps，multiplier 2）
let r = ttiBreakdown({ ttfbMs: 200, htmlKB: 50, jsKB: 200, hydrationMs: 300,
  deviceMultiplier: 2 }, { bandwidthKbps: 1000 });
// html = 50×8/1000×1000×2 = 800ms；js = 200×8/1000×1000×2 = 3200ms
console.log(r.breakdown.htmlTransfer === 800);
console.log(r.breakdown.jsDownload === 3200);
console.log(r.bottleneck === 'jsDownload');
console.log(r.suggestion.includes('code split'));

// 4G 设备
r = ttiBreakdown({ ttfbMs: 100, htmlKB: 50, jsKB: 100, hydrationMs: 100 },
  { bandwidthKbps: 10000 });
// html = 40ms, js = 80ms, hydration = 100ms
console.log(r.total === 320);
console.log(r.bottleneck === 'hydration');               // 水合最大
console.log(r.suggestion.includes('水合优先级'));

// 纯静态（无水合）
r = ttiBreakdown({ ttfbMs: 50, htmlKB: 20, jsKB: 0, hydrationMs: 0 });
console.log(r.breakdown.hydration === 0);
console.log(r.bottleneck === 'htmlTransfer');

// 空
console.log(ttiBreakdown({}).noData === true);
```

**评分点**：
- 四段分解（TTFB/html 传输/JS 下载/水合——带宽×设备倍率换算）；bottleneck 识别 + 策略映射
- deviceMultiplier（低端机传输与算力的倍增——RUM 校准的设备分布）；纯静态无水合段
- 边界（空 no-data/极低带宽传输主导）；每段的可操作建议
- 能说清「TTI 分解让优化靶向化：瓶颈段决定策略——code split 解决 JS 下载、水合调度解决水合瓶颈」属于加分
