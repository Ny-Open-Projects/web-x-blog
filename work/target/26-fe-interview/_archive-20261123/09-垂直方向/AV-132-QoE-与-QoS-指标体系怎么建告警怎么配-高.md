---
title: [AV-132] QoE 与 QoS 指标体系怎么建？告警怎么配？（高频收束）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-132：QoE 与 QoS 指标体系怎么建？告警怎么配？（高频收束）
**答**：
- QoS 是服务视角（服务端可测：推流成功率、CDN 命中率、转码延迟）；QoE 是用户视角（端上采样：首帧/卡顿/失败/音画偏移）。
- 分层：北极星（秒开率、卡顿率、播放成功率）→ 过程指标（TTFB、buffer 水位、重试率）→ 根因指标（DNS 失败、TCP 重传、license 失败）。
- 采集口径：端上 SDK 统一埋点，按"分钟 × 维度"聚合上报，采样 1%-10%，错误样本全量。
- 告警设计：绝对值告警（卡顿率 > 3%）+ 环比突变告警（5 分钟环比 +50%），后者对灰度事故更敏感。
- 闭环：告警 → 维度自动定位（哪省/哪家 CDN/哪协议）→ 预案执行（切 CDN/降档）→ 复盘沉淀。

```json
{
  "north-star": {
    "first-frame-1s-rate": { "target": ">=92%", "dim": ["cdn", "isp", "protocol"] },
    "stall-duration-ratio": { "target": "<=1.5%", "note": "卡顿时长除以播放时长" },
    "play-success-rate": { "target": ">=99.5%", "note": "开播30秒内出画算成功" }
  },
  "alerts": [
    { "metric": "stall-duration-ratio", "abs": ">3%", "level": "P0", "action": "自动切CDN预案" },
    { "metric": "first-frame-1s-rate", "delta": "5min环比-20%", "level": "P1", "action": "联动CDN排查" },
    { "metric": "rtmp-push-fail-rate", "abs": ">1%", "level": "P0", "action": "切推流边缘" },
    { "metric": "av-sync-drift-p95", "abs": ">180ms", "level": "P2", "action": "排查转码时间戳" }
  ],
  "sampling": { "qoe-logs": "5%", "full-on-error": true, "aggregation": "1min x dims" }
}
```

## 十六、场景工程深化（AV-133 ~ AV-139）
