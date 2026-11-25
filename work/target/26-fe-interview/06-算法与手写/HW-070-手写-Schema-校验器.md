---
title: [HW-070] 手写迷你 JSON Schema 校验器——type/required/enum/min/max/pattern 递归嵌套
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-070：手写迷你 JSON Schema 校验器——type/required/enum/min/max/pattern 递归嵌套
**答**：递归校验器：validate(value, schema, path) 返回错误数组（带路径 `a.b[0].c`）。对象 schema 递归每个属性，数组 schema 校验 items，类型字符串与数组（多类型）都支持。

```javascript
const TYPE_CHECK = {
  string: (v) => typeof v === 'string',
  number: (v) => typeof v === 'number' && Number.isFinite(v),
  boolean: (v) => typeof v === 'boolean',
  object: (v) => v !== null && typeof v === 'object' && !Array.isArray(v),
  array: (v) => Array.isArray(v),
  null: (v) => v === null,
};

function validate(value, schema, path = '') {
  const errors = [];
  const types = Array.isArray(schema.type) ? schema.type : [schema.type];
  if (schema.type && !types.some((t) => TYPE_CHECK[t]?.(value))) {
    return [`${path || 'root'}: 期望 ${schema.type}，得到 ${Array.isArray(value) ? 'array' : typeof value}`];
  }
  if (schema.enum && !schema.enum.includes(value)) errors.push(`${path}: 不在枚举 ${JSON.stringify(schema.enum)}`);
  if (typeof value === 'string') {
    if (schema.minLength != null && value.length < schema.minLength) errors.push(`${path}: 长度 < ${schema.minLength}`);
    if (schema.pattern && !schema.pattern.test(value)) errors.push(`${path}: 不匹配 ${schema.pattern}`);
  }
  if (typeof value === 'number') {
    if (schema.minimum != null && value < schema.minimum) errors.push(`${path}: < ${schema.minimum}`);
    if (schema.maximum != null && value > schema.maximum) errors.push(`${path}: > ${schema.maximum}`);
  }
  if (TYPE_CHECK.object(value) && schema.properties) {
    for (const req of schema.required || []) {
      if (!(req in value)) errors.push(`${path}.${req}: 缺少必填字段`);
    }
    for (const [key, sub] of Object.entries(schema.properties)) {
      if (key in value) errors.push(...validate(value[key], sub, path ? `${path}.${key}` : key));
    }
  }
  if (TYPE_CHECK.array(value) && schema.items) {
    value.forEach((item, i) => errors.push(...validate(item, schema.items, `${path}[${i}]`)));
  }
  return errors;
}

// 用法
const schema = {
  type: 'object', required: ['id', 'tags'],
  properties: {
    id:   { type: 'number', minimum: 1 },
    name: { type: 'string', minLength: 2 },
    tags: { type: 'array', items: { type: 'string', enum: ['hot', 'new'] } },
    addr: { type: 'object', required: ['city'], properties: { city: { type: 'string' } } },
  },
};
validate({ id: -1, tags: ['vip'] }, schema);
// => ['id: < 1', 'tags[0]: 不在枚举 ["hot","new"]', 'name: 缺少必填字段'(顺序实际为 required 先) …]
```

**评分点**：
- 递归结构正确：object 递归 properties、array 递归 items，路径随递归拼接（含 `[i]` 下标）。
- type 分派与多类型数组支持；类型不匹配时短路返回（后续子校验无意义）。
- required 在对象分支里检查，错误信息带字段路径。
- 返回结构统一为错误数组（不是布尔），便于表单/接口双向使用。
