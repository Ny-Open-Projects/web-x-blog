---
title: [AV-184] TURN 成本失控的治理案例。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-184：TURN 成本失控的治理案例。（高频）
**答**：
- 现象：月账单突增 3 倍，relay 流量占比从 15% 涨到 45%。
- 归因一：某客户端版本 SDP/ICE 配置错误，大量本可 P2P 的连接退化为 relay；归因二：TURN 无鉴权被外部白嫖。
- 治理：TURN 一次性凭证（REST API 按 user/realm 下发，带 TTL 与配额）、relay 流量按房间维度监控与预算告警、ICE 配置回归测试进 CI。
- 降本：iceServers 池按地区就近下发；保证 host/srflx 候选收集完整，能直连绝不 relay。
- 沉淀：基础设施成本纳入发布检查——灰度期对比 relay 占比基线，劣化即暂停放量。

```json
{
  "turn-governance": {
    "auth": { "mode": "REST一次性凭证", "ttl": "3600s", "per-user-quota-gb-day": 2 },
    "alerts": [
      { "metric": "relay-traffic-ratio", "baseline": "<20%", "delta": "灰度期对比 +10% 即暂停", "level": "P1" },
      { "metric": "turn-anonymous-conn", "abs": ">0", "level": "P0", "note": "无凭证连接直接拒绝" }
    ],
    "ci": { "sdp-regression": "候选类型断言 host与srflx 必须出现" },
    "regional-pool": { "cn": "turn-cn-1", "ap": "turn-ap-1", "eu": "turn-eu-1" }
  }
}
```
