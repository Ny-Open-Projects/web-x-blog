---
title: [DP-032] 用 Proxy 实现缓存代理和虚拟代理？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-032：用 Proxy 实现缓存代理和虚拟代理？
**答**：
- Proxy 元编程能力让代理模式实现更通用：`get/set/apply` 等陷阱天然是"控制访问"的切面。
- 缓存代理：拦截重复计算/重复请求，命中缓存直接返回——`get` 陷阱记录结果。
- 虚拟代理：把"昂贵操作"推迟到真正需要时（如懒初始化重资源对象、函数的惰性执行）。
- 与 DP-031 区别：传统代理需手写包装类，Proxy 可以代理任意对象而无需改其类。

```javascript
// 缓存代理1：纯函数结果缓存
function memoize(fn) {
  const cache = new Map();
  return new Proxy(fn, {
    apply(target, thisArg, args) { // 拦截函数调用
      const key = JSON.stringify(args);
      if (!cache.has(key)) {
        console.log('真实计算', key);
        cache.set(key, target.apply(thisArg, args));
      }
      return cache.get(key);
    },
  });
}
const slowSquare = memoize((n) => { for (let i = 0; i < 1e6; i++); return n * n; });
console.log(slowSquare(9), slowSquare(9)); // 真实计算 [9] 81 81 —— 第二次命中缓存

// 缓存代理2：请求结果缓存（带过期时间）
function cachedFetch(ttl = 5000) {
  const cache = new Map();
  return new Proxy(fetch, {
    apply(target, thisArg, [url, init]) {
      const hit = cache.get(url);
      if (hit && Date.now() - hit.t < ttl) { console.log('缓存命中', url); return hit.v; }
      const p = target(url, init);
      cache.set(url, { v: p, t: Date.now() });
      return p;
    },
  });
}
// const f = cachedFetch(); f('/api/a'); f('/api/a'); —— 第二次直接命中

// 虚拟代理：重对象懒初始化
class HeavyChart {
  constructor() { console.log('初始化重型图表引擎'); } // 昂贵
  draw(data) { console.log('draw', data); }
}
function lazyProxy(Factory) {
  let inst = null;
  return new Proxy({}, {
    get(_, prop) {
      if (!inst) inst = new Factory(); // 第一次真正访问时才创建
      return Reflect.get(inst, prop);
    },
  });
}
const chart = lazyProxy(HeavyChart);   // 此刻不初始化
// ...页面其他逻辑...
chart.draw([1, 2]);                    // 输出：初始化重型图表引擎 -> draw [1, 2]
```
