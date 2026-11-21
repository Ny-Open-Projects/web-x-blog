---
title: [FRP-159] forwardRef 的实现原理是什么？React 19 的 ref as prop 改了什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-159：forwardRef 的实现原理是什么？React 19 的 ref as prop 改了什么？

**答**：
- 函数组件本接收不到 ref（ref 是 fiber 的特殊字段不是普通 prop）；`forwardRef` 生成 `{$$typeof: REACT_FORWARD_REF_TYPE, render}` 的包装元素，React 在 beginWork 中**特判该类型**，把 ref 作为第二参传给 render。
- React 19 取消了这个特判的必要性：函数组件的 `ref` 变成**普通 prop**（props.ref 直接可读可透传），forwardRef 仍向后兼容但可移除。
- 类组件一直不受影响（ref 指向实例）；DOM 元素的 ref 仍由 React 在 commit 阶段特殊处理（attach/detach）。
- 19 的迁移收益：类型更简单（无需泛型双参）、ref 可与其他 props 一样在自定义 Hook 间传递、统一了"ref 也是 props"的心智。

```javascript
// 简化实现，帮助理解 forwardRef 与 React19 变化
// —— 19 之前：特判包装元素 ——
const ForwardRefSymbol = Symbol.for('react.forward_ref');
function forwardRef(render) {
  return { $$typeof: ForwardRefSymbol, render };
}
function beginWork(fiber) {
  if (fiber.tag === ForwardRefComponent) {
    // 关键：ref 不是 props 的一部分，需要单独取出
    const { ref } = fiber;
    const props = fiber.pendingProps;
    const children = fiber.type.render(props, ref); // ref 作为第二参
    return reconcileChildren(fiber, children);
  }
  // 普通函数组件：render(props) —— 根本拿不到 ref
}

// —— React 19：ref 就是普通 prop ——
function beginWork19(fiber) {
  const props = fiber.pendingProps;
  // ref 混入 props：函数组件直接读取
  // <MyInput ref={inputRef} label="名" /> -> props = { ref: inputRef, label: '名' }
  const children = fiber.type(props);   // 组件内 props.ref 即 inputRef
  return reconcileChildren(fiber, children);
}

// 19 之前的写法：
const MyInputLegacy = forwardRef((props, ref) => (
  <input ref={ref} {...props} />
));

// React 19 的写法：
function MyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;   // ref 与其他 prop 一样转发
}
// 类组件不变：ref 仍指向实例（React 在 commit 的 attachRef 里特判类 fiber）
// DOM 元素不变：ref 由 commitLayoutEffects 里 commitAttachRef 统一处理
```
