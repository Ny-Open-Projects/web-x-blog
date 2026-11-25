---
title: [R19-365] React19 ref 简化与 ref 回调清理
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, React19]
type: 面试题
---

## R19-365：React19 ref 简化与 ref 回调清理

**答**：
- ref 作为 prop：React 19 起 function 组件可直接接收 ref prop（不再需要 forwardRef 包裹）——forwardRef 仍可用但新代码废弃
- ref 回调清理函数：ref 回调可返回 cleanup 函数（挂载时调用 ref(el)，卸载时调用 cleanup）——替代「ref 回调里 return 前手动清理」的混乱模式
- 清理语义细节：依赖变化时 React 先调旧 cleanup 再调新回调；cleanup 不能返回值以外的内容（严格模式检查）
- 迁移注意：旧模式「ref 回调里写 return 表达式」会变成 cleanup——codemod 检查（历史上有人把箭头函数当表达式返回造成意外 cleanup）
- 与 useImperativeHandle 的关系：ref prop 直传后 useImperativeHandle 依然用于「暴露实例方法集合」——两者正交

```jsx
// React 19 新写法
function Input({ ref }) {
  return <input ref={ref} />;
}
// ref 回调清理
<input ref={(el) => {
  el.addEventListener('focus', onFocus);
  return () => el.removeEventListener('focus', onFocus);   // cleanup
}} />
```
