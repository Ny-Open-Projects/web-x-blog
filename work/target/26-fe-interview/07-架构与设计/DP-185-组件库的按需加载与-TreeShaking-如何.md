---
title: [DP-185] 组件库的按需加载与 Tree-Shaking 如何设计？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-185：组件库的按需加载与 Tree-Shaking 如何设计？（高频）
**答**：
- 两种形态：全量 install（工厂注册全部）与按需引入（ESM 子路径导出 + sideEffects:false 声明，构建器 tree-shake）——后者本质是虚拟代理（用到才真正加载模块，DP-156）。
- 样式按需：组件内 import './style.less'（依赖联邦进 bundle）或 unplugin 按需注入样式；token 主题用 CSS 变量避免多份样式产物（DP-143）。
- 验证手段：打包分析产物应只含引用组件；`npm run size` CI 卡口。

```javascript
// package.json 关键声明
// { "sideEffects": ["**/*.css", "**/*.less"], "exports": {
//     ".": "./es/index.js",                       // 全量入口
//     "./pagination": "./es/pagination/index.js", // 子路径：按需入口（虚拟代理）
//     "./pagination/style": "./es/pagination/style/index.js" } }
// 组件源码：样式与逻辑同目录，便于单独引
// es/pagination/index.js
export { default as Pagination } from './Pagination.jsx';
export { usePagination } from './usePagination';               // Headless 也单独导出
// 按需插件（unplugin 思路）：编译期把全量引用重写为子路径（构建期工厂）
function createElementImport() {
  return {
    name: 'element-import',
    transform(code) {
      return code.replace(/import \{ ([^}]+) \} from ['"]x-ui['"];?/g, (_, names) =>
        names.split(',').map((n) => `import { ${n.trim()} } from 'x-ui/${kebab(n.trim())}';\nimport 'x-ui/${kebab(n.trim())}/style';`).join('\n'));
    },                                                         // import { Pagination } from 'x-ui' → 两条按需 import
  };
}
// 享元补充：通用工具单例共享（同包内 formatter/date 只装一份）
// 验证：npx webpack-bundle-analyzer --stats dist/stats.json → 确认未引用组件不在产物中
```
