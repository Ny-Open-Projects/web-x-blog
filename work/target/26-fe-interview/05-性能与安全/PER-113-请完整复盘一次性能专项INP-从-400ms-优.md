---
title: [PER-113] 请完整复盘一次性能专项：INP 从 400ms 优化到 180ms。
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-113：请完整复盘一次性能专项：INP 从 400ms 优化到 180ms。

**答**：
- 定位：INP 归因显示 `inputDelay 180ms + processing 190ms + presentation 30ms`，罪魁是商品卡点击回调里的**同步渲染 200 条卡片 + 同步埋点上报 + 强制同步布局**。
- 优化三步：重计算拆分（卡片渲染改增量 + `scheduler.yield` 让路）、埋点延后（`requestIdleCallback` 批量）、布局读写分离（先批量读 rect 再统一写样式）。
- 收益归因：inputDelay 400->80ms（主线程空闲了）、processing 190->90ms（回调瘦身）、presentation 保持 30ms；P75 INP 400 -> 180ms。
- 防劣化：INP 回归用例进 CI（Playwright 模拟点击测长任务）、归因指标进看板按版本对比。

```javascript
// 优化前：INP 400ms 的典型回调（反例保留做对照）
function onCardClickOld(e) {
  renderCards(fetchAll(200));            // 同步渲染 200 张卡，150ms
  track('card_click', getPayload());     // 同步序列化上报，40ms
  const h = list.getBoundingClientRect(); // 写后读，强制同步布局，40ms
  positionTooltip(e.clientX, h.top);
}

// 优化后：P75 INP 180ms
async function onCardClick(e) {
  const t0 = performance.now();
  // 1) 立即做视觉反馈（3ms 内）
  e.currentTarget.classList.add('active');

  // 2) 让路渲染：确保本帧先画出来（inputDelay 降 320ms 的关键）
  await (scheduler.yield?.() ?? new Promise(requestAnimationFrame));

  // 3) 增量渲染：首屏 12 张同步，其余空闲分批
  renderCardsIncremental(fetchAll(200), { first: 12, chunk: 8 });

  // 4) 埋点延后到空闲，且只序列化一次
  requestIdleCallback(() => track('card_click', getPayload()));

  // 5) 布局读写分离：rect 在写操作前批量读取
  const rect = list.getBoundingClientRect();
  positionTooltip(e.clientX, rect.top);
  if (performance.now() - t0 > 50) console.warn('回调仍超标'); // 自我监控
}
```
