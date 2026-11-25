---
title: [RBL-853] 迁移复盘：构建团队的值班 SLA——支持请求的分级与自我服务的边界
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-853：迁移复盘：构建团队的值班 SLA——支持请求的分级与自我服务边界

**答**:
- 平台团队的 SLA 分级：1) **构建不可用**（全员无法构建——P0：15 分钟响应）；2) 单仓库构建故障（P1：当天）；3) 咨询类（怎么配置 X——P2：48h 或引导到文档）；4) 需求类（新特性——进 backlog 不在值班处理）。分级的意义：值班时间被 P0/P1 占据说明平台有系统性问题（要立项修复而不是持续救火）。
- 自我服务的边界设计：文档/工具能解决的不进值班（自检脚本 RBL-822/FAQ RBL-848）——「值班处理的是文档没覆盖的真问题」，每个值班问题都要回答「这能否变成自服务」——值班数据的转化率是平台成熟度指标。
- 值班的成本可见性：工单分类统计（故障/咨询/需求）——咨询类占比高 = 文档缺口（针对性补文档）；故障类占比高 = 平台缺陷（立项）；数据驱动资源分配。
- 事件复盘的轻量化：值班事件的 5 分钟复盘（分类 + 是否可自动化）——不做重复盘，但要留痕；「重复出现 3 次的问题」自动升级为立项候选。
- 追问钩子：为什么「咨询类引导到文档」不是推诿？——值班回答一次的成本 + 下次还要回答；文档沉淀后边际成本归零；且文档回答的一致性比个人回答高（值班者水平不齐）——把「回答」升级为「沉淀」是平台团队规模化的唯一路径，前提是文档可发现性（搜索体验 RBL-673）跟得上。

```javascript
// 值班工单分类与转化
const SLA = {
  P0: { match: (t) => t.allBlocked, respond: 15 * 60_000, channel: 'page' },
  P1: { match: (t) => t.repo && t.broken, respond: 4 * 3600_000, channel: 'assign' },
  P2: { match: (t) => t.question, respond: 48 * 3600_000, channel: 'doc-first' },   // 先查文档命中
};
function intake(ticket) {
  const level = Object.entries(SLA).find(([k, s]) => s.match(ticket))?.[0] ?? 'P2';
  // doc-first：咨询类先查 FAQ
  const faq = level === 'P2' ? searchFAQ(ticket.question) : null;
  if (faq?.score > 0.8) return { level, resolved: 'self-service', faq: faq.id };
  return { level, resolved: 'human', sla: SLA[level].respond };
}
// 月度复盘：分类占比 -> 行动
function monthlyOps(tickets) {
  const byType = groupBy(tickets, 'type');
  return {
    faqCandidates: byType.question?.filter(t => t.repeated >= 3) ?? [],
    platformDefects: byType.broken?.length ?? 0,
    docGap: byType.question?.length / tickets.length,   // > 40% = 文档缺口
  };
}
```
