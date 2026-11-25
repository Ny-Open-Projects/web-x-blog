---
title: [AGT-527] 用户在生成中途输入新消息纠正方向（例如：不对，我说的是B方案），如何处理？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-527：用户在生成中途输入新消息纠正方向（例如：不对，我说的是B方案），如何处理

**答**：
- 生成中新输入默认「排队追加」，用户点"转向"才中断当前流：中断= cancel 流 + 把已生成部分标记为"被中断"，新消息带引用指向被中断内容让模型理解语境。
- 中断不是丢弃：被中断的回答保留可展开（用户可能想要其中一半），转向后的新回答要考虑已生成内容避免重复劳动。
- 快速连续转向要防抖合并：200ms 内的多条纠正合并成一轮，避免"别别别"打出三段生成。

```javascript
async function steerTurn(turn, newMsg) {
  await turn.cancel();                       // 中断当前流
  turn.markInterrupted();                    // 半成品保留可展开
  await send({
    parts: [newMsg,
      { type: 'ctx_ref', ref: turn.id, note: '上一回答已被中断' }],
    instruction: '用户纠正了方向，结合上文已生成部分重新回答，避免重复',
  });
}
// 连续纠正合并：debounce 200ms 聚合后再发送
const steer = debounce((msgs) => steerAll(turn, msgs), 200);
```

