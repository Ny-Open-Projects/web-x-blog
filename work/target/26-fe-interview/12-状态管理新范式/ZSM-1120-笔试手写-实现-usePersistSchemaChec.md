---
title: [1120] 笔试手写：实现 usePersistSchemaCheck
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 持久化]
type: 笔试题
---

## 1120：笔试手写：实现 usePersistSchemaCheck

**答**：恢复持久化数据前做 schema 校验。实现 hydrateSafe(raw, schema, fallback)：schema 为 { field: 'string'|'number'|'boolean'|'array'|'object' }。逐字段校验类型；全部通过返回解析值；任一失败返回 fallback()（干净默认值）并记录坏字段；raw 本身 JSON 解析失败同样走 fallback。

```js
function hydrateSafe(raw, schema, fallback) {
  let data;
  try { data = JSON.parse(raw); }
  catch (e) { return { value: fallback(), badFields: ['<parse>'] }; }
  const bad = [];
  const check = {
    string: v => typeof v === 'string',
    number: v => typeof v === 'number' && Number.isFinite(v),
    boolean: v => typeof v === 'boolean',
    array: v => Array.isArray(v),
    object: v => v !== null && typeof v === 'object' && !Array.isArray(v),
  };
  for (const [f, t] of Object.entries(schema)) {
    const v = data[f];
    if (v === undefined) continue; // 缺字段允许（增量演进）
    if (!check[t](v)) bad.push(f);
  }
  if (bad.length) return { value: fallback(), badFields: bad };
  return { value: data, badFields: [] };
}
```

**评分点**：
- JSON 解析失败与字段校验失败统一 fallback（坏数据不进 store）
- 类型检查表驱动（check 映射）
- 缺字段宽容、坏字段严格（向后兼容 vs 数据安全的平衡）
- 能讨论：fallback 的内容应是 store 初始值工厂而非 {}（防字段缺失引发下游崩溃）
