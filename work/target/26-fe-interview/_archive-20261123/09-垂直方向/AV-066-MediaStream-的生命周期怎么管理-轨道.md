---
title: [AV-066] MediaStream 的生命周期怎么管理？（轨道结束/设备热插拔）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-066：MediaStream 的生命周期怎么管理？（轨道结束/设备热插拔）
**答**：
- 轨道结束的来源：用户点浏览器"停止共享"（ended 事件）、设备拔出、对端 removeTrack、mute 属性变化（静音不是 ended）。
- 清理原则：track.stop() 释放硬件（关摄像头灯）；PC.close() 后再 stop 本地轨；移除 video.srcObject 前先置 null 释放解码器。
- mute/unmute 监听用于 UI（头像遮罩），ended 用于移除画面与释放资源，两者语义不同。
- 热插拔：devicechange 事件 + 检查当前 track 是否仍 readyState === 'live'；被拔设备要自动切到剩余设备。
- 内存泄漏高发点：每次 ontrack 都创建新 video 元素不释放、旧 MediaStream 未停轨、事件监听未解绑。

```javascript
// MediaStream 生命周期管家
class TrackLifecycle {
  constructor(stream) {
    this.stream = stream;
    stream.getTracks().forEach((t) => this.bind(t));
  }
  bind(track) {
    track.addEventListener('ended', () => {
      console.log('轨道结束', track.kind);
      this.onEnded?.(track);       // UI 移除 + 资源释放
      this.cleanupIfEmpty();
    });
    track.addEventListener('mute', () => this.onMute?.(track, true));   // 静音≠结束
    track.addEventListener('unmute', () => this.onMute?.(track, false));
  }
  cleanupIfEmpty() {
    const live = this.stream.getTracks().filter((t) => t.readyState === 'live');
    if (!live.length) {
      this.video.srcObject = null;  // 先解绑再清引用，防解码器泄漏
      this.video = null;
    }
  }
  // 设备热插拔自愈
  async autoHeal(getStream) {
    navigator.mediaDevices.addEventListener('devicechange', async () => {
      const dead = this.stream.getTracks().filter((t) => t.readyState === 'ended');
      if (!dead.length) return;
      const fresh = await getStream(); // 重新采集可用设备
      dead.forEach((old) => {
        const repl = fresh.getTracks().find((t) => t.kind === old.kind);
        repl && old.onreplace?.(repl); // 调用方执行 replaceTrack
      });
    });
  }
  destroy() {
    this.stream.getTracks().forEach((t) => t.readyState === 'live' && t.stop());
  }
}
```
