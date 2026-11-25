---
title: [RBL-506] 笔试：手写 VLQ 编解码器（roundtrip 校验 + 负数支持）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-506：手写 VLQ 编解码器（roundtrip 校验 + 负数支持）
**需求**：实现 `encodeVLQ(value)` / `decodeVLQ(str)`：1) 有符号整数 ↔ Base64 VLQ 字符串；2) 多字节续传（值 > 31）；3) `roundtrip`：随机值编解码比对恒等；4) `decodeMappings(mappings)`：按分号/逗号解析还原绝对位置数组（差值累加）；5) 附用例：负数、大数、roundtrip 与差值还原。

```javascript
const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
const B64_MAP = Object.fromEntries([...B64].map((c, i) => [c, i]))

function encodeVLQ(value) {
  let vlq = value < 0 ? ((-value) << 1) + 1 : value << 1
  let out = ''
  do {
    let digit = vlq & 31
    vlq >>>= 5
    if (vlq > 0) digit |= 32
    out += B64[digit]
  } while (vlq > 0)
  return out
}

function decodeVLQ(str) {
  const values = []
  let shift = 0, value = 0
  for (const c of str) {
    const digit = B64_MAP[c]
    value += (digit & 31) << shift          // 累加 5-bit 组
    if (digit & 32) { shift += 5 }          // 续传
    else {
      const negate = value & 1              // 最低位符号
      value >>>= 1
      values.push(negate ? -value : value)
      value = 0; shift = 0
    }
  }
  return values
}

function decodeMappings(mappings) {
  const result = []
  let genLine = 0
  let prev = [0, 0, 0, 0, 0]
  for (const lineStr of mappings.split(';')) {
    if (lineStr) {
      for (const seg of lineStr.split(',')) {
        if (!seg) continue
        const fields = decodeVLQ(seg)
        const abs = [0, 1, 2, 3].map((i) => (prev[i] += fields[i]))   // 差值累加
        if (fields.length === 5) prev[4] += fields[4]
        result.push({ genLine, genCol: abs[0], sourceIdx: abs[1], srcLine: abs[2], srcCol: abs[3] })
      }
    }
    genLine++
  }
  return result
}

// 用例
console.log(encodeVLQ(0), encodeVLQ(1), encodeVLQ(-1), encodeVLQ(16))   // A C D gB
console.log(decodeVLQ(encodeVLQ(-123456)))                              // [-123456]：大负数 roundtrip

// 随机 roundtrip
let ok = true
for (let i = 0; i < 1000; i++) {
  const v = Math.floor(Math.random() * 1e9) - 5e8
  if (decodeVLQ(encodeVLQ(v))[0] !== v) { ok = false; break }
}
console.log(ok)                                                          // true

// 差值还原
const mappings = encodeVLQ(0) + encodeVLQ(0) + encodeVLQ(0) + encodeVLQ(0) + ';' +
  encodeVLQ(5) + encodeVLQ(0) + encodeVLQ(1) + encodeVLQ(3)
const decoded = decodeMappings(mappings)
console.log(decoded)
// [{ genLine:0, genCol:0, ... }, { genLine:1, genCol:5, srcLine:1, srcCol:3 }]
```
**评分点**：
- VLQ 符号位在最低位（负数支持）
- 多字节续传（shift 累加 + 续传标志位）
- roundtrip 随机校验（编解码恒等）
- decodeMappings 差值累加（prev 数组跨段持续——sourceIdx/srcLine/srcCol 跨行持续、genCol 每行重置的真实规范此处简化）
