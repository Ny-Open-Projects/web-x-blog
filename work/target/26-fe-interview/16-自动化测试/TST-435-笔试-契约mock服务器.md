---
title: [TST-435] 笔试：从 schema 生成 mock 响应的最小实现。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-435：笔试：从 schema 生成 mock 响应的最小实现。
**答**：schema `{field: type}`（type 支持 string/number/boolean/array:string）。实现 `mockFromSchema(schema, opts)`：按类型生成确定性假值（string→`mock-{field}`、number→1、array→[值,值]），可选按示例值优先。

```javascript
function mockValue(field, type, example) {
  if (example !== undefined) return example;
  switch (type) {
    case 'string': return `mock-${field}`;
    case 'number': return 1;
    case 'boolean': return true;
    case 'array:string': return [`mock-${field}`];
    default: throw new Error(`未知类型: ${type}（字段 ${field}）`);
  }
}
function mockFromSchema(schema) {
  return Object.fromEntries(
    Object.entries(schema).map(([f, def]) =>
      typeof def === 'object' && 'type' in def
        ? [f, mockValue(f, def.type, def.example)]
        : [f, mockValue(f, def)]));
}
console.log(mockFromSchema({ id: 'string', count: 'number', tags: 'array:string' }));

```

**评分点**：
- 类型→假值映射表（确定性不随机）。
- 示例值优先（schema 有 example 用 example）。
- 数组长度可配置。
- 未知类型报错（schema 缺口）。
