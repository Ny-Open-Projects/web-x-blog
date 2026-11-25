---
title: [NODE-709] 接口幂等的框架级中间件化怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-709：幂等中间件化怎么做？
**答**：
- 框架级抽象：幂等作为中间件（声明式——路由标注幂等策略，业务代码无感知）：`router.post('/pay', idempotent({ ttl: 24h, store: 'db' }), handler)`。
- 中间件职责：幂等键提取（header/body 字段配置化）→ 查幂等表（命中返回原结果/处理中等待）→ in-flight 锁 → 执行 handler → 结果落幂等表（SCN-NODE-697 全流程框架化）。
- 结果序列化：响应快照存储（原结果重放——含状态码与头）。
- 失败语义：handler 失败 → 幂等表标记失败（可重试——下次重试重新执行而非返回错误快照——失败不缓存，SCN-NODE-697 失败释放）。
- 追问钩子：为什么幂等中间件要「失败不缓存」——缓存失败快照后，客户端重试拿到的是「上次的错误」（重试永远失败——错误固化）；只有成功结果才缓存（失败让重试真正重试）——「成功可重放、失败可重试」是幂等层的状态机语义。

```javascript
function idempotent({ ttl = 86400_000, keyFrom = (req) => req.headers['x-idem-key'] } = {}) {
  return async (req, res, next) => {
    const key = keyFrom(req); if (!key) return next();
    const prior = await idemStore.get(key);
    if (prior?.status === 'DONE') return res.status(prior.status_code).set(prior.headers).json(prior.body);
    if (prior?.status === 'RUNNING') return waitAndRespond(key, res);   // 并发等待
    await idemStore.markRunning(key);
    captureResponse(res, async (snapshot) => {           // 结果捕获
      await idemStore.finish(key, snapshot, ttl);
    });
    next();
  };
}
```
