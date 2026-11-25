---
title: [V3-489] 组件库的按需加载与 tree-shaking
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## V3-489：组件库的按需加载与 tree-shaking

**答**：
- tree-shaking 生效条件：ESM 导出 + 副作用标记（package.json sideEffects: false 但样式/插件除外）——组件库要精确标注（unplugin-vue-components 自动按需导入）
- 按需导入两方案：unplugin-vue-components（模板里直接用，构建期替换 import）vs 手动 `import { ElButton } from 'element-plus'`——前者零心智负担但要配置 d.ts
- 样式按需：组件样式随组件 import 自动引入（unplugin 的样式解析）或全量引入后 purge——大型项目全量 CSS + purge 有时更优（缓存友好）
- tree-shaking 失效场景：组件注册到全局（app.use(ElementPlus) 全量）、动态组件名（resolveComponent('ElXxx')）、sideEffect 隐蔽（构建时 polyfill）
- 量化验证：构建产物分析（rollup-plugin-visualizer）比对「引入组件数 vs 体积」——目标「用 10 个组件只付 10 个组件的体积」

```javascript
// vite.config
Components({ resolvers: [ElementPlusResolver()] })   // 模板直接 <el-button>
// 全量引入(反模式, unless 中后台全用):
// app.use(ElementPlus)  → 打包整个组件库
```
