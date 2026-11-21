---
title: [NODE-408] Node 服务的混沌演练（依赖故障/资源耗尽）如何开展？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-408：Node 服务的混沌演练
**答**:
- 演练对象按风险排序：依赖故障（DB/Redis/MQ 延迟与不可用——验证降级与熔断）、网络故障（丢包/分区）、资源耗尽（连接池打满/内存压力/磁盘满）、实例级故障（杀 Pod——K8s 自愈与流量迁移）。
- 演练方法：生产环境小流量灰度域内注入（可控爆炸半径）、注入工具（ChaosBlade/Litmus：网络延迟 tc、依赖故障 proxy）+ 应用层开关（内置故障注入 NODE-426 配合）。
- 验收标准每场景定义："Redis 挂 5 分钟 → 用户侧错误率 < 0.1%（降级生效）、恢复后 1 分钟内自动回切"；不达标 = 降级缺陷，进修复队列。
- 安全护栏：演练范围白名单（灰度实例/测试租户）、一键终止、演练窗口避开业务高峰、提前周知值班与下游。
- 节奏：月度例行（单场景）、季度大演练（组合故障 + 容灾切换 ARC-459）、新能力上线必演练（降级框架 NODE-390 的每个声明）。
```javascript
// 应用层故障注入开关（配合演练）
app.use((ctx, next) => {
  const rule = chaos.match(ctx.path);                 // { path:/api/goods, delayMs:3000, errRate:0.5 }
  if (rule && chaos.enabled && ctx.gray === 'chaos') {
    if (rule.delayMs) ctx.delay = rule.delayMs;
    if (Math.random() < rule.errRate) return ctx.throw(503);
  }
  return next();
});
```
