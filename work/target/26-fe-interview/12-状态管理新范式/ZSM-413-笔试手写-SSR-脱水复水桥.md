---
title: [ZSM-413] 笔试：手写通用脱水/复水桥（带版本与截断）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-413：手写通用脱水/复水桥（带版本与截断）
**答**：实现 `dehydrate(obj)` 与 `rehydrate(str)`：1) dehydrate 输出 JSON 字符串，附带 `__v` 版本与 `__ts` 时间戳；2) 值内 Date→`{__t:'date',v:ISO}`、Map→`{__t:'map',v:[[k,v]]}`、Set→`{__t:'set',v:[...]}`；3) 循环引用抛错；4) 单条体积超 maxBytes 抛错（防止 HTML 膨胀）；5) rehydrate 还原上述类型并校验版本——版本不符返回 null（调用方走默认值）。

```javascript
const VERSION = 2

function dehydrate(obj, { maxBytes = 50_000 } = {}) {
  const seen = new Set()
  const enc = (v) => {
    if (v instanceof Date) return { __t: 'date', v: v.toISOString() }
    if (v instanceof Map) return { __t: 'map', v: [...v].map(([k, x]) => [enc(k), enc(x)]) }
    if (v instanceof Set) return { __t: 'set', v: [...v].map(enc) }
    const t = typeof v
    if (v === null || t !== 'object') return v
    if (seen.has(v)) throw new Error('circular')
    seen.add(v)
    try {
      return Array.isArray(v) ? v.map(enc) : Object.fromEntries(Object.entries(v).map(([k, x]) => [k, enc(x)]))
    } finally { seen.delete(v) }
  }
  const s = JSON.stringify({ __v: VERSION, __ts: Date.now(), data: enc(obj) })
  if (new TextEncoder().encode(s).length > maxBytes) throw new Error('payload too large')
  return s
}

function rehydrate(str) {
  try {
    const { __v, data } = JSON.parse(str)
    if (__v !== VERSION) return null                 // 版本不符走默认值
    const dec = (v) => {
      if (v && typeof v === 'object') {
        if (v.__t === 'date') return new Date(v.v)
        if (v.__t === 'map') return new Map(v.v.map(([k, x]) => [dec(k), dec(x)]))
        if (v.__t === 'set') return new Set(v.v.map(dec))
        return Array.isArray(v) ? v.map(dec) : Object.fromEntries(Object.entries(v).map(([k, x]) => [k, dec(x)]))
      }
      return v
    }
    return dec(data)
  } catch { return null }
}
```
**评分点**：
- 类型标签编码完备（Date/Map/Set 三类）且 decode 对称
- 版本不符返回 null 而不是报错（复水失败静默降级是产品要求）
- 体积上限在 stringify 后按字节检查（中文多字节陷阱）
- 循环引用检测 + 兄弟重入（finally）
