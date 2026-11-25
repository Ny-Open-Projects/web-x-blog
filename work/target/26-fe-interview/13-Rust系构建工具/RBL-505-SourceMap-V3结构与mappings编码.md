---
title: [RBL-505] SourceMap V3 结构与 VLQ mappings 编码
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-505：SourceMap V3 结构与 VLQ mappings 编码

**答**：
- SourceMap V3 五要素：`version/sources/sourcesContent/names/mappings`。核心是 **mappings**：分号分段（生成文件每行一段）、逗号分组（每段的映射项）、每项是 **VLQ 编码的相对差值五元组**（生成列、源索引、源行、源列、名字索引）。
- VLQ（Base64 变长编码）：每个数拆 5-bit 组、低位在前、连续位最高位为续传标志——相对差值设计（相对上一项，而非绝对值）让相邻映射数值小、编码紧凑——这是「为什么 mappings 是天书」的答案。
- 生成侧的要点：codegen 输出「生成列位置 + 对应 AST 节点 span」→ sourcemap builder 按行分组排序 → 前项差值 VLQ 编码。**列差值可能为负**（回绕）——VLQ 支持有符号数。
- 消费侧（浏览器/Sourcemap 库）：解析同样按差值累加还原绝对位置——「生产与消费对称」是 sourcemap 正确性测试的方法（roundtrip 校验）。
- 追问钩子：sourcemap 链式合并（loader 链：ts→js→min.js）的多级 map——每级 map 反解到原始位置再合成一张——合并实现最容易丢 names 与源行偏移，RBL-506 的正确性测试覆盖。

```javascript
// VLQ 编码（SourceMap V3）
function encodeVLQ(value) {
  let vlq = value < 0 ? ((-value) << 1) + 1 : value << 1   // 符号位放最低位
  let out = ''
  do {
    let digit = vlq & 31            // 5-bit 组
    vlq >>>= 5
    if (vlq > 0) digit |= 32        // 续传标志
    out += 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'[digit]
  } while (vlq > 0)
  return out
}

// mappings 生成：按行分段、相对差值编码
function encodeMappings(segmentsByLine) {
  // segment = [genCol, sourceIdx, srcLine, srcCol, nameIdx]（绝对值）
  let prev = [0, 0, 0, 0, 0]
  return segmentsByLine.map((line) =>
    line.map((seg) => {
      const fields = [seg[0], seg[1], seg[2], seg[3], seg[4] ?? 0]
      const out = fields.map((v, i) => encodeVLQ(v - prev[i])).join('')   // 相对差值
      prev = fields
      return out
    }).join(',')
  ).join(';')
}
// 相对差值设计：相邻映射数值小 → VLQ 紧凑（mappings 是天书的原因）
// 负差值合法（列回绕）——VLQ 有符号
// 正确性测试：生产↔消费 roundtrip（解码累加还原绝对位置比对）
```
