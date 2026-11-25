---
title: [SCN-1239] AI 对话的流式过程中的用户中断输入（边生成边输入）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1239：AI 对话的流式过程中的用户中断输入（边生成边输入）

**答**：
- 体验：回复生成中用户可继续输入（不打断生成），发送排队（生成完自动发）。
- 打断：新消息可选择打断当前生成（转向新问题）。
- 队列：排队消息可视化（n 条待发）。

```javascript
// 边生成边输入
class ChatQueue {
  constructor() { this.q = []; this.generating = false; }
  enqueue(msg) {
    this.q.push(msg);
    if (this.generating) return { queued: this.q.length };
    return this.process();
  }
  async process() {
    this.generating = true;
    while (this.q.length) {
      const m = this.q.shift();
      await generateAndRender(m);                      // 逐条生成
    }
    this.generating = false;
  }
}
async function generateAndRender(m) { return true; }
```
