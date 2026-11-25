---
title: [SCN-1212] AI 对话的敏感内容过滤与前置拦截
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1212：AI 对话的敏感内容过滤与前置拦截

**答**：
- 拦截：用户输入前置过滤（违规内容拦截，给合规提示）；输出后置过滤（模型越狱防护）。
- 流式：流式中途触发过滤（已输出部分撤回+替换提示）。
- 透明：拦截原因展示（分类标签），申诉入口。

```javascript
// 内容过滤
function contentGuard(input, output) {
  const inHit = MODERATION.check(input);              // 输入前置
  if (inHit.flagged)
    return { blocked: true, category: inHit.category,
      action: '拦截并提示合规使用' };
  const outHit = MODERATION.checkStream(output);
  if (outHit.flagged)
    return { streamCut: true,                          // 流中撤回
      action: '已输出部分替换为提示文案' };
  return { ok: true };
}
```
