---
title: [HW-183] 手写音频上下文懒初始化——AudioContext 用户手势解锁 + 挂起恢复状态机 + 提示音队列
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-183：手写音频上下文懒初始化——AudioContext 用户手势解锁 + 挂起恢复状态机 + 提示音队列
**答**：浏览器音频限制的完整处理：AudioContext 必须在用户手势后才能 resumed——懒初始化（首次手势时创建/resume）+ 状态机（suspended→resumed）+ 提示音队列（手势前积累的提示音在手势解锁后按序播放）+ 自动挂起恢复（系统打断（来电）后 interrupted 状态处理 iOS）。

```javascript
class AudioHub {
  #ctx = null; #queue = [];
  async ensure() {                                        // 必须在用户手势内调用
    if (!this.#ctx) this.#ctx = new AudioContext();
    if (this.#ctx.state === 'suspended') await this.#ctx.resume();
    // 解锁后：按序播积累的提示音（手势前的通知）
    while (this.#queue.length) {
      const play = this.#queue.shift();
      await play(this.#ctx);
    }
    return this.#ctx;
  }
  notify(playFn) {                                        // 提示音入口
    if (this.#ctx?.state === 'running') playFn(this.#ctx);
    else this.#queue.push(playFn);                        // 未解锁：排队待手势后播
  }
}
// 用法：任意用户手势（click/keydown）解锁
addEventListener('pointerdown', () => audioHub.ensure(), { once: true });
// IM 新消息：audioHub.notify((ctx) => beep(ctx, 800));
// 语义：
// 手势前收到的消息 → 排队（不丢），首次点击时补播（"叮"声延迟但不丢失）
// iOS 电话打断 → state 变 'interrupted' → visibilitychange/恢复事件里重新 resume
```

**评分点**：
- 用户手势解锁 AudioContext（suspended→resume）——本题核心。
- 提示音队列（手势前不丢，手势后补播）。
- iOS interrupted 状态的意识。
- once: true 的解锁监听。
