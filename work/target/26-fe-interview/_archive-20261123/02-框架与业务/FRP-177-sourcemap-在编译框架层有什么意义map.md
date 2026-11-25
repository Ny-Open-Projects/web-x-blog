---
title: [FRP-177] sourcemap 在编译框架层有什么意义？mappings 是怎么工作的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-177：sourcemap 在编译框架层有什么意义？mappings 是怎么工作的？

**答**：
- 编译框架（Vue SFC/Svelte/Solid/Babel）把用户代码映射到生成代码：**断点落在源码、报错栈还原到模板行号、CSS-in-JS 回溯类名**——全靠 sourcemap。
- 格式核心是 `mappings`：VLQ 编码的"生成行列 → 源行列"映射段序列；每个段 5 个字段（生成列、源文件索引、源行、源列、名字索引）。
- 框架层特殊用法：模板编译错误要指向**原模板的行列**（编译器在 parse 时记录每个 AST 节点的 loc 并传给 generate）；生产环境错误上报用 sourcemap 反解。
- 调试体验的决定性细节：`sourcesContent` 内嵌源码让 DevTools 直接显示模板原文；Vue SFC 三个块（template/script/style）各自出 map 再合并。

```javascript
// 简化实现，帮助理解 sourcemap 的生成与使用
const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

// VLQ 编码：把整数变成 base64 字符（可表示负数，用于行列差值）
function encodeVLQ(value) {
  let vlq = value < 0 ? ((-value) << 1) | 1 : value << 1;
  let out = '';
  do {
    let digit = vlq & 31;                 // 低 5 位
    vlq >>>= 5;
    if (vlq > 0) digit |= 32;             // 还有后续：置延续位
    out += B64[digit];
  } while (vlq > 0);
  return out;
}

// 生成 mappings：逐段记录"生成位置 -> 源位置"（增量编码）
function buildMappings(segments) {
  // segments: [{ genLine, genCol, srcIdx, srcLine, srcCol }, ...]（已按生成位置排序）
  let prevGenCol = 0, prevSrcLine = 0, prevSrcCol = 0, prevSrcIdx = 0;
  const lines = [];
  let currentLine = '';
  let lastGenLine = 0;
  for (const s of segments) {
    if (s.genLine !== lastGenLine) { lines.push(currentLine); currentLine = ''; lastGenLine = s.genLine; prevGenCol = 0; }
    currentLine += encodeVLQ(s.genCol - prevGenCol)          // 生成列（差值）
                 + encodeVLQ(s.srcIdx - prevSrcIdx)          // 源文件索引
                 + encodeVLQ(s.srcLine - prevSrcLine)        // 源行（差值）
                 + encodeVLQ(s.srcCol - prevSrcCol);         // 源列
    prevGenCol = s.genCol; prevSrcIdx = s.srcIdx; prevSrcLine = s.srcLine; prevSrcCol = s.srcCol;
  }
  lines.push(currentLine);
  return lines.join(';');
}

// 使用：报错栈反解（错误监控平台的核心步骤）
function originalPosition(map, genLine, genCol) {
  const seg = findSegment(map.mappings, genLine, genCol);  // 二分查找最近映射段
  return { line: seg.srcLine + 1, column: seg.srcCol, source: map.sources[seg.srcIdx] };
}
// "Cannot read property of undefined at render:12:8"
//   -> 反解 -> "Cannot ... at App.vue 模板第 4 行 {{ user.name }}"

// 框架层要点：编译器在每个 AST 节点上带 loc（源模板行列），
// generate 为每个产物 token 记录 segment —— 映射链路才能一路保持到源模板
```
