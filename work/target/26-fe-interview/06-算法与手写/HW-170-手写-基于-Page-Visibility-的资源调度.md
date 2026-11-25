---
title: [HW-170] 手写可见性资源调度——hidden 时暂停重资源（视频/轮询/动画），恢复时分级续播
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-170：手写可见性资源调度——hidden 时暂停重资源（视频/轮询/动画），恢复时分级续播
**答**：后台标签页省电的资源调度器：hidden 时按等级暂停（视频暂停播放、轮询暂停、canvas 动画停帧、WS 心跳降频）；恢复时分级续播（用户离开期间的缺口处理——视频 seek 到暂停点、轮询立即补一次）。注册式 API（各资源声明 pause/resume），统一生命周期管理。

```javascript
class VisibilityScheduler {
  #resources = new Map();                                // key -> { level, pause, resume }
  #levelOrder = { video: 0, animation: 1, poll: 2, ws: 3 };   // level 小 = 先暂停
  constructor() {
    document.addEventListener('visibilitychange', () => {
      document.visibilityState === 'hidden' ? this.#pauseAll() : this.#resumeAll();
    });
  }
  register(key, level, { pause, resume }) {
    this.#resources.set(key, { level, pause, resume });
    if (document.visibilityState === 'hidden') pause();  // 注册时已在后台：立即暂停
    return () => this.#resources.delete(key);
  }
  #pauseAll() {
    [...this.#resources.values()]
      .sort((a, b) => this.#levelOrder[a.level] - this.#levelOrder[b.level])
      .forEach((r) => { try { r.pause(); } catch {} });  // 按级暂停：视频先停、WS 最后（心跳降频而非断开）
  }
  #resumeAll() {
    [...this.#resources.values()]
      .sort((a, b) => this.#levelOrder[b.level] - this.#levelOrder[a.level])
      .forEach((r) => { try { r.resume(); } catch {} }); // 恢复反序：WS 先重连，视频最后续播
  }
}
// 用法：
// sched.register('video', 'video', { pause: () => v.pause(), resume: () => v.play().catch(() => {}) });
// sched.register('poll', 'poll', { pause: () => poller.stop(), resume: () => poller.start() });
// 分级语义：视频（最贵）先停；WS（连接成本高）最后动且只降频——断开重连成本 > 降频
// 恢复反序：先恢复连接类（WS/轮询），再恢复播放类——数据先到位，体验连续
```

**评分点**：
- 分级暂停/恢复（视频先停、WS 最后且降频不断开）——本题核心。
- 恢复反序的数据先到位语义。
- 注册时已在后台的边界处理。
- 每资源 try-catch 隔离 + 取消注册函数。
