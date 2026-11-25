---
title: [AIC-668] 怎么度量 AI 是否真降低了团队「认知负荷」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-668：怎么度量 AI 是降低了还是增加了团队「认知负荷」？

**答**：
- 结论先行：**AI 把「写代码」的负荷转成了「审代码 + 管 AI」的负荷，总负荷未必下降——度量要同时看「编写负荷↓」和「审查负荷↑」，而非只看前者**（AIC-018 人的注意力放在哪）。
- 认知负荷的三个来源：1) **内在负荷**：理解业务逻辑本身的难度（不变）；2) **外在负荷**：理解工具/流程/AI 脾气的负担（AI 可能增加——要学 prompt、要验证幻觉）；3) **相关负荷**：用于创造性架构设计的「有效负荷」（希望 AI 释放的）。
- 度量方法（代理指标）：1) **审查时长占比**：如果人花在 review AI 代码的时间 > 写代码的节省，认知负荷没降；2) **上下文切换次数**（AIC-612 心流）：AI 频繁打断增加切换成本；3) **主观量表**：开发者自评「心智负担」打分（NASA-TLX 简化版）；4) **上手时间**：新人用 AI 后多久能独立交付——若变长说明外在负荷增加。
- 关键洞察：Senior 用 AI 认知负荷降（他能快速判断 AI 对错），新手可能升（他缺乏判断力，还得额外学验证）——度量要分层看，别被平均值骗（AIC-069）。
- 追问钩子：为什么「审查时长」是认知负荷的关键代理？——因为审查是「理解 + 判断」的高认知活动；AI 把编码（相对机械）外包了，但审查（高认知）留给人还增加了量；如果审查时间暴涨，说明 AI 只是把负荷从低认知转移到高认知环节，人反而更累。

```typescript
type Workload = { codingMin: number; reviewMin: number; switchCount: number; selfRating: number }; // selfRating 1-10 越高越累

function cognitiveLoad(before: Workload, after: Workload) {
  const beforeTotal = before.codingMin + before.reviewMin + before.switchCount * 2; // 切换成本折算2分钟
  const afterTotal = after.codingMin + after.reviewMin + after.switchCount * 2;
  return {
    beforeTotal, afterTotal,
    delta: afterTotal - beforeTotal,
    reduced: afterTotal < beforeTotal,
    reviewIncreased: after.reviewMin > before.reviewMin,
    note: after.reviewMin > before.reviewMin ? '审查负荷上升，需关注是否转嫁而非减少' : undefined,
  };
}

const r = cognitiveLoad(
  { codingMin: 300, reviewMin: 60, switchCount: 5, selfRating: 5 },
  { codingMin: 100, reviewMin: 220, switchCount: 20, selfRating: 7 },
);
console.log(r.codingMin === undefined); // 只读字段不返回
console.log(r.reviewIncreased === true && r.reduced === false); // 编码省200，审查多160+切换多30，净增
```
