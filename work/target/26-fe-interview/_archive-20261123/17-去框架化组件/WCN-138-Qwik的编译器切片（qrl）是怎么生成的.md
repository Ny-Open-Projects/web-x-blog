---
title: [WCN-138] Qwik 编译器的切片（qrl）是怎么生成的？闭包如何变成可懒加载 chunk？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-138：Qwik 编译器的切片（qrl）是怎么生成的？

**答**：
- 编译器扫描 `useXxx$()` 标记（`onClick$`、`useTask$` 等），把回调抽成独立模块导出：`const onClick$ = $(...)` → 产物 `chunk-abc.js` 导出 `onClick` 符号。
- 原地替换为 `qrl(() => import('./chunk-abc.js'), 'onClick', [捕获的 signal 引用])`——闭包变量变成显式捕获列表（scoped 引用序列化到 HTML）。
- 运行时恢复：事件触发 → loader 解析 qrl → import chunk → 执行 `onClick(props, capturedState)`；捕获的 signal 从序列化状态取回。
- 切片粒度：每个事件处理器/任务一个 chunk（细粒度按需），可以由打包器进一步合并；商品页 100 个按钮 = 100 个可懒加载单元但实际按点击加载。
- 约束：qrl 内不能引用组件作用域的未捕获变量（编译器报错强制显式化）——这是 resumability 的语言级保证。

```tsx
// 源码 → 切片示意
const AddCart = component$(() => {
  const cart = useStore({ items: [] });
  return <button onClick$={() => cart.items.push(1)}>加入</button>;
});
// 编译产物
const AddCart = component$(() => {
  const cart = useStore({ items: [] });
  return <button onClick$={qrl(() => import('./add-cart.js'), 'onClick', [cart])}>加入</button>;
});
// add-cart.js
export const onClick = (props, [cart]) => cart.items.push(1);
```
