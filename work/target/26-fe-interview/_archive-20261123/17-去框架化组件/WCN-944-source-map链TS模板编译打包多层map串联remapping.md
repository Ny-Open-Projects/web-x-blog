---
title: [WCN-944] source map 链：TS → 模板编译 → 打包多层 map 怎么串起来
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-944：source map 链：TS → 模板编译 → 打包多层 map 怎么串起来

**答**：
- 结论先行：每一步编译都产生自己的 map，浏览器只认最后一步；要把它们串成一条链——用 `@ampproject/remapping` 或 `source-map-chain` 合成「最终产物 → 最初源码」的单一 map。
- 链的原理：后一步 map 的 sources 指向前一步的输出文件，remapping 沿 sources 递归回溯，把中间层替换成最初源文件，得到合成映射。
- 常见断裂点：某一步丢了 `sourcesContent` 或改了文件名前缀，链就断在中间，DevTools 只能还原到中间层（常见「断点打到编译产物而非 TS」）。
- 实践：Vite/Rollup 的 `sourcemap: true` 会保留链，但自定义 loader（模板编译器）要正确声明 `map` 字段，否则链在该处断裂。
- 追问钩子：面试官问「链太长会不会失真」——答：会，映射精度随层数累积下降；尽量在关键中间层保留精确列映射，或让编译器直接输出对最初源码的 map。

```javascript
// 合成多层 source map 链
import { remapping } from '@ampproject/remapping';
// 三层 map：bundle.js.map -> compiled.js.map -> source.ts.map
const chain = [
  { file: 'bundle.js', mappings: 'AAAA', sources: ['compiled.js'] },
  { file: 'compiled.js', mappings: 'AACA', sources: ['source.ts'], sourcesContent: ['const x=1'] },
];
const merged = remapping(chain, () => null); // 合成：bundle -> source.ts
console.log(merged.sources); // ['source.ts']（中间层被穿透）
// DevTools 断点落在 source.ts，而非 compiled.js
```
