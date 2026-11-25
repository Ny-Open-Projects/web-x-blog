---
title: [DP-138] 如何用适配器统一 REST / GraphQL / WebSocket 三种数据源？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-138：如何用适配器统一 REST / GraphQL / WebSocket 三种数据源？（高频）
**答**：
- 定义统一 DataSource 接口：`query(schema, params)` 读、`subscribe(topic, cb)` 订阅、`mutate(cmd, body)` 写；三端各写一个适配器实现（DP-026）。
- 选源策略层：按数据特性路由——实时性数据走 WS、列表详情走 REST、聚合页走 GraphQL；上层业务无感（外观 + 策略）。
- 注意语义差异收敛：REST 分页 ↔ GraphQL connection、WS 推送 ↔ 请求响应，都在适配器内抹平成统一返回形状。

```javascript
// 统一接口 + 三种适配器
class RestSource {
  async query(path, params) { return http.get(path, params); }                     // 分页在适配器内抹平
  async subscribe(topic, cb) { const t = setInterval(() => http.get(topic).then(cb), 5000); return () => clearInterval(t); } // 轮询模拟
}
class GraphqlSource {
  async query(query, variables) {
    const { data } = await http.post('/graphql', { query, variables });
    return data;
  }
  async subscribe() { throw new Error('gql 订阅请走 ws 适配器'); }                  // 能力差异显式暴露
}
class WsSource {
  #handlers = new Map();
  constructor(url) { this.ws = new WebSocket(url); this.ws.onmessage = (e) => this.#handlers.get(JSON.parse(e.data).topic)?.(JSON.parse(e.data).payload); }
  async query(topic, params) { /* 请求-响应语义封装 */ return rpc(this.ws, topic, params); }
  async subscribe(topic, cb) { this.#handlers.set(topic, cb); return () => this.#handlers.delete(topic); }  // 推送 → 统一订阅
}
// 数据网关：策略路由 + 统一出口（外观）
class DataGateway {
  #routes;
  constructor(routes) { this.#routes = routes; }              // { realtime: ws, list: rest, aggregate: gql }
  of(kind) { return this.#routes[kind]; }
}
const gateway = new DataGateway({ realtime: new WsSource('wss://x'), list: new RestSource(), aggregate: new GraphqlSource() });
const off = await gateway.of('realtime').subscribe('stock/AAPL', renderTick);  // 业务不认识 WebSocket
const page = await gateway.of('list').query('/orders', { page: 1 });           // 业务不认识 fetch
```

---

## 十七、UI 架构模式
