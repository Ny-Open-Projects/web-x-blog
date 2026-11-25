---
title: [V3-521] 笔试：手写 provide/inject 与 nextTick
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 语言特性]
type: 笔试题
---

## V3-521：笔试：手写 provide/inject 与 nextTick

**答**：实现：① `provide(key, value)`：写入当前实例的 provides 对象（原型链指向父 provides）；② `inject(key, default)`：沿 provides 原型链查找（Vue 用原型链实现查找——比手动向上遍历优雅）；③ `nextTick(fn)`：基于微任务批合并（同一 tick 内多次调用只注册一个 promise）；④ nextTick 与渲染时序（在 patch flushPromise 之后执行）。写出实现。

```javascript
let currentInstance = null;

function provide(key, value) {
  const inst = currentInstance;
  inst.provides = inst.provides ?? Object.create(inst.parent?.provides ?? null); // 原型链挂父级
  inst.provides[key] = value;
}

function inject(key, defaultValue, treatDefaultAsFactory = false) {
  const inst = currentInstance;
  if (inst && inst.provides && key in inst.provides)
    return inst.provides[key];                        // 原型链自动向上查找
  if (defaultValue != null)
    return treatDefaultAsFactory && typeof defaultValue === 'function' ? defaultValue() : defaultValue;
}

// nextTick: 微任务批合并
const pended = [];
let flushing = false;
function nextTick(fn) {
  const p = flushing ? resolvedPromise : (flushing = true, resolvedPromise = Promise.resolve().then(flushJobs));
  return fn ? p.then(fn) : p;
}
async function flushJobs() {
  flushing = false;
  while (pended.length) pended.shift()();   // patch flush 在此之前已跑(框架内部同队列)
}
const resolvedPromise = Promise.resolve();
```

**评分点**：
- provides 原型链实现注入查找（Object.create(parent.provides)）
- inject 默认值与工厂函数形态
- nextTick 微任务合并与「渲染后执行」时序认知
- currentInstance 的设置时机（setup 期间）
