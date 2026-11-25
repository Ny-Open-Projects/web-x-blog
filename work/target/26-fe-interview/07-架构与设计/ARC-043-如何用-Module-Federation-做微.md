---
title: [ARC-043] 如何用 Module Federation 做微前端？与 qiankun 路线差异？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-043：如何用 Module Federation 做微前端？与 qiankun 路线差异？
**答**：
- MF 在构建期声明 exposes/remotes/shared：子应用暴露模块，主应用运行时远程加载，本质是"运行时模块级组合"而非"应用级容器"。
- 与 qiankun 差异：MF 无 HTML Entry 与沙箱，多个应用共享同一个 JS 上下文（冲突自己负责）；但粒度更细（可只共享一个组件/一段逻辑）、依赖共享机制内建。
- 取舍：同技术栈 + 信任边界内的模块化共享选 MF；异构栈/强隔离/老应用选 qiankun 类容器方案。

```javascript
// 子应用 webpack.config.js —— 暴露模块
const { ModuleFederationPlugin } = require('webpack').container;
module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'appTrade',
      filename: 'remoteEntry.js',
      exposes: {
        './OrderList': './src/pages/OrderList',   // 暴露页面级模块
        './Button': './src/components/Button',    // 也可只暴露一个组件
      },
      shared: { react: { singleton: true, requiredVersion: false }, 'react-dom': { singleton: true } },
    }),
  ],
};
// 主应用：const OrderList = React.lazy(() => import('appTrade/OrderList'));
// 注意：MF 没有沙箱，shared singleton 的版本协商失败会直接运行时报错
```

**追问**：

1. shared 里 react 版本协商失败，运行时报什么、怎么兜底？ → 会报 shared module 不可用或版本不符，需在 shared 填真实 requiredVersion、宿主启动时校验并打印冲突模块，兜底是让远端自带副本、放弃 singleton。
2. 没有沙箱，两个子应用同时改 window 和全局样式怎么治理？ → 全局变量约定命名空间并禁止裸写 window，样式用前缀或 Shadow DOM 局部隔离，构建期加 lint 规则扫 window 赋值，跨应用通信只走显式事件总线。
3. remoteEntry 挂了、子应用又发了新版，主应用怎么感知？ → 入口地址带版本或 hash 防 CDN 缓存旧入口，加载失败由 error boundary 兜住并重试，新版按远端地址灰度切换，别指望远端自己覆盖。
