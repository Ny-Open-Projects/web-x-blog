---
title: [BLD-253] 大仓构建的内存治理（OOM）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-253：内存治理怎么做？
**答**：
- 内存去向：模块图（数千模块的 AST/依赖对象驻留）、sourcemap（sourcesContent 巨大）、缓存对象（插件内部缓存）——大头通常是 sourcemap 与模块图。
- 治理手段：转换后释放 AST（插件不要持有 AST 引用——闭包泄漏）、sourcemap 延迟生成（不需要时不生成 sourcesContent）、堆分析定位（--inspect + heap snapshot 按保留树找持有者）。
- Node 堆配置与指标：--max-old-space-size 显式设 + 构建内存监控（超阈值告警——OOM 前预警，SCN-ENG-269 遥测扩展）。
- 架构级方案：分包构建（多进程各构建子集再合并）/原生工具（Rust 无 GC 压力）。
- 追问钩子：为什么「插件持有 AST 引用」是 OOM 的头号嫌疑——转换完成后模块 AST 本应被 GC，但插件把 AST 存进自己的 cache 对象（比如做依赖分析），导致全部模块 AST 常驻堆内存——堆快照的 retained size 排序能直接揪出「哪个对象链持有数千 AST」——这是 OOM 排查的第一步。

```javascript
// 插件泄漏模式
const cache = {};                                     // 插件级缓存
transform(code, id) { cache[id] = parse(code); }      // AST 常驻 → OOM
// 修复：只存派生数据
transform(code, id) { cache[id] = extractDeps(parse(code)); }   // AST 可被 GC
// 构建内存监控
telemetry.push({ heap: process.memoryUsage().heapUsed, module: moduleId });
```
