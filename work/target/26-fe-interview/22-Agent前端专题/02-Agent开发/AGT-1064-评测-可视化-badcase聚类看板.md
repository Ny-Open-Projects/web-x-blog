---
title: [1064] badcase 看板怎么设计才有人看
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 评测, 看板]
type: 面试题
---

## 1064：badcase 看板怎么设计才有人看

**答**：
- 看板三区：趋势区（失败率周趋势，按归因类别堆叠）、聚类区（本周 badcase 语义聚类 top10 簇，每簇显示代表 case 与规模）、行动区（每簇的处理状态：已修/修复中/搁置——看板的价值在行动闭环）。
- 聚类用嵌入向量 + 层次聚类，簇标签用 LLM 生成短语（「检索空-政策类」「格式漂移-表格」）；簇要稳定（同一簇跨周 ID 不变）才能看修复进度。
- 反模式警示：只放原始列表的看板没人看（几百条谁翻得动）、只放分数的看板没法行动——「聚类 + 状态」才是可行动视图。
- 追问钩子：簇大小怎么定优先级？——按「规模 × 严重度 × 可修复性」打分排序，规模最大但不可修的降级，可修且高发的优先派工。

```ts
async function board(failures) {
  const clusters = await cluster(embed(failures), { method: 'hier', stable: true });
  const labeled = await Promise.all(clusters.map(async c => ({
    id: c.stableId, size: c.items.length,
    label: await llmLabel(c.representative),
    priority: c.items.length * severity(c) * fixability(c),
    status: tracker.of(c.stableId) ?? 'new',       // 行动闭环
  })));
  return sort(labeled, 'priority');
}
```
