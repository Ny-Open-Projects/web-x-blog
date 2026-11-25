---
title: [SCN-1149] IoT 设备控制台的指令发送队列（前端指令风暴防护）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1149：IoT 设备控制台的指令发送队列（前端指令风暴防护）

**答**：
- 场景：运维批量操作触发指令风暴——前端队列限速（10 条/秒），失败重排队。
- 实现：令牌桶限速 + 队列持久化（页面刷新不丢）。
- 反馈：队列进度 + 取消能力。

```javascript
// 指令队列限速
class CmdQueue {
  constructor(rate = 10) { this.rate = rate; this.q = []; this.running = false; }
  push(cmd) { this.q.push(cmd); this.run(); }
  async run() {
    if (this.running) return; this.running = true;
    while (this.q.length) {
      const batch = this.q.splice(0, this.rate);
      await Promise.allSettled(batch.map(c => sendCommand(c.id, c.cmd)));
      await sleep(1000);                               // 每秒一批
    }
    this.running = false;
  }
}
async function sendCommand(id, cmd) { return true; }
```
