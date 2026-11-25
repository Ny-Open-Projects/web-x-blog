---
title: [FRP-122] 集合类型 Map/Set 的代理处理为什么要单独实现一套 instrument 方法？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-122：集合类型 Map/Set 的代理处理为什么要单独实现一套 instrument 方法？

**答**：
- Proxy 只能拦截对象上的属性操作，而 `map.get(k)` 中 `get` 是**原型方法**，方法内的 `this` 指向原始对象——如果直接返回原始方法，响应式就被绕过了。
- 所以 Vue 对 Map/Set 的 `get/set/has/delete` 提供 instrument 版本：代理的 get trap 里，若读到的是这些方法名，就返回一个 `this` 绑定为**代理**的包装函数，并在其中做 track/trigger。
- `size` 与 `forEach`、迭代方法 track **ITERATE_KEY**；`get/has` track 对应 key；`set/delete` 在新增/删除时分别 trigger ADD/DELETE。
- 迭代出来的值要再包一层 `toReactive`，保证 `for (const [k, v] of map)` 拿到的是响应式对象。

```javascript
// 简化实现，帮助理解 Map 的代理 instrument
const rawMap = new Map();
const ITERATE_KEY = Symbol('iterate');
const deps = new Map(); // key -> Set<fn>
let active = null;

function reactiveMap(target) {
  const proxy = new Proxy(target, {
    get(target, key, receiver) {
      if (key === 'size') {
        track(ITERATE_KEY); // size 依赖整体结构
        return Reflect.get(target, key, target);
      }
      // 返回绑定代理的方法版本：让 map.get 内部 this 是 proxy
      return function (...args) {
        switch (key) {
          case 'get':
            track(args[0]);                       // 依赖该 key 的值
            const v = target.get(args[0]);
            return v;                             // 深层对象时此处应 toReactive(v)
          case 'has':
            track(args[0]); return target.has(args[0]);
          case 'set':
            const had = target.has(args[0]);
            target.set(args[0], args[1]);
            trigger(args[0], had ? 'set' : 'add');
            if (!had) trigger(ITERATE_KEY, 'add');
            return proxy; // 保持链式：m.set(a,1).set(b,2)
          case 'delete':
            const had2 = target.has(args[0]);
            target.delete(args[0]);
            if (had2) { trigger(args[0], 'delete'); trigger(ITERATE_KEY, 'delete'); }
            return had2;
          case 'forEach': {
            track(ITERATE_KEY);
            return (cb) => target.forEach((val, k) => cb(val, k, proxy));
          }
          default:
            return Reflect.get(target, key, receiver);
        }
      };
    }
  });
  return proxy;
}

function track(key) { if (active) (deps.get(key) ?? deps.set(key, new Set()).get(key)).add(active); }
function trigger(key) { (deps.get(key) || []).forEach(f => f()); }

// 验证
const m = reactiveMap(rawMap);
active = () => console.log('alice =', m.get('alice'));
track('alice');
m.set('alice', 100); // alice = 100（get 依赖被触发）
m.set('bob', 1);     // 不触发（只依赖 alice）
```
