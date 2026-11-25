---
title: [NODE-390] Node 服务的降级框架（统一声明与编排）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-390：Node 服务的降级框架
**答**:
- 降级要框架化而非散落 if：每个可降级能力声明"降级策略 + 触发条件 + 恢复条件"，统一编排器执行——散落的 try/catch 降级无人能盘点全貌。
- 声明结构：feature: { degradeWhen: 'redis-down' | 'err-rate>5%' | 'manual-switch', fallback: () => DEFAULT, alarm: true }；手动开关（NODE-329 配置平台）与自动熔断（NODE-352 熔断器）双通道。
- 编排器职责：触发检测（熔断器状态/配置开关/依赖健康）→ 执行 fallback → 降级事件上报（前端可见"降级徽标"数据来源标记 ARC-447）→ 恢复探测（half-open）→ 恢复通知。
- 分级：核心链路降级策略保守（宁可慢不可错）、边缘功能激进（直接砍）；涉资操作永不静默降级（失败显式报错，ARC-460）。
- 演练验证：降级预案每个都真实演练过（ARC-426），"写了但没触发过"的降级等于没有。
```javascript
const degradeRegistry = {
  recommend: { degradeWhen: c => c.redisDown || c.manual.degrade.recommend,
    fallback: () => HOT_DEFAULTS, level: 'edge' },
  stock: { degradeWhen: c => c.manual.degrade.stock, fallback: () => { throw new ServiceDegraded(); },
    level: 'core' }                                             // 核心链路：显式失败不静默
};
function withDegrade(name, fn) {
  const r = degradeRegistry[name];
  if (r.degradeWhen(ctx)) { reportDegrade(name); return r.fallback(); }
  return fn();
}
```
