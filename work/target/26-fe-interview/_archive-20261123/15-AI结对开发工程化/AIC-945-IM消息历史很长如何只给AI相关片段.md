---
title: [AIC-945] IM 消息模块排障时会话历史上千条，如何让 AI 只看到相关片段而不是把聊天记录全贴进去？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-945：IM 消息模块排障时会话历史上千条，如何让 AI 只看到相关片段而不是把聊天记录全贴进去？
**答**：
- 用「检索 + 时间窗 + 角色过滤」组合：先按关键词/错误码检索相关消息，再限定出问题时间前后窗口，最后只保留相关角色（如系统事件、报错日志）的消息。
- 保留「上下文骨架」：给 AI 的不只是命中消息本身，还要带前后各几条（上下文窗口）和会话元信息（ participants、时间线），避免断章取义。
- 结论：目标是「最小充分上下文」——够 AI 理解问题即可，既降本又降低噪声；要给检索结果的相关性打分并设置阈值。
- 追问钩子：能提出「检索片段要标注来源消息 ID，便于 AI 引用和人复核（呼应可追溯）」的候选人，把检索与审计打通了。

```typescript
// IM 排障上下文检索：关键词 + 时间窗 + 上下文骨架
function buildDebugContext(messages, { query, centerId, span = 2 }) {
  const hit = messages.filter(m => m.text.includes(query));
  const centerIdx = messages.findIndex(m => m.id === centerId);
  const window = centerIdx >= 0
    ? messages.slice(Math.max(0,centerIdx-span), centerIdx+span+1) : [];
  const merged = new Map([...hit, ...window].map(m => [m.id, m]));
  return [...merged.values()]
    .sort((a,b) => a.seq - b.seq)
    .map(m => ({ id:m.id, text:m.text, source:'msg-'+m.id })); // 带来源便于追溯
}
console.log(buildDebugContext(
  [{id:1,seq:1,text:'登录成功'},{id:2,seq:2,text:'ERROR 500'},{id:3,seq:3,text:'重试'}],
  { query:'ERROR', centerId:2 }));
```
