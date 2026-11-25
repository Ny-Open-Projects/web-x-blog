---
title: [SCN-1115] IoT 设备的原始报文调试台（开发者模式）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1115：IoT 设备的原始报文调试台（开发者模式）

**答**：
- 调试：设备上下行报文查看（topic/payload/时间），过滤（设备/报文类型）。
- 模拟：虚拟设备模拟器（模拟上行报文测试规则）。
- 安全：调试台仅开发环境（生产关闭）。

```javascript
// 报文调试台
class RawConsole {
  constructor(ws) {
    this.ws = ws; this.buffer = []; this.max = 1000;
    ws.onmessage = e => this.push({ dir: 'up', ...JSON.parse(e.data), at: Date.now() });
  }
  push(msg) {
    this.buffer.push(msg);
    if (this.buffer.length > this.max) this.buffer.shift();
  }
  publish(topic, payload) {                             // 模拟上行
    this.ws.send(JSON.stringify({ action: 'publish', topic, payload }));
    this.push({ dir: 'down', topic, payload, at: Date.now() });
  }
}
```
