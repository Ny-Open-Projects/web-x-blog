---
title: [BLD-297] 笔试题——实现 sourcemap 链合成（remapping）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-297：手写 sourcemap 合成

**需求与边界**：
- 需求：转换链 babel(TS→JS) → minify(JS→min) 两段 map 合成最终 map——① min 位置 → babel 产物位置（map1）→ TS 源位置（map2）两级跳；② 边界：某位置在 map1 无精确映射时取最近前序映射（sourcemap 语义）；③ 输出合并 map（sources 为 TS 文件）。
- 边界：① mappings 的 VLQ 编码解码/重编码（实现核心）；② sourcesContent 传递（TS 源码内容——还原可读性）；③ 无匹配位置输出 null（不硬猜）。

**答**：
```javascript
import { decode, encode } from '@jridgewell/sourcemap-codec';
function remap(minMap, babelMap) {
  const bdecoded = decode(babelMap.mappings);          // 行 → 段数组
  const bIndex = indexByGenerated(bdecoded);           // 生成行列 → 段（最近前序查找）
  const mappings = decode(minMap.mappings).map((line, genLine) =>
    line.map(seg => {
      const [gCol, srcIdx, srcLine, srcCol] = seg;     // min 生成位置 → babel 产物位置
      const mid = bIndex.find(genLine, gCol);          // 最近前序映射（sourcemap 语义）
      if (!mid) return [gCol];                         // 无匹配：只保留生成列
      const [, bSrcIdx, bLine, bCol] = mid;
      const bSrc = babelMap.sources[bSrcIdx];
      const tIdx = minMap.sources.length;              // TS 源追加
      return [gCol, tIdx, bLine, bCol];                // 二级跳（SCN-BLD-207 链式）
    }));
  return {
    version: 3,
    sources: [...minMap.sources, ...babelSourcesToTs(babelMap)],   // TS 源文件
    sourcesContent: [null, ...babelMap.sourcesContent],            // TS 内容传递
    mappings: encode(mappings),
  };
}
// indexByGenerated: 预处理 babel map（按生成行分组，列排序——二分最近前序）
```

**评分点**:
- 二级跳逻辑（min→babel→TS）与 sources 合并。
- 最近前序映射（sourcemap 规范语义——无精确匹配不硬猜）。
- sourcesContent 传递（还原可读性）。
- VLQ 编解码正确（mappings 结构处理）。
