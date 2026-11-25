---
title: [WCN-749] 浏览器原生 Signals（TC39）落地后，现有框架的信号库如何平滑对齐？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-749：浏览器原生 Signals（TC39）落地后，现有框架的信号库如何平滑对齐？

**答**：
- 结论：把自研 signal 封装成兼容原生 `Signal.State/Computed` 接口的适配层，优先用原生实现，检测不到时回退 polyfill；业务代码只依赖统一 API。
- 迁移分期：先对齐 API 形状 → 再替换底层实现 → 最后利用原生能力（如开发者工具集成）；用特性检测 `typeof Signal !== 'undefined'`。
- 追问钩子：原生 Signal 与框架信号的语义差异（惰性 vs 即时、effect 归属）怎么抹平？考察适配层设计功力。

```javascript
const NativeSignal = globalThis.Signal;
function createState(initial) {
  if (NativeSignal?.State) return new NativeSignal.State(initial); // 优先原生
  return { get value(){return this._v;}, set value(v){this._v=v;}, _v:initial }; // polyfill
}
function createComputed(fn) {
  if (NativeSignal?.computed) return new NativeSignal.computed(fn);
  return { get value(){return fn();} };
}
const s = createState(1);
console.log('使用实现:', NativeSignal ? 'native' : 'polyfill', s.value);
```
