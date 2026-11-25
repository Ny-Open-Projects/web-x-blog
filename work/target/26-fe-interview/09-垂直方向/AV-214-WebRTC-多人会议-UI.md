---
title: [AV-214] WebRTC 多人会议 UI：活跃说话人与布局策略
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-214：WebRTC 多人会议 UI：活跃说话人与布局策略

**答**：
- 活跃说话人检测：audioLevel 采样 > 阈值持续 500ms → 标记 active；布局：宫格（≤9 人）/ 演讲者模式（>9 人只放大 active）。
- 订阅策略：大房间（>25 人）只订阅 activeSpeaker 与最近说话者视频，其余只订阅音频（省带宽与解码）。
- 实现：SFU audioLevel 事件或前端 getStats audioLevel 轮询。

```javascript
class ActiveSpeakerManager {
  constructor(peers, { threshold = 0.05, holdMs = 500 } = {}) {
    this.levels = new Map(); this.active = null;
    setInterval(async () => {
      for (const [id, pc] of peers) {
        const stats = await pc.getStats();
        const audio = [...stats.values()].find(r => r.type === 'inbound-rtp' && r.kind === 'audio');
        const level = audio?.audioLevel ?? 0;
        if (level > threshold) this.levels.set(id, Date.now());   // 说话时间戳
      }
      const latest = [...this.levels.entries()]
        .filter(([, t]) => Date.now() - t < holdMs)          // 500ms 内说过话
        .sort((a, b) => b[1] - a[1])[0];
      if (latest && latest[0] !== this.active) {
        this.active = latest[0];
        this.onActiveChange?.(this.active);                  // 驱动布局切换
      }
    }, 200);
  }
}
```
