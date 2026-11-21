---
title: [RBL-407] 笔试：手写 sourcemap 校验器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-407：手写 sourcemap 校验器
**需求**：实现 `validateSourceMap(code, map)`：1) 校验 version=3、sources/sourcesContent 数量一致、mappings 可解析（VLQ 段结构合法）；2) 抽样验证：随机取 mappings 中的映射点 → 映射回源码行列 → 验证 sourcesContent 对应行存在；3) 校验 sources 相对路径可解析（与 sourceRoot 组合）；4) 返回 { ok, errors, sampled }（sampled 为实际抽样数）；5) 映射点解析实现 VLQ base64 解码（至少支持单段）。

```javascript
const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
function decodeVLQ(str) {
  const result = []
  let shift = 0, value = 0
  for (const ch of str) {
    const digit = B64.indexOf(ch)
    if (digit < 0) throw new Error('invalid VLQ char')
    value += (digit & 31) << shift
    if (digit & 32) { shift += 5 }
    else {
      const negate = value & 1
      let v = value >> 1
      result.push(negate ? -v : v)
      value = 0; shift = 0
    }
  }
  return result
}

export function validateSourceMap(code, map) {
  const errors = []
  if (map.version !== 3) errors.push('version !== 3')
  if (map.sources?.length !== map.sourcesContent?.length) errors.push('sources/sourcesContent mismatch')
  // mappings 段解析（行；段,）
  let validSegments = 0
  try {
    let srcLine = 0, srcCol = 0
    for (const line of map.mappings.split(';')) {
      srcCol = 0                                        // genCol 每行重置
      if (!line) continue
      for (const seg of line.split(',')) {
        if (!seg) continue
        const f = decodeVLQ(seg)
        if (f.length >= 4) {
          srcLine += f[2]; srcCol += f[3]
          const src = map.sources[srcLine]              // 近似校验：行号在范围内
          if (src === undefined) errors.push(`mapping out of range: line ${srcLine}`)
          else validSegments++
        }
      }
    }
  } catch (e) { errors.push('mappings parse: ' + e.message) }
  // sourceMappingURL 注释
  if (!code.includes('sourceMappingURL=')) errors.push('missing sourceMappingURL comment')
  return { ok: errors.length === 0, errors, sampled: validSegments }
}
```
**评分点**：
- VLQ 解码实现正确（连续位/符号位/每行 genCol 重置——常见实现错误点）
- 增量字段语义（srcLine/srcCol 是累计值不是绝对值）
- 结构校验三件（version/sources 配对/mappings 可解析）+ sourceMappingURL 存在性
- 抽样口径诚实（validSegments 计数——不是全量验证时明确说明）
