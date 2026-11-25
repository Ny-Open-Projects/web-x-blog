---
title: [SCN-973] 医院预约检查（CT/MRI）的时段管理
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-973：医院预约检查（CT/MRI）的时段管理

**答**：
- 时段：检查设备排程（每时段一台机器），禁忌筛查（造影剂过敏史）。
- 流程：开单 -> 预约时段 -> 检查前准备提示（禁食/憋尿）-> 签到。
- 改期：检查前 2 小时可改期，超时改期需重新开单。

```javascript
// 检查预约
async function bookExam(exam, patient) {
  const contra = checkContraindication(exam, patient.history);   // 禁忌
  if (contra) return { ok: false, reason: contra };
  const slots = await api(`/exam/${exam.id}/slots`);
  return { slots: slots.map(s => ({ ...s,
    prep: exam.prep?.[s.type] })),                     // 检查前准备提示
    changeable: true, changeDeadline: '检查前 2 小时' };
}
```
