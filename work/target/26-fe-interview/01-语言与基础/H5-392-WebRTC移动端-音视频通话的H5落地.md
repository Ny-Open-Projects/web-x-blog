---
title: [H5-392] WebRTC 移动端：音视频通话的 H5 落地要点
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 多媒体]
type: 面试题
---

## H5-392：WebRTC 移动端：音视频通话的 H5 落地要点

**答**：
- 信令与媒体分离：信令走 WebSocket 自建/商业服务，媒体走 RTCPeerConnection P2P 或 SFU（多人必走 SFU）；移动端弱网下 SFU + simulcast（多档码率）是标准架构
- 移动端约束：video 约束分辨率按网络自适应（接收到 remote stream 质量下降时降订阅档位）；前后摄像头切换用 track.applyConstraints 或重建 track
- 生命周期坑：iOS 切后台自动停止发送（视频冻结），回前台要 renegotiate；锁屏时通话中断——纯 H5 通话体验有硬天花板，重度场景引导 App
- 性能与功耗：VP8/H264 兼容性最好（H265/AV1 按支持度协商）；本地预览用小分辨率 + 降低帧率省电；音频处理 echoCancellation/noiseSuppression 默认开
- 弱网策略：RTT/丢包统计（getStats）驱动降码率、关闭视频保音频；断线重连（ICE restart）与「通话重建」流程要设计

```javascript
const pc = new RTCPeerConnection({ iceServers: [{ urls: 'stun:stun.example.com' }] });
const stream = await navigator.mediaDevices.getUserMedia({
  video: { facingMode: 'user', width: { ideal: 640 }, frameRate: { ideal: 15 } }, // 移动端省电约束
  audio: { echoCancellation: true, noiseSuppression: true },
});
stream.getTracks().forEach(t => pc.addTrack(t, stream));
pc.ontrack = (e) => remoteVideo.srcObject = e.streams[0];
// 弱网监控: getStats 驱动降级
setInterval(async () => {
  const stats = await pc.getStats();
  stats.forEach((r) => {
    if (r.type === 'inbound-rtp' && r.kind === 'video' && r.packetsLost / (r.packetsReceived || 1) > 0.05)
      downgradeVideo();                 // 降码率/关视频
  });
}, 3000);
```

## 追问（补充）

**追问**：

1. 多人通话为什么必须走 SFU 而不是全互联 P2P？ → 全互联时每人上行路数随人数增长，移动端带宽和编码压力扛不住；SFU 每人只上行一路，由服务端按订阅转发。
2. simulcast 解决了什么协商成本？ → 发送端同时编多档分辨率，接收端按网络与窗口大小直接切换订阅档位，无需重新协商 SDP 就能降级。
3. iOS 切后台导致视频冻结怎么处理？ → 监听 visibilitychange，回前台重新 applyConstraints 或重建 track 并触发 renegotiation，必要时降级为纯音频提示用户。
