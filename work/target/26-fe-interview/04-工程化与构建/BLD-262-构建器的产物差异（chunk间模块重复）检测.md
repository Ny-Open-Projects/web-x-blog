---
title: [BLD-262] chunk 间模块重复检测怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-262：chunk 重复检测怎么做？
**答**：
- 重复形态：同一模块打进多个 chunk（分配算法未去重）、同一包多版本（依赖树问题——SCN-ENG-293）、运行时库多份（每个独立构建的产物内嵌 runtime）。
- 检测实现：产物解析（模块 ID/源路径提取——从 sourcemap sources 或产物内注释）→ 按模块标识聚合 → 出现次数 >1 报告（含所在 chunk 与体积）。
- 修复路径：分配算法调参（manualChunks/splitChunks priority）、依赖统一（alias）、共享提取（公共 chunk）。
- 微前端的放大效应：多个独立构建产物相互加载时重复概率放大（各自内嵌依赖）——跨产物检测（多个 manifest 聚合分析）。
- 追问钩子：为什么「从 sourcemap sources 提取模块标识」比解析产物内注释更可靠——注释（webpack 模块路径注释）在 minify 后可能被删除/混淆；sourcemap 的 sources 数组是结构化数据（不受压缩影响），且自带「源文件真实路径」——用 map 做模块归因是产物分析的通用底座。

```javascript
// 从 sourcemap 提取模块清单
const modules = sources.map(s => s.replace(/^webpack:\/\//, ''));
const dup = groupBy(modules, m => m).filter(([m, list]) => list.length > 1);
// 跨产物（微前端）
aggregate([...manifests]).duplicates();   // 跨 manifest 聚合检测
```
