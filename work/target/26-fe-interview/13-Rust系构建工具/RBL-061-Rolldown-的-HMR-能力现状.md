---
title: [RBL-061] Rolldown 自身的 HMR 能力如何实现？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-061：Rolldown 自身的 HMR 能力如何实现？
**答**：
- rolldown 最初定位纯打包器（对标 rollup），HMR 由上层框架（vite/rolldown-vite）提供；但 rolldown 内核补了增量构建（experimental full bundle mode + HMR runtime）以支撑 vite 全量切换。
- 增量方式：复用模块级缓存 + 受影响子图重算（与 Rspack 同思路），产物级 diff 后只产出变更 chunk。
- rolldown-vite 的路径：先让 prod 打包换 rolldown（一致性收益），dev 的 HMR 继续沿用 vite 的 esbuild/native 管线，最终收敛到 rolldown 一体内核。
- 开发者视角：HMR API（import.meta.hot）不变，由 vite 层承载；rolldown 只负责"更快地产出 update"。
- 现状注意：实验性能力随版本变动大，面试答题聚焦"分层职责"而不是具体实现细节。
- 追问钩子：Turbopack 选择了另一条路——把 dev 增量做进内核（持久化的 function-level 增量计算），对比时强调架构差异。

```javascript
// rolldown-vite 下开发者 API 不变
if (import.meta.hot) {
  import.meta.hot.accept('./App.vue', (newMod) => {
    // vite 层负责 accept/dispose 协议，rolldown 负责更快产出增量产物
  });
}
// rolldown 侧：增量 = 模块缓存复用 + 子图重算 + chunk diff
```
