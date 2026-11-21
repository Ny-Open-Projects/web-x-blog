---
title: [AGT-395] 长尾任务——用户自定义/超纲任务的处理策略？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-395：用户提出产品没预设的长尾任务时，Agent 怎么处理？

**答**:
- 处理阶梯：工具组合可达（Agent 自主组合现有工具尝试——通用能力的价值区）、部分可达（完成可达部分+明确缺口声明，AGT-265 部分回答）、不可达（诚实说明能力边界+最接近的替代方案+引导到正确工具）、不应做（安全边界内拒绝）——关键是"尝试的勇气"与"承认边界的诚实"平衡。
- 尝试的安全护栏：未知组合任务的操作降级（新意图默认只读+人审写操作——不认识的任务不自动获得写权限 AGT-283）、步数与成本预算收紧（探索性任务熔断阈值更低 AGT-277）。
- 长尾转化为资产：高频长尾意图聚类（AGT-353）→ 新技能包需求池（AGT-356）→ 产品化——长尾处理记录是产品 roadmap 的真实需求源。
- 期望管理：对用户透明"我在尝试未预设的任务"（标注实验性），失败率预期管理——长尾任务是"惊喜"不是"承诺"，说明书不夸口（AGT-388 不超卖）。

```javascript
async function handleLongtail(task) {
  mark({ experimental: true });                 // 实验性标注
  const caps = lowerDefaults({ writeApproval: true,
    stepBudget: REDUCED });                     // 护栏收紧
  const r = await agent.try(task, caps);
  if (r.partial) return r.withGapStatement();   // 缺口声明
  logIntentCluster(task);                       // 聚类进需求池
  return r;
}
// 阶梯：组合尝试 → 部分+缺口 → 替代引导
// → 边界内拒绝。
```
