---
title: [SCN-1228] AI 对话的性能预算（长会话 DOM 治理）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1228：AI 对话的性能预算（长会话 DOM 治理）

**答**：
- 问题：长会话数千消息 DOM 爆炸——虚拟化（视口外消息卸载）+ 只保留最近 N 条完整渲染。
- 策略：历史消息折叠为"加载更多"分页（不进 DOM）。
- 度量：DOM 节点数上限（< 2000）与内存监控。

```javascript
// 会话虚拟化
function sessionDomBudget(messages, { maxDom = 2000 } = {}) {
  const visible = messages.slice(-Math.floor(maxDom / 10));   // 最近消息完整渲染
  return {
    render: visible,
    older: { count: messages.length - visible.length,
      action: 'load-more' },                          // 旧消息分页
    domEstimate: visible.length * 10,
    over: visible.length * 10 > maxDom,
  };
}
```
