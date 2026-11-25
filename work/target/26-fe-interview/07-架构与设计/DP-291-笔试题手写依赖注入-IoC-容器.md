---
title: [DP-291] 笔试题：手写依赖注入（IoC 容器 + 单例作用域）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-291：笔试题：手写依赖注入（IoC 容器 + 单例作用域）？
**答**：实现 IoC 容器：1) register(name, factory, { deps, singleton })；2) resolve 递归注入依赖；3) singleton 单例缓存 vs transient 每次新建；4) 循环依赖报错。
**评分点**：
- 递归 resolve 正确（依赖闭包求值）。
- 单例缓存键正确（容器级，非全局）。
- 循环依赖用解析栈检测。
- 工厂拿到的是解析后的依赖实例。
```javascript
class Container {
  #defs = new Map();
  #instances = new Map();       // 3) 单例缓存
  register(name, factory, { deps = [], singleton = true } = {}) {
    this.#defs.set(name, { factory, deps, singleton });
    return this;
  }
  resolve(name, stack = new Set()) {                        // 4) 循环检测
    if (stack.has(name)) throw new Error(`循环依赖: ${[...stack, name].join(' → ')}`);
    if (this.#instances.has(name)) return this.#instances.get(name);
    const def = this.#defs.get(name);
    if (!def) throw new Error(`未注册: ${name}`);
    stack.add(name);
    const deps = def.deps.map(d => this.resolve(d, stack));  // 2) 递归注入
    stack.delete(name);
    const instance = def.factory(...deps);
    if (def.singleton) this.#instances.set(name, instance);
    return instance;
  }
}
// 用：
const c = new Container();
c.register('http', (auth) => createHttp(auth), { deps: ['auth'] });
c.register('auth', () => createAuth());
c.register('api', (http, log) => createApi(http, log), { deps: ['http', 'log'] });
c.register('log', () => new Logger(), { singleton: false });  // transient：每次新建
```
