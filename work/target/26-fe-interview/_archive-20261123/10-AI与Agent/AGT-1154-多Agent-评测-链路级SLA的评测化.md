---
title: [1154] 「链路 SLA」怎么从口号变成评测断言
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, SLA]
type: 面试题
---

## 1154：「链路 SLA」怎么从口号变成评测断言

**答**：
- SLA 评测化：把「P95 < 30s、成功率 > 99%、成本 < $0.5」写成夜间评测的断言项（固定任务集回放计时），违规即红——SLA 从监控图表升级为门禁。
- 固定任务集的选择：SLA 任务集要覆盖「典型路径 + 最重路径」（最重路径决定 P95 上限），且 mock 外部波动（否则外部抖动污染结论）。
- 分环境 SLA：预发环境压测 SLA 与生产监控 SLA 双轨——预发验证「设计容量」，生产验证「真实体验」。
- 追问钩子：SLA 违规的第一反应是什么？——不是调阈值，而是定位漂移来源：任务集变重了（业务变了）还是系统变慢了（退化），两者解法完全不同。

```ts
const sla = { p95Ms: 30000, successRate: 0.99, costMax: 0.5 };
async function nightlySla() {
  const rs = await Promise.all(slaTaskSet.map(t => timed(run(t))));
  const p95 = quantile(rs.map(r => r.ms), 0.95);
  const ok = p95 < sla.p95Ms && rate(rs) > sla.successRate;
  if (!ok) gate('sla', { p95, drift: await classifyDrift(rs) }); // 定位漂移来源
}
```
