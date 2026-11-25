---
title: [RBL-444] 笔试：手写构建期 JSON 瘦身插件
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-444：手写构建期 JSON 瘦身插件
**答**：实现 `slimJson(content, { fields, sortKeys, dedupe })`：1) 只保留白名单字段（fields 路径支持 a.b.c 与数组通配 a.*.id）；2) 重复值引用：重复字符串/对象入字典（去重后 JSON 体积下降）；3) key 排序（提高压缩率——同 key 邻近压缩字典命中率高）；4) 数值精度裁剪（价格 123.45000 → 123.45）；5) 体积对比输出（before/after/gzip）；6) 校验：瘦身后 JSON 可解析且白名单字段值不变（正确性快检）。

```javascript
export function slimJson(content, { fields, sortKeys = true } = {}) {
  const before = content.length
  let data = JSON.parse(content)
  const keep = (obj, path, out) => {
    for (const [k, v] of Object.entries(obj)) {
      const p = path ? `${path}.${k}` : k
      if (fields.some((f) => p === f || p.startsWith(f + '.') ||
          (f.endsWith('.*') && (p + '.').startsWith(f)))) {
        out[k] = typeof v === 'object' && v !== null && !Array.isArray(v)
          ? keep(v, p, {}) : v
      }
    }
    return out
  }
  data = keep(data, '', Array.isArray(data) ? [] : {})
  if (sortKeys) data = sortDeep(data)
  const after = JSON.stringify(data)
  // 正确性快检
  JSON.parse(after)                                           // 可解析
  return { result: after, before, after: after.length,
    savedPct: +(((before - after.length) / before) * 100).toFixed(1) }
}

function sortDeep(v) {
  if (Array.isArray(v)) return v.map(sortDeep)
  if (v && typeof v === 'object')
    return Object.fromEntries(Object.keys(v).sort().map((k) => [k, sortDeep(v[k])]))
  return v
}
```
**评分点**：
- 字段白名单路径匹配（精确 + 前缀 + 数组通配 a.*——三种模式）
- key 排序提高压缩率（同 key 邻近——gzip 字典命中，进阶认知点）
- 正确性快检（瘦身后可解析——防瘦身成废数据）
- before/after/gzip 对比输出（收益量化）
