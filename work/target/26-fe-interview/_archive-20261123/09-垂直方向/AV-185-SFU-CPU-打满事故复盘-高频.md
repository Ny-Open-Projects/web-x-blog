---
title: [AV-185] SFU CPU 打满事故复盘。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-185：SFU CPU 打满事故复盘。（高频）
**答**：
- 现象：晚间高峰某大房间全员卡顿，该 SFU CPU 100%，其他节点正常。
- 归因：房间内一个 Producer 恶意上行 1080p60 高码率，SFU 对 N 个 Consumer 的转发放大开销（扇出放大）。
- 处置：立即限流该 Producer（SFU 侧上限），房间降级为只订阅音频，15 分钟恢复。
- 改进：上行准入（SDP 校验 maxBitrate/分辨率上限）、扇出预算（房间 Consumer 总码率超限自动拆房）、压测覆盖"恶意上行"场景。
- 前端配合：订阅端上报解码能力，SFU 据此限制下发档位。

```json
{
  "sfu-guardrails": {
    "producer-limits": { "max-width": 1280, "max-fps": 30, "max-bitrate-bps": 2500000, "enforce": "SDP校验加超限降采样" },
    "fanout-budget": { "room-max-total-bps": 60000000, "action": "超限自动拆房或锁定新订阅" },
    "circuit-breaker": { "cpu-percent": 85, "action": "新房间调度到备用节点" },
    "monitor": ["cpu-per-room", "fanout-bps-per-producer", "drop-rate"]
  }
}
```
