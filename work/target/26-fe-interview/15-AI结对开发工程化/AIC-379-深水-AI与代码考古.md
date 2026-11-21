---
title: [AIC-379] 「这段代码是谁为什么在什么时候写的」——AI 代码考古如何做？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-379：「这段代码是谁为什么在什么时候写的」——AI 代码考古如何做？
**答**：
- 多层证据聚合：git blame → commit → PR（描述与评审）→ 关联 issue/事故。
- 时间线输出：该区域的历史变更时间线 + 每次变更的动机（从 PR/issue 提取）。
- 区分事实与推断：git 记录是事实，动机推断要标注「推断」与置信度。
- 用途：接手遗留代码/评估改动风险/避免「好心修复」破坏隐含设计意图。

```javascript
async function archaeology(file: string) {
  const blames = await blame(file);
  const timeline = await Promise.all(blames.map(async b => ({
    when: b.commit.date, what: b.commit.message,
    why: await motive(b.commit.pr),   // PR/issue 提取，标注推断置信度
  })));
  return timeline; // 接手者先读时间线再动代码
}
r
```
