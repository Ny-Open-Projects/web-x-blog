---
title: [AGT-517] 几十上百个历史会话，列表页的检索、分组与清理交互怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-517：几十上百个历史会话，列表页的检索、分组与清理交互怎么设计

**答**：
- 检索是刚需：标题搜索之外必须支持全文搜（服务端索引），搜索命中要高亮在消息片段而非只有标题。
- 自动分组（今天/近7天/更早）+ 手动置顶/文件夹；AI 生成的会话摘要标题（首答后自动命名）比"新对话 3"体验好一个量级。
- 批量清理给安全网：批量删除进回收站（可恢复 30 天），避免误删焦虑。

```javascript
// 会话自动命名：首轮回答完成后异步生成
async function autoTitle(sessionId, firstAnswer) {
  const title = await llm.chat({ model: 'mini',   // 用便宜模型
    prompt: `用不超过10字概括这个对话主题：${firstAnswer.slice(0, 500)}` });
  api.patchSession(sessionId, { title: title.slice(0, 20) });
}
```

