---
title: [RBL-624] 资源提示的生成策略：modulepreload、preload 与 prefetch 的构建器决策
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-624：资源提示的生成策略：modulepreload、preload 与 prefetch 的构建器决策

**答**:
- 三种提示的语义分工：`modulepreload`（预下载+预解析+预编译 ESM 及其依赖闭包——模块图语义）；`preload`（高优先级预载当前导航必需资源，跨类型通用）；`prefetch`（低优先级预取**未来导航**资源，空闲时）。构建器能自动生成前两者（因为拥有依赖图），prefetch 需要路由级预测（框架配合）。
- modulepreload 的生成范围决策：静态 import 闭包全预载（首屏 chunk 链）——但「全量闭包」可能很大，激进策略反而与业务 JS 抢带宽；工程折中：**关键路径深度截断**（预载到 N 层或 X KB 预算内），深依赖留给运行时动态 import（进入时浏览器本身有 modulepreload 队列）。Vite/Rolldown 的 `modulePreload.polyfill` 还处理「Safari 不递归预载」的兼容垫片。
- preload 的误用防线：构建器无法知道字体/首屏 API 是「必需」，但可以对「已知模式」自动 preload（如 CSS 里的 @font-face 主字体、入口同目录的 hero 图片约定）；同时要给 lint 诊断：preload 的资源若当前导航不用 → 浪费带宽告警（对照响应真实加载行为，RUM 数据回环）。
- prefetch 与版本滚动的坑：prefetch 的 URL 若是 hash 产物，跨版本 prefetch 会拉旧版（用户下次导航拿的是新 html 引用新 hash）——prefetch 由框架在导航意图时生成（用当前 manifest），构建器只需输出 manifest（chunk → hash URL 映射，RBL-598）供运行时查询。
- 追问钩子：为什么 modulepreload 比 preload 更适合模块？——preload 只下载不解析；modulepreload 让模块「下载+解析+实例化」提前，把主线程的模块图构建也移出关键路径——对 ESM 应用是量级差异。

```javascript
// modulepreload 生成（预算截断策略）
function generateModulePreloads(entryChunk, manifest, { depth = 2, budgetKB = 100 }) {
  const hints = []; let used = 0;
  const walk = (chunk, d) => {
    if (d > depth || used > budgetKB) return;
    for (const dep of chunk.staticImports) {
      const url = manifest.nameOf(dep);                 // 级联 hash 文件名
      if (used + dep.sizeKB > budgetKB) break;          // 预算截断，深依赖动态加载
      hints.push(`<link rel="modulepreload" href="${url}">`);
      used += dep.sizeKB;
      walk(dep, d + 1);                                 // modulepreload 语义上会递归，预算内显式列出
    }
  };
  walk(entryChunk, 0);
  return hints;
}

// 字体自动 preload（构建器识别主字体约定）
const fonts = manifest.assets.filter(a => a.kind === 'font' && a.preload === true);
// <link rel="preload" as="font" type="font/woff2" crossorigin>

// lint 诊断：preload 未使用检测（RUM 回环）
// 诊断码 RBL3001: resource preloaded but never used in 30d -> 建议移除或降级 prefetch
```
