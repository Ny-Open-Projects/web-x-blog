---
title: [BLD-039] HMR 的完整流程是怎样的？画出时序图。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-039：HMR 的完整流程是怎样的？画出时序图。
**答**：
- 第一步：文件变化，webpack 的 watcher 触发重编译，webpack-dev-middleware 内存 fs 更新。
- 第二步：服务端通过 websocket 推送消息（先 ok/hash，带本次编译 hash）。
- 第三步：客户端 HMR runtime 收到新 hash 后请求两个文件：manifest（.hot-update.json，记录哪些 chunk 变了）和 update（.hot-update.js，新模块代码）。
- 第四步：runtime 调 module.hot.accept 注册的回调，用新模块替换旧模块；替换成功则热更新，失败回退整页刷新。
- 面试高频追问：hash 的作用是匹配版本（请求的 update 文件名带 hash，避免串版本）；accept 的粒度是模块，谁 accept 谁负责替换。

```mermaid
sequenceDiagram
  participant F as 文件系统
  participant W as webpack 编译器
  participant S as dev server
  participant C as 浏览器 HMR runtime
  F->>W: 文件变化触发重编译
  W->>W: 增量编译生成新模块与 hash
  W->>S: 内存 fs 更新产物
  S-->>C: websocket 推送 hash 消息
  C->>S: GET manifest.hot-update.json
  S-->>C: 返回本次变化的 chunk 列表
  C->>S: GET chunk.hot-update.js
  S-->>C: 返回新模块代码
  C->>C: 调用 module.hot.accept 回调替换模块
  alt 替换成功
    C->>C: 页面保持状态 更新完成
  else 替换失败
    C->>C: fallback 整页刷新
  end
```

```javascript
// webpack.config.js：开启 HMR 的最小生产级配置
module.exports = {
  mode: 'development',
  devServer: {
    hot: true,               // 注入 HMR runtime 与 websocket 服务
    liveReload: false,       // 关闭整页刷新通道 逼出热更新问题
    static: { directory: 'public' },
  },
  devtool: 'eval-cheap-module-source-map', // HMR 场景最快的可读 sourcemap
};
```
