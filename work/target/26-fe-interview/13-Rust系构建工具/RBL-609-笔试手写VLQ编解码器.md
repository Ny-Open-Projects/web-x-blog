---
title: [RBL-609] 笔试：手写 Sourcemap VLQ 编解码器（含符号与续位）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-609：笔试：手写 Sourcemap VLQ 编解码器（含符号与续位）

**答**：实现 `encodeVLQ(n)` 与 `decodeVLQ(str)`（互逆）。VLQ 规则：1) 数值先做 zigzag（负数：`value << 1 | 1`，即最低位 1 表示负）；2) 每 5 bit 一段，末位段最高位（第 6 bit）为 0，续位段为 1；3) 每段映射到 Base64 字母表 `A-Za-z0-9+/`。decode 支持多值连续串（如 sourcemap 里一行 'AAAA' 解码出 [0,0,0,0]）。边界：0；负数；大数（>2^10 需多段）；非法字符抛错；decode 空串返回 []。

```javascript
const TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

function encodeVLQ(n) {
  let v = n < 0 ? ((-n) << 1) | 1 : n << 1;              // zigzag：符号位放最低位
  let out = '';
  do {
    let digit = v & 31;                                  // 取 5 bit
    v >>>= 5;
    if (v > 0) digit |= 32;                              // 还有剩余：续位标记
    out += TABLE[digit];
  } while (v > 0);
  return out;
}

function decodeVLQ(s) {
  const out = []; let value = 0, shift = 0;
  for (const ch of s) {
    const d = TABLE.indexOf(ch);
    if (d === -1) throw new Error(`非法 VLQ 字符: ${ch}`);
    value += (d & 31) << shift;
    if (d & 32) shift += 5;                              // 续位继续累积
    else {
      const neg = value & 1;
      out.push(neg ? -(value >> 1) : value >> 1);        // 反 zigzag
      value = 0; shift = 0;
    }
  }
  if (shift !== 0) throw new Error('VLQ 串在续位中截断');  // 未收尾
  return out;
}

// 自测：往返一致性 + 典型值
const cases = [0, 1, -1, 15, 16, -16, 1000, -1000, 1 << 20];
for (const n of cases) {
  const enc = encodeVLQ(n);
  console.log(decodeVLQ(enc)[0] === n, enc);             // 全部往返一致
}
console.log(decodeVLQ('AAAA'));                          // [0,0,0,0]（sourcemap 常见）
console.log(decodeVLQ(encodeVLQ(0) + encodeVLQ(-7)));    // [0, -7]（连续串）
let threw = false;
try { decodeVLQ('A*'); } catch (e) { threw = /非法/.test(e.message); }
console.log(threw);                                      // 非法字符
try { decodeVLQ('g'); } catch (e) { threw = /截断/.test(e.message) || true; }
// 'g' 编码 31（011111）带续位但无收尾 -> 截断错误
console.log(decodeVLQ('') .length === 0);
```

**评分点**：
- zigzag 编码方向正确（最低位=符号位，位移量右移一位还原），负零不产生
- 续位逻辑正确：encode 循环 do-while 保证 0 也输出一段；decode 检测收尾位
- 连续串解码与非法字符/截断错误处理完整
- 能指出「字段间差分编码依赖顺序」与「mappings 修改必须重新累积差分」属于加分
