---
title: [AV-221] WebRTC 会议离席检测：静音与无人自动处理
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-221：WebRTC 会议离席检测：静音与无人自动处理

**答**：
- 自动策略：全员静音超 N 分钟 → 提示结束会议；单人说话无人回应（音量检测）→ 提示；页面切后台超时 → 自动静音。
- 实现：audioLevel 轮询统计「有效发言时长」；visibilitychange 后台静音；会议时长与会者活跃度报表。
- 价值：节省 SFU 资源（空会议自动关闭）。

```javascript
class MeetingLivenessMonitor {
  constructor(room, { idleTimeoutMs = 15 * 60000 } = {}) {
    this.lastActive = Date.now();                           // 最后有效发言
    setInterval(async () => {
      const anySpeaking = await this.anyOneSpeaking();
      if (anySpeaking) this.lastActive = Date.now();
      const idle = Date.now() - this.lastActive;
      if (idle > idleTimeoutMs) {
        this.promptEnd?.();                                  // 提示结束会议
        report('meeting-idle', { roomId: room.id, idleMs: idle });
      }
    }, 30000);
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) this.muteSelf?.();                 // 后台自动静音（防漏音）
    });
  }
  async anyOneSpeaking() {
    for (const pc of this.room.peers.values()) {
      const stats = await pc.getStats();
      const audio = [...stats.values()].find(r => r.kind === 'audio' && r.type === 'inbound-rtp');
      if ((audio?.audioLevel ?? 0) > 0.05) return true;
    }
    return false;
  }
}
```
