---
title: [DP-219] 源码识别：Rollup/Vite 插件体系源码中的钩子模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-219：源码识别：Rollup/Vite 插件体系源码中的钩子模式？
**答**：
- 插件+钩子（模板方法）：构建流程是固定骨架（resolve → load → transform → generate），插件实现各钩子参与步骤——Rollup/Vite/Rspack/webpack 全家通用模式（Tapable 事件流也是）。
- 职责链：transform 钩子按插件顺序串行处理代码（postcss → vue → ts），任一插件返回 null 即透传。
- 观察者：Vite dev server 的事件（configureServer/热更 handleHotUpdate）基于 chokidar 文件事件 + 自定义 emitter——文件系统观察者 → 模块图失效 → HMR 广播。
- 识别要点：能区分"构建期钩子"（buildStart/buildEnd）与"输出期钩子"（renderChunk），说明插件按 enforce: 'pre'/'post' 插入链位置。

```javascript
// Rollup 插件执行模型（简化）
async function build(plugins, entry) {
  for (const p of plugins) await p.buildStart?.();
  let id = entry;
  for (const p of plugins) {                     // resolve 职责链：第一个非 null 胜出
    const r = await p.resolveId?.(id);
    if (r) { id = r; break; }
  }
  let code = null;
  for (const p of plugins) {
    const l = await p.load?.(id);                // load 链
    if (l != null) { code = l; break; }
  }
  for (const p of plugins) {                     // transform 链：串行加工
    const r = await p.transform?.(code, id);
    if (r) code = typeof r === 'string' ? r : r.code;
  }
  for (const p of plugins) await p.buildEnd?.();
}
// 插件示例：{ name: 'replace', transform(code) { return code.replace('__VERSION__', '2.0') } }
```
