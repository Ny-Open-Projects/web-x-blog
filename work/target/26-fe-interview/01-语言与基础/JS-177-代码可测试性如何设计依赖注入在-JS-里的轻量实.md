---
title: [JS-177] 代码可测试性如何设计？依赖注入在 JS 里的轻量实现？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-177：代码可测试性如何设计？依赖注入在 JS 里的轻量实现？

**答**：
- 可测试性核心 = 依赖可替换：业务代码不 hardcode `fetch/Date.now/localStorage`，而是从外部注入。
- 最小 DI 容器：register 存工厂函数，resolve 时执行工厂并传入容器自身，支持嵌套解析。
- 测试时 resolve 传 overrides 注入 mock：时钟固定、API 返回固定值，不发真实请求。
- 轻量替代方案：模块默认导出真实实现 + 导出 setter，或函数参数注入（纯函数最易测）。
- 判断标准：不启动浏览器、不 mock 网络库全局、100ms 内跑完的逻辑，才算可测。

```javascript
// 1. 轻量 DI 容器
function createContainer() {
  const registry = new Map();
  return {
    register(name, factory) { registry.set(name, factory); return this; },
    resolve(name, overrides = {}) {            // overrides 供测试注入 mock
      if (name in overrides) return overrides[name];
      if (!registry.has(name)) throw new Error(`未注册依赖：${name}`);
      return registry.get(name)(this);         // 工厂收到容器，支持嵌套解析
    },
  };
}

// 2. 业务代码：依赖全部来自容器
const c = createContainer()
  .register('clock', () => ({ now: () => Date.now() }))
  .register('api', () => ({
    async getPrice(id) { return (await fetch(`/api/p/${id}`)).json(); },
  }))
  .register('pricer', (d) => {
    const clock = d.resolve('clock');
    const api  = d.resolve('api');
    return {
      async quote(id) {
        const { price } = await api.getPrice(id);
        return { id, price, at: clock.now() };
      },
    };
  });

// 3. 生产：真实依赖
// const pricer = c.resolve('pricer');

// 4. 测试：注入 mock，不发请求、时间固定
const mock = c.resolve('pricer', {
  clock: { now: () => 0 },
  api: { getPrice: async () => ({ price: 9.9 }) },
});
mock.quote(1).then((r) => console.log(r));   // { id: 1, price: 9.9, at: 0 }
```

## 二十六、内存与性能
