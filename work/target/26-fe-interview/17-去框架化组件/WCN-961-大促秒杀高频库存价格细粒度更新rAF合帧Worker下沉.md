---
title: [WCN-961] 大促秒杀高频库存 / 价格更新下，细粒度更新怎么避免主线程卡顿
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-961：大促秒杀高频库存 / 价格更新下，细粒度更新怎么避免主线程卡顿

**答**：
- 结论先行：秒杀场景每秒几十次库存/价格变更，细粒度虽然省去 diff，但每个变更触发的 effect still 在主线程跑；要「合帧 + 下沉」——把计算放 Worker，把写 DOM 合并到每帧一次。
- 合帧：用 requestAnimationFrame 把一帧内的多次信号写合并成一次 DOM 更新，避免每帧多次布局（高频写入先标脏、rAF 统一 flush）。
- 下沉：纯计算（优惠价计算、库存显示格式化、倒计时差）放 Web Worker，通过 postMessage 回传结果，主线程只做最小 DOM patch。
- 视觉降级：极端高频时只更新「可见区」条目，非可见区暂停更新（结合 IntersectionObserver），倒计时用 CSS animation 而非 JS 逐帧。
- 追问钩子：面试官问「Worker 回传仍然太频繁怎么办」——答：Worker 侧也做节流（如每 100ms 一次快照），主线程侧再做 rAF 合帧，双层缓冲。

```javascript
// 高频写 -> rAF 合帧 + Worker 下沉
let pending = null, scheduled = false;
function writeStock(sku, val) {
  pending = { ...(pending || {}), [sku]: val }; // 只保留最新
  if (scheduled) return;
  scheduled = true;
  requestAnimationFrame(() => {
    for (const [k, v] of Object.entries(pending)) updateDOM(k, v); // 一帧一次
    pending = null; scheduled = false;
  });
}
function updateDOM(sku, val) {
  document.querySelector(`[data-sku="${sku}"]`).textContent = val;
}
writeStock('a', 10); writeStock('a', 9); writeStock('b', 3); // 一帧内合并为 a=9,b=3
```
