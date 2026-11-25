---
title: [NODE-690] 优雅降级框架（统一降级中间件）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-690：降级框架怎么做？
**答**：
- 统一降级抽象：声明式降级（每个接口声明 fallback 数据源/策略——SCN-NODE-644 部分成功体系化）；降级中间件统一执行（熔断触发 → 查找 fallback → 返回降级响应 + 降级标记——SCN-NODE-669 熔断配套）。
- 降级策略库：缓存兜底（last good——SCN-NODE-669）、默认值、裁剪（去非核心字段）、静态内容——策略组合声明。
- 降级开关矩阵：全局降级开关（大促预案——SCN-OPS-329 降级矩阵服务端版）+ 自动降级（熔断触发）——手动与自动两级。
- 降级可观测：降级率看板 + 降级原因统计（哪个下游/哪个策略）——降级不是静默的。
- 追问钩子：为什么降级响应要带「降级标记」——前端需要知道数据是降级的（展示「数据可能延迟」/隐藏实时性敏感的 UI）；运营需要降级率数据（降级面评估）——无标记的降级会让「陈旧数据被当实时数据」使用，决策失真（SCN-联想-675 健康度可见同源）。

```javascript
const fallbacks = defineFallbacks({
  '/api/recommend': { strategy: 'cache', ttl: 300, mark: 'stale' },
  '/api/stock': { strategy: 'default', value: 'INQUIRY', mark: 'degraded' },
});
app.use(degradeMiddleware(fallbacks, breakers));       // 熔断触发自动降级
res.setHeader('X-Degraded', '1');                      // 降级标记（前端可感知）
```
