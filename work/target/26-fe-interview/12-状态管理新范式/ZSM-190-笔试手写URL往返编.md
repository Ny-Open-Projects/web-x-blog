---
title: [ZSM-190] 笔试：手写 URL 筛选状态双向转换器（encode/decode 互逆 + 默认值省略）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-190：手写 URL 筛选状态双向转换器（encode/decode 互逆 + 默认值省略）
**需求**：实现 `encodeFilters(filters, schema)` 与 `decodeFilters(sp, schema)`：1) 按 schema 声明字段类型（string/number/enum/list/boolean）；2) decode 对缺失字段填默认值，非法值回退默认值（?page=abc → 1，enum 越界 → def）；3) encode 值等于默认值时不写入（URL 保持干净）；4) 两者互为逆运算：decode(encode(f)) 深等于 f（默认值语义下）；5) list 用逗号分隔并正确转义。

```javascript
export function decodeFilters(sp, schema) {
  const out = {}
  for (const [k, s] of Object.entries(schema)) {
    const raw = sp.get(k)
    if (raw === null) { out[k] = s.def; continue }
    try {
      out[k] = {
        string: () => raw,
        number: () => { const n = Number(raw); if (Number.isNaN(n)) throw 0; return n },
        boolean: () => raw === '1' || raw === 'true',
        enum: () => { if (!s.values.includes(raw)) throw 0; return raw },
        list: () => raw.length ? raw.split(',') : [],
      }[s.type]()
    } catch { out[k] = s.def }                // 非法值回退默认
  }
  return out
}

export function encodeFilters(filters, schema) {
  const sp = new URLSearchParams()
  for (const [k, s] of Object.entries(schema)) {
    const v = filters[k]
    if (deepEq(v, s.def)) continue            // 默认值不写入
    const str = Array.isArray(v) ? v.map(encodeURIComponent).join(',')   // 转义
      : typeof v === 'boolean' ? (v ? '1' : '0')
      : String(v)
    sp.set(k, str)
  }
  return sp
}

function deepEq(a, b) {
  return JSON.stringify(a) === JSON.stringify(b)
}

// const schema = {
//   page: { type: 'number', def: 1 },
//   tags: { type: 'list', def: [] },
//   status: { type: 'enum', def: 'all', values: ['all','paid'] },
// }
// decode(encode({ page: 2, tags: ['a','b'], status: 'all' }), schema)
//   → { page: 2, tags: ['a','b'], status: 'all' }   // status=默认值被省略

// 评分点：
// 1. schema 驱动：类型分派 + 默认值声明
// 2. decode 对缺失/非法值的回退策略（NaN、enum 越界）
// 3. encode 省略默认值 → URL 最短化
// 4. 互逆性：decode∘encode = identity（在默认值语义下）
// 5. list 转义（encodeURIComponent）防逗号内容破坏分隔
```
