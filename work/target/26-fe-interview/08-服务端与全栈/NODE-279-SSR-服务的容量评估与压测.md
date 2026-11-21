---
title: [NODE-279] SSR 服务的容量评估与压测？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-279：SSR 服务的容量评估与压测？
**答**:
- 容量公式：单实例并发 = 核数 × 渲染并发系数；单实例 QPS = 并发 / 渲染耗时 P95——先实测单实例基线再乘实例数。
- 压测口径：真实页面混压（流量模型按大盘分布），不是单一页面打满——热点页面单独压测定水位线。
- 弱点暴露：压测要覆盖"慢下游"场景（模拟下游 2s 延迟）——验证降级与队列策略（NODE-272）真的生效。
- 大促预案：预扩容（HPA 提前 1h）+ 渲染降级开关（SSR→CSR）+ 静态化预热（NODE-273 ISR 预生成）。

```javascript
// 压测脚本（混压）
const scenarios = [
  { path: '/', weight: 60 }, { path: '/list', weight: 25 }, { path: '/detail/:id', weight: 15 },
];
// autocannon 按权重轮询路径；下游故障注入：
chaos.inject({ match: /\/api\/recommend/, delay: 3000 });   // 模拟慢下游
// 验证：降级率（fallback 比例）上升但 P95 不爆炸 —— NODE-272 队列生效
// 容量：单实例 100 QSS × 40 实例 → 大促峰值 4000 QPS 渲染（其余走 CDN 缓存）
```
