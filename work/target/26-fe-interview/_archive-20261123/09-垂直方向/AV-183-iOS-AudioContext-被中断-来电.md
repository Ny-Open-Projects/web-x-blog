---
title: [AV-183] iOS AudioContext 被中断（来电/Siri）后的恢复案例。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-183：iOS AudioContext 被中断（来电/Siri）后的恢复案例。（高频）
**答**：
- 现象：iOS 来电/微信语音后页面所有 Web Audio 无声，AudioContext.state 停在 interrupted/suspended，resume() 部分场景无效。
- 根因：系统中断打断 AudioContext；部分版本中断后 sampleRate 变化，旧节点全部失效。
- 恢复方案：监听 onstatechange，中断后重建 AudioContext 与整条音频图（节点不可跨 context 复用）。
- RTC 场景：中断后麦克风轨道可能被系统收回，要监听 track onended 与 devicechange，重新 getUserMedia + replaceTrack。
- 预防：进后台主动 suspend 释放，回前台重建；关键业务提示用户"恢复后请重新检查设备"。

```javascript
// iOS 音频中断自愈：重建 AudioContext
class AudioInterruptionRecovery {
  private ctx?: AudioContext;
  private graphSampleRate = 48000;
  async ensure() {
    if (!this.ctx || this.ctx.state === 'closed') this.ctx = new AudioContext();
    if (this.ctx.state === 'suspended') await this.ctx.resume();
  }
  install() {
    this.ctx!.onstatechange = async () => {
      if (this.ctx!.state === 'interrupted') {
        report({ level: 'info', msg: 'audio interrupted' });
      }
      if (this.ctx!.state === 'running' && this.ctx!.sampleRate !== this.graphSampleRate) {
        // 中断后采样率变了 旧节点全部失效 必须重建整条音频图
        await this.rebuildGraph(this.ctx!.sampleRate);
      }
    };
    document.addEventListener('visibilitychange', async () => {
      if (document.visibilityState === 'visible') await this.recoverRtcTracks(); // 恢复被收回的麦克风
    });
  }
  private async rebuildGraph(rate: number) { this.graphSampleRate = rate; /* 按描述重建所有节点 */ }
  private async recoverRtcTracks() { /* 重新 getUserMedia 并 replaceTrack */ }
}
```
