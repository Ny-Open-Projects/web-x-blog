---
title: [ZSM-410] 笔试：手写 queryKey 规范化器（稳定序列化 + 命中率）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-410：手写 queryKey 规范化器（稳定序列化 + 命中率）
**需求**：实现 `canonicalKey(parts)`：1) 输入数组各元素规范化：对象 key 排序后序列化、Date→ISO、undefined 跳过、数组保序；2) 输出稳定字符串（同语义输入必同输出）；3) `registerKey(key)` 登记 + `stats()` 返回 { unique, total, hitRate }（total 含重复登记，hitRate=1-unique/total）；4) 相同 key 重复登记计为命中（缓存复用信号）；5) 循环引用抛错。

```javascript
export function canonicalKey(parts) {
  const seen = new Set()
  const norm = (v) => {
    if (v === null) return 'null'
    if (v instanceof Date) return `d:${v.toISOString()}`
    const t = typeof v
    if (t === 'number' || t === 'boolean') return `${t}:${v}`
    if (t === 'string') return `s:${v}`
    if (t === 'undefined') return 'u'
    if (t !== 'object') throw new TypeError(`unsupported ${t}`)
    if (seen.has(v)) throw new Error('circular')
    seen.add(v)
    try {
      if (Array.isArray(v)) return `[${v.map(norm).join('|')}]`
      const keys = Object.keys(v).filter((k) => v[k] !== undefined).sort()
      return `{${keys.map((k) => `${k}:${norm(v[k])}`).join(',')}}`
    } finally { seen.delete(v) }
  }
  return parts.map(norm).join('::')
}

const reg = new Map()
export const keyStats = (() => {
  let total = 0
  return {
    registerKey(key) {
      const c = canonicalKey(key)
      reg.set(c, (reg.get(c) ?? 0) + 1); total++
    },
    stats: () => {
      const unique = reg.size
      return { unique, total, hitRate: total === 0 ? 0 : 1 - unique / total }
    },
  }
})()
```
**评分点**：
- 规范化规则完备：对象排序、Date 归一、undefined 剔除、类型前缀防 '1' 与 1 碰撞
- 循环引用检测且兄弟分支可重入（finally 删 seen）
- hitRate 语义正确：total 含重复，unique 为不同 key 数
- 规范化在「进缓存前」做（key 不稳定 = 永不命中，这是命中率问题的根因）
