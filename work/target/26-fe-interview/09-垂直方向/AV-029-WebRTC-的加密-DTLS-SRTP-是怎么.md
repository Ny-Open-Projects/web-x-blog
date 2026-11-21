---
title: [AV-029] WebRTC 的加密 DTLS/SRTP 是怎么回事？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-029：WebRTC 的加密 DTLS/SRTP 是怎么回事？
**答**：
- 强制加密是 WebRTC 硬性要求：媒体走 SRTP（RTP 加密版），控制走 SRTCP，密钥通过 DTLS-SRTP 握手协商。
- 流程：ICE 连通后，先 DTLS 握手（证书自签，SDP 中的 `a=fingerprint` 校验防中间人）→ 协商出 SRTP 密钥 → 媒体加解密。
- DataChannel 走 SCTP over DTLS，同样是加密的。
- 对前端的意义：无需手写加密；但 `a=fingerprint` 变化会导致重协商失败；自建 SFU 要持有证书私钥。
- 常见误区：HTTPS 站点 ≠ WebRTC 加密，两者独立；信令要 wss，媒体加密由 DTLS/SRTP 保证。

```javascript
// 从 SDP 中提取并校验指纹（防信令篡改的入门做法）
function extractFingerprint(sdp) {
  const m = sdp.match(/a=fingerprint:(sha-256)\s+([0-9A-F:]+)/i);
  return m ? { algo: m[1], value: m[2].toUpperCase() } : null;
}
// 预共享指纹校验：对端指纹应与业务服务器下发的一致
function verifyPeerFingerprint(receivedSdp, expected) {
  const fp = extractFingerprint(receivedSdp);
  if (!fp || fp.value !== expected) {
    throw new Error('对端 DTLS 指纹不符，可能存在中间人'); // 拒绝 setRemoteDescription
  }
  return true;
}
// DTLS 状态监听
pc.addEventListener('connectionstatechange', () => {
  // new → connecting(ICE+DTLS) → connected；dtls 失败表现为 failed
  console.log('connectionState:', pc.connectionState);
});
```
