---
title: [AV-107] RTCPeerConnection 有哪些关键事件？分别在什么时机触发？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-107：RTCPeerConnection 有哪些关键事件？分别在什么时机触发？（高频）
**答**：
- onicecandidate：收集到本地候选逐个触发，发信令给对端；candidate 为 null 表示收集结束。
- ontrack：远端媒体到达，绑 video.srcObject 渲染；重协商时可能再次触发，注意解绑旧流防泄漏。
- onconnectionstatechange：connected/failed/disconnected，驱动重连机制；failed 要 ICE restart，disconnected 可观察自愈。
- oniceconnectionstatechange：更底层的 ICE 状态，与 connectionstate 并不同步，监控两边都要。
- onnegotiationneeded：addTrack/换流后触发，是发起 offer 的正确时机，配合完美协商（AV-108）防碰撞。

```javascript
// 事件接线全景：一个生产级 peer 的骨架
function wirePeer(pc, { onRemoteStream, onState, sendSignal }) {
  pc.onicecandidate = ({ candidate }) => {
    if (candidate) sendSignal({ type: 'candidate', candidate }); // 逐个转发
    else sendSignal({ type: 'candidate-done' });                 // 收集完成
  };
  pc.ontrack = (ev) => {
    onRemoteStream(ev.streams[0], ev.track.kind);                // 按 kind 分发渲染
    ev.track.onended = () => console.warn('远端轨道结束', ev.track.id);
    ev.track.onmute = () => console.info('远端静音或丢流', ev.track.id);
  };
  pc.onconnectionstatechange = () => {
    onState(pc.connectionState);
    if (pc.connectionState === 'failed') pc.restartIce();        // 触发重新协商
  };
  pc.onnegotiationneeded = async () => {                          // addTrack 后自动进入
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);
    sendSignal({ type: 'offer', sdp: pc.localDescription });
  };
}
```
