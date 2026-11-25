---
title: [DP-094] HTTP 请求库的拦截器模式链路综合题：设计"重试+限流+缓存+取消"？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-094：HTTP 请求库的拦截器模式链路综合题：设计"重试+限流+缓存+取消"？
**答**：
- 综合运用：职责链（拦截器编排各切面）、策略（重试策略/退避算法）、享元（缓存池）、状态机（请求生命周期 idle→running→done/canceled）。
- 链路设计：请求拦截器做"缓存命中短路 + 限流令牌"，dispatchRequest 外围做"取消信号注入"，响应拦截器做"重试判定 + 错误归一化"。
- 关键权衡：缓存与重试可能冲突（重试要绕过缓存）；取消要用 AbortController 透传到最底层。

```javascript
// 请求引擎：拦截器职责链 + 各切面独立可插拔
function createHttpClient(config = {}) {
  const cachePool = new Map();                       // 享元：缓存池（key -> {t, promise}）
  const inflight = new Map();                        // 并发去重：同一 key 共享同一 Promise
  const tokens = [];                                 // 简单限流：时间窗令牌

  async function send(config, attempt = 0) {         // 状态机：attempt 表示重试轮次
    const key = `${config.method}:${config.url}:${JSON.stringify(config.params || {})}`;
    // 切面1：缓存（只缓存 GET，且首次成功后 5s 内有效）
    if (config.method === 'GET' && config.cache !== false) {
      const hit = cachePool.get(key);
      if (hit && Date.now() - hit.t < 5000) return hit.p;
    }
    // 切面2：并发去重（in-flight 共享）
    if (inflight.has(key)) return inflight.get(key);
    // 切面3：限流（滑动窗口 100ms 内最多 5 个）
    const now = Date.now();
    tokens.filter((t) => now - t < 100);
    tokens.length = tokens.filter((t) => now - t < 100).length; // 清理过期
    if (tokens.length >= 5) throw new Error('请求过于频繁');
    tokens.push(now);

    const p = (async () => {
      try {
        const res = await fetch(config.url, {
          method: config.method,
          signal: config.signal,                     // 取消：透传至底层
          body: config.data ? JSON.stringify(config.data) : undefined,
        });
        if (res.status >= 500 && attempt < (config.retries ?? 2)) {
          // 策略：指数退避重试（只重试幂等请求）
          const backoff = 2 ** attempt * 300;
          await new Promise((r) => setTimeout(r, backoff));
          return send({ ...config, cache: false }, attempt + 1); // 重试绕过缓存
        }
        if (!res.ok) throw Object.assign(new Error(`HTTP ${res.status}`), { status: res.status });
        const data = await res.json();
        return { data, status: res.status };
      } finally {
        inflight.delete(key);                        // 结束后释放并发位
      }
    })();
    inflight.set(key, p);
    if (config.method === 'GET' && config.cache !== false) {
      p.then((r) => cachePool.set(key, { t: Date.now(), p: r })).catch(() => {}); // 成功才入缓存
    }
    return p;
  }
  return { send };
}
const client = createHttpClient();
const ac = new AbortController();
setTimeout(() => ac.abort(), 500);                   // 500ms 后取消
client.send({ method: 'GET', url: '/api/list', signal: ac.signal, cache: true })
  .then((r) => console.log(r.data))
  .catch((e) => console.log('终态', e.message));
// 链路总结：缓存短路(享元) -> 并发去重 -> 限流(策略) -> 状态机重试(指数退避) -> 取消透传
```
