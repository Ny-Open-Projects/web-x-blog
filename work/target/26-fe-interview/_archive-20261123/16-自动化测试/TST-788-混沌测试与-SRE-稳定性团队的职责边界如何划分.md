---
title: [TST-788] 混沌测试与 SRE/稳定性团队的职责边界如何划分
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-788：混沌测试与 SRE/稳定性团队的职责边界如何划分

**答**：
- 结论：SRE 拥有稳定性目标与平台（SLO、监控、熔断），测试团队拥有验证方法（假设设计、场景、断言），二者在「演练」上交汇协作。
- 分工：SRE 定义稳态指标与兜底能力，测试设计可证伪假设并验证恢复行为，业务团队确认场景的业务相关性。
- 避免真空：要有明确的 RACI，防止「都以为对方负责」导致演练没人做。
- 追问钩子：演练发现的问题没人认领，架构师如何推动？

```javascript
// RACI 矩阵：谁负责什么
const RACI = {
  sloDefinition: { responsible: 'SRE', accountable: 'SRE', consulted: ['test'], informed: [] },
  experimentDesign: { responsible: 'test', accountable: 'SRE', consulted: ['business'], informed: [] },
  execution: { responsible: 'test', accountable: 'SRE', consulted: [], informed: ['business'] },
};
function ownerOf(activity) { return RACI[activity]?.responsible; }
console.log(ownerOf('experimentDesign')); // test
```
