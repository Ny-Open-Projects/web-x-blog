---
title: [AV-048] AudioContext 的生命周期与移动端解锁怎么做？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-048：AudioContext 的生命周期与移动端解锁怎么做？（高频压轴）
**答**：
- AudioContext 创建后默认 `suspended`，必须在用户手势内调用 `resume()` 才能运行（iOS 严格、Android Chrome 同样受限）。
- 状态机：suspended → running（resume 成功）→ closed（close 后不可复用）；`onstatechange` 监听。
- 实践模式：首次交互（click/touchstart）统一 resume；音频提前加载用 fetch/decodeAudioData（不受 suspended 限制），播放时才需要 running。
- Safari 老版本要 `webkitAudioContext`，且要求在手势回调的同步调用链里 resume。
- 数量限制：每个页面 AudioContext 不宜多（上限约 6 个），全局单例 + 复用是标准做法。

```javascript
// 全局 AudioContext 单例 + 手势解锁
class AudioEngine {
  static #instance;
  static get instance() {
    this.#instance ??= new AudioEngine();
    return this.#instance;
  }
  constructor() {
    const AC = window.AudioContext ?? window.webkitAudioContext;
    this.ctx = new AC();
    document.addEventListener('pointerdown', () => this.ctx.resume(), { capture: true });
    this.ctx.addEventListener?.('statechange', () =>
      console.log('AudioContext:', this.ctx.state));
  }
  get ready() { return this.ctx.state === 'running'; }
  async ensureRunning() {
    if (this.ctx.state !== 'running') await this.ctx.resume();
  }
}
// iOS 安全封装：所有发声入口先 ensureRunning
async function playSafe(node) {
  await AudioEngine.instance.ensureRunning();
  node.start(0);
}
```
