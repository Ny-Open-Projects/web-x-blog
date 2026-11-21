---
title: [H5-225] WebRTC 建连的 SDP 交换与 ICE 是什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, RTC]
type: 面试题
---

## H5-225：WebRTC 建连的 SDP 交换与 ICE 是什么

**答**：
- 建连三步：createOffer/Answer 生成 SDP（媒体能力协商：编码、分辨率）→ 信令服务器转发 SDP → 交换 ICE 候选直到连通
- ICE 候选类型：host（本机局域网地址）、srflx（STUN 探测到的公网映射）、relay（TURN 服务器中转）；连通性检查按优先级尝试
- STUN：帮你发现「NAT 后的公网地址」；TURN：打洞失败时的中转兜底（成本最高，约 20% 连接需要）
- 信令服务器不在 WebRTC 规范内，需要自建（WebSocket 常用）；WebRTC 数据本身加密，信令通道自己负责安全
- 面试话术：能画出 offer/answer/candidate 三条消息的时序即达标

```javascript
// offer/answer 交换（信令略）
const offer = await pc.createOffer();
await pc.setLocalDescription(offer);
signal.send({ sdp: offer });
pc.onicecandidate = ({ candidate }) => candidate && signal.send({ candidate });
signal.onmessage = async ({ data }) => {
  if (data.sdp) await pc.setRemoteDescription(data.sdp);
  if (data.candidate) await pc.addIceCandidate(data.candidate);
};
```
