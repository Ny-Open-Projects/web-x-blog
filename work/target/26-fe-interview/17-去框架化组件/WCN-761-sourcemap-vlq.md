---
title: [WCN-761] 笔试：手写编译产物的 source map（VLQ 编码）生成与映射
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-761：笔试：手写编译产物的 source map（VLQ 编码）生成与映射

**答**：
- 需求：实现 `encodeVLQ(value)` 与 `genMappings(generatedLines)`：generatedLines 是二维数组，每项为 `[genCol, srcIndex, srcLine, srcCol]`（相对上一条的增量），输出 base64 VLQ 编码的 mappings 字符串。
- 要点：VLQ 用 5 位一组，最高位 continuation、最低位符号位；负数取反<<1、正数<<1；用 base64 字符表；边界：value=0、多组编码。

```javascript
const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
function encodeVLQ(value) {
  let v = value < 0 ? ((-value) << 1) | 1 : (value << 1); // 最低位符号
  let out = '';
  do {
    let digit = v & 31;
    v >>>= 5;
    if (v > 0) digit |= 32;                              // 续位
    out += B64[digit];
  } while (v > 0);
  return out;
}
function genMappings(lines) {
  return lines.map((seg) => seg.map((n) => encodeVLQ(n)).join('')).join(';');
}
console.log(encodeVLQ(0), encodeVLQ(1), encodeVLQ(-1));
console.log(genMappings([[0, 0, 0, 0], [4, 0, 1, 2]]));
```

**评分点**：
- VLQ 符号位/续位编码正确（负奇正偶）。
- 5 位分组与 base64 字符表映射正确。
- genMappings 用 ';' 分行、段内拼接，符合 source map 格式。
- value=0 等边界正确。
