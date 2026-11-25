---
title: [BLD-080] Vite HMR 的原理是什么？与 webpack 的消息模型差异在哪？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-080：Vite HMR 的原理是什么？与 webpack 的消息模型差异在哪？
**答**：
- 模块图精确失效：文件变化 → Vite 找到模块图中该文件的 module 节点，沿 import 链向上找最近的"接受更新边界"（声明 import.meta.hot.accept 的模块），只失效该边界以下模块。
- WebSocket 消息：`{ type: 'update', updates: [{ type: 'js-update' | 'css-update', path, timestamp }] }`，客户端按 timestamp 给模块 URL 加 `?t=` 破缓存重新请求。
- CSS 直接由 `type: 'css-update'` 换 link/style 内容，不走 JS 模块链，比 webpack 快。
- 自定义接受：import.meta.hot.accept(deps, cb)、dispose、prune、invalidate 对应 webpack 的 module.hot 全套语义；full-reload 消息触发整页刷新。

```javascript
// vite.config.js + 组件侧 HMR API
import { defineConfig } from 'vite';

export default defineConfig({
  server: { hmr: { overlay: true } },
});

// src/state.ts：自定义 HMR 处理
import { createGlobalState } from './store';

export const store = createGlobalState();

if (import.meta.hot) {
  // 保存旧状态 新模块复用（等价 webpack dispose）
  import.meta.hot.dispose((data) => { data.snapshot = store.snapshot; });

  // self accept：更新时用 data 恢复
  import.meta.hot.accept((next) => { /* next.store 使用新实现 */ });

  // 依赖失效时清除该模块导出
  import.meta.hot.prune(() => store.destroy());
}

// text 代码块：ws 消息流
// <- { type: 'connected' }
// <- { type: 'update', updates: [{ type: 'js-update', path: '/src/App.tsx', timestamp: 1710000 }] }
// -> GET /src/App.tsx?t=1710000   （单模块重新请求）
// <- { type: 'css-update', path: '/src/style.css', timestamp: 1710001 }
// <- { type: 'full-reload', path: '/index.html' }  （无法热替换时）
```

**追问**：

1. 改了文件为什么变成整页刷新？→ 沿 import 链向上找不到声明了 `accept` 的边界，只能 `full-reload`；React 项目要靠 Fast Refresh 插件在组件模块上注入 accept。
2. HMR 更新成功但组件状态丢了，为什么？→ 模块被整体替换而非原地更新，或者组件签名变了（hook 数量/顺序变化），Fast Refresh 会放弃保留 state 直接重挂。
3. Vite 与 webpack 的消息模型差在哪？→ webpack 只推 hash，客户端还要再请求 `hot-update.json` 拿变更清单；Vite 直接推 `path + timestamp` 精确到单模块，少一次往返。
