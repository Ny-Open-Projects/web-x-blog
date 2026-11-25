---
title: [JS-361] 并发聚合：Promise.allSettled 的部分失败策略
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-361：并发聚合：Promise.allSettled 的部分失败策略

**答**：
- 聚合三语义：all（一损俱损，适合强依赖）、allSettled（各自结算，适合独立数据块）、any（一荣俱荣，适合多源容灾）——按业务依赖关系选，不是习惯
- 部分失败策略：仪表盘类页面用 allSettled——失败的卡片显示重试态，成功的正常渲染；「部分失败也要能重试单个」，聚合器要保留每个任务的引用
- 关键依赖拆分：聚合中区分「必须成功」（首屏骨架）与「可选增强」（推荐位）——必须失败的进 all，可选的进 allSettled，两层组合
- 超时聚合：任一任务超时不该拖死整页——allSettled + 每任务带超时包装（AbortSignal.timeout），失败即刻结算
- 结果映射：allSettled 返回数组按输入序——用「命名结果对象」而不是下标取值，避免加任务后错位

```javascript
async function loadDashboard() {
  const critical = await Promise.all([           // 必须成功
    api.user(), api.summary(),
  ]);
  const optional = await Promise.allSettled([    // 可选增强
    withTimeout(api.recommend(), 3000),
    withTimeout(api.activity(), 2000),
  ]);
  return {
    ...zip(['user', 'summary'], critical),
    optional: optional.map((r, i) =>
      r.status === 'fulfilled'
        ? { name: NAMES[i], data: r.value }
        : { name: NAMES[i], error: r.reason, retryable: true }),
  };
}
const withTimeout = (p, ms) => Promise.race([p, new Promise((_, rj) => setTimeout(() => rj(new Error('timeout')), ms))]);
```
