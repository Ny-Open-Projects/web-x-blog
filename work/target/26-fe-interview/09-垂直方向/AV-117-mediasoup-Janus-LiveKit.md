---
title: [AV-117] mediasoup、Janus、LiveKit 这些开源 SFU 怎么选？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-117：mediasoup、Janus、LiveKit 这些开源 SFU 怎么选？（高频）
**答**：
- mediasoup：Node.js/C++ 库而非成品服务器，灵活度最高，房间/信令/权限全要自己写，适合有研发深度的团队。
- Janus：C 写的老牌全家桶（插件体系：视频会议/SIP/流媒体），成熟稳定，二开门槛较高。
- LiveKit：Go 编写，开箱即用 + 官方多端 SDK 全（Web/iOS/Android/React），可托管，适合快速上线。
- 其他：Jitsi（自带完整前后端的整套会议方案）、SRS（RTC+CDN 融合直播）、Pion 生态（Go 库）。
- 选型逻辑：要成品选 LiveKit/Jitsi，深度定制选 mediasoup，对接 SIP 选 Janus，融合直播看 SRS。

```json
{
  "sfu-comparison": {
    "mediasoup": { "lang": "Node.js与C++", "type": "library", "sdk": "自建", "fit": "深度定制团队", "复杂度": "高" },
    "janus":     { "lang": "C", "type": "server", "sdk": "社区", "fit": "SIP网关与传统会议", "复杂度": "中高" },
    "livekit":   { "lang": "Go", "type": "server与cloud", "sdk": "官方多端", "fit": "快速上线", "复杂度": "低" },
    "jitsi":     { "lang": "Java与C", "type": "全栈方案", "sdk": "自带前端", "fit": "开源自部署会议", "复杂度": "中" },
    "srs":       { "lang": "C++", "type": "流媒体服务器", "sdk": "HTTP API", "fit": "RTC与CDN融合直播", "复杂度": "中" }
  },
  "decision": {
    "两周内上线": "livekit 或云服务商",
    "深度自研SFU": "mediasoup",
    "对接SIP电话": "janus",
    "整包开源会议": "jitsi"
  }
}
```
