---
title: [WCN-135] Solid 编译响应式的两个经典坑：解构丢响应与 effect 中读写时序？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-135：Solid 编译响应式的两个经典坑：解构丢响应与 effect 读写时序？

**答**：
- 坑一：解构 props——`const { name } = props` 是一次性快照，后续 props.name 变化不再更新（编译器只把 `props.name` 访问点编译为 getter）；正确做法保持 `props.name` 访问或用 `mergeProps`/`splitProps`（后者返回可解构的响应式对象）。
- 坑二：effect 里先写后读同一 signal——Solid 的 effect 是同步批处理语义，写操作会立即同步触发依赖该 signal 的其他 effect（不同于 Vue 微任务批处理），可能造成执行顺序意外；批量场景用 `batch()`。
- 坑三（补充）：`<For>` 里解构 item 同样丢响应（item 对象本身被替换才有新引用）。
- 调试方法：`on()`/`untrack()` 明确读取边界；solid-devtools 可视化依赖图。
- 深层原因：Solid 组件只跑一次，"快照"语义比 VDOM 框架更容易踩（React 每次重渲染天然拿到新值）。

```jsx
function Profile(props) {
  // const { name } = props;          // ❌ 快照，丢响应
  const [first, rest] = splitProps(props, ['name']);  // ✅ 响应式解构
  createEffect(() => {
    const n = props.name;             // 同步读取建立依赖
    console.log(n);
    batch(() => {                     // 多次写入合并
      setA(1); setB(2);
    });
  });
  return <div>{props.name}</div>;     // ✅ 保持访问点
}
```
