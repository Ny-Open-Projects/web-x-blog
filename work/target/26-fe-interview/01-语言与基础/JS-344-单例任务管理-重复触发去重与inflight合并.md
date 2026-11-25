---
title: [JS-344] 单例任务管理：in-flight 合并与结果缓存
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-344：单例任务管理：in-flight 合并与结果缓存

**答**：
- in-flight 合并：相同 key 的并发调用共享同一 Promise（去重请求）——实现：Map<key, Promise>，完成后删除；「第一个发起、大家共享结果、各自拿到自己的 resolve」
- 结果缓存分层：in-flight（进行中共享）+ 短 TTL 缓存 + SWR（先回旧值再刷新）——React Query/swr 的最小核心就是这个三元组
- 错误处理细节：共享 Promise reject 时所有等待方一起失败——要决定「失败是否也共享」（短暂负缓存防重试风暴）还是「失败即清理可重试」
- key 设计：参数序列化稳定（排序后 stringify），含业务维度（用户 ID）防串数据
- 场景落地：并发列表渲染请求同一详情接口、全局配置拉取、登录态获取——一处实现处处受益

```javascript
const inflight = new Map();
const cache = new Map();

async function once(key, fn, ttl = 5000) {
  const cached = cache.get(key);
  if (cached && Date.now() - cached.t < ttl) return cached.v;
  if (inflight.has(key)) return inflight.get(key);   // 合并并发
  const p = fn().then(
    (v) => { cache.set(key, { v, t: Date.now() }); return v; },
    (e) => { throw e; },                              // 失败不缓存(可重试)
  ).finally(() => inflight.delete(key));
  inflight.set(key, p);
  return p;
}
// 并发调用合并: once('user:1', loadUser) × N 次 → 1 个请求
```

**追问**：

1. 合并后的请求被其中一个调用方取消，其他等待者会怎样？ → 共享同一个 Promise，直接 reject 会连累所有人；正确做法是每个调用方持有独立 `AbortSignal` 并引用计数，最后一个退出时才真正 abort 底层请求。
2. key 直接用 `JSON.stringify(params)` 有什么坑？ → 对象属性顺序不同会生成不同 key 导致去重失效；`undefined`、函数会被丢弃，大对象还会让 Map 长期持有引用。应先按键名排序再序列化。
3. 失败也缓存（负缓存）会带来什么副作用？ → 故障期间用户主动重试仍拿到旧错误，服务恢复后还要等 TTL 过期；负缓存 TTL 要用秒级，并提供手动清除入口。
