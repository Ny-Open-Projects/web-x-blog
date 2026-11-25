---
title: [SCN-1238] AI 对话的Token 计数前端实现（近似计数）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1238：AI 对话的Token 计数前端实现（近似计数）

**答**：
- 近似：前端 token 估算（中文≈1.5 字/token，英文≈4 字符/token），精确计数服务端。
- 用途：输入框字数/token 提示（上下文剩余空间）。
- 校准：本地估算与服务端实际计数校准（系数学习）。

```javascript
// token 估算
function estimateTokens(text) {
  const cjk = (text.match(/[\u4e00-\u9fa5]/g) ?? []).length;
  const other = text.length - cjk;
  return Math.ceil(cjk * 1.5 + other / 4);            // 近似估算
}
function ctxMeter(text, maxTokens) {
  const used = estimateTokens(text);
  return { used, pct: +(used / maxTokens * 100).toFixed(1) + '%',
    warn: used > maxTokens * 0.8 ? '接近上下文上限，早期内容将被裁剪' : null };
}
```
