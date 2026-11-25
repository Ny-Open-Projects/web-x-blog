---
title: [AGT-855] 线上前端报错，AI 自动归因（聚合错误→定位代码→建议修复）的管线怎么搭？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-855：线上前端报错，AI 自动归因（聚合错误→定位代码→建议修复）的管线怎么搭

**答**：
- 三级管线：① 聚合降噪（错误指纹聚合成 issue，别让 AI 看 1 万条重复报错）；② 归因（每个 issue：堆栈+sourcemap 还原+同时段发布 diff+用户分布 → AI 输出归因假设与置信度）；③ 行动（低置信给排查线索，高置信给修复 PR 草稿——但 PR 永远人工审）。
- 归因的上下文来源：监控数据（影响用户数/版本分布）+ 代码库（报错位置上下文）+ 变更史（最近发布 diff），三源合一才准。
- 闭环：AI 归因命中率人工抽检，命中率数据反哺提示词与上下文策略。

```javascript
async function autoAttribute(issue) {
  const ctx = {
    stack: await sourcemap.resolve(issue.stack),   // 还原源码位置
    release: diffSince(issue.firstSeen),           // 变更史
    stats: { users: issue.users, versions: issue.versions },
  };
  const attr = await llm.attribute(ctx, { format: 'hypothesis+confidence' });
  return attr.confidence > 0.8
    ? draftFixPR(attr)                             // 高置信出PR草稿
    : { clue: attr.reasoning, links: attr.suspects }; // 低置信给线索
}
```
