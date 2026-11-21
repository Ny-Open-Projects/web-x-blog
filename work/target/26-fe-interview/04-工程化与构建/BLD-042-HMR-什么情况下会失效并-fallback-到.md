---
title: [BLD-042] HMR 什么情况下会失效并 fallback 到整页刷新？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-042：HMR 什么情况下会失效并 fallback 到整页刷新？
**答**：
- 无 accept 冒泡链断裂：更新的模块没有被自身或任何祖先 accept，runtime 无法替换 → 整页刷新（liveReload）。
- dispose/accept 回调抛错：更新过程异常，runtime 判定失败 → 刷新（错误会打到 overlay）。
- 非模块资源变化：index.html、动态加载的 worker、CDN 文件等不在 HMR 体系内 → 刷新。
- runtime/manifest 拉取失败：hash 对不上、.hot-update 文件 404（代理/多进程编译抢端口时常见）→ 刷新。
- 主动 decline 或 plugin 声明 noEmitOnErrors 时编译错误也会阻断热更新。

```javascript
// 1 常见失效场景与处理
// src/index.js —— 没有任何 accept：深层模块更新冒泡到入口失败 整页刷新
// 修复：为需要热更新的子树显式 accept
import App from './App';
import { render } from './render';
render(App);

if (module.hot) {
  module.hot.accept('./App', () => {
    // 用最新模块重新渲染 保持页面状态
    import('./App').then(({ default: NextApp }) => render(NextApp));
  });
  module.hot.accept('./render', () => location.reload()); // 工具模块主动声明刷新
}

// 2 devServer 排查配置
module.exports = {
  devServer: {
    hot: 'only',      // HMR 失败不回退整页刷新 便于观察问题（或 hot: true 回退）
    liveReload: true, // fallback 通道开关
    client: { logging: 'verbose' }, // 客户端日志看到 [HMR] 全过程
  },
};
```
