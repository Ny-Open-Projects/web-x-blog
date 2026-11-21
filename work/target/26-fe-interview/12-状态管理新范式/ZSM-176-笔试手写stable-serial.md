---
title: [ZSM-176] 笔试：手写 stableStringify（缓存 key 稳定序列化器）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-176：手写 stableStringify（缓存 key 稳定序列化器）
**需求**：实现 `stableStringify(value)`：1) 对象 key 按字典序排序后序列化，保证相同结构不同书写顺序输出一致（缓存 key 命中同一条目）；2) 数组保序；3) 支持 null/undefined/数字/布尔/字符串/嵌套对象/数组；4) undefined 的对象属性直接跳过，数组中的 undefined 保留为 null；5) 循环引用抛出明确错误。要求 O(n)，不依赖 JSON.stringify 对 key 的固定顺序。

```javascript
export function stableStringify(value) {
  const seen = new Set()
  return serialize(value)

  function serialize(v) {
    if (v === null) return 'null'
    const t = typeof v
    if (t === 'number') return Number.isFinite(v) ? String(v) : 'null'
    if (t === 'boolean') return String(v)
    if (t === 'string') return JSON.stringify(v)
    if (t === 'undefined') return 'null'           // 数组内 undefined → null
    if (t !== 'object') throw new TypeError(`unsupported type: ${t}`)

    if (seen.has(v)) throw new Error('circular reference')  // 循环引用
    seen.add(v)
    try {
      if (Array.isArray(v)) {
        return '[' + v.map(serialize).join(',') + ']'        // 数组保序
      }
      const keys = Object.keys(v)
        .filter(k => v[k] !== undefined)                     // 属性 undefined 跳过
        .sort()                                              // key 稳定排序
      return '{' + keys
        .map(k => JSON.stringify(k) + ':' + serialize(v[k]))
        .join(',') + '}'
    } finally {
      seen.delete(v)                                          // 允许兄弟分支重入
    }
  }
}

// 评分点：
// 1. 对象 key 排序后序列化，两份异序对象输出一致
// 2. 数组保序不排序（顺序是语义）
// 3. 属性 undefined 跳过、数组内 undefined 转 null 的区分处理
// 4. 循环引用用 seen 集合检测且 try/finally 恢复，兄弟分支不受污染
// 5. 字符串经 JSON.stringify 保证转义正确
```
