---
title: [AV-193] 指标总表：QoE/QoS 全量指标字典。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-193：指标总表：QoE/QoS 全量指标字典。（高频）
**答**：
- QoE（用户视角，端上采）：首帧时间/秒开率、卡顿频次与时长占比、播放成功率、直播延迟、音画偏移、清晰度达标率。
- QoS（服务视角，服务端采）：推流成功率、转码延迟、CDN 命中率/回源率、SFU CPU 与扇出、信令成功率、TURN relay 占比。
- 每个指标三要素：口径定义（分子分母）、采集方式（埋点/日志/拨测）、目标值（基线）。
- 关联性：QoE 劣化时沿"播放器→CDN→源站→推流端"逐段对账 QoS 指标定位（关联 AV-132/199）。

```json
{
  "qoe": {
    "first-frame-ms":  { "p50": "<800", "p90": "<1500", "collect": "rVFC打点" },
    "stall-ratio":     { "def": "卡顿总时长除以播放总时长", "target": "<1.5%" },
    "play-success":    { "def": "开播30秒内成功出画", "target": ">99.5%" },
    "live-latency":    { "def": "端到端延差", "target": "按场景0.5-5s" },
    "av-drift-ms":     { "def": "音画偏移绝对值", "target": "<180" }
  },
  "qos": {
    "push-success":    { "target": ">99.9%" },
    "transcode-lag":   { "target": "<1s 实时流" },
    "cdn-hit-rate":    { "target": ">95%" },
    "sfu-cpu":         { "target": "<70% 基线" },
    "turn-ratio":      { "target": "<20%" },
    "signal-success":  { "target": ">99.99%" }
  }
}
```
