---
title: [TST-406] 笔试：实现一个模块依赖注入容器（测试/生产双绑定）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-406：笔试：实现一个模块依赖注入容器（测试/生产双绑定）。
**答**：`createContainer({ overrides })`：注册服务工厂，`get(name)` 返回实例；overrides 里的名字直接用测试替身；循环依赖检测报错。

```javascript
export function createContainer(defs = {}, overrides = {}) {
  const cache = new Map(); const resolving = [];
  return {
    get(name) {
      if (name in overrides) return overrides[name];
      if (cache.has(name)) return cache.get(name);
      if (!(name in defs)) throw new Error(`未注册服务: ${name}`);
      if (resolving.includes(name)) throw new Error(`循环依赖: ${[...resolving, name].join('→')}`);
      resolving.push(name);
      const inst = defs[name](this);
      resolving.pop();
      cache.set(name, inst);
      return inst;
    },
  };
}
const c = createContainer({ db: () => ({ q: () => 1 }), svc: (c) => ({ v: c.get('db').q() }) },
  { db: { q: () => 42 } });
console.log(c.get('svc').v); // 42（测试替身生效）

```

**评分点**：
- 注册惰性实例化（get 时创建，单例缓存）。
- overrides 优先级最高且不实例化原工厂。
- 循环依赖：实例化栈检测，发现回边报错。
- 未注册服务明确报错（含名字）。
