---
title: [NODE-054] SSR 服务的性能如何保障（渲染缓存、限流、进程模型）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-054：SSR 服务的性能如何保障（渲染缓存、限流、进程模型）？
**答**：
- **渲染缓存**：按 URL+用户态分桶缓存渲染结果（匿名页可 CDN/Redis 缓存整页 HTML，`s-maxage` + `stale-while-revalidate`）；组件级用 React `cache()`/Memo 去重数据请求。
- **限流**：SSR 渲染是 CPU 密集 + 下游数据依赖，入口必须限流（每 IP/每路由 QPS 上限），过载直接降级为 CSR（返回壳 + 骨架屏），比排队雪崩好。
- **进程模型**：cluster 多进程榨干多核；渲染超时（如 3s）后中断返回壳；监控 `event loop lag`，超阈值告警。
- 经验值：单核 React SSR 渲染吞吐约几十到几百 RPS，取决于组件树大小——缓存命中率是关键。

```javascript
const { renderToPipeableStream } = require('react-dom/server');
const Redis = require('ioredis');
const redis = new Redis();

// 1. 整页渲染缓存（匿名用户）
async function renderPage(url) {
  const key = `ssr:page:${url}`;
  const cached = await redis.get(key);
  if (cached) return { html: cached, hit: true };
  const html = await new Promise((resolve, reject) => {
    const stream = renderToPipeableStream(<App url={url} />, {
      onAllReady() {                          // 缓存场景等全部就绪
        let buf = '';
        stream.pipe(new require('stream').Writable({
          write(c, _e, cb) { buf += c; cb(); },
          final(cb) { resolve(buf); cb(); },
        }));
      },
      onError: reject,
    });
  });
  await redis.setex(key, 60, html);           // 60s 缓存，配 stale-while-revalidate 更佳
  return { html, hit: false };
}

// 2. 令牌桶限流 + 过载降级 CSR
const buckets = new Map();
function rateLimit(ip, capacity = 20, refillPerSec = 5) {
  const now = Date.now() / 1000;
  const b = buckets.get(ip) ?? { tokens: capacity, last: now };
  b.tokens = Math.min(capacity, b.tokens + (now - b.last) * refillPerSec);
  b.last = now;
  if (b.tokens < 1) { buckets.set(ip, b); return false; }
  b.tokens -= 1; buckets.set(ip, b);
  return true;
}

app.get('*', async (req, res) => {
  if (!rateLimit(req.ip)) {
    // 过载：降级为 CSR 壳，不让渲染队列堆积
    return res.status(503).sendFile('shell.html', { root: 'public' });
  }
  const isAnonymous = !req.cookies.sid;
  if (isAnonymous) {
    const { html } = await renderPage(req.url);  // 命中缓存直接返回
    return res.type('html').send(html);
  }
  // 登录用户：个性化渲染 + 3s 超时中断
  renderWithTimeout(req, res, 3000);
});
```
