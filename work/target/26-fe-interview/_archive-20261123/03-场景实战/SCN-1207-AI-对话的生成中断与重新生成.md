---
title: [SCN-1207] AI 对话的生成中断与重新生成
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1207：AI 对话的生成中断与重新生成

**答**：
- 中断：用户点击停止（AbortController 中断流），已生成内容保留（不丢）。
- 重新生成：同 prompt 重发（多样性：temperature 微调），旧回答保留可对比。
- 体验：中断后按钮变"继续生成"（续写）。

```javascript
// 生成控制
class GenerationControl {
  constructor() { this.ctrl = null; }
  async generate(payload, onDelta) {
    this.ctrl = new AbortController();
    let acc = '';
    try {
      await streamChat(payload, this.ctrl.signal, d => {
        acc += d; onDelta(acc);
      });
    } catch (e) {
      if (e.name !== 'AbortError') throw e;
      return { partial: acc, stopped: true };
    }
    return { partial: acc, stopped: false };
  }
  stop() { this.ctrl?.abort(); }
}
```
