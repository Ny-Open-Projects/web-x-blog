---
title: [AV-239] 直播 PK 与连麦互动：跨房间连麦架构
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-239：直播 PK 与连麦互动：跨房间连麦架构

**答**：
- PK 场景：两个主播跨房间连麦——SFU 间级联（房间 A 的 SFU 与房间 B 的 SFU 互推流）；观众端看合成画面（服务端混流）或双画面。
- 信令：PK 邀请/接受/断开流程；计分（礼物值）同步广播。
- 前端关注：PK 布局切换（单画面→左右分屏）的过渡动画、连麦延迟差补偿。

```javascript
class PKSession {
  async invite(opponentId) { this.signaling.send('pk-invite', { target: opponentId }); }
  async accept(inviteId) {
    await this.signaling.send('pk-accept', { inviteId });
    // SFU 间级联由服务端完成——客户端收到 PK 模式切换事件
  }
  onPKStart({ opponent }) {                                  // 切换 PK 布局
    this.layout.transitionTo('split', { left: this.localVideo, right: opponent.video });
    this.scoreboard.bind(opponent);                         // 计分板
  }
  onScoreUpdate(scores) {                                    // 礼物计分广播
    this.scoreboard.update(scores);                         // 动画：数字滚动
    if (scores.some(s => s.value >= this.target)) this.onPKEnd?.();
  }
}
```
