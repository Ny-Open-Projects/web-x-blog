---
title: [V3-292] 组件库按需加载与 tree-shaking 怎么实现？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-292：组件库按需加载与 tree-shaking 怎么实现？
**答**：
- ESM + sideEffects：package.json 声明 `"sideEffects": ["*.css", "es/**/*.vue"]`（样式与 SFC 有副作用），纯 JS 模块标 false，rollup/webpack 才敢摇树。
- 产物结构：es/lib 双目录 + 每组件独立入口（`element-plus/es/components/button/index.mjs`），样式同名 index.css，按需方各自引入。
- 按需方案演进：手动按路径引入 → babel 插件（unplugin-vue-components 自动转换模板里的组件为精确 import + 样式 import）→ 直接全量 + 依赖 bundler tree-shaking（现代产物体积可控后可行）。
- 样式隔离坑：unplugin 自动引样式只覆盖模板中的组件，动态组件/指令（如 vLoading）需要手动 import 指令样式。
- 校验方法：打包产物分析确认未用组件 JS/CSS 未进 bundle；CI 里加体积预算检查防退化。

```javascript
// package.json
{
  "module": "es/index.mjs",
  "sideEffects": ["dist/*", "*.css", "es/**/*.vue"],
  "exports": {
    ".": { "import": "./es/index.mjs" },
    "./es/components/button": { "import": "./es/components/button/index.mjs" },
    "./es/components/button/style/css": { "import": "./es/components/button/style/css.mjs" },
  },
}
// unplugin-vue-components：模板 <ElButton> 自动变为
import { ElButton } from 'my-ui/es/components/button';
import 'my-ui/es/components/button/style/css';
// 指令样式（unplugin 覆盖不到）：
import 'my-ui/es/components/loading/style/css'; // 手动补
```
