---
title: [SCN-1219] AI 产品的用户反馈闭环（点赞/点踩/原因）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1219：AI 产品的用户反馈闭环（点赞/点踩/原因）

**答**：
- 反馈：回答点赞/点踩（点踩原因标签：错误/无关/有害），反馈进 RLHF 数据管道。
- 修正：点踩后允许用户提交正确答案（贡献语料）。
- 度量：反馈率与负反馈率看板（按场景/模型）。

```javascript
// 反馈闭环
async function feedback(msgId, rating, reason, correction) {
  const r = await api('/feedback', { msgId, rating, reason, correction });
  return { thanks: true, id: r.id,
    note: correction ? '你的修正将用于改进模型' : null };
}
const REASONS = ['事实错误', '答非所问', '有害内容', '格式问题'];
```
