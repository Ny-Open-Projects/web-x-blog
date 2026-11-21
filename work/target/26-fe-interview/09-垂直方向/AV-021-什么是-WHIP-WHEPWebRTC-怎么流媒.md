---
title: [AV-021] 什么是 WHIP/WHEP？WebRTC 怎么流媒体化？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-021：什么是 WHIP/WHEP？WebRTC 怎么流媒体化？
**答**：
- WHIP（WebRTC-HTTP Ingestion Protocol）/ WHEP（Egress）：用简单 HTTP POST 交换 SDP 完成推/拉流的标准化协议，省去自研信令。
- 客户端 POST `Offer SDP` 到 endpoint，服务器返回 `201 + Answer SDP`，再 PATCH/DELETE 管理 ICE 与会话——三步完成接入。
- 意义：让 CDN 厂商（Cloudflare、阿里云等）能提供"WebRTC 推流/拉流"的开放接口，直播延迟进入亚秒级。
- 适用：超低延迟直播、云游戏、云端渲染画面回传；传统 RTC 会议仍用自研 WebSocket 信令。
- 前端要点：会写 WHIP 客户端请求体（application/sdp）、处理 Location 头返回的 session URL。

```javascript
// 最小 WHIP 推流客户端
async function whipPublish(pc, whipUrl, token) {
  const offer = await pc.createOffer();
  await pc.setLocalDescription(offer); // 触发 ICE 收集
  // 等 ICE gathering 完成（简单实现；生产可用 trickle + PATCH）
  await new Promise((r) =>
    pc.iceGatheringState === 'complete' ? r() :
      pc.addEventListener('icegatheringstatechange', () =>
        pc.iceGatheringState === 'complete' && r()));
  const res = await fetch(whipUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/sdp',
      Authorization: `Bearer ${token}`,
    },
    body: pc.localDescription.sdp,
  });
  if (res.status !== 201) throw new Error(`WHIP 失败 ${res.status}`);
  await pc.setRemoteDescription({ type: 'answer', sdp: await res.text() });
  return res.headers.get('Location'); // session URL，用于 DELETE 挂断
}
```
