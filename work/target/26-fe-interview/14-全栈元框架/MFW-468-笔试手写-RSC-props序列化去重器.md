---
title: [MFW-468] 笔试：手写 RSC props 序列化去重器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-468：RSC props 序列化去重器
**需求**：实现 `serializeWithDedup(value)`：1) 同一对象引用在树中出现多次时只序列化一次，第二次起输出 `$ref:id`（Flight 的引用传递语义——大列表页体积减半）；2) 循环引用不爆栈：用 WeakMap 记录访问中节点，再遇到输出 `$ref:循环`；3) 字符串值若本身以 `$` 开头需转义为 `$` + 前缀（Flight 保留前缀语义）；4) 输出 JSON 可逆：提供 `deserialize` 还原共享引用（同一 id 还原后仍为同一对象引用）。

```javascript
export function serializeWithDedup(value) {
  const seen = new Map() // object -> id
  const store = []       // id -> json
  const visiting = new Set()

  function walk(v) {
    if (v !== null && typeof v === 'object') {
      if (visiting.has(v)) return { $ref: 'cycle' }
      if (seen.has(v)) return { $ref: seen.get(v) }
      const id = String(store.length)
      seen.set(v, id)
      visiting.add(v)
      const out = Array.isArray(v) ? v.map(walk) : Object.fromEntries(
        Object.entries(v).map(([k, x]) => [k, walk(x)]))
      visiting.delete(v)
      store[id] = out
      return { $ref: id }
    }
    if (typeof v === 'string' && v.startsWith('$')) return '$' + v // $ 转义
    return v
  }

  walk(value)
  return { refs: store }
}

export function deserialize({ refs }) {
  const resolved = new Array(refs.length)
  const resolve = (v) => {
    if (v && typeof v === 'object' && '$ref' in v) {
      if (v.$ref === 'cycle') return null
      const id = Number(v.$ref)
      if (resolved[id]) return resolved[id] // 同引用还原
      resolved[id] = Array.isArray(refs[id]) ? [] : {}
      const target = resolved[id]
      const src = refs[id]
      if (Array.isArray(src)) src.forEach((x, i) => target[i] = resolve(x))
      else Object.entries(src).forEach(([k, x]) => target[k] = resolve(x))
      return target
    }
    if (typeof v === 'string' && v.startsWith('$$')) return v.slice(1)
    return v
  }
  return resolve({ $ref: '0' }.$ref !== undefined && refs[0] !== undefined ? { $ref: 0 } : refs[0])
}
```

**评分点**：
- 引用去重（对象引用等价而非值等价——Map 键用对象本身）
- visiting 集合断循环（WeakMap/WeakSet 是标准解）
- `$` 前缀转义（协议保留字符不处理即数据损坏）
- 还原后引用同一性（id 缓存复用，不只是值相等）
