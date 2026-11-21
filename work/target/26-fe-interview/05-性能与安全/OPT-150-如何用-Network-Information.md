---
title: [OPT-150] 如何用 Network Information API 做弱网画像与前端自适应降级？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-150：如何用 Network Information API 做弱网画像与前端自适应降级？

**答**：
- `navigator.connection` 提供四个关键信号：`effectiveType`（2g/3g/4g）、`downlink`（估算带宽 Mb/s）、`rtt`（估算往返时延 ms）、`saveData`（省流量开关）。
- 自适应策略分层：saveData/2g → 关闭自动播放、图片降质到 30%、禁止预取；3g → 图片降质、关闭视频自动播放；4g 以上全量体验。
- 信号变化监听 `change` 事件：地铁/电梯场景网络跌落时动态降级，恢复时升级。
- 注意兼容性（Safari 不支持），要做特性检测并回退到"基于实测 RTT 的自研画像"；弱网画像还要结合埋点验证 effectiveType 的准确率。

```javascript
// 一一对应：Network Information API 驱动的自适应降级管理器
class NetworkQuality {
  constructor() {
    this.level = 'high'; // high | mid | low
    this.conn = navigator.connection;
    this.listeners = new Set();
    if (this.conn) {
      this.update();
      this.conn.addEventListener('change', () => { this.update(); this.notify(); });
    }
  }
  update() {
    const c = this.conn;
    if (!c) { this.level = 'high'; return; }
    if (c.saveData) return this.level = 'low';                  // 用户主动省流量：最高优先级
    if (c.effectiveType === 'slow-2g' || c.effectiveType === '2g') return this.level = 'low';
    if (c.effectiveType === '3g' || (c.effectiveType === '4g' && (c.rtt > 400 || c.downlink < 1))) {
      return this.level = 'mid';                                 // 4g 但质量差的"伪4g"
    }
    this.level = 'high';
  }
  on(fn) { this.listeners.add(fn); return () => this.listeners.delete(fn); }
  notify() { this.listeners.forEach(fn => fn(this.level)); }
}

export const net = new NetworkQuality();

// 消费方：图片组件按网络档位选清晰度
function pickImageQuality(level) {
  return { low: '?w=360&q=30', mid: '?w=720&q=60', high: '?w=1080&q=80' }[level];
}
net.on(level => {
  document.documentElement.dataset.net = level;   // CSS 侧联动：[data-net=low] 隐藏非关键动效
  if (level === 'low') window.__autoplayDisabled = true;  // 视频自动播放关闭
});
```
