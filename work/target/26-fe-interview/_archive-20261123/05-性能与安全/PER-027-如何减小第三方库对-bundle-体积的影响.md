---
title: [PER-027] 如何减小第三方库对 bundle 体积的影响？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-027：如何减小第三方库对 bundle 体积的影响？

**答**：
- **按需引入**：组件库只 import 用到的组件，配合 babel-plugin-import 或库自带的 ESM 入口。
- **CDN externals**：react/vue 等大而稳定的库不打包，用 CDN 引入并命中 CDN 缓存。
- **替换**：moment 换 dayjs（280KB 到 2KB）、lodash 全量导入改 `lodash-es` 按函数导入。
- 用 `webpack-bundle-analyzer` 持续盯产物，配合 size-limit 在 CI 里对体积做卡点。

```javascript
// webpack.config.js —— 大而稳定的库走 CDN，不打进 bundle
module.exports = {
  externals: {
    react: 'React',
    'react-dom': 'ReactDOM'
  }
};

// index.html 中用 CDN 引入，可命中 CDN 缓存
// 注意：React 19 起官方不再提供 UMD 产物，externals 方案更适合 Vue 2/3 UMD
// 或仍停留在 React 18 的旧项目；React 19 建议保留 ESM 由打包器处理
// <script src="https://cdn.example.com/vue@3.global.prod.js"></script>

// 组件库按需引入：只打包用到的组件（Vue 3 生态示例）
import { ElButton, ElDialog } from 'element-plus';
```
