---
title: [JS-114] WeakRef 与 FinalizationRegistry 的用途与边界？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-114：WeakRef 与 FinalizationRegistry 的用途与边界？

**答**：
- WeakRef 持有对象的弱引用，`deref()` 在对象存活时返回它、被回收后返回 undefined。
- FinalizationRegistry 在对象被 GC 后回调注册的清理函数，可携带一个 heldValue 标识。
- 硬边界：GC 时机不确定且回调自身不保证及时运行，绝不能用于业务正确性逻辑。
- 缓存场景优先 WeakMap/WeakSet；WeakRef 只适合"大对象缓存失效后自动释放"这类优化。

```javascript
let target = { data: new Array(1e6).fill('x') };

const ref = new WeakRef(target);
const registry = new FinalizationRegistry((held) => {
  console.log('对象已回收，清理登记项：', held); // 时机不保证，仅做资源提示
});
registry.register(target, 'big-cache-entry');

console.log(ref.deref()?.data.length); // 1000000 — 还活着

// 解除强引用后，GC 随时可能回收
target = null;
setTimeout(() => {
  console.log('回收后 deref：', ref.deref()); // 可能是 undefined，也可能还没被回收
}, 100);

// 边界总结：
// 1. 不能用 deref 结果判断"是否已回收"——deref 本身会短暂复活引用
// 2. FinalizationRegistry 回调运行在 JS 里，清理逻辑本身也可能被 GC 拖延
// 3. WeakMap 不能遍历、WeakRef 不能可靠探测，都是"给 GC 的提示"而非控制手段
// 4. 正确姿势：缓存挂 WeakMap，注册表只用于关闭文件句柄等资源提示
```

## 十七、浏览器交互与存储
