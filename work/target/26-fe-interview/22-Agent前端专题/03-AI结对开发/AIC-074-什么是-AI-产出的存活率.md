---
title: [AIC-074] 什么是 AI 产出的「7 天存活率」？为什么它比「一次通过率」更诚实？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-074：什么是 AI 产出的「7 天存活率」？为什么它比「一次通过率」更诚实？
**答**：
- 定义：AI 生成的代码在合并后 7 天内未被重写、回滚或大改的比例。7 天是经验窗口——多数「当时能过」的问题（边界、性能、维护性）会在一周内的使用中暴露。
- 比「一次通过率」诚实的原因：一次通过可以被「宽松 review + 妥协合并」刷高；存活率骗不了人，重写意味着之前的生成是负资产。
- 统计口径要清晰：以「函数/文件」还是「PR」为单位要固定；追踪方式用 git blame + AI 标记（生成时在 commit body 记录 co-authored-by: AI 或内部标记）。
- 配套解读：存活率低要区分原因——任务描述不清（人的问题）还是能力边界（工具问题），处理方式完全不同。
- 追问钩子：存活率也是「哪些任务适合 AI」的数据来源——长期低于 50% 的任务类别应改回人工为主。

```javascript
// 7 天存活率统计（基于 commit 标记）
function survivalRate(commits, { windowDays = 7 } = {}) {
  const aiCommits = commits.filter(c => c.body.includes('co-authored-by: AI'));
  const survived = aiCommits.filter(c => {
    const later = commits.filter(k => k.time > c.time + windowDays * 864e5 &&
      k.files.some(f => c.files.includes(f.path)));
    return !later.some(k => k.message.startsWith('revert') || k.rewriteRatio > 0.6);
  });
  return survived.length / aiCommits.length;
}
```
