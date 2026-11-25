---
title: [WCN-943] 手写 source map 消费端定位器：VLQ 解码 + 二分查找映射段反查原始行列
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-943：手写 source map 消费端定位器：VLQ 解码 + 二分查找映射段反查原始行列

**题目**：实现 `createMapLocator(map)`，map 形如 `{ sources:['a.js'], mappings:'AAAA;AACA' }`（VLQ 编码的简化 source map）。返回 `{ originalPosition(genLine, genCol) }`，要求：① 实现 base64 VLQ 解码（字符集 A-Za-z0-9+/）；② 按 `;` 分行、`,` 分映射段，逐段累加生成列（段内5字段：genCol 增量、source 索引增量、origLine 增量、origCol 增量、name 增量），还原每段的绝对行列；③ originalPosition 用二分查找找到 genCol ≤ 目标的最近段，返回 `{ source, line, column }`（0 基→1 基转换：行 +1、列 +1）；④ 找不到返回 null；⑤ 不依赖外部库，纯函数可测试。请自足实现并给出可运行示例。

**答**：

```javascript
const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
function decodeVLQ(str) {
  const out = []; let i = 0;
  while (i < str.length) {
    let shift = 0, value = 0, cont;
    do {
      const d = B64.indexOf(str[i++]);
      cont = d & 32;
      value += (d & 31) * Math.pow(2, shift);
      shift += 5;
    } while (cont && i < str.length);
    out.push((value & 1) ? -(value >> 1) : (value >> 1));
  }
  return out;
}
function createMapLocator(map) {
  const lines = map.mappings.split(';').map(seg => seg ? seg.split(',').map(decodeVLQ) : []);
  const decoded = lines.map(segs => {
    let src = 0, ol = 0, oc = 0;
    return segs.map((f, gc) => {
      src += f[1] || 0; ol += f[2] || 0; oc += f[3] || 0;
      return { genCol: (f[0] || 0) + (segs.length > 1 ? 0 : 0), source: map.sources[src], line: ol + 1, column: oc + 1, gc };
    });
  });
  return { originalPosition(genLine, genCol) {
    const segs = decoded[genLine - 1] || [];
    if (!segs.length) return null;
    let lo = 0, hi = segs.length - 1, best = null;
    while (lo <= hi) { const mid = (lo + hi) >> 1;
      if (segs[mid].genCol <= genCol) { best = segs[mid]; lo = mid + 1; } else hi = mid - 1; }
    return best ? { source: best.source, line: best.line, column: best.column } : null;
  } };
}
const loc = createMapLocator({ sources: ['a.js'], mappings: 'AAAA;AACA' });
console.log(loc.originalPosition(2, 1)); // { source:'a.js', line:2, column:1 }
```

**评分点**：
- base64 VLQ 解码正确（含续位与符号位处理）。
- mappings 按 ;/, 分段并累加生成列与 source/原始行列增量。
- originalPosition 用二分查找最近段，返回 1 基行列，找不到返回 null。
- 纯函数、不依赖外部库，示例可运行。
- 边界：空段、无匹配行处理正确。
