---
title: [PER-325] 如何探测用户弱网状态？Network Information API 的能力与边界是什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-325：如何探测用户弱网状态？Network Information API 的能力与边界是什么？

**答**：
- Network Information API（`navigator.connection`）：`effectiveType`（slow-2g/2g/3g/4g，按 RTT+下行估算）、`rtt`（往返时延 ms）、`downlink`（下行 Mbps）、`saveData`（用户开了省流模式）、`change` 事件（网络变化实时感知）。
- 边界一：effectiveType 是**粗档估计**（四档），不精确到具体带宽；实验室 throttling 与它口径不同。边界二：兼容性——Safari/iOS 不支持（关键缺口），Firefox 支持部分字段。所以不能作为唯一信号。
- 自建探测补充：首屏关键资源的实际加载耗时（Resource Timing 反推 RTT 与带宽）、接口 TTFB 滑动平均（自建 RTT 信号）、上传耗时样本。信号融合：connection API（可用时）+ 接口 TTFB 分位数 + 页面加载耗时，三信号投票出"弱/中/强"档位。
- 用途：弱网降级——关自动播放视频、降低图片质量（1x 图/预览图）、拉长轮询间隔、禁用 prefetch；saveData=true 时不预取任何非关键资源（尊重用户选择）。

```javascript
function networkTier() {
  const c = navigator.connection;
  const signals = [];
  if (c) signals.push(c.saveData ? 'slow' : ({ 'slow-2g': 'slow', '2g': 'slow', '3g': 'mid' }[c.effectiveType] || 'fast'));
  // 自建信号：最近接口 TTFB p50
  const ttfbP50 = rumAgg.ttfbP50();                          // 自建聚合
  if (ttfbP50 > 1200) signals.push('slow');
  else if (ttfbP50 > 400) signals.push('mid');
  else signals.push('fast');
  const votes = { slow: 0, mid: 0, fast: 0 };
  signals.forEach((s) => votes[s]++);
  return Object.entries(votes).sort((a, b) => b[1] - a[1])[0][0];
}
// 降级应用：
const tier = networkTier();
if (tier === 'slow') { imgQuality = 'preview'; disableAutoPlay(); pollInterval = 15000; }
if (navigator.connection?.saveData) prefetchDisabled = true;   // 尊重省流
```
