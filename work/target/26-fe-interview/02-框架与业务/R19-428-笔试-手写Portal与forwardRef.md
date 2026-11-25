---
title: [R19-428] 笔试：手写 Portal 与 ref 转发（含 cleanup）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## R19-428：笔试：手写 Portal 与 ref 转发

**答**：实现：① `createPortal(children, container)`：children 渲染到 container（DOM 位置不同但 React 树父子关系保持——事件冒泡按 React 树）；② ref 转发：React19 直接 ref prop 版本 + 兼容版；③ ref 回调 cleanup 语义（挂载调用、卸载调用 cleanup）；④ 卸载时 portal 容器内 DOM 清理。写出实现。

```javascript
const PORTAL_KEY = '__portal_container';

function createPortal(children, container) {
  return { $$portal: true, children, container };   // 渲染器识别特殊标记
}
// 渲染器挂载分支:
function mount(vnode, parentDom) {
  if (vnode.$$portal) {
    mountChildren(vnode.children, vnode.container); // 挂到目标容器
    // 但事件冒泡仍按 React 树: 事件系统用 fiber 树而非 DOM 树
    return;
  }
  // ...普通挂载
}
function unmount(vnode) {
  if (vnode.$$portal) {
    unmountChildren(vnode.children, vnode.container);  // 从目标容器清理
    return;
  }
}

// ref 转发 (React19 直接 ref prop)
function FancyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}
// ref 回调 cleanup (React19)
function Demo() {
  return <input ref={(el) => {
    el?.addEventListener('focus', onFocus);
    return () => el?.removeEventListener('focus', onFocus);   // 卸载/变更时调用
  }} />;
}
// 兼容旧版: forwardRef((props, ref) => <input ref={ref} />)
```

**评分点**：
- portal 的「DOM 挂载点切换 + React 树不变」语义（事件冒泡按树）
- 卸载时目标容器清理
- ref 回调 cleanup 的时序（先 cleanup 再新回调）
- forwardRef 与 React19 ref prop 的兼容
