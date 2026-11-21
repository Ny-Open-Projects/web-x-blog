---
title: [DP-017] React 的 createElement / Vue 的 h 函数为什么是工厂模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-017：React 的 createElement / Vue 的 h 函数为什么是工厂模式？（高频）
**答**：
- 它们把"描述 UI 的意图"（type/props/children）工厂化为统一的 VNode 对象，调用方不关心 VNode 内部结构。
- 同一个 `h` 可以创建元素、组件、Fragment、Text——多态工厂，产物由参数决定。
- VNode 是纯数据（不可变描述），后续 renderer/diff 才消费它——"创建"与"渲染"解耦，这正是工厂的价值。
- 面试加分：能对照写出简化版 `createElement` 并说明 key/ref/children 的处理。

```javascript
// React 简化版 createElement：把 JSX 工厂化为统一 VNode
function createElement(type, config, ...children) {
  const props = {};
  let key = null;
  if (config) {
    for (const k in config) {
      if (k === 'key') key = config.key;
      else if (k !== 'ref' && k !== '__source' && k !== '__self') props[k] = config[k];
    }
  }
  if (children.length === 1) props.children = children[0];
  else if (children.length > 1) props.children = children;
  return { $$typeof: Symbol('react.element'), type, key, props }; // 统一产物：VNode
}
// JSX <div id="a">hello</div> 编译后就是工厂调用
const vnode = createElement('div', { id: 'a' }, 'hello');
console.log(vnode.props.children); // hello

// Vue3 的 h 同理：一份工厂，多类产物
// import { h } from 'vue';
// h('div', { id: 'a' }, 'hello')        -> 元素 vnode
// h(MyComp, { msg: 1 })                 -> 组件 vnode
// h('div', [h('span'), 'text'])         -> 嵌套 vnode，children 形态由参数决定
const h = (type, props = null, children = null) => ({ type, props, children });
console.log(h('span', { class: 'x' }, 'hi')); // { type: 'span', props: { class: 'x' }, children: 'hi' }
```
