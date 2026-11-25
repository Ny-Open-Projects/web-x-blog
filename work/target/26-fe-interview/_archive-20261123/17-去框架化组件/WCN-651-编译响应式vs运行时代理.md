---
title: [WCN-651] 编译期响应式（如 Solid/Svelte）与运行时代理（如 Vue 3 Proxy）本质区别是什么？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-651：编译期响应式（如 Solid/Svelte）与运行时代理（如 Vue 3 Proxy）本质区别是什么？

**答**：
- 结论：运行时代理在「读取时」动态收集依赖（灵活但有代理开销）；编译响应式在「构建时」静态分析模板生成精准更新代码（零代理开销但需编译期信息完整）。
- 取舍：代理能处理运行时才确定的动态依赖（如 obj[key]）；编译方案对动态表达式需回退到运行时兜底。
- 追问钩子：为什么 Svelte 编译后体积反而可能更大？考察对「编译产物包含运行时辅助代码」的理解，而非绝对化结论。

```javascript
// 运行时代理：动态收集，灵活但有 trap 开销
const state = new Proxy({ a: 1 }, {
  get(t, k) { track(t, k); return Reflect.get(t, k); },
  set(t, k, v) { const r = Reflect.set(t, k, v); trigger(t, k); return r; },
});
// 编译响应式：模板 <div>{count}</div> 被编译为
function render_compiled(count, setText) {
  // 构建期就知道这个 div 只依赖 count，直接生成：
  setText('div-1', count());
  // 无需 Proxy，无需 diff，依赖在编译期固化
}
```
