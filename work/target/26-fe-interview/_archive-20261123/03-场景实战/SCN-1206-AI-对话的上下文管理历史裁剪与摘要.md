---
title: [SCN-1206] AI 对话的上下文管理（历史裁剪与摘要）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1206：AI 对话的上下文管理（历史裁剪与摘要）

**答**：
- 问题：上下文窗口有限——历史裁剪策略（保留 system+最近 N 轮+早期摘要）。
- 实现：超长会话自动摘要压缩（服务端调用模型摘要），前端展示"已压缩"标记。
- 成本：上下文 token 计数展示（用户可感知成本）。

```javascript
// 上下文管理
function contextTrim(messages, maxTokens, tokenizer) {
  const sys = messages.filter(m => m.role === 'system');
  const rest = messages.filter(m => m.role !== 'system');
  let used = sys.reduce((s, m) => s + tokenizer(m.content), 0);
  const kept = [];
  for (let i = rest.length - 1; i >= 0; i--) {
    const t = tokenizer(rest[i].content);
    if (used + t > maxTokens * 0.7) break;             // 留 30% 给回复
    kept.unshift(rest[i]); used += t;
  }
  return { kept: [...sys, ...kept], trimmed: rest.length - kept.length };
}
```
