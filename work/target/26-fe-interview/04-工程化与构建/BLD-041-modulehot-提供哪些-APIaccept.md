---
title: [BLD-041] module.hot 提供哪些 API？accept/dispose/status 分别怎么用？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-041：module.hot 提供哪些 API？accept/dispose/status 分别怎么用？
**答**：
- module.hot.accept(deps, callback)：声明"这个模块（或依赖模块）更新时调用 callback 自行处理替换"；不注册则该模块更新默认冒泡到父级，最终无人处理就整页刷新。
- module.hot.dispose(callback)：模块被替换前执行清理（移除定时器、事件监听、还原全局状态），避免内存泄漏与重复执行。
- module.hot.status()：idle/apply/check 等状态机；module.hot.decline() 明确拒绝热更（该模块变化即触发刷新）。
- accept 的两个签名：self-accept（当前模块更新）与 accept 依赖（子模块更新但自己保留）；自下而上冒泡直到有 accept。

```javascript
// src/store.js：演示完整 HMR API
let state = { count: 0 };
let timer = null;

export function getState() { return state; }
export function setState(patch) { state = { ...state, ...patch }; }

// 依赖方（src/main.js）：
// import { getState, setState } from './store';
// module.hot.accept('./store', () => { render(); }); // store 更新时重渲染 main 自身不替换

if (module.hot) {
  // 自身被替换前的清理
  module.hot.dispose(() => {
    clearInterval(timer);
    state = { count: 0 }; // 恢复初始状态 防止状态串台
  });

  // 自我接受 状态更新不冒泡（单参数形式是该模块热更出错时的 error handler）
  module.hot.accept(() => {
    console.log('store 热替换完成 status =', module.hot.status());
  });

  // 明确拒绝热更 变化即整页刷新
  // module.hot.decline();
}
```
