---
title: [ARC-279] 灰度与 AB 的监控对账与自动止损如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-279：灰度与 AB 的监控对账与自动止损如何设计？
**答**：
- 对账三层：分桶对账（进桶用户数与配置比例一致，防 SRM）、指标对账（新版本核心指标 vs 对照组）、日志对账（版本指纹覆盖率——有多少请求没带版本标，丢失标等于盲飞）。
- 自动止损规则：灰度桶错误率 > 对照 2 倍且持续 10 分钟 → 自动缩比例至 0（回滚版本指针）；护栏指标破线 → 暂停放量等待人工。
- 止损动作分级：暂停放量（可逆）→ 缩量回滚（秒级，ARC-276 指针回拨）→ 告警人工介入。每级有明确触发条件，避免"人工犹豫期"放大故障。
- 防误杀：规则阈值考虑流量小时级波动（同环比而非绝对值），重要止损动作留"一次撤销"窗口。

```typescript
// 止损引擎（平台侧）
setInterval(async () => {
  const g = await metrics.window('v2', '10m');
  const c = await metrics.window('v1', '10m');
  if (g.errRate > c.errRate * 2 && g.sample > 500) {
    grayConfig.ratio = 0;                                     // 自动回滚版本指针
    audit.log('auto-rollback', { errRate: g.errRate, control: c.errRate });
    notify.oncall('gray auto rollback');
  }
}, 60_000);
// 护栏：whiteRate(v2) > 0.5% → pause('no-more-ramp-up')，等人工判断
```
