---
title: [FRP-116] 手写迷你 React（一）：createElement + render 循环 + 函数组件？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-116：手写迷你 React（一）：createElement + render 循环 + 函数组件？

**答**：
- `createElement(type, props, ...children)`：把 JSX 转成 `{ type, props: { ...props, children } }` 普通对象（JSX 编译即此调用）。
- render 循环：`render(vnode, container)` 把 vnode 树转成真实 DOM——文本节点单独处理、函数组件**调用它拿到 children vnode** 再递归、宿主元素建 DOM + 挂 props + 递归 children。
- 函数组件不产生 DOM，只做"调用展开"：`const el = fn(props); render(el, container)`——React 中对应 beginWork 里执行 renderWithHooks。
- commit 与 render 在这个玩具版里是一体的（同步直出）；真实 React 把"算出 fiber 树"与"提交 DOM"拆开以支持中断（见 FRP-087）。

```jsx
// 简化实现，帮助理解：createElement 与递归 render 循环
function createElement(type, props, ...children) {
  return {
    type,
    props: {
      ...props,
      children: children.flat().map((c) =>
        typeof c === 'object' ? c : createTextElement(c)), // 原始值包成文本 vnode
    },
  };
}
const createTextElement = (text) => ({ type: 'TEXT_ELEMENT', props: { nodeValue: text, children: [] } });

function render(vnode, container) {
  if (vnode.type === 'TEXT_ELEMENT') {               // 文本叶子
    container.appendChild(document.createTextNode(vnode.props.nodeValue));
    return;
  }
  const isFn = typeof vnode.type === 'function';
  if (isFn) {
    // 函数组件：调用展开成它的返回值，再递归 render（无实例无 Hook）
    const childVNode = vnode.type(vnode.props);
    render(childVNode, container);
    return;
  }
  // 宿主元素：建 DOM -> 挂属性 -> 递归子节点
  const dom = document.createElement(vnode.type);
  Object.entries(vnode.props)
    .filter(([k]) => k !== 'children')
    .forEach(([k, v]) => {
      if (k.startsWith('on')) dom.addEventListener(k.slice(2).toLowerCase(), v); // 事件
      else dom[k] = v;                               // 简化：直接设 DOM property
    });
  vnode.props.children.forEach((child) => render(child, dom));
  container.appendChild(dom);
}

// 用法：JSX 会被编译为 createElement 调用，这里手写等价形式
const Title = (props) => createElement('h1', null, 'Hello ', props.name);
const App = () => createElement('div', { className: 'root' },
  createElement(Title, { name: 'mini-react' }),
  createElement('button', { onClick: () => console.log('clicked') }, 'ok'),
);
render(createElement(App, null), document.querySelector('#root'));
// DOM 结果：<div class="root"><h1>Hello mini-react</h1><button>ok</button></div>
```
