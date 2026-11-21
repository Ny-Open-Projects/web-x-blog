---
title: [SCN-436] 笔试题——实现 ETA 动态更新（延迟检测/主动告知/补偿引导）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-436：手写 ETA 处理：动态更新、延迟主动告知、补偿引导、区间呈现

**需求与边界**：
- 输入：ETA 推送流；输出：ETA 展示与延迟处理。
- 边界要求：① ETA 显示区间（30~40 分钟比精确值诚实）；② 延迟超阈值主动告知（原因+新 ETA）；③ 补偿引导（延迟券）；④ ETA 恢复正常→降级提示（不持续打扰）。

**答**：
```javascript
class EtaTracker {
  constructor({ delayThreshold = 10 }) {
    this.delayThreshold = delayThreshold;
    this.notified = false;
  }
  onEta(e) {                                   // e: {min, reason?}
    if (this.prev != null &&
        e.min - this.prev >= this.delayThreshold) {
      // 延迟主动告知：原因+新 ETA+补偿
      banner(`${e.reason ?? '路况变化'}，预计延至 ${e.min} 分钟`, {
        action: e.compCoupon
          ? { label: '领取延迟补偿券', fn: () => grant(e.compCoupon) }
          : null,
        dismissible: true,
      });
      this.notified = true;
    } else if (this.notified &&
               e.min <= this.prev) {           // 恢复正常
      banner('配送已提速，预计 ' + e.min + ' 分钟到达',
        { level: 'info' });                    // 恢复降级提示
      this.notified = false;
    }
    this.prev = e.min;
    render(`${e.min}~${e.min + 10} 分钟`);     // 区间呈现
  }
}
// ETA 权威在服务端（多因子融合），前端只呈现与预期管理；
// 延迟推送带 reason（透明优于模糊"稍晚"）。
```

**评分点**:
- 区间呈现（min~min+10）比精确值诚实——预期管理意识。
- 延迟阈值主动告知（原因+新 ETA+补偿券引导）。
- 恢复正常的降级提示（不打扰）+ notified 状态防重复。
- ETA 权威在服务端的边界意识。
