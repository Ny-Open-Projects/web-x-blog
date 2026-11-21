---
title: [BLD-130] vite 的 import 分析与模块图：es-module-lexer 和导入重写是怎么工作的？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-130：vite 的 import 分析与模块图：es-module-lexer 和导入重写是怎么工作的？
**答**：
- dev 模式浏览器原生 ESM 要求"import 路径必须是可请求 URL"：vite 把 `import { x } from 'vue'` 重写为 `/node_modules/.vite/deps/vue.js?v=hash`，把相对导入重写为**带源码绝对路径的 URL**（`/src/App.vue`），源码保持原样存 moduleGraph。
- 轻量解析用 **es-module-lexer**（只找 import/export 位置，不做完整 AST，微秒级）+ 魔法字符串拼接重写；需要深入时才回退 acorn。这是 dev 冷启动毫秒级响应的关键取舍。
- 模块图：`server.moduleGraph` 按 url 记录 ModuleNode（importers/importedModules/transformResult/ssrTransformResult），HMR 时**从变更文件反向遍历 importers** 找边界（isSelfAccepting）。
- query 语义：`?import` 标记 JS 模块、`?raw` 原文、`?url` 资源地址、`?t=时间戳` 强制缓存失效（HMR 更新后改写 import 带 t）。

```javascript
// 复现 vite 的 import 重写核心（源码在 importAnalysis 插件，约 200 行的精华）
import { init, parse as parseImports } from 'es-module-lexer';

async function rewriteImports(code, importer, resolve) {
  await init;                                    // 初始化 wasm
  let imports;
  [imports] = parseImports(code);                // 只提取 import 语句位置，不做 AST
  let s = 0, e = code.length;
  const str = () => code.slice(s, e);
  for (let i = imports.length - 1; i >= 0; i--) {
    const { s: start, e: end, d: dynamicIndex } = imports[i];
    const rawUrl = code.slice(start, end);
    // ① 裸导入：'vue' → '/node_modules/.vite/deps/vue.js?v=043c...'
    // ② 相对导入：'./App.vue' → '/src/App.vue'
    // ③ 动态导入：import('./x') → import('/src/x.js')（dynamicIndex >= 0）
    const resolved = await resolve(rawUrl, importer);
    const url = dynamicIndex > -1 ? resolved : resolved; // 简化：真实源码区分动态并加 ?import
    s = start; e = end;
    // 用 overwrite 方式改写（真实实现是 MagicString）
    code = code.slice(0, start) + url + code.slice(end);
  }
  return { code: str(), map: null };
}
// 模块图侧：transform 完成后 moduleGraph.getModuleByUrl(url) 更新
//   .importedModules / .importers —— HMR 反向传播的数据基础
// 浏览器收到的形态：
// import { createApp } from '/node_modules/.vite/deps/vue.js?v=043c9a21'
// import App from '/src/App.vue?t=1699000000000'
```
