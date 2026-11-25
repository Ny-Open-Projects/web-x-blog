---
title: [RBL-608] Sourcemap 深水：VLQ 编码、映射段合并与运行时二分查询
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-608：Sourcemap 深水：VLQ 编码、映射段合并与运行时二分查询

**答**：
- sourcemap 的 mappings 是「生成位置 → 源位置」的差分编码：每行内的段用 VLQ（可变长度量）编码五个字段（genCol、sourceIdx、srcLine、srcCol、nameIdx），字段间做**增量差分**——这是为什么手工改 sourcemap 极易出错，也是体积优势所在（相邻映射差异小）。
- 多级变换的合并链：TS→JS→minified 三次变换产生三张 map，逐级合并（source-map 库的 applySourceMap）保持「生成物 → 最初源码」的直连；构建器内嵌转换时应直接维护「复合映射」（transform 时同步映射）避免事后合并的精度损失与 O(n²) 成本。
- 运行时查询：给定生成文件行列找源码位置——**按行分桶 + 行内二分**（genCol 排序，找 ≤col 的最后一个映射）；误差语义「best match」——没有精确命中时取最近左侧映射并标注近似。 SourceMapConsumer 的 originalPositionFor 就是这个查询。
- 性能工程：大 bundle 的 map 可达几十 MB——线上错误反解服务要把 map 预处理为「行 → 段数组」的紧凑索引（跳过源内容字段），查询单次 O(log n)；VLQ 解码用预编译查表。sources 字段可选择「源码内置」（sourcesContent）或「仅路径」（反解服务按构建版本拉源码）——体积与隐私权衡。
- 追问钩子：为什么 minifier 的 map 段密度更高？——压缩重命名让「每个 token」都可能换位置，映射段从「语句级」变「token 级」，这也是压缩 map 体积大的原因；反解精度直接决定错误堆栈定位到列的能力。

```javascript
// VLQ 解码（查表版）
const CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
const decodeVLQ = (s) => {
  const out = []; let shift = 0, value = 0;
  for (const ch of s) {
    const d = CHARS.indexOf(ch);
    value += (d & 31) << shift;                          // 5 bit 一段
    if (d & 32) shift += 5;                              // 续位
    else {
      const negate = value & 1; value >>= 1;             // 最低位是符号
      out.push(negate ? -value : value); shift = 0; value = 0;
    }
  }
  return out;
};

// 行分桶 + 二分查询
class FastMap {
  constructor(mappings) { this.rows = mappings.map(segs => segs.sort((a, b) => a[0] - b[0])); }
  find(genLine, genCol) {
    const row = this.rows[genLine]; if (!row) return null;
    let lo = 0, hi = row.length - 1, best = null;
    while (lo <= hi) {                                   // 找 <= genCol 的最后一个映射
      const mid = (lo + hi) >> 1;
      if (row[mid][0] <= genCol) { best = row[mid]; lo = mid + 1; } else hi = mid - 1;
    }
    return best;                                         // { genCol, srcIdx, srcLine, srcCol } 近似命中
  }
}
```
