---
title: [TST-569] 如何用 AI 合成测试测试数据
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-569：如何用 AI 合成测试测试数据

**答**：
- 结论：AI 适合生成「结构正确 + 语义合理 + 覆盖边界」的仿真数据（如各类商品、用户、地址），比手写更丰富；但必须经 schema 校验与隐私脱敏。
- 做法：用 schema/约束驱动生成（ Few-shot 给样例）；对生成数据做合法性校验（类型/范围/唯一）；避免生成真实个人信息；标注合成数据来源，防止进生产。
- 追问钩子：AI 生成数据会不会引入偏差导致漏测？——会（如只生成「正常」数据）；要在 Prompt 中显式要求边界/异常样本，并用覆盖率与变异分数验证数据多样性。

```javascript
// 合成数据校验：schema 合法性 + 隐私脱敏
function validateSynthetic(data, schema) {
  const errors = [];
  for (const [k, rule] of Object.entries(schema)) {
    const v = data[k];
    if (rule.type === 'number' && !(v >= rule.min && v <= rule.max)) errors.push(`${k} 越界`);
    if (rule.type === 'string' && (v?.length || 0) > rule.maxLen) errors.push(`${k} 过长`);
    if (rule.required && v == null) errors.push(`${k} 缺失`);
  }
  const pii = /1[3-9]\d{9}|\d{17}[\dX]/i.test(JSON.stringify(data));
  return { valid: errors.length === 0 && !pii, errors, pii };
}
```
