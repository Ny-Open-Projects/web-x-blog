---
title: [WCN-828] 跨框架 signal 适配层的统一 API 怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-828：跨框架 signal 适配层的统一 API 怎么设计？

**答**：
- 结论先行：适配层要「一套内核、多套薄壳」——内核只提供 `signal/computed/effect` 的框架无关语义，壳负责把读取与订阅翻译成各框架 reactivity；API 设计遵循最小公分母，避免暴露框架特有概念。
- 统一原语：`signal(initial, opts?)`、`computed(fn)`、`effect(fn)`、`batch(fn)`、`untrack(fn)`——语义与 TC39/主流库对齐，让业务代码换框架时不用改状态逻辑。
- 桥接 API：`toFrameworkStore(s)`（转成 React/Vue 可消费的 store）与 `fromFrameworkStore(store)`（把框架状态接回 signal）；为 WC 场景提供 `bind(el, signal)` 直连 DOM。
- 设计要点：统一相等性策略（默认 `Object.is`）、统一批处理边界（微任务 flush）、统一错误与清理语义（effect 返回 cleanup）——语义一致才能「跨框架行为一致」。
- 分层隔离：业务只依赖统一 API，底层可替换（今天用 preact-signals-core，明天换原生 Signal），符合依赖倒置。
- 追问钩子：面试官会问「适配层会不会性能差」——答：shell 只是读值+订阅的薄封装，热点路径（高频更新）可以直接拿到底层 signal 做直写 DOM 逃逸通道，适配层不挡路。

```javascript
// 统一适配层内核（框架无关），壳按需桥接
const core = {
  signal: (v) => ({ value: v, subs: new Set(),
    get() { return this.value; },
    set(nv) { if (Object.is(this.value, nv)) return; this.value = nv; this.subs.forEach(f => f()); },
    subscribe(f) { this.subs.add(f); return () => this.subs.delete(f); } }),
  computed(fn) { const s = core.signal(undefined); const read = () => { s.set(fn()); }; read(); return s; },
};
function toReactStore(s) { return { subscribe: cb => s.subscribe(cb), getSnapshot: () => s.get() }; }
function toVueRef(s, vue) { return vue.customRef((track, trigger) => ({
  get() { track(); return s.get(); }, set(v) { s.set(v); trigger(); } })); }

const count = core.signal(1);
const dbl = core.computed(() => count.get() * 2);
count.subscribe(() => console.log('changed:', dbl.get()));
count.set(3); // → changed: 6
// React: useSyncExternalStore(...toReactStore(count))
```
