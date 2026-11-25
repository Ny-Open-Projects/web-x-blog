---
title: [FRP-127] shallow 系列（shallowRef/shallowReactive/shallowReadonly）适用场景的原理层原因是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-127：shallow 系列（shallowRef/shallowReactive/shallowReadonly）适用场景的原理层原因是什么？

**答**：
- 原理层只有一条分支差异：深层版本在 get trap 里对值为对象的结果递归 `toReactive`，shallow 版本**直接返回原始对象**——省掉为每个嵌套对象建 Proxy 的内存与读取开销。
- `shallowRef` 只在 `.value` **整体替换**时 trigger，不代理 value 内部：适合大列表、地图实例、Canvas 上下文等"整体换、内部不直接改"的对象；内部确实变了就手动 `triggerRef(ref)`。
- `shallowReactive` 只有第一层响应式：适合"配置对象"——总是整层替换、从不单独改深层字段的场景；深层修改不触发更新（这是特性不是 bug）。
- `shallowReadonly` 只锁第一层写：典型用途是保护 props 根对象不被整体覆盖，同时不影响深层对象传给第三方库。
- 反过来说：需要"深层字段随意改也能更新"就必须深层响应式，两者是性能与能力的选择。

```javascript
// 简化实现，帮助理解 shallow 与深层的分支差异
const targetMap = new Map();   // key -> Set<effect>
let activeEffect = null;

function track(key) {
  if (!activeEffect) return;
  let dep = targetMap.get(key);
  if (!dep) targetMap.set(key, dep = new Set());
  dep.add(activeEffect);
}
function trigger(key) { (targetMap.get(key) || []).forEach(f => f()); }

function reactive(obj, shallow = false) {
  return new Proxy(obj, {
    get(target, key) {
      track(key);
      const v = Reflect.get(target, key);
      // 全部差异就在这一行：shallow 时不递归建代理
      if (!shallow && typeof v === 'object' && v !== null) {
        return reactive(v);                       // 深层：嵌套对象也被代理
      }
      return v;                                   // shallow：返回原始对象
    },
    set(target, key, nv) {
      const old = Reflect.get(target, key);
      const r = Reflect.set(target, key, nv);
      if (old !== nv) trigger(key);
      return r;
    }
  });
}

// shallowRef：只有 value 整体替换才 trigger，value 内部不代理
function shallowRef(v) {
  const subs = new Set();
  return {
    get value() { if (activeEffect) subs.add(activeEffect); return v; },
    set value(nv) { if (nv !== v) { v = nv; subs.forEach(f => f()); } }
  };
}
// triggerRef：内部变更后手动强制触发（ref 内部没有代理，框架感知不到）
function triggerRef(r) { r.value = r.value; } // 触发 set（值未变时源码会强制派发，这里用同值写入示意）

// 场景对比
const bigList = { items: new Array(1000).fill(0) }; // 模拟大数据
const data = shallowRef(bigList);

let runs = 0;
activeEffect = () => { runs++; console.log('render, items.length =', data.value.items.length); };
data.value; activeEffect = null;   // 首次执行，收集 .value 依赖

data.value = { items: [1, 2, 3] }; // 整体替换 —— 触发，runs = 2
data.value.items.push(4);          // 内部变更 —— 不触发！shallowRef 的代价
triggerRef(data);                  // 手动补救：runs = 3

// shallowReactive：只有第一层响应式
const cfg = reactive({ api: '/v1', meta: { debug: true } }, true /* shallow */);
activeEffect = () => console.log('cfg.api =', cfg.api);
cfg.api; activeEffect = null;
cfg.api = '/v2';        // 触发
cfg.meta.debug = false; // 不触发 —— 深层无代理
```

## 十九、Vue 组件模型深水区
