---
title: [FRP-132] expose 与模板引用（ref 拿组件实例）是如何实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-132：expose 与模板引用（ref 拿组件实例）是如何实现的？

**答**：
- ref 挂在组件标签上时，mount/patch 的 `setRef` 时机把**实例**写入 ref：`templateRef.value = instance`（源码在 patch 的特定阶段统一处理 vnode.ref）。
- `<script setup>` 组件默认"封闭"：外部拿到的不是真实 instance，而是**公共实例代理**——get 先查 `instance.exposed`（expose() 写入的对象），查不到再有限度地透传。
- `defineExpose({ foo })` 就是往 `instance.exposed` 写对象；`useTemplateRef`/`ref(null)` 变量在 onMounted 后即可读到这个公共实例。
- 选项式组件默认暴露 `this` 的全部（proxy），这就是两种写法"封装性不同"的源码根源。

```javascript
// 简化实现，帮助理解 setRef 与 exposed 代理
function setRef(rawRef, vnode) {
  const { ref: r, type } = vnode;
  if (!r) return;
  const value = type.__async
    ? vnode.component.exposed ?? vnode.component.proxy   // 异步组件暴露 exposed
    : vnode.component                                     // 组件 ref -> 实例
    ?? vnode.el;                                          // 元素 ref -> DOM
  if (isRef(r)) r.value = value;
  else r[value.key] = value;
}

// 公共实例代理：限制 <script setup> 组件对外暴露的表面
function createPublicInstance(instance) {
  return new Proxy({}, {
    get(_, key) {
      // 1. 优先查 exposed —— defineExpose 写入的白名单
      if (instance.exposed && key in instance.exposed) return instance.exposed[key];
      // 2. setupState / props / ctx 的有限透传（源码里顺序严格且 dev 下告警）
      if (key in instance.setupState) return instance.setupState[key];
      if (key in instance.props) return instance.props[key];
      if (key[0] === '$') return instance.appContext.config.globalProperties[key];
      // 其余一律拿不到 —— 这就是"默认封闭"
    }
  });
}

// 用法与验证
const Child = {
  setup(props, { expose }) {
    const count = ref(0);
    function reset() { count.value = 0; }
    expose({ reset });        // 只暴露 reset —— count 与其他内部状态都被隐藏
    return { count, reset };
  }
};
const childRef = { value: null };
// <Child ref="childRef" /> mount 后：
// childRef.value.reset()      可以调用
// childRef.value.count        undefined —— 未 expose，公共代理不透传
// childRef.value.$.vnode      通过内部实例 $ 才能深入（不推荐）
```
