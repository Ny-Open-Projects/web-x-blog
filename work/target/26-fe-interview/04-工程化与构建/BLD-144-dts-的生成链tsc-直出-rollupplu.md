---
title: [BLD-144] d.ts 的生成链：tsc 直出、rollup-plugin-dts、api-extractor 三种方案对比。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-144：d.ts 的生成链：tsc 直出、rollup-plugin-dts、api-extractor 三种方案对比。
**答**：
- **tsc 直出**：`tsc --emitDeclarationOnly` 按源码结构输出 d.ts 树（最稳定，零额外工具）；缺点是类型文件碎片化，需配 `"typesVersions"` 或导出入口聚合。
- **rollup-plugin-dts**：把 tsc 产出的 d.ts 再"打包"成单文件 `index.d.ts`（合并 module augmentation、处理重导出）；要求上游 tsc 先跑，链路 = tsc → rollup dts pass。
- **api-extractor**（微软）：生成**单个 rolled-up 类型 + 报告文件**，能检测公共 API 泄露（未导出类型被引用）与 semver diff（api-report 变更进 PR review）——大库（monaco/angular 组件库）标配。
- 常见错误：`TS2742`（类型推断泄露）、私有类型未导出、`/// <reference types>` 断链——面试讲清"链路：tsc 产类型树 → 打包聚合 → 校验"。

```javascript
// 方案一：tsc 直出 + rollup-plugin-dts 聚合（最常见组合）
// tsconfig.build.json
// {
//   "compilerOptions": {
//     "declaration": true, "emitDeclarationOnly": true,
//     "outDir": "dist/types", "isolatedModules": true, "skipLibCheck": true
//   },
//   "include": ["src"]
// }
// scripts: { "build:types": "tsc -p tsconfig.build.json && rollup -c rollup.dts.mjs" }

// rollup.dts.mjs
import dts from 'rollup-plugin-dts';
export default {
  input: 'dist/types/index.d.ts',
  output: [{ format: 'esm', file: 'dist/index.d.ts' }],
  plugins: [dts({ respectExternal: true })],
};
```

```json
// 方案二：api-extractor 的配置与产物（面向大型库）
// api-extractor.json
{
  "$schema": "https://developer.microsoft.com/json-schemas/api-extractor/v7/api-extractor.schema.json",
  "mainEntryPointFilePath": "<projectFolder>/dist/types/index.d.ts",
  "bundledPackages": [],
  "apiReport": {
    "enabled": true,
    "reportFolder": "<projectFolder>/etc/",
    "reportTempFolder": "<projectFolder>/etc/temp/"
  },
  "dtsRollup": {
    "enabled": true,
    "untrimmedFilePath": "<projectFolder>/dist/index.d.ts",
    "publicTrimmedFilePath": "<projectFolder>/dist/public.d.ts"  // 修剪内部 API
  },
  "messages": {
    "extractorMessageReporting": {
      "ae-missing-release-tag": { "logLevel": "error" },   // 强制 @public/@internal 标记
      "ae-forgotten-export": { "logLevel": "error" }      // 类型泄露直接构建失败
    }
  }
}
// CI 价值：etc/api-report.md 进 git，PR 中类型签名变更一目了然（配合 semver 审核）
```
