---
title: [BLD-051] 把大库外部化（externals + CDN）的时机与做法？与 DLL 的关系？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-051：把大库外部化（externals + CDN）的时机与做法？与 DLL 的关系？
**答**：
- 时机：超大型稳定库（echarts、moment、xlsx）不常升级且体积巨大时，改由 CDN script 提供，构建产物只留引用；内网/离线部署要自托管 CDN 资源。
- 做法：html-webpack-plugin 注入 script 标签 + externals 映射全局变量；SSR/node 场景 externals 走 commonjs。
- 与 DLL：webpack 5 时代 DLL 已不建议（升级麻烦、缓存体系不兼容），externals + 持久缓存 + vendor 分组是主流；DLL 只在"无法 CDN 的老工程"里残留。
- 风险：CDN 可用性与版本漂移要用 lock 语义（固定版本 URL + SRI）。

```javascript
// webpack.config.js：externals + 自动注入 CDN
const HtmlWebpackPlugin = require('html-webpack-plugin');

const CDN = {
  react: { pkg: 'react', version: '18.3.1', global: 'React' },
  'react-dom': { pkg: 'react-dom', version: '18.3.1', global: 'ReactDOM' },
};

module.exports = {
  externals: [
    function ({ request }, callback) {
      if (CDN[request]) {
        return callback(null, `root ${CDN[request].global}`);
      }
      callback();
    },
  ],
  plugins: [
    new HtmlWebpackPlugin({
      template: 'public/index.html',
      cdnJs: Object.values(CDN).map((d) =>
        `https://cdn.example.com/${d.pkg}@${d.version}/umd/${d.pkg}.production.min.js`),
    }),
  ],
};

// public/index.html 模板片段（text 代码块）：
// <% htmlWebpackPlugin.options.cdnJs.forEach(function(url){ %>
//   <script src="<%= url %>" crossorigin="anonymous"></script>
// <% }) %>
```
