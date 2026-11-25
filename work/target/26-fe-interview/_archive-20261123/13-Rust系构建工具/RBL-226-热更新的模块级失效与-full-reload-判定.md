---
title: [RBL-226] HMR 的模块级失效与 full reload 判定
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-226：HMR 的模块级失效与 full reload 判定

**答**:
- 失效传播：变更模块标脏 → 沿「接受边界」（module.hot.accept）向上传播；找到接受者就停（局部替换），无接受者到达 root → full reload
- CSS 特例：CSS 模块天然可自接受（style 替换），无 JS 传播；React Fast Refresh 是「接受者 + 组件边界判定」的实现
- 不可 HMR 的变更：配置变更（vite.config）、HTML 入口、依赖预构建变化 → 强制 full reload（工具应明示原因而非静默刷新）
- 深层坑：接受边界错位（父组件 accept 但子组件 state 未清理）导致「更新后旧状态残留」——HMR 语义是「保留 state 尽力替换」

```javascript
// 接受边界
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => render(newModule.App))   // 局部替换
  import.meta.hot.dispose((data) => cleanup())                   // 清副作用
}
// 无 accept 的模块链 → 传播到入口 → full reload
```
