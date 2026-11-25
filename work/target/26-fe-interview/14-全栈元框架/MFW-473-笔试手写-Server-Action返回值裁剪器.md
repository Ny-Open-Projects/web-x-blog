---
title: [MFW-473] 笔试：手写 Server Action 返回值裁剪器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-473：Server Action 返回值裁剪器
**答**：实现 `pickActionReturn(result, schema)`：1) schema = { fields: ['id','title'], redact: ['email','phone'] }；2) 只保留 fields 白名单字段，redact 命中的字段（含嵌套数组对象内）整体剔除并记录剔除日志；3) 序列化校验：值必须可过 RSC 序列化（Date/Map 允许，function/Class 实例拒绝并 throw `UnserializableReturn`——Action 返回值走网络）；4) 剔除后体积对比：返回 { data, dropped: [...], bytesBefore, bytesAfter }（审计用）。

```javascript
const isPlain = v => v === null || ['string','number','boolean','undefined'].includes(typeof v)

export function pickActionReturn(result, { fields = [], redact = [] } = {}) {
  const bytesBefore = JSON.stringify(result ?? null)?.length ?? 0
  const dropped = []

  function clean(v, path = '') {
    if (v instanceof Date || v instanceof Map || v instanceof Set) return v
    if (typeof v === 'function' || (v && v.constructor && v.constructor.name !== 'Object' && !Array.isArray(v) && !(v instanceof Date)))
      throw new Error(`UnserializableReturn at ${path}: ${v.constructor?.name}`)
    if (redact.includes(path.split('.').pop())) { dropped.push(path); return undefined }
    if (Array.isArray(v)) return v.map((x, i) => clean(x, `${path}[${i}]`)).filter(x => x !== undefined)
    if (v && typeof v === 'object') {
      const out = {}
      for (const [k, x] of Object.entries(v)) {
        if (fields.length && path === '' && !fields.includes(k) && !redact.includes(k)) continue
        const c = clean(x, path ? `${path}.${k}` : k)
        if (c !== undefined) out[k] = c
      }
      return out
    }
    return v
  }

  const data = clean(result)
  return { data, dropped, bytesBefore, bytesAfter: JSON.stringify(data)?.length ?? 0 }
}
```

**评分点**：
- 白名单优先 + redact 双层（白名单漏配靠 redact 兜敏感字段）
- 嵌套路径穿透（敏感字段藏在数组对象里也要剔）
- function/Class 实例拒绝（RSC 序列化边界——构造器名检测）
- dropped 与字节对比可审计（裁剪本身要可验证）

## 变体与延伸（补充）

**变体与延伸**：

1. `fields` 白名单只在 `path === ''` 生效，嵌套对象就没被裁剪吗 → 是当前实现的缺口，深层要靠每层字段表或仅顶层裁剪加 redact 兜底，需主动说明取舍。
2. `JSON.stringify` 算字节数对 Date/Map 准确吗 → 不准，Date 序列化成字符串、Map 直接变 `{}`，字节数被低估；应改用真实 RSC 序列化后的长度。
3. 返回值里有循环引用会怎样 → `JSON.stringify` 抛错、`clean` 递归也会栈溢出；需要 WeakMap 记录已访问对象或提前显式拒绝。
