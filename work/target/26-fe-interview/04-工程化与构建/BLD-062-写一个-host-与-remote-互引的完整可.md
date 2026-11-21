---
title: [BLD-062] 写一个 host 与 remote 互引的完整可运行配置。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-062：写一个 host 与 remote 互引的完整可运行配置。
**答**：
- 结构：两个应用各自配 MF；host 通过 remotes 指向 remote 的 remoteEntry.js（module 类型导入）。
- 远端模块导入两种方式：import('app2/ProductList') 异步（推荐，自动拉容器）或 new Container().get 同步控制。
- async 边界：shared 依赖要求入口必须是异步 bootstrap（import('./bootstrap') 模式），否则初始化时容器尚未协商好依赖版本。
- remote 也可反引 host，形成互引；注意循环引用时的加载时序。

```javascript
// host/src/bootstrap.jsx：异步入口（shared 协商需要）
import { createRoot } from 'react-dom/client';
import App from './App';
createRoot(document.getElementById('root')).render(<App />);

// host/src/index.jsx：仅做异步引导
import('./bootstrap');

// host/webpack.config.js
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shellHost',
      remotes: {
        shopRemote: 'shopRemote@http://localhost:3001/remoteEntry.js',
        // 运行时动态地址（不写死）：
        // shopRemote: 'promise new Promise(resolve => { ... 动态 fetch 地址 ... })',
      },
      shared: {
        react: { singleton: true, eager: false, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true },
      },
    }),
    new (require('html-webpack-plugin'))(),
  ],
};

// host/src/App.jsx：消费远端模块
const RemoteProductList = React.lazy(() => import('shopRemote/ProductList'));
export default function App() {
  return (
    <Suspense fallback="加载中">
      <RemoteProductList />
    </Suspense>
  );
}

// remote 端入口同理：index.jsx -> import('./bootstrap')，webpack.config.js 见 BLD-061
```
