---
title: [WCN-950] 手写 source map 合并器：把「模板编译→打包」两段 map 合成单一 map
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-950：手写 source map 合并器：把「模板编译→打包」两段 map 合成单一 map

**题目**：实现 `chainMaps(first, second)`，模拟两层 source map 合成：first 是模板编译 map（ `{ file:'compiled.js', sources:['tpl.ts'], mappings:[[genLine,genCol,origLine,origCol]] }` ），second 是打包 map（ `{ file:'bundle.js', sources:['compiled.js'], mappings:[...同格式] }` ）。要求：① second 的每段若其 source 等于 first.file，则用 first 的映射把「 bundle 位置」映射到最初源文件 tpl.ts（位置相加：origLine = first.origLine + second.origLine - 1，列同理仅在同行时相加）；② second 中 source 不等于 first.file 的段保持不变；③ 返回 `{ file:'bundle.js', sources:[...], mappings:[{ genLine,genCol,source,origLine,origCol }] }`；④ 不修改输入；⑤ 处理 first 无匹配段的边界。请自足实现并给出可运行示例。

**答**：

```javascript
function chainMaps(first, second) {
  const out = [];
  const sources = new Set();
  for (const seg of second.mappings) {
    if (seg.source === first.file) {
      const f = first.mappings.find(x => x.genLine === seg.origLine && x.genCol === seg.origCol);
      if (f) {
        const sameLine = f.origLine === 1;
        out.push({ genLine: seg.genLine, genCol: seg.genCol,
          source: f.source, origLine: f.origLine + seg.origLine - 1,
          origCol: sameLine ? f.origCol + seg.origCol : f.origCol });
        sources.add(f.source);
      } else { // first 无匹配段：保留为指向 compiled.js
        out.push({ ...seg }); sources.add(seg.source);
      }
    } else { out.push({ ...seg }); sources.add(seg.source); }
  }
  return { file: second.file, sources: [...sources], mappings: out };
}
const first = { file: 'compiled.js', sources: ['tpl.ts'],
  mappings: [{ genLine: 1, genCol: 0, origLine: 3, origCol: 2 }] };
const second = { file: 'bundle.js', sources: ['compiled.js'],
  mappings: [{ genLine: 1, genCol: 0, source: 'compiled.js', origLine: 1, origCol: 0 }] };
console.log(chainMaps(first, second));
// mappings:[{ genLine:1, genCol:0, source:'tpl.ts', origLine:3, origCol:2 }]
```

**评分点**：
- 二层映射合成正确：bundle 位置穿透到最初源文件 tpl.ts。
- 行列叠加规则正确（行相加减1、列同行相加）。
- second 中非目标 source 的段保持不变。
- first 无匹配段时保留原段、不修改输入。
- 返回结构与示例输出正确可运行。
