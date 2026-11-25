---
title: [1096] 笔试手写：实现按 schema 的深度假名化与字段剥离
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 安全, 数据处理]
type: 笔试题
---

## 1096：笔试手写：实现按 schema 的深度假名化与字段剥离

**答**：实现 conform(data, schema)：schema 为 { type: 'object', props: { name: { type: 'string' }, age: { type: 'number' }, addr: { type: 'object', props: { city: 'string' } } }, extra: 'strip' }。规则：仅保留 schema 声明的字段（剥离额外字段，递归）；类型不符的字段删除；数组按 item schema 逐项处理。返回清洗后数据。

```js
function conform(data, schema) {
  if (schema.type === 'object') {
    if (!data || typeof data !== 'object' || Array.isArray(data)) return undefined;
    const out = {};
    for (const [k, sub] of Object.entries(schema.props || {})) {
      if (!(k in data)) continue;
      const v = conform(data[k],
        typeof sub === 'string' ? { type: sub } : sub);
      if (v !== undefined) out[k] = v;      // 类型不符/未通过的被删除
    }
    return out;                              // 额外字段天然被丢弃
  }
  if (schema.type === 'array') {
    if (!Array.isArray(data)) return undefined;
    return data.map(x => conform(x, schema.items)).filter(v => v !== undefined);
  }
  return typeof data === schema.type ? data : undefined;
}
const s = { type: 'object', props: { name: 'string', addr: { type: 'object', props: { city: 'string' } } } };
console.log(conform({ name: 'A', hack: 'x', addr: { city: 'BJ', zz: 1 } }, s));
// { name: 'A', addr: { city: 'BJ' } }  hack 与 zz 被剥离
```

**评分点**：
- 递归剥离额外字段（恶意载荷藏匿点被清除）
- 类型不符删除而非报错（安全清洗语义）
- 数组逐项处理 + undefined 过滤
- 能讨论：schema 校验库（zod）生产替代手写；剥离与告警结合（被剥离字段记录审计）

