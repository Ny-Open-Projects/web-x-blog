---
title: [FRP-069] 生命周期钩子在源码里如何注册与调用？mounted 为什么在 DOM 挂载后才执行？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-069：生命周期钩子在源码里如何注册与调用？mounted 为什么在 DOM 挂载后才执行？

**答**：
- 注册：`onMounted(fn)` 等本质是 `injectHook(type, fn, instance)`——把 fn push 到 `instance[type]`（如 `instance.m = [fn]`）数组里，并用 `currentInstance` 定位到"哪个组件的钩子"；这也是钩子必须在 setup 同步期调用的原因（异步调用后 currentInstance 为 null，注入失败并警告）。
- 钩子数组按**调用顺序**有固定插槽：beforeCreate/create 在 setupComponent 前后、beforeMount/mounted 在首次 patch 前后、beforeUpdate/updated 在重渲染 patch 前后、beforeUnmount/unmounted 在卸载逻辑前后。
- mounted "异步"的原因：首次 patch 中**先递归挂完所有子孙 DOM**，子组件先于父组件完成挂载，各组件的 mounted 回调被推入 **post 队列（queuePostRenderEffect）**，patch 全部结束后统一 flush——所以子 mounted 先于父 mounted 打印。
- 多次调用同一钩子会按序全部执行（数组语义）；组合式 API 中钩子注册在 setup 内即隐式绑定当前实例，无需 this。

```javascript
// 简化实现，帮助理解钩子注册与 post 队列调用时机
const postFlushCbs = []; // mounted 等钩子的 post 队列

function injectHook(type, hook, instance) {
  if (!instance) return console.warn('[hook] setup 之外调用丢失实例');
  (instance[type] || (instance[type] = [])).push(hook); // 数组：支持多次注册
}

let currentInstance = null;
const createHooks = (type) => (...args) => injectHook(type, args[0], currentInstance);
const onMounted = createHooks('m'), onBeforeMount = createHooks('bm');

function setupComponent(setupFn, instance) {
  currentInstance = instance;
  instance.bm?.forEach((h) => h());      // beforeMount：DOM 未创建
  const render = setupFn();              // setup 内注册的钩子挂到 instance
  currentInstance = null;
  return render;
}

function mountWithHooks(setupFn, instance, container) {
  const render = setupComponent(setupFn, instance);
  const subTree = render();              // 生成子树
  // 真实递归 patch 挂载（简化为直接建 DOM）
  subTree.el = document.createElement(subTree.tag);
  subTree.el.textContent = subTree.children;
  container.appendChild(subTree.el);
  // 挂载完成 -> 推入 post 队列，统一 flush（保证子先父后）
  instance.m?.forEach((h) => postFlushCbs.push(h));
  queuePostFlush();
}

function queuePostFlush() {
  Promise.resolve().then(() => {
    const cbs = [...postFlushCbs];
    postFlushCbs.length = 0;
    cbs.forEach((h) => h());             // mounted 全部在 DOM 就绪后执行
  });
}

// 验证：两个组件 mounted 的执行顺序
const parent = { m: [] }, childInst = { m: [] };
const childRender = setupComponent(() => () => ({ tag: 'span', children: 'c' }), childInst);
onMounted(() => console.log('child mounted'), childInst); // 注册进 childInst.m

const parentRender = setupComponent(() => () => ({ tag: 'div', children: 'p' }), parent);
onMounted(() => console.log('parent mounted'), parent);

mountWithHooks(() => childRender, childInst, document.body);
mountWithHooks(() => parentRender, parent, document.body);
// 输出顺序：child mounted -> parent mounted（post 队列按注册/完成序 flush）
```
