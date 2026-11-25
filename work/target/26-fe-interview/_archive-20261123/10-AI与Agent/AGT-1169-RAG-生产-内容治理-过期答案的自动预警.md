---
title: [1169] RAG 答案「内容过时」怎么自动预警
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 内容治理]
type: 面试题
---

## 1169：RAG 答案「内容过时」怎么自动预警

**答**：
- 预警三信号：来源信号（引用文档被标记 superseded/到期）、一致性信号（同意图的新旧文档冲突）、行为信号（该答案的负反馈率随时间上升）——三信号聚合触发「答案过期复核」工单。
- 复核动作分级：自动（检测到新版文档，答案引用自动切新版重新生成）+ 人工（事实类答案要领域 owner 确认）。
- 时效标注体系：答案卡展示「依据文档版本与日期」，用户能自己判断新旧——透明度本身就是治理手段。
- 追问钩子：为什么「行为信号」重要？——文档层面看不出答案过时（文档没更新但事实变了），只有用户行为（重问、点踩上升）能暴露「世界变了而知识库没变」。

```ts
const staleness = signals({
  source: hit => isSuperseded(hit.doc),                     // 来源过期
  consistency: async ans => await conflictWithNew(ans),     // 新旧冲突
  behavior: ans => trendUp(negativeRate(ans), '7d'),        // 负反馈上升
}, { any: 'ticket', all: 'auto_regen' });                    // 单信号开工单，多信号自动重生成
```
