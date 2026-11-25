---
title: [SCN-1246] AI 对话的消息状态机（发送/生成/完成/失败）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1246：AI 对话的消息状态机（发送/生成/完成/失败）

**答**：
- 状态机：sending→streaming→done / failed（重试）；每个状态 UI 对应（转圈/流式/完成勾）。
- 持久：状态持久化（刷新后恢复消息列表状态）。
- 失败：失败消息保留输入（一键重发，不重输）。

```javascript
// 消息状态机
const MSG_FSM = {
  sending: ['streaming', 'failed'],
  streaming: ['done', 'failed'],
  failed: ['sending'],
};
function msgAction(msg) {
  return msg.status === 'failed'
    ? { retry: true, text: '重新发送', payload: msg.rawInput }   // 保留原输入
    : msg.status === 'streaming' ? { stop: true } : null;
}
```
