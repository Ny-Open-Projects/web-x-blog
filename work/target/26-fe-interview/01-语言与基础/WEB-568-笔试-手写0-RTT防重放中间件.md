---
title: [WEB-568] 笔试：手写 0-RTT 防重放中间件
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-568：笔试：手写 0-RTT 防重放中间件

**答**：实现 Express 风格中间件 `antiReplay`：① 识别请求头 `Early-Data: 1`（0-RTT 重放窗口内的请求）；② 对非幂等方法（POST/PUT/DELETE）直接拒绝返回 425 Too Early；③ 幂等方法放行；④ 业务层可选的自定义 nonce 去重钩子（Redis SETNX 语义，用传入的 store 抽象）。写出实现并说明为什么不直接拒绝所有 0-RTT 请求。

```javascript
const IDEMPOTENT = new Set(['GET', 'HEAD', 'OPTIONS']);

function antiReplay(store) {
  return async (req, res, next) => {
    if (req.headers['early-data'] !== '1') return next();
    if (!IDEMPOTENT.has(req.method)) {
      return res.status(425).set('Accept-Ranges', 'none').json({
        error: 'replay-risk', retry: 'after-handshake',
      });
    }
    if (store && req.headers['x-nonce']) {
      const ok = await store.setnx(`replay:${req.headers['x-nonce']}`, 1, 60);
      if (!ok) return res.status(425).json({ error: 'dup-replay' });
    }
    next();
  };
}

// store 抽象（Redis 适配）
const redisStore = {
  setnx: (k, v, ttl) => redis.set(k, v, 'EX', ttl, 'NX').then(r => r === 'OK'),
};
```

**评分点**：
- 认识 `Early-Data: 1` 是「代理/服务端标记该请求可能被重放」的标准信号（RFC 8470）
- 只拦非幂等方法，理解 0-RTT 的风险本质是重放而非窃听
- 425 状态码正确使用，且客户端语义是「握手后重试」
- nonce 去重用 SETNX + TTL，知道幂等方法是兜底、业务 nonce 是加强
