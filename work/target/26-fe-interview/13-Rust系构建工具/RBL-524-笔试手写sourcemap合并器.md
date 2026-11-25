---
title: [RBL-524] 笔试：手写 sourcemap 合并器（两级链式映射）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-524：手写 sourcemap 合并器（两级链式映射）
**答**：实现 `combineMaps(mapAtoB, mapBtoC)`：ts→js 与 js→min.js 两级 map 合成 ts→min.js：1) 对 mapBtoC 的每个生成位置，用 mapAtoB 反解到 ts 位置（存在映射时替换源）；2) 无上游映射的段保留（可能到不了 ts——transpile 中间生成）；3) names/sources 按 remap 后索引重组；4) 附用例：两级映射合成与上游缺失段保留。

```javascript
function combineMaps(mapAB, mapBC) {
  // mapAB: { sources, mappings: { [genLine]: [{ genCol, srcIdx, srcLine, srcCol }] } }
  // mapBC: 同结构；合成 ts→min.js
  const outSources = [...mapAB.sources]
  const outMappings = {}

  for (const [genLine, segs] of Object.entries(mapBC.mappings)) {
    const outSegs = []
    for (const seg of segs) {
      // 在 mapAB 中找「B 文件的该行该列」对应的 ts 位置（最近的前置映射）
      const upstream = findUpstream(mapAB, seg.srcLine, seg.srcCol)
      if (upstream) {
        outSegs.push({
          genCol: seg.genCol,
          srcIdx: upstream.srcIdx,
          srcLine: upstream.srcLine,
          srcCol: upstream.srcCol,
        })
      } else {
        // 无上游映射（中间生成代码）：保留指向 B（退化为单级）
        outSegs.push({ genCol: seg.genCol, srcIdx: seg.srcIdx, srcLine: seg.srcLine, srcCol: seg.srcCol })
      }
    }
    outMappings[genLine] = outSegs.sort((a, b) => a.genCol - b.genCol)
  }

  return { sources: outSources, mappings: outMappings }
}

function findUpstream(mapAB, line, col) {
  const segs = mapAB.mappings[line]
  if (!segs?.length) return null
  // 找 genCol <= col 的最近映射
  let best = null
  for (const s of segs) {
    if (s.genCol <= col) best = s
    else break
  }
  return best ?? segs[0]
}

// 用例
const mapAB = {   // ts → js
  sources: ['app.ts'],
  mappings: {
    0: [{ genCol: 0, srcIdx: 0, srcLine: 5, srcCol: 2 }, { genCol: 20, srcIdx: 0, srcLine: 6, srcCol: 4 }],
    1: [{ genCol: 0, srcIdx: 0, srcLine: 7, srcCol: 0 }],
  },
}
const mapBC = {   // js → min.js
  sources: ['app.js'],
  mappings: {
    0: [{ genCol: 0, srcIdx: 0, srcLine: 0, srcCol: 0 }, { genCol: 15, srcIdx: 0, srcLine: 0, srcCol: 20 }],
    1: [{ genCol: 0, srcIdx: 0, srcLine: 1, srcCol: 0 }],
    2: [{ genCol: 0, srcIdx: 0, srcLine: 9, srcCol: 0 }],   // js 第 9 行：ts 无映射（中间生成）
  },
}
const combined = combineMaps(mapAB, mapBC)
console.log(combined.mappings['0'])
// [{ genCol:0, srcIdx:0(→app.ts), srcLine:5, srcCol:2 }, { genCol:15, srcIdx:0, srcLine:6, srcCol:4 }]
console.log(combined.mappings['2'])
// [{ genCol:0, srcIdx:0, srcLine:9, srcCol:0 }]：上游缺失段保留（指向 js）
```
**评分点**：
- 上游反解（findUpstream 最近前置映射）
- 无上游映射段保留（transpile 中间生成的降级）
- genCol 排序输出（规范要求）
- sources 索引重组意识（此简版直接沿用 A 的 sources）
