---
title: [NODE-207] AbortSignal.any 与组合取消实战？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-207：AbortSignal.any 与组合取消实战？
**答**：
- AbortSignal.any([sig1, sig2])：任一源 abort 即生效——把"超时取消 + 上游取消 + 限流取消"组合成一个 signal 传给下游（BFF 聚合必备）。
- AbortSignal.timeout(ms)：构造即计时，适合单调用超时。
- 组合取消的服务端意义：BFF 聚合三个下游接口，一个失败/超时 → 其余在途请求一并取消，释放连接池（NODE-052 容错的细节层）。
- 配套：signal.addEventListener('abort') 做清理（关闭子流/记日志），AbortSignal 由 GC 安全回收。

```javascript
import { request } from 'node:https';

async function fetchDownstream(url, { timeout, parent, rateLimit } = {}) {
  const signal = AbortSignal.any([
    AbortSignal.timeout(timeout ?? 3000),       // 1) 调用级超时
    parent ?? AbortSignal.timeout(10_000),      // 2) 请求级上游取消
  ]);
  const res = await fetch(url, { signal });
  return res;
}
// BFF 聚合：请求级 signal 打穿所有下游
app.post('/aggregate', async (req, res) => {
  const parent = AbortSignal.timeout(5000);     // 整个聚合的预算
  const [user, orders, stock] = await Promise.allSettled([
    fetchDownstream('/user', { parent, timeout: 2000 }),
    fetchDownstream('/orders', { parent }),
    fetchDownstream('/stock', { parent }),
  ]);   // 任一超时 → parent abort → 其余请求同时取消，不占连接
});
```
