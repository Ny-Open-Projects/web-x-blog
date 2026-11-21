---
title: [AIC-164] 笔试：实现一个 Function Calling Schema 校验器：递归校验嵌套对象/数组/枚举，产出友好错误路径？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-164：笔试：实现一个 Function Calling Schema 校验器：递归校验嵌套对象/数组/枚举，产出友好错误路径？
**需求**：实现 `validateFC(args, schema)`：
- 支持 types: string/number/boolean/array/object/enum；array/object 递归 items/properties；
- 错误信息带完整路径（如 `items[2].filters[0].op`）而非笼统「参数错误」；
- 额外字段报错（防止模型夹带私货参数）；number 的 NaN/Infinity 视为非法。

```javascript
function validateFC(args, schema, path = '') {
  const errs = [];
  const add = (p, msg) => errs.push(`${p}: ${msg}`);

  for (const key of Object.keys(args ?? {})) {
    if (!(key in schema)) add(join(path, key), '多余字段（模型夹带）');
  }
  for (const [key, rule] of Object.entries(schema)) {
    const p = join(path, key);
    const v = args?.[key];
    if (v === undefined) { if (rule.required) add(p, '缺少必填字段'); continue; }
    checkValue(v, rule, p, errs);
  }
  return errs;
}

function checkValue(v, rule, p, errs) {
  const t = rule.type;
  if (t === 'enum') {
    if (!rule.values.includes(v)) errs.push(`${p}: 必须是 ${rule.values.join('|')} 之一`);
    return;
  }
  if (t === 'number') {
    if (typeof v !== 'number' || !Number.isFinite(v)) { errs.push(`${p}: 需为有限数字`); return; }
    return;
  }
  if (t === 'array') {
    if (!Array.isArray(v)) { errs.push(`${p}: 需为数组`); return; }
    v.forEach((item, i) => checkValue(item, rule.items, `${p}[${i}]`, errs));
    return;
  }
  if (t === 'object') {
    if (typeof v !== 'object' || v === null || Array.isArray(v)) { errs.push(`${p}: 需为对象`); return; }
    errs.push(...validateFC(v, rule.properties, p));
    return;
  }
  if (typeof v !== t) errs.push(`${p}: 需为 ${t}`);
}
const join = (p, k) => p ? `${p}.${k}` : k;

// 测试
const schema = {
  query: { type: 'string', required: true },
  filters: {
    type: 'array',
    items: { type: 'object', properties: {
      op: { type: 'enum', values: ['eq', 'gt'] },
      val: { type: 'number', required: true },
    } },
  },
};
const args = {
  query: 'x', extra: 1,
  filters: [{ op: 'eq', val: 1 }, { op: 'bad', val: NaN }],
};
console.log(validateFC(args, schema));
// ['extra: 多余字段（模型夹带）', 'filters[1].op: ...', 'filters[1].val: 需为有限数字']
```

**评分点**：
1. 递归结构（array→items、object→properties）与路径拼接是核心，扁平校验只能得一半分；
2. 「多余字段」检测：模型夹带未定义参数是 function calling 高频问题；
3. NaN/Infinity 的 typeof 是 'number'，必须用 Number.isFinite——细节陷阱；
4. 错误信息带完整索引路径，可直接回喂模型定位修复；
5. enum 用专用分支而非字符串猜测。
