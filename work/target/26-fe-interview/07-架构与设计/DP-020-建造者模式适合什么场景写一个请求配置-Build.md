---
title: [DP-020] 建造者模式适合什么场景？写一个请求配置 Builder？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-020：建造者模式适合什么场景？写一个请求配置 Builder？
**答**：
- 建造者：把"复杂对象的分步构建"与"最终装配"分离，避免巨型构造函数/巨型配置对象。
- 前端场景：复杂请求配置（超时/重试/鉴权/埋点）、Canvas 绘图配置、复杂查询条件。
- 与 options 模式区别：options 适合"一次性传一堆可选字段"；builder 适合"步骤有依赖、需要校验/默认派生"的构建过程。
- 收益：构建过程可读、可复用（build 半成品再继续配置）、可在 build 时统一校验。

```javascript
// 请求配置 Builder：分步构建，build 时统一装配与校验
class RequestBuilder {
  #config = { method: 'GET', headers: {}, timeout: 10000, retry: 0 };

  url(u) { this.#config.url = u; return this; }       // 每步返回 this 实现链式
  method(m) { this.#config.method = m.toUpperCase(); return this; }
  header(k, v) { this.#config.headers[k] = v; return this; }
  token(t) { this.header('Authorization', `Bearer ${t}`); return this; } // 派生方法复用步骤
  timeout(ms) { this.#config.timeout = ms; return this; }
  retry(n) { this.#config.retry = n; return this; }

  build() { // 装配 + 校验集中在一处
    const c = this.#config;
    if (!c.url) throw new Error('url 必填');
    if (c.retry > 0 && c.method !== 'GET') throw new Error('非 GET 请求不允许重试');
    return { ...c }; // 返回冻结副本，防止构建后篡改
  }
}
// 使用：意图一目了然
const config = new RequestBuilder()
  .url('/api/orders')
  .method('post')
  .token('jwt-abc')
  .timeout(5000)
  .build();
console.log(config.method, config.headers.Authorization); // POST Bearer jwt-abc
```
