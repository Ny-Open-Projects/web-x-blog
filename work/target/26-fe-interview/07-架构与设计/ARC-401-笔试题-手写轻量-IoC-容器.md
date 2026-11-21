---
title: [ARC-401] 笔试题：手写轻量 IoC 容器（注册/依赖解析/单例）
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-401：笔试题：手写轻量 IoC 容器
**题目**：实现 Container：1) register(name, factory) 注册工厂函数；2) resolve(name) 支持依赖注入（factory 参数声明依赖名）；3) 默认单例缓存；4) 循环依赖检测报错。
**评分点**：
- 依赖解析用参数名（或显式 deps）递归 resolve。
- 单例缓存正确（首次 resolve 后复用实例）。
- 循环依赖用 resolving 中集合检测，报错信息含环路径。
- resolve 未知依赖报错清晰。
```javascript
class Container {
  #defs = new Map(); #singletons = new Map(); #resolving = [];
  register(name, factory, { singleton = true } = {}) { this.#defs.set(name, { factory, singleton }); return this; }
  resolve(name) {
    if (this.#singletons.has(name)) return this.#singletons.get(name);
    const def = this.#defs.get(name);
    if (!def) throw new Error(`未知依赖: ${name} (注册: ${[...this.#defs.keys()]})`);
    if (this.#resolving.includes(name))
      throw new Error(`循环依赖: ${[...this.#resolving, name].join(' -> ')}`);
    this.#resolving.push(name);
    const instance = def.factory((dep) => this.resolve(dep));   // 注入 resolver
    this.#resolving.pop();
    if (def.singleton) this.#singletons.set(name, instance);
    return instance;
  }
}
const c = new Container();
c.register('config', () => ({ apiUrl: '/api' }));
c.register('http', (get) => ({ base: get('config').apiUrl }));
c.register('api', (get) => new GoodsApi(get('http')));
console.log(c.resolve('api') === c.resolve('api')); // true 单例
```
