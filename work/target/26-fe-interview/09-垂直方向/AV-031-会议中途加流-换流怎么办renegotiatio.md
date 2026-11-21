---
title: [AV-031] 会议中途加流/换流怎么办？renegotiation 怎么做才安全？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-031：会议中途加流/换流怎么办？renegotiation 怎么做才安全？（高频）
**答**：
- 触发 renegotiation 的操作：addTrack/removeTrack/replaceTrack（方向变化）、addTransceiver、setDirection；会在对端触发 `negotiationneeded`。
- 共享屏幕常用 `replaceTrack`：把 camera track 换成 screen track，不触发重协商、不断流（编码器参数变化瞬间可能抖动）——这是"无缝换流"的关键。
- addTrack 才触发完整重协商；要防 glare：每次协商加锁（makingOffer 标志），并用"完美协商"（perfect negotiation）模式处理冲突。
- 接收方处理 negotiationneeded 时如果自己不是 polite peer，要回滚（rollback）对方的 offer。

```javascript
// replaceTrack 无缝换流（摄像头 ↔ 屏幕），不触发重协商
async function switchToScreen(pc, videoSender) {
  const screenStream = await navigator.mediaDevices.getDisplayMedia({ video: true });
  const [screenTrack] = screenStream.getVideoTracks();
  await videoSender.replaceTrack(screenTrack); // 毫秒级切换，观众无感知断流
  screenTrack.addEventListener('ended', () => { // 用户点"停止共享"
    navigator.mediaDevices.getUserMedia({ video: true })
      .then((s) => videoSender.replaceTrack(s.getVideoTracks()[0]));
  });
}

// 完美协商模式：防 glare 冲突
class PerfectNegotiator {
  constructor(pc, sig, polite) {
    this.pc = pc; this.sig = sig; this.polite = polite;
    this.makingOffer = false; this.ignoreOffer = false;
    pc.onnegotiationneeded = async () => {
      try {
        this.makingOffer = true;
        await pc.setLocalDescription();
        sig.send({ type: 'description', sdp: pc.localDescription });
      } finally { this.makingOffer = false; }
    };
    sig.on('description', async ({ sdp }) => {
      const readyForOffer = !this.makingOffer &&
        (pc.signalingState === 'stable' || pc.signalingState === 'have-local-offer');
      const offerCollision = sdp.type === 'offer' && !readyForOffer;
      this.ignoreOffer = !this.polite && offerCollision;
      if (this.ignoreOffer) return;
      await pc.setRemoteDescription(sdp).catch(async (e) => {
        if (sdp.type === 'offer') await pc.setRemoteDescription(); // rollback
        else throw e;
      });
      if (sdp.type === 'offer') {
        await pc.setLocalDescription();
        sig.send({ type: 'description', sdp: pc.localDescription });
      }
    });
  }
}
```
