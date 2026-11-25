---
title: [BLD-207] Source Map 的生成原理与版本对齐怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-207：Source Map 原理怎么工作？
**答**：
- 结构：mappings（VLQ 编码的行列映射：生成位置 → 源位置）、sources（源文件）、sourcesContent（内联源码）——多重转换链（TS→JS→min）通过「链式 map」合成最终 map。
- VLQ 编码：Base64 变长整数，每段五字段（生成列/源索引/源行/源列/名字索引）——列粒度映射是压缩后还原的关键。
- 链式合成：转换工具输出转换前后两份 map，打包器合并链（remapping）——任何一环丢失 map 都会让最终还原断链。
- 版本对齐：map 与产物 hash 绑定（buildinfo 关联，SCN-OPS-246/ENG-305），跨版本还原是错源码。
- 追问钩子：为什么压缩后还能精确到列——minifier 保留「名字索引」与列级映射；但terser 的 mangle（变量重命名）依赖 names 字段还原原始变量名；mangle: true 且没保留原始名映射时，堆栈还原出的是改名后的变量——还原精度取决于转换链每一环的信息保留。

```javascript
// map 结构
{ version: 3, sources: ['src/app.ts'], sourcesContent: ['...'],
  mappings: 'AAAA,SAASA;;AACA' }                     // VLQ 编码
// 链式合成
import { remapping } from '@ampproject/remapping';
const final = remapping(minMap, () => babelMap);     // min→babel→ts 链合成
```
