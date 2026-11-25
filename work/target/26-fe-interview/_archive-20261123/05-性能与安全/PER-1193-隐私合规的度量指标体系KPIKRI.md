---
title: [PER-1193] 隐私合规的度量指标体系（KPI/KRI）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1193：隐私合规的度量指标体系（KPI/KRI）

**答**：
- KPI（治理成效）：字段注册覆盖率 100%、审计通过率、DSAR 按时完成率 100%、培训通过率。
- KRI（风险预警）：未登记采集数（应恒为 0）、敏感日志命中数、撤回未停采事件数（P0）、第三方未评审数。
- 汇报：月度 KRI 看板 + 季度 KPI 报告；KRI 红色即触发专项。
- 基线演进：指标随成熟度收紧（第一年覆盖率，第二年 0 违规）。

```javascript
// 隐私指标看板
function privacyKPI(month) {
  return {
    kpi: { registryCoverage: '100%', dsarOnTime: '100%', trainingPass: '95%' },
    kri: { undeclared: 0, sensitiveLogHits: 2, consentViolations: 0,
      unauditedVendors: 1 },
    alarms: ['sensitiveLogHits > 0', 'unauditedVendors > 0'].filter(x => eval(x)),
  };
}
// alarm 触发 -> 当月专项 + 下月复验
```
