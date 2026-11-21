---
title: [BLD-125] preset-env 与 browserslist 联动机制：目标怎么决定编译与垫片行为？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-125：preset-env 与 browserslist 联动机制：目标怎么决定编译与垫片行为？
**答**：
- preset-env 先读**目标浏览器**（`targets` 或 browserslist 配置，含 `package.json`/`.browserslistrc`），再对照 `compat-data`（caniuse 数据）算出"需要编译的语法集合"与"需要垫的 API 集合"——同一份目标，同时控制 babel 语法转换与 useBuiltIns 的 polyfill 注入量。
- 优先级：preset-env 的 `targets` > browserslist 的 `env` 段（如 `production`）> 默认 `> 0.5%, last 2 versions`；webpack/babel/postcss/autoprefixer 全部消费同一份 browserslist，**一处配置全局生效**（联动高频考点）。
- 目标越现代产物越小：`targets: { chrome: '80' }` 时可选链/可选捕获不转译、polyfill 注入趋近 0；不配 targets 会按"全兼容"转译，产物徒增。
- 查询调试：`npx browserslist` 列出命中的浏览器；`npx browserslist --coverage` 看覆盖率；preset-env 配 `debug: true` 打印"启用了哪些插件/垫了哪些 API"。

```json
// package.json：一份 browserslist 驱动 babel/postcss/构建产物目标
{
  "browserslist": {
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version"]
  }
}
```

```javascript
// babel.config.js：验证联动（debug 输出可看到最终 targets 与插件清单）
module.exports = {
  presets: [
    ['@babel/preset-env', {
      // 不写 targets：完全交给 browserslist（推荐，避免两处配置漂移）
      useBuiltIns: 'usage',           // API 垫片按使用点注入
      corejs: { version: 3, proposals: false },
      debug: process.env.BABEL_DEBUG === '1', // 打印：targets / plugins / polyfills 三张表
      // exclude: ['es.promise.includes'], // 某垫片引发兼容 bug 时的排除法
    }],
  ],
};
// 面试演示：browserslist 写 ["chrome >= 90"]
// → debug 输出 "@babel/preset-env: no transform needed"（语法不降级）
// → 产物里没有 core-js；把目标改成 ["ie 11"] 后立即出现一堆 helper 与 core-js import
```
