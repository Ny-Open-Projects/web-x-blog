---
title: [PER-1037] 接口聚合与 BFF：减少前端请求轮次的架构手段
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1037：接口聚合与 BFF：减少前端请求轮次的架构手段

**答**：
- 问题：页面依赖 8 个接口串并行请求，任何慢接口拖住首屏；HTTP 层无法解决"轮次"问题。
- BFF 聚合：前端一次请求，BFF 内并行调下游并组装；数据裁剪只回所需字段，省带宽与解析。
- GraphQL 对比：字段级按需 + 单端点，适合复杂页面；简单场景 REST + BFF 聚合更轻。
- 注意：BFF 是新的故障点——超时传导、缓存策略、限流都要重新设计；聚合接口本身要有 SLO。

```javascript
// BFF 聚合示意
app.post('/bff/page-data', async (req, res) => {
  const { pageId } = req.body;
  const [user, items, banners] = await Promise.allSettled([
    svc(`/user/${req.uid}`),
    svc(`/items?page=${pageId}`),
    svc('/banners'),
  ]);
  res.json({
    user: user.status === 'fulfilled' ? user.value : null,      // 局部降级
    items: items.status === 'fulfilled' ? items.value.slice(0, 20) : [],
    banners: banners.status === 'fulfilled' ? banners.value : [],
  });   // 前端一次 RTT 拿全；每个子服务独立超时 500ms
});
```
