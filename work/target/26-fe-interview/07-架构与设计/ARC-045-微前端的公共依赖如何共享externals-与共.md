---
title: [ARC-045] 微前端的公共依赖如何共享？externals 与共享作用域怎么选？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-045：微前端的公共依赖如何共享？externals 与共享作用域怎么选？
**答**：
- externals：主应用 CDN 加载一次，子应用声明外部化，简单高效；缺点是全局变量耦合、版本由主应用锁死、Tree-shaking 失效。
- Module Federation shared：按 semver 协商 + 单例 + 惰性加载，版本可异步化，但失败模式复杂（版本冲突运行时才炸）。
- 微前端 + Monorepo 组合：公共依赖（React/请求层/工具）收敛为 monorepo 内部包，统一版本与构建产物，externals 或 shared 都指向它，避免"每个子应用带一份 React"。

```javascript
// 方案A：externals —— 主应用统一提供
// 主应用 index.html：<script src="/vendor/react-18.3.1.min.js"></script>
module.exports = {
  externals: {
    react: 'React', 'react-dom': 'ReactDOM',      // 子应用不再打包 React
  },
};

// 方案B：MF shared —— 版本协商的共享作用域
shared: {
  react: { singleton: true, strictVersion: true, requiredVersion: '^18.3.0' },
  'react-dom': { singleton: true },
  '@corp/request': { singleton: true },   // 内部包也走共享，全站一份
},
// strictVersion: true —— requiredVersion 不满足直接报错（fail fast），优于静默降级

// Monorepo 组合：packages/react-wrapper 统一封装版本升级与适配层
// 所有子应用从内部包 import React API，未来升级只改一处
```
