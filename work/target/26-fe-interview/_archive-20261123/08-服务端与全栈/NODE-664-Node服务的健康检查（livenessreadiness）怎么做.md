---
title: [NODE-664] Node 服务的健康检查（liveness/readiness）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-664：健康检查怎么做？
**答**：
- 两类探针语义：liveness（活着吗——失败则重启容器）、readiness（能服务吗——失败则摘流量不重启）；混用是常见事故源（readiness 误配成 liveness → 依赖抖动引发重启风暴）。
- readiness 的构成：进程健康 + 关键依赖可达（DB/Redis——依赖挂了摘流量，SCN-NODE-638 摘流先行）；依赖检查带超时（探针不能被慢依赖拖死——探针超时独立于业务超时）。
- liveness 的极简：只查进程自响应（不查依赖——依赖抖动不该重启自己）；事件循环阻塞检测（节拍器——主线程阻塞 > N s 即不健康，SCN-FIN-664 watchdog 同源）。
- 启动探针：slow-start 应用（预热缓存）的 startupProbe——防止启动期被 liveness 误杀。
- 追问钩子：为什么 readiness 检查依赖而 liveness 不能——liveness 失败触发容器重启；若 liveness 查 DB 且 DB 抖动，所有实例被同时重启（服务全灭——比依赖故障更糟）；readiness 只摘流量（DB 恢复后自动回流）——「重启是自愈的最后手段，摘流才是依赖故障的正确响应」。

```javascript
app.get('/healthz', (req, res) => res.status(200).end());   // liveness：极简
app.get('/readyz', async (req, res) => {
  const checks = await Promise.allSettled([
    withTimeout(db.ping(), 500), withTimeout(redis.ping(), 300),
  ]);
  const ok = checks.every(c => c.status === 'fulfilled');
  res.status(ok ? 200 : 503).end();                    // 依赖挂 → 摘流不重启
});
// 事件循环阻塞检测（liveness 增强）
setInterval(() => { const d = Date.now() - last; if (d > 5000) markUnhealthy(); last = Date.now(); }, 1000);
```
