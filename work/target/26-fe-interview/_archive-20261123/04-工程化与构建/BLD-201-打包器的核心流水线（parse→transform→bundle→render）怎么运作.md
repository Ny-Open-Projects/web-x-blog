---
title: [BLD-201] 打包器的核心流水线（parse→transform→bundle→render）怎么运作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-201：打包器核心流水线怎么运作？
**答**：
- 四阶段：parse（源码→AST，识别依赖引用）→ transform（loader/插件转换 AST 或源码）→ bundle（构建模块图，解析路径成模块 ID）→ render（按输出格式生成 chunk 代码）——理解阶段才能定位性能与正确性问题。
- 模块图构建：从入口递归解析依赖（resolve 相对/裸模块/别名路径），每个模块一个 ID；动态 import 生成独立入口（异步 chunk）。
- render 阶段关键：模块包装（CJS wrapper/ESM 直出）、chunk 拓扑排序（依赖先行）、runtime 注入（加载器/热更新）。
- 阶段差异：Rspack/esbuild 用原生实现 parse/render（快），webpack 插件贯穿全流程（灵活）。
- 追问钩子：为什么「resolve 阶段」是打包错误的头号来源——别名配置/扩展名缺失/条件导出（exports 字段）解析失败占打包报错大半；理解 resolver 的查找顺序（alias→extensions→exports→mainFields）才能快速定位。

```javascript
// 模块图示意
const moduleGraph = {
  'entry.js': { deps: ['utils.js', 'react'], chunk: 'main' },
  'utils.js': { deps: [], chunk: 'main' },
  'chart.js': { deps: ['d3'], chunk: 'async-chart', dynamic: true },
};
// render: 每模块包装
// __webpack_modules__[id] = function (module, exports, require) { /* 转换后代码 */ }
```
