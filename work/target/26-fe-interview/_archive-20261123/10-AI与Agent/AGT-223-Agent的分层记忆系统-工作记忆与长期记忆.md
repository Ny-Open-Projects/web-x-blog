---
title: [AGT-223] Agent 的分层记忆——工作记忆/情景记忆/语义记忆怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-223：Agent 的记忆系统怎么分层设计？

**答**:
- 三层模型：工作记忆（当前任务上下文：窗口内的对话+工具结果，会话结束即弃）、情景记忆（历史交互事件：用户说过什么/做过什么任务，按时间线存，可检索回放）、语义记忆（提炼后的稳定知识：用户偏好/项目事实/经验教训，结构化存储）——对应人类记忆的工作/情景/语义三分。
- 写入策略：不是什么都存——写入判据 = 新颖性（与已有记忆不重复）× 未来有用性（偏好/决策/约束值得记），由写入前的小模型判断；噪声记忆会污染检索。
- 检索与注入：新任务开始时按当前任务相关性检索语义与情景记忆注入（带来源与时间戳，过期记忆降权），冲突记忆以时间新者为准并标记冲突。
- 遗忘机制：记忆要有 TTL 与衰减（长期未命中的偏好降权归档）、用户可查看可删除（隐私合规）——记忆系统没有遗忘，就是负债累积。

```javascript
// 分层记忆读写
async function writeMemory(ep) {           // ep: 一轮交互
  const relevant = await searchMemory(ep.text, 5);
  const isNew = await judge(`与已有记忆是否重复？
    ${relevant}`, ep);
  if (isNew) await store({ ...ep,
    type: classify(ep), ts: Date.now() });
}
async function recall(taskQuery, user) {
  const hits = await searchMemory(taskQuery, 10,
    { filter: { user }, decay: true });     // 时间衰减
  return resolveConflicts(hits);            // 新者优先，标记冲突
}
```
