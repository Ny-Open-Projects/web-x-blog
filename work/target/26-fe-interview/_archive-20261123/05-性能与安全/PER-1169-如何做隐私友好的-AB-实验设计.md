---
title: [PER-1169] 如何做"隐私友好"的 A/B 实验设计
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1169：如何做"隐私友好"的 A/B 实验设计

**答**：
- 原则：实验分桶基于假名（非明文 uid）、实验目的写进政策、敏感字段不进实验指标计算。
- 实现：实验平台接入同意门禁（未同意个人化的用户分桶受限，用 cohort 而非个体）。
- 指标计算：在假名层聚合（k-匿名桶）而非个体明细；结果报告过 kAnonymity 检查（1149）。
- 审计：每次实验登记（目的/数据项/时长），到期自动停止。

```javascript
// 隐私友好的实验登记
function experimentRegister(exp) {
  return {
    id: exp.id, purpose: exp.purpose,             // 必填目的
    pseudonymized: true,                          // 分桶用假名
    sensitiveFields: exp.fields.filter(f => FIELD_LEVEL[f] >= 3),
    endDate: exp.endAt,
    autoStop: true,                               // 到期自动停
    kAnonChecked: false,                          // 报告发布前检查
  };
}
// 发布结果前：kAnonymity(rows, ['cohort','page']) 必须通过
```
