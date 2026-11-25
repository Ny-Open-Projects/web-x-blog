---
title: [AV-209] WebRTC 信令设计：房间管理与协商时序
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-209：WebRTC 信令设计：房间管理与协商时序

**答**：
- 信令职责：房间加入/离开、Offer-Answer 交换、ICE candidate 交换、成员变更广播——不含媒体（媒体走 P2P/SFU）。
- 时序保障：join → 拿房间状态 → 与每个已有成员建连（新人对老人发起 Offer）；避免 Glare（双方同时 Offer）用 polite/impolite 角色仲裁。
- 重连：信令断线重连后 ICE restart（pc.restartIce()）恢复媒体。

```javascript
class SignalingSession {
  constructor(ws, roomId, polite) {                        // polite: 较新成员
    this.polite = polite; this.pendingOffer = null;
  }
  async onOffer(description) {
    if (this.makingOffer || this.pc.signalingState !== 'stable') {
      // Glare：双方同时发 Offer——polite 一方回滚
      if (!this.polite) throw new Error('glare-impolite');
      await this.pc.setLocalDescription({ type: 'rollback' });
    }
    await this.pc.setRemoteDescription(description);
    await this.pc.setLocalDescription(await this.pc.createAnswer());
    this.ws.send({ answer: this.pc.localDescription });
  }
  onIceRestart() { this.pc.restartIce(); }                 // 网络切换：ICE 重启
}
// 完美协商（Perfect Negotiation）模式：polite/impolite + rollback 解决冲突
```
