---
title: [AV-026] SDP 是什么？Offer/Answer 模型怎么工作？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-026：SDP 是什么？Offer/Answer 模型怎么工作？（高频压轴）
**答**：
- SDP（Session Description Protocol）是文本协议，描述：媒体行 m=（音频/视频/应用）、属性 a=（编码 payload、ICE 参数、DTLS 指纹、方向）。
- Offer/Answer 模型：A 生成 offer（我有这些能力）→ B 生成 answer（取交集作为最终能力）→ 双方 setLocal/RemoteDescription。
- `a=mid` 标识 m-line 顺序（BUNDLE 复用一条传输通道）；`a=setup` 决定 DTLS 角色；`a=sendrecv/sendonly/recvonly` 表方向。
- 常见考题：callee 只收不发用 recvonly；单向屏幕共享 sendonly；`offerToReceiveVideo` 已废弃，用 addTransceiver。
- SDP 不能裸改就生效——改完要重新 setLocalDescription；munging 是黑魔法，优先用 setParameters/RTCRtpTransceiver。

```sdp
v=0
o=- 4611731400430051336 2 IN IP4 127.0.0.1
s=-
t=0 0
a=group:BUNDLE 0 1
a=msid-semantic: WMS stream-1
m=audio 9 UDP/TLS/RTP/SAVPF 111
c=IN IP4 0.0.0.0
a=rtcp:9 IN IP4 0.0.0.0
a=ice-ufrag:EsAw
a=ice-pwd:P2uYro0UCOQ4zxjKXaWCBui1
a=fingerprint:sha-256 D2:FA:0E:C3:22:59:5E:14:95:69:92:3D:13:B4:84:24
a=setup:actpass
a=mid:0
a=sendrecv
a=rtpmap:111 opus/48000/2
a=fmtp:111 minptime=10;useinbandfec=1
a=ssrc:1001 cname:webrtc
m=video 9 UDP/TLS/RTP/SAVPF 96
c=IN IP4 0.0.0.0
a=mid:1
a=sendrecv
a=rtpmap:96 VP8/90000
a=rtcp-fb:96 nack pli
a=rtcp-fb:96 goog-remb
a=ssrc:2002 cname:webrtc
```
