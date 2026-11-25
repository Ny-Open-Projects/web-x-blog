---
title: [AV-218] WebRTC 网络切换处理：WiFi/蜂窝切换与 ICE restart
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 笔试题, 26]
type: 笔试题
---

## AV-218：WebRTC 网络切换处理：WiFi/蜂窝切换与 ICE restart

**答**：
- 题目：用户从 WiFi 切 4G，视频卡 3 秒恢复——实现网络切换处理：检测切换、ICE restart、恢复确认。
- 思路：navigator.connection.onchange 或 onicecandidate 变化（新候选类型 = network 切换）→ restartIce → 监听 iceConnectionState 恢复 connected → 上报切换耗时。
- 评分点：切换检测；restartIce 时序；恢复确认与上报。

```javascript
class NetworkSwitchHandler {
  constructor(pc) {
    this.pc = pc;
    navigator.connection?.addEventListener('change', () => this.onNetworkChange());
    this.pc.onicecandidate = (e) => {
      if (e.candidate?.candidate.includes('typ srflx')) {   // 新公网候选 = 可能切换
        if (this.lastCandidateType && this.lastCandidateType !== e.candidate.candidate) {
          this.switchDetectedAt = Date.now();
          this.pc.restartIce();                              // 触发重新探测
        }
        this.lastCandidateType = e.candidate.candidate;
      }
    };
    this.pc.oniceconnectionstatechange = () => {
      if (this.pc.iceConnectionState === 'connected' && this.switchDetectedAt) {
        report('network-switch-recovered', {                // 恢复上报
          ms: Date.now() - this.switchDetectedAt,
          type: navigator.connection?.effectiveType });
        this.switchDetectedAt = null;
      }
    };
  }
  onNetworkChange() {
    report('network-changed', { type: navigator.connection?.effectiveType,
      downlink: navigator.connection?.downlink });
  }
}
```
