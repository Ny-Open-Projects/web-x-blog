---
title: [R19-007] React 19 中 ref 作为 prop，forwardRef 发生了什么变化？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-007：React 19 中 ref 作为 prop，forwardRef 发生了什么变化？
**答**：
- React 19 中函数组件可以直接把 `ref` 当作普通 prop 接收，forwardRef 被标记为弃用。
- `function MyInput({ ref, ...props })` 即可把 ref 透传给内部 DOM 元素。
- forwardRef 在 React 19 仍可运行以保持兼容，但新代码推荐直接用 ref prop，类组件行为不变。
- 组件库迁移时注意：类型签名从 `ForwardRefRenderFunction` 变为普通函数组件参数里的 ref。

```jsx
// React 19：ref 就是普通 prop，不再需要 forwardRef 包装
function MyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

function Parent() {
  const inputRef = useRef(null);

  const focusInput = () => {
    inputRef.current?.focus();
  };

  return (
    <>
      <MyInput ref={inputRef} placeholder="无需 forwardRef" />
      <button onClick={focusInput}>聚焦</button>
    </>
  );
}
```
