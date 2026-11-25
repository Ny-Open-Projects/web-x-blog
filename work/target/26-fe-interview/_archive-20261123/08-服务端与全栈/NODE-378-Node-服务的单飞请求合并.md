---
title: [NODE-378] Node 服务的 singleflight 请求合并（防缓存击穿）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-378：singleflight 请求合并
**答**:
- 场景：热 key 缓存过期瞬间，N 个并发请求同时回源 DB（缓存击穿）。singleflight：同 key 并发请求合并为一次回源，其余等待共享结果。
- 实现：Map<key, Promise>——第一个请求创建 Promise 回源，后续请求 await 同一个 Promise；完成后删除 entry（注意失败也要删除，防毒缓存）。
- 扩展语义：fresh-window（结果新鲜期内直接共享，过期后第一个请求触发刷新、其余拿旧值 stale-while-revalidate 语义）；单飞范围是进程内，多实例间加分布式锁或接受多实例各回源一次。
- 边界：等待共享结果也要有超时（回源挂了别一起挂死——失败传播让等待者走各自降级）；value 大对象共享同一引用（调用方不得原地修改，或冻结）。
- 应用位：进程内缓存回源（NODE-353）、DB 查询合并、下游调用合并；指标：合并率（等待者数/回源数）。
```javascript
class Singleflight {
  #inflight = new Map();
  run(key, fn) {
    if (this.#inflight.has(key)) return this.#inflight.get(key); // 共享同一次回源
    const p = Promise.resolve().then(fn).finally(() => this.#inflight.delete(key));
    this.#inflight.set(key, p);
    return p;
  }
}
const sf = new Singleflight();
const goods = await sf.run(`goods:${id}`, () => db.loadGoods(id)); // 并发 id 相同只查一次
```
