---
title: [FRP-117] 手写迷你 React（二）：函数组件 + useState 的 Hook 链实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-117：手写迷你 React（二）：函数组件 + useState 的 Hook 链实现？

**答**：
- 关键结构：把"每次 render"改造成**可重复执行的工作单元**——`wipFiber` 上挂 `hooks` 数组（对应真实 React 的链表，数组是简化版）；`useState` 按调用序号取 hook：首次初始化、后续复用。
- setState：不直接改 DOM，而是把新值写入对应 hook（真实 React 是 update queue），然后**把 fiber 根标记为待渲染**，用微任务调度一次 `render`——这就是批处理的雏形。
- render 时 `hookIndex = 0` 复位；函数组件执行中每次 useState 调用按 `hookIndex++` 对位（顺序一致性，呼应 FRP-079）。
- 局限说明：真实 React 的 reconciliation 是增量可中断的 fiber 循环，这里是全量同步重渲染，但 useState 的核心机制（槽位复用 + 调度重渲染）已经完整。

```javascript
// 简化实现，帮助理解：useState 的槽位复用与调度重渲染
let wipFiber = null;      // 当前正在渲染的 fiber（简化为全局单根）
let hookIndex = 0;
let rerenderScheduled = false;

function renderApp(component, container) {
  wipFiber = { hooks: [], container, component };
  hookIndex = 0;
  const vnode = component();          // 函数组件执行，useState 依次注册槽位
  container.innerHTML = '';
  renderVnode(vnode, container);      // renderVnode 同 FRP-116 的 render
}
function renderVnode(vnode, container) {
  if (typeof vnode.type === 'function') return renderVnode(vnode.type(vnode.props), container);
  const el = vnode.type === 'TEXT_ELEMENT'
    ? document.createTextNode(vnode.props.nodeValue)
    : Object.assign(document.createElement(vnode.type), { className: vnode.props.className });
  Object.entries(vnode.props || {})
    .filter(([k]) => !k.startsWith('on') && k !== 'children' && k !== 'nodeValue' && k !== 'className')
    .forEach(([k, v]) => (el[k] = v));
  if (vnode.props?.onClick) el.addEventListener('click', vnode.props.onClick);
  (vnode.props?.children || []).forEach((c) => renderVnode(c, el));
  container.appendChild(el);
}

function useState(initial) {
  const hooks = wipFiber.hooks;
  const idx = hookIndex++;
  if (hooks[idx] === undefined) hooks[idx] = { value: initial }; // 首次：初始化槽位
  const hook = hooks[idx];
  const setState = (newVal) => {
    hook.value = typeof newVal === 'function' ? newVal(hook.value) : newVal;
    if (!rerenderScheduled) {         // 批处理：同一 tick 多次 setState 一次渲染
      rerenderScheduled = true;
      Promise.resolve().then(() => {
        rerenderScheduled = false;
        renderApp(wipFiber.component, wipFiber.container); // 全量重渲染
      });
    }
  };
  return [hook.value, setState];      // 按槽位对位返回，顺序必须稳定
}

// 用法：计数器
function Counter() {
  const [count, setCount] = useState(0);
  const [msg, setMsg] = useState('hi');
  return { type: 'div', props: { children: [
    { type: 'TEXT_ELEMENT', props: { nodeValue: `count: ${count} msg: ${msg}` } },
    { type: 'button', props: {
      onClick: () => { setCount(count + 1); setMsg('updated'); }, // 批处理合并
      children: [{ type: 'TEXT_ELEMENT', props: { nodeValue: '+1' } }] } },
  ] } };
}
renderApp(Counter, document.querySelector('#root'));
console.log('点击按钮后：微任务合并两次 setState 为一次渲染，两个 useState 槽位各自对位更新');
```
