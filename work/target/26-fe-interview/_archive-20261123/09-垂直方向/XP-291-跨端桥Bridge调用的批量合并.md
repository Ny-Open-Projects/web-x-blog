---
title: [XP-291] 跨端桥（Bridge）调用的批量合并
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-291：跨端桥（Bridge）调用的批量合并

**答**：
- 问题：高频桥调用（滚动/传感器）逐条过桥开销大（序列化+线程切换 ~1ms/次）。
- 方案：客户端侧批量（100ms 聚合一次调用）、JSI 直接调用（RN）绕过异步序列化。
- 度量：桥调用次数/s 与耗时占比（> 10ms/帧告警）。

```javascript
// 桥调用批处理
class BridgeBatcher {
  constructor(bridge, { windowMs = 100 } = {}) {
    this.bridge = bridge; this.win = windowMs; this.buf = [];
  }
  call(method, args) {
    this.buf.push({ method, args });
    if (!this.timer)
      this.timer = setTimeout(() => this.flush(), this.win);
  }
  flush() {
    this.timer = null;
    if (this.buf.length) {
      this.bridge.call('__batch__', this.buf);       // 一次过桥
      this.buf = [];
    }
  }
}
```
