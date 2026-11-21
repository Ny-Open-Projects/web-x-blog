---
title: [MFW-186] 笔试：手写幂等 Server Action（requestId 去重 + 过期清理）
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-186：笔试：手写幂等 Server Action（requestId 去重 + 过期清理）
**题目**：实现一个幂等包装器 `withIdempotency(action)`：① 客户端每次提交生成唯一 requestId，服务端按 requestId 去重——同键并发请求只执行一次，其余等待并返回相同结果；② 执行中的请求要互斥（防止并发双写）；③ 结果缓存 5 分钟后过期（过期键可重新执行）；④ 请求失败（throw）不缓存结果，允许重试；⑤ 提供测试用例说明并发双击只产生一次写入。

```ts
type Pending = { promise: Promise<unknown> };
const results = new Map<string, { at: number; value: unknown }>();
const pending = new Map<string, Pending>();
const TTL = 5 * 60 * 1000;

export function withIdempotency<A extends unknown[]>(
  action: (...args: A) => Promise<unknown>,
) {
  return async (requestId: string, ...args: A) => {
    const hit = results.get(requestId);
    if (hit && Date.now() - hit.at < TTL) return hit.value; // ① 命中直接返回

    const inflight = pending.get(requestId);
    if (inflight) return inflight.promise; // ② 并发请求共享同一次执行

    const promise = (async () => {
      try {
        const value = await action(...args);
        results.set(requestId, { at: Date.now(), value }); // ④ 只缓存成功结果
        return value;
      } finally {
        pending.delete(requestId); // 失败/成功都要释放，失败者可重试
      }
    })();
    pending.set(requestId, { promise });
    return promise;
  };
}

// 定期清理过期键（真实场景交给定时任务）
export function sweep() {
  for (const [k, v] of results) if (Date.now() - v.at > TTL) results.delete(k);
}
```

**评分点**：
1. 并发互斥用 in-flight 表（pending Map + 共享 promise），而不是「查了再写」——先查后写存在竞态窗口，是常见扣分点。
2. 只缓存成功结果：失败请求必须放行重试，且 finally 里释放 pending 防死锁。
3. TTL 过期语义正确：过期后允许重新执行（幂等键有生命周期，不是永久去重）。
4. 至少提一句生产化方向：Map 换单机可用，多实例要落到 Redis SET NX + TTL。
5. 能指出 Action 自动重试与用户双击都会产生同 requestId 场景，说明为什么幂等键由客户端生成。
