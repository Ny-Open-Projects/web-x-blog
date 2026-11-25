---
title: [NODE-846] 笔试题——实现自适应限流（BBR 拥塞思想 + 自动调整）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-846：手写自适应限流

**需求与边界**：
- 需求：自适应限流（SCN-NODE-641 进阶）——① BBR 思想（最大吞吐探测——maxQPS × minRT 的窗口容量）；② 自动调整（无需人工配阈值——按实时吞吐自适应）；③ 过载保护（CPU/ELD 超限自动降档——SCN-NODE-721 ELD）；④ 平滑调整（限流率突变抖动防御——SCN-OPS-237）。
- 边界：① minRT 的估计（滑窗最小 RT——吞吐探测的基准）；② 降档的恢复（负载回落回升——SCN-NODE-726）；③ 与固定配额限流的组合（自适应 + 配额——两层）。

**答**：
```javascript
class AdaptiveLimiter {
  constructor() { this.maxQPS = 0; this.minRT = Infinity; this.cur = 100; }
  onRequest(rt) {
    this.minRT = Math.min(this.minRT, rt);             // 滑窗最小 RT（BBR 基准）
    this.maxQPS = Math.max(this.maxQPS, windowQPS());
    this.cur = clamp(this.maxQPS * this.minRT,         // BBR 容量 = maxQPS × minRT（SCN-NODE-641 进阶）
      this.cur * 0.8, this.cur * 1.2);                 // 平滑调整（SCN-OPS-237 抖动）
    this.inflight++;
    if (this.inflight > this.cur || eldP99() > 100) {  // 过载（SCN-NODE-721 ELD）
      this.inflight--;
      return { allowed: false, retryAfter: 100 };      // 过载拒绝
    }
    return { allowed: true };
  }
  done() { this.inflight--; }
}
```

**评分点**:
- BBR 思想（maxQPS × minRT——无需人工配阈值）。
- 平滑调整（±20%——SCN-OPS-237 抖动防御）。
- ELD 联合过载判定（SCN-NODE-721 Node 特有）。
- 与固定配额组合声明（两层限流——SCN-NODE-641）。
