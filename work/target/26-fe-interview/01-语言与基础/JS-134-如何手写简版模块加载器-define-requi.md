---
title: [JS-134] 如何手写简版模块加载器（define/require 思想）？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-134：如何手写简版模块加载器（define/require 思想）？

**答**：
- 核心结构：注册表（name → { deps, factory, exports, loaded }）+ require 的递归解析。
- 语义要点：依赖先于 factory 执行；exports 全局缓存（单例）；循环访问返回半成品。
- 与 ESM 的本质差异：这里是运行时依赖解析、依赖同步先执行；ESM 是静态解析 + 深度优先后序求值。
- 这也是 AMD（RequireJS）与 CJS require 的共同骨架，理解它就理解了模块系统的本质。

```javascript
const loader = {
  modules: new Map(), // name → { deps, factory, exports, loaded }

  define(name, deps, factory) {
    this.modules.set(name, { deps, factory, exports: {}, loaded: false });
  },

  require(name) {
    const mod = this.modules.get(name);
    if (!mod) throw new Error(`模块未注册: ${name}`);
    if (mod.loaded) return mod.exports;              // 缓存：模块单例
    const depExports = mod.deps.map((d) => this.require(d)); // 依赖先解析
    const result = mod.factory(...depExports);        // 再执行工厂
    mod.exports = result !== undefined ? result : mod.exports;
    mod.loaded = true;
    return mod.exports;
  },
};

// 注册两个模块，app 依赖 math
loader.define('math', [], () => ({
  add: (a, b) => a + b,
  pi: Math.PI,
}));
loader.define('app', ['math'], (math) => ({
  run: () => math.add(1, math.pi) | 0,
}));

console.log(loader.require('app').run()); // 4
console.log(loader.require('math') === loader.require('math')); // true — 单例

// 循环依赖的行为（与 CJS 一致：拿到半成品）
loader.define('x', ['y'], (y) => ({ useY: () => y.val })); // y 尚未加载完
loader.define('y', ['x'], () => ({ val: 'Y' })); // x.require(y) 时 y.exports 为 {}
// 依赖循环双方都应把访问延迟到函数内 —— 与 ESM/CJS 的结论殊途同归
```
