---
title: [AV-192] 协议总表升级版：含 LL-HLS/SRT/RIST。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-192：协议总表升级版：含 LL-HLS/SRT/RIST。（高频）
**答**：
- 在 AV-096 基础上补全两块：低延迟档位（LL-HLS/WebTransport）与贡献传输协议（SRT/RIST）。
- SRT：ARQ + 加密的可靠 UDP 传输，公网替代专线做"贡献传输"（赛事回传/跨国上行），延迟可控 100-800ms。
- RIST：SRT 的标准化同类（互通性好），广电行业用得多。
- 选型补全维度：成本（专线 vs SRT）、互通性（开源生态）、延迟全谱（400ms-10s）。
- 记忆锚点：主播上行看 RTMP/SRT，大众分发看 HLS/FLV/LL-HLS，互动看 WHIP/WHEP，远程制作看 SRT/RIST。

```json
{
  "protocol-table-v2": {
    "RTMP":             { "delay": "1-3s", "role": "推流主力", "note": "上行推流事实标准" },
    "HLS":              { "delay": "3-10s", "role": "分发", "note": "兼容性最好" },
    "LL-HLS":           { "delay": "0.5-2s", "role": "分发", "note": "Part分片加阻塞加载" },
    "HTTP-FLV":         { "delay": "1-2s", "role": "分发", "note": "依赖MSE 国产生态" },
    "DASH":             { "delay": "3-10s", "role": "分发", "note": "国际标准 DRM生态好" },
    "WebRTC-WHIP-WHEP": { "delay": "<1s", "role": "互动与超低延迟", "note": "SFU架构" },
    "SRT":              { "delay": "0.1-0.8s", "role": "贡献传输", "note": "公网替代专线 ARQ加密" },
    "RIST":             { "delay": "0.1-1s", "role": "贡献传输", "note": "广电标准化 互通性好" },
    "WebTransport":     { "delay": "0.5-1s", "role": "分发实验", "note": "QUIC 可靠加不可靠双通道" }
  },
  "selection": {
    "主播上行": "RTMP 通用 或 SRT 弱网跨国",
    "大众分发": "HLS 或 FLV 按延迟与生态",
    "互动场景": "WHIP与WHEP 加 SFU",
    "远程制作": "SRT 或 RIST"
  }
}
```
