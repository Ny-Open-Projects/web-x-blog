---
title: [VIZ-305] 手写图表配置 Schema 校验器（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-305：手写图表配置 Schema 校验器（笔试）

**答**：
- 题目：图表 option schema 校验器——递归校验（type/required/enum/range），错误路径输出，非法字段警告不阻断。
- 思路：schema 描述（JSON Schema 子集）→ 递归校验器；错误路径 $..series[0].type；enum/range 支撑合法值域。
- 评分点：递归校验；错误路径；宽松模式（警告不阻断）。

```javascript
function validateOption(option, schema, path = '$', errors = [], warnings = []) {
  if (schema.type === 'object') {
    for (const [k, sub] of Object.entries(schema.properties ?? {})) {
      if (option[k] === undefined) {
        if (sub.required) errors.push(`${path}.${k}: required`);
        continue;
      }
      validateOption(option[k], sub, `${path}.${k}`, errors, warnings);
    }
    for (const k of Object.keys(option))                   // 未知字段：警告
      if (!schema.properties?.[k])
        warnings.push(`${path}.${k}: unknown field (ignored)`);
  } else if (schema.type === 'array') {
    if (!Array.isArray(option)) { errors.push(`${path}: expected array`); return { errors, warnings }; }
    option.forEach((item, i) => validateOption(item, schema.items, `${path}[${i}]`, errors, warnings));
  } else {
    if (schema.enum && !schema.enum.includes(option))
      errors.push(`${path}: expected one of ${schema.enum}`);
    if (schema.type === 'number' && typeof option !== 'number')
      errors.push(`${path}: expected number`);
  }
  return { errors, warnings };
}
// 用法：validateOption(option, CHART_SCHEMA) → 宽松模式下 warnings 不阻断渲染
```
