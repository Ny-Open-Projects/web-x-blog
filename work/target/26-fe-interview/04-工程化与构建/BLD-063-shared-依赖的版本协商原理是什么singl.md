---
title: [BLD-063] shared 依赖的版本协商原理是什么？singleton、requiredVersion、strictVersion 各起什么作用？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-063：shared 依赖的版本协商原理是什么？singleton、requiredVersion、strictVersion 各起什么作用？
**答**：
- 每个应用把 shared 依赖注册进一个全局共享作用域（share scope）：{ 依赖名: { 版本: { get, from } } }。
- host 先注册自己的版本，remote 加载时对比：有满足 requiredVersion 的版本就复用（不再加载自己打包的副本），否则加载自己的副本（fallback chunk）。
- singleton: true：强制全局唯一实例（react/vue/router 必须单例，两个 React 实例会导致 hooks 报错）；版本不满足时用警告/报错代替多实例。
- strictVersion: true：版本不匹配直接抛错（生产严格）；默认只 console.warn。
- eager: true：把 shared 打进入口（牺牲体积换首屏，仅 host 入口常用）。

```javascript
// webpack.config.js：shared 精细配置示例
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'appA',
      shared: {
        // 必须 singleton：实例不唯一会导致 hooks 状态错乱
        react: { singleton: true, requiredVersion: '~18.3.1', strictVersion: true, eager: true },
        'react-dom': { singleton: true, strictVersion: true },
        'react-router-dom': { singleton: true, requiredVersion: '^6.0.0' },
        // 大型工具库允许版本共存（多实例无害 只多占体积）
        lodash: { requiredVersion: '^4.17.0' },
        // 纯 UI 组件库 允许 host 提供版本 fallback
        '@app/design': { import: false, shareKey: '@app/design' },
      },
    }),
  ],
};

// text 代码块：协商结果伪码
// shareScope.react = { '18.3.1': { get: () => __webpack_require__('react-18.3.1') } }
// remote 要求 ^18.2.0 -> 18.3.1 满足 -> 复用 host 版本，remote 自带副本作为 fallback 不加载
```
