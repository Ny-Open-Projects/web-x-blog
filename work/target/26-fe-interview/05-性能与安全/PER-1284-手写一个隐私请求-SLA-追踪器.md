---
title: [PER-1284] 手写一个隐私请求 SLA 追踪器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1284：手写一个隐私请求 SLA 追踪器

**答**：
- 需求：implement dsarSla(tickets, slaDays)。tickets 为 [{ id, type, submittedAt, completedAt }]；输出 { onTime: [id], late: [{ id, daysOver }], pending: [{ id, daysLeft }] }；late = completedAt - submittedAt > slaDays；pending 为未完成的（剩余天数，负数即已逾期）。
- 边界：completedAt 缺失为 pending；type 不影响 SLA（统一）；按逾期天数降序；空输入全空。
- 评分点：三态分类；逾期天数；剩余天数；排序

```javascript
function dsarSla(tickets, slaDays = 30) {
  const now = Date.now();
  const onTime = [], late = [], pending = [];
  for (const t of tickets) {
    if (!t.completedAt) {
      const left = +(slaDays - (now - t.submittedAt) / 86400_000).toFixed(1);
      pending.push({ id: t.id, daysLeft: left });
    } else {
      const days = (t.completedAt - t.submittedAt) / 86400_000;
      if (days > slaDays) late.push({ id: t.id, daysOver: +(days - slaDays).toFixed(1) });
      else onTime.push(t.id);
    }
  }
  late.sort((a, b) => b.daysOver - a.daysOver);
  return { onTime, late, pending };
}
```
