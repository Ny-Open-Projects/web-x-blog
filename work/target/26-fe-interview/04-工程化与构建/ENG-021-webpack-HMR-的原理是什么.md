---
title: [ENG-021] webpack HMR 的原理是什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-021：webpack HMR 的原理是什么？
**答**：
- 文件变化 -> webpack watch 重新编译 -> 生成新的 hash 与更新模块（manifest + chunk）。
- dev server 通过 WebSocket 把 hash 推给浏览器，浏览器比对后按需拉取更新的模块。
- module.hot.accept 声明模块的热替换边界：只更新指定模块并执行其回调，状态可保留。
- 找不到可接受的边界或替换失败时，回退为整页刷新。

```javascript
// 业务代码中手动声明热更新边界
if (module.hot) {
  // print.js 更新时只重新执行它，不刷新整页
  module.hot.accept('./print.js', () => {
    document.body.removeChild(document.getElementById('status'));
    require('./print.js')();
  });
}

// HMR 全链路：watch 编译 -> WebSocket 推送 hash -> 拉取 hot-update 文件
// -> 沿 accept 边界逐层向上替换 -> 失败则 live reload 兜底
```

---

## 第四章 Rollup esbuild 与 SWC（ENG-022 ~ ENG-024）
