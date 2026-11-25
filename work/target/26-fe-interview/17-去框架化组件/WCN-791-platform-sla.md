---
title: [WCN-791] 组件平台的 SLA 指标体系如何定义并向业务方承诺？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-791：组件平台的 SLA 指标体系如何定义并向业务方承诺？

**答**：
- 结论：SLA 分三层——可用性（文档站/构建服务 99.9%）、时效（组件发布 ≤10 分钟、issue 响应 ≤1 工作日）、质量（构建成功率 ≥99%、API 契约零破坏）。
- 指标要可测量、可归因、有错误预算；与 SRE 对齐监控与告警；对外承诺写入服务目录，对内驱动改进。
- 追问钩子：SLA 没达标对业务方怎么补偿/沟通？考察「透明通报 + 根因分析 + 改进承诺」的成熟度。

```javascript
const SLA = {
  availability: 0.999,
  publishMinutes: 10,
  buildSuccessRate: 0.99,
  issueResponseHours: 24,
};
function checkSLA(actual) {
  const errs = [];
  if (actual.availability < SLA.availability) errs.push('可用性未达标');
  if (actual.publishMinutes > SLA.publishMinutes) errs.push('发布时效未达标');
  if (actual.buildSuccessRate < SLA.buildSuccessRate) errs.push('构建成功率未达标');
  return errs;
}
console.log(checkSLA({ availability: 0.995, publishMinutes: 8, buildSuccessRate: 0.995 }));
```
