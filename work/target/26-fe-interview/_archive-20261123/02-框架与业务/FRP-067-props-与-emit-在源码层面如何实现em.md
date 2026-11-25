---
title: [FRP-067] props 与 emit 在源码层面如何实现？emit 是怎么找到对应事件的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-067：props 与 emit 在源码层面如何实现？emit 是怎么找到对应事件的？

**答**：
- props 分两层：`props`（声明与未声明的"可被父访问"属性，最终落 DOM 或透传）与 `attrs`（未声明进 attrs，不做响应式代理）；组件实例上 `instance.props` 是 **shallowReactive**（浅层代理即可，父组件更新会整体换引用）。
- emit 实现（runtime-core 的 `emit`）：核心是**事件名到 props 的映射查找**——事件 `foo` 依次尝试 props 上的 `onFoo`、`onFOO`（camelCase → 首字母大写），命中即调用 `props[`on${cap(event)}`](...args)`；`@update:modelValue` 对应 props 里 `onUpdate:modelValue` 这个 key。
- `emits` 声明的作用：把声明过的 `onXxx` 从 attrs 中**剥除**（否则 `@click` 未声明会同时作为 attr 落到根元素上，造成二次触发），并对未声明事件给开发警告。
- emit 还会校验返回值：若声明了校验函数且返回 false，仅警告不阻断调用。

```javascript
// 简化实现，帮助理解 emit 的事件查找与 attrs 剥离
function capitalize(s) { return s[0].toUpperCase() + s.slice(1); }

function emit(instance, event, ...args) {
  const props = instance.vnode.props;
  let handler = null;
  // 查找顺序：onFoo -> onFOO（kebab/camel 兼容）
  const camel = event.replace(/-(\w)/g, (_, c) => c.toUpperCase());
  handler = props[`on${capitalize(camel)}`] || props[`on${camel.toUpperCase()}`];
  if (!handler) {
    console.warn(`[emit] 未找到事件 ${event} 的监听器`);
    return;
  }
  handler(...args);
}

function initProps(vnode, emits) {
  const props = {}, attrs = {};
  for (const key in vnode.props) {
    // 声明了 emits 的事件监听器不进 attrs（避免落到根元素二次触发）
    const evt = key.startsWith('on') ? key.slice(2).toLowerCase() : null;
    if (evt && (emits || []).includes(evt)) props[key] = vnode.props[key];
    else if (key.startsWith('on')) props[key] = vnode.props[key];
    else attrs[key] = vnode.props[key];
  }
  return { props, attrs };
}

// 用法：父组件 <Child @inc="n++" class="btn" />
const Child = {
  emits: ['inc'],
  setup(props, { emit }) {
    return { click() { emit('inc', 1); } }; // emit('inc') 找 props.onInc
  },
};
const vnode = createVNode(Child, { onInc: (n) => console.log('父收到 inc', n), class: 'btn' });
const { props, attrs } = initProps(vnode, Child.emits);
console.log('onInc 在 props:', 'onInc' in props, '| class 在 attrs:', 'class' in attrs); // true true
emit({ vnode }, 'inc', 1); // 父收到 inc 1
```
