---
title: [WCN-672] 编译型框架里 HMR（热更新）如何实现？为什么有时必须刷新整页？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-672：编译型框架里 HMR（热更新）如何实现？为什么有时必须刷新整页？

**答**：
- 结论：HMR 按「模块边界」替换编译产物，保留组件状态（用代理缓存状态）；若修改影响模块拓扑/副作用（如顶层样式注入、循环依赖），需回退整页刷新。
- 做法：编译时给模块注入 accept/hot 接口；运行时用状态代理保存旧实例的 state；替换后重新 mount 并恢复状态。
- 追问钩子：为什么改 props 定义常需刷新？因为类型/运行时 schema 变化影响调用方契约——考察对「HMR 边界」的理解。

```javascript
// 编译注入的 HMR 接口（示意）
const hot = {
  accept(deps, cb) { /* 依赖更新时调用 cb */ },
  dispose(cb) { /* 模块替换前清理 */ },
  data: {}, // 跨替换保留的状态
};
function applyHotUpdate(newModule, oldState) {
  // 保留状态：用代理接管新旧实例的读写
  const state = new Proxy(hot.data, {
    get(t, k) { return k in t ? t[k] : oldState?.[k]; },
  });
  newModule.mount(state);
}
// 若 newModule 改变了顶层副作用或模块图 → 返回 false，触发 full reload
```
