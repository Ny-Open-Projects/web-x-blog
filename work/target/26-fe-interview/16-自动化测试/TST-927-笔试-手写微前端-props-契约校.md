---
title: [TST-927] 笔试：手写微前端 props 契约校验器，支持 required/类型/枚举/向后兼容判定
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-927：笔试：手写微前端 props 契约校验器，支持 required/类型/枚举/向后兼容判定
**答**：
- 需求：实现 validateProps(props, schema, prevSchema) 返回 { valid, errors, breaking }。
- 规则：校验 required 缺失、类型不符、枚举越界；breaking 判定：相比 prevSchema 删除了字段、改了类型、收紧了枚举视为破坏性变更。
- 边界：新增 required 字段且无默认值也是 breaking；prevSchema 缺省时只做基本校验不算 breaking。

```javascript
function validateProps(props, schema, prevSchema) {
  const errors = [], breaking = [];
  for (const k of schema.required || []) if (!(k in props)) errors.push(`缺失必填字段 ${k}`);
  for (const [k, def] of Object.entries(schema.properties || {})) {
    const v = props[k];
    if (v === undefined) continue;
    if (def.type && typeof v !== def.type) errors.push(`${k} 类型应为 ${def.type}，实际 ${typeof v}`);
    if (def.enum && !def.enum.includes(v)) errors.push(`${k} 值 ${v} 不在枚举内`);
  }
  if (prevSchema) {
    const prevProps = prevSchema.properties || {}, curProps = schema.properties || {};
    for (const [k, def] of Object.entries(prevProps)) {
      if (!curProps[k]) breaking.push(`删除字段 ${k}`);
      else if (curProps[k].type !== def.type) breaking.push(`${k} 类型变更`);
      else if (def.enum && curProps[k].enum &&
        def.enum.some(e => !curProps[k].enum.includes(e))) breaking.push(`${k} 枚举收紧`);
    }
    const prevReq = new Set(prevSchema.required || []);
    const curReq = new Set(schema.required || []);
    for (const k of curReq) if (!prevReq.has(k)) breaking.push(`新增必填字段 ${k}（无默认值）`);
  }
  return { valid: errors.length === 0, errors, breaking };
}
const prev = { required: ['userId'], properties: { userId: { type: 'string' } } };
const cur = { required: ['userId', 'token'], properties: { userId: { type: 'string' }, token: { type: 'string' } } };
console.log(validateProps({ userId: 'u1' }, cur, prev).breaking); // ['新增必填字段 token（无默认值）']
```
**评分点**：
- required 缺失、类型不符、枚举越界三类错误均能检出。
- breaking 正确判定：删字段/改类型/收紧枚举/新增必填。
- 新增可选字段不判为 breaking，兼容规则准确。
- prevSchema 缺省时只做基本校验，边界处理完整。
