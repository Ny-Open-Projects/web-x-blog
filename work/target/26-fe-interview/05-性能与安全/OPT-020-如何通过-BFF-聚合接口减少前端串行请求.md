---
title: [OPT-020] 如何通过 BFF 聚合接口减少前端串行请求？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-020：如何通过 BFF 聚合接口减少前端串行请求？

**答**：
- 前端页面常需要"用户信息 + 订单 + 推荐"三份数据，分别请求客户端要串行/并行多次往返，还可能造成瀑布。
- BFF（Backend For Frontend）层提供一个聚合接口：并行调用下游微服务，统一裁剪字段后一次性返回。
- 落地要点：用 `Promise.allSettled` 并行调用并做**部分失败降级**（某个下游挂了不能拖垮整页）；设置整体超时；对稳定数据加短 TTL 缓存。
- 收益：请求数从 N 到 1，弱网下减少 RTT 往返，前端逻辑简化。

```javascript
// 一一对应：BFF 聚合接口，并行调用 + 部分失败降级
import express from 'express';
const app = express();

app.get('/api/page-data', async (req, res) => {
  const timeout = (p, ms) => Promise.race([
    p,
    new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), ms)),
  ]);

  // 并行调用三个下游服务，互不等待
  const [user, orders, recommend] = await Promise.allSettled([
    timeout(fetch('http://user-svc/api/user?id=' + req.query.uid).then((r) => r.json()), 800),
    timeout(fetch('http://order-svc/api/orders?uid=' + req.query.uid).then((r) => r.json()), 800),
    timeout(fetch('http://rec-svc/api/rec?uid=' + req.query.uid).then((r) => r.json()), 800),
  ]);

  // 只取需要的字段，部分失败返回降级默认值
  res.json({
    user: user.status === 'fulfilled' ? user.value : null,
    orders: orders.status === 'fulfilled' ? orders.value.list.slice(0, 10) : [],
    recommend: recommend.status === 'fulfilled' ? recommend.value : [],
  });
});

app.listen(3000);
```
