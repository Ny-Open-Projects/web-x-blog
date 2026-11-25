---
title: [SCN-1235] AI 产品的审计与合规（企业版日志）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1235：AI 产品的审计与合规（企业版日志）

**答**：
- 审计：企业版对话审计（管理员可查：谁在何时问了什么——员工知情同意）。
- 分类：敏感类目统计（代码/财务/个人信息）合规风险报告。
- 隔离：企业数据不用于模型训练（承诺与配置验证）。

```javascript
// 企业审计
function enterpriseAudit(tenant, period) {
  return {
    sessions: countSessions(tenant, period),
    categories: classifyQueries(tenant, period),       // 敏感类目分布
    piiHits: piiDetected(tenant, period),              // PII 命中（合规风险）
    trainingOptOut: true,                              // 数据不用于训练
    export: () => exportAudit(tenant, period),         // 合规审计导出
  };
}
```
