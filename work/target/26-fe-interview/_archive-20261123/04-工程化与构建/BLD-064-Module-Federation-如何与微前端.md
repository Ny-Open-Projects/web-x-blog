---
title: [BLD-064] Module Federation 如何与微前端架构结合？运行时集成指什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-064：Module Federation 如何与微前端架构结合？运行时集成指什么？
**答**：
- 微前端的三种集成时机：构建期集成（整站一起打，无独立部署）、运行时 iframe（强隔离弱体验）、运行时 MF/模块注册（独立开发部署 + 原生体验）。
- MF 的运行时集成：主应用只持有"远端地址清单"，页面挂载时动态 new URL 加载对应 remoteEntry，再 import exposed 模块——版本与地址都可下发。
- 主应用职责收敛：路由分发、公共依赖 singleton 提供、全局状态/登录态通过 context 传递（不是 iframe 的 window 隔离）。
- 与 qiankun 差异：qiankun 以 HTML 为入口、沙箱劫持 window；MF 以模块为入口、无沙箱（要自己做隔离，见 BLD-066）。

```javascript
// host/src/dynamicRemotes.js：运行时动态加载远端
export function loadRemote(remoteName, modulePath) {
  // 地址由配置中心下发 可灰度可回滚
  const entryUrl = window.__APP_CONFIG__.remotes[remoteName];
  return import(`${remoteName}@${entryUrl}/${modulePath}`); // 需要 remotes 配 promise 形式配合
}

// webpack.config.js：promise 形式的 remotes（动态地址）
module.exports = {
  plugins: [new (require('webpack').container.ModuleFederationPlugin)({
    name: 'shellHost',
    remotes: {
      shopRemote: `promise new Promise((resolve) => {
        const script = document.createElement('script');
        script.src = window.__APP_CONFIG__.remotes.shopRemote;
        script.onload = () => resolve(window.shopRemote);
        document.head.appendChild(script);
      })`,
    },
  })],
};
```
