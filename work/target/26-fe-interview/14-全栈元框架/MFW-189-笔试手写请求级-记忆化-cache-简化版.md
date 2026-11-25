---
title: [MFW-189] 笔试：手写请求级记忆化（React cache() 简化版）
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-189：笔试：手写请求级记忆化（React cache() 简化版）
**答**：实现 `memoizePerRequest(fn)`：① 同一请求内按参数缓存结果，同参调用只执行一次（含并发：第一个 promise 被共享）；② 不同请求之间互不可见（不会把 A 用户的取数给 B）；③ 缓存上限（单请求最多 100 个键，防异常爆炸）；④ 用 AsyncLocalStorage 或等价机制实现请求隔离；⑤ 错误结果也按请求缓存吗？说明并实现你的选择。

```ts
import { AsyncLocalStorage } from 'node:async_hooks';

const storage = new AsyncLocalStorage<Map<string, Promise<unknown>>>();
const MAX_KEYS = 100;

// 每个请求入口先建立缓存域
export function withRequestScope<T>(run: () => T): T {
  return storage.run(new Map(), run); // ②/④ Map 挂在当前请求的异步上下文
}

export function memoizePerRequest<A extends unknown[], R>(
  fn: (...args: A) => R,
): (...args: A) => R {
  return (...args: A) => {
    const cache = storage.getStore();
    if (!cache) return fn(...args); // 不在请求域内：退化为直接调用（不全局缓存）
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key) as R; // ① 命中（含共享进行中的 promise）
    if (cache.size >= MAX_KEYS) return fn(...args); // ③ 超限降级，不缓存
    const p = Promise.resolve(fn(...args));
    cache.set(key, p);
    return p as R;
  };
}

// 用法
const getUser = memoizePerRequest((id: string) => db.users.find(id));
export async function handle() {
  return withRequestScope(async () => {
    await getUser('u1'); // 真实查询
    await getUser('u1'); // 命中，同 promise
  });
}
```

**评分点**：
1. 请求隔离正确：缓存表挂在 AsyncLocalStorage 的 store 上，请求结束随上下文销毁——绝不能用模块级 Map（跨用户串数据是重大扣分项）。
2. 缓存值是 promise 而非结果值：并发同参调用共享同一次进行中的查询，避免「同时到达的两次请求都查询」。
3. 非请求上下文的降级行为明确（直接执行，不退化为全局缓存）。
4. 错误处理有明确选择并能说理：React cache() 的实现中失败 promise 也被缓存于当次渲染（防止错误循环重试），但我们的版本可选不缓存错误以便重试——关键是要说出取舍。
5. 键生成用参数序列化，能指出 JSON.stringify 对对象键序敏感，生产可用稳定序列化。
