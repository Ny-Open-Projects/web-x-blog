---
title: [NODE-735] 笔试题——实现幂等中间件完整版（并发/失败语义/结果重放）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-735：手写幂等中间件

**需求与边界**：
- 需求：框架级幂等（SCN-NODE-709）——① DB 唯一约束兜底（并发原子——SCN-NODE-655）；② 三态（RUNNING/DONE/FAILED——失败不缓存可重试，SCN-NODE-709）；③ 并发同 key 等待首请求结果（SCN-NODE-697）；④ 结果快照重放（状态码+体）。

**答**：
```javascript
function idempotent({ ttl = 86_400_000 } = {}) {
  return (req, res, next) => {
    const key = req.headers['x-idem-key'];
    if (!key) return next();
    res.locals.sendSnapshot = false;
    (async () => {
      try {
        await db.query('INSERT INTO idem (key, status) VALUES ($1, $2)', [key, 'RUNNING']);   // 唯一约束兜底
      } catch (e) {
        if (e.code === '23505') {                      // 并发：等首请求结果（SCN-NODE-697）
          for (let i = 0; i < 100; i++) {
            const row = await db.query('SELECT status, body, code FROM idem WHERE key=$1', [key]);
            if (row?.status === 'DONE') return res.status(row.code).json(row.body);
            if (row?.status === 'FAILED') return res.status(409).json({ retryable: true });   // 失败可重试
            await sleep(100);
          }
          return res.status(409).json({ code: 'IN_FLIGHT' });
        }
        throw e;
      }
      capture(res, async (code, body) => {             // 结果捕获（成功才缓存——SCN-NODE-709）
        await db.query(`UPDATE idem SET status='DONE', code=$2, body=$3, expire_at=now()+$4 WHERE key=$1`,
          [key, code, JSON.stringify(body), ttl]);
      });
      res.on('finish', () => {                         // 失败（5xx）：标记失败可重试
        if (res.statusCode >= 500)
          db.query(`UPDATE idem SET status='FAILED' WHERE key=$1`, [key]);
      });
      next();
    })();
  };
}
```

**评分点**:
- DB 唯一约束兜底并发（竞态原子——SCN-NODE-655）。
- 三态语义（DONE 重放/RUNNING 等待/FAILED 可重试——SCN-NODE-709）。
- 并发等待首请求结果（轮询——不重复执行）。
- 失败不缓存（5xx 标记 FAILED——错误固化防御）。

## 变体与延伸（补充）

**变体与延伸**：

1. RUNNING 状态的请求一直不结束，同 key 后续请求会永久等待吗 → 等待方设 3s 超时即返回 409 让客户端重试，同时给 RUNNING 记录加 TTL 兜底，避免死锁一直挂着。
2. 结果快照重放会不会越权拿到别人的响应 → 快照 key 必须带 userId 维度，且只缓存 body 与状态码，不缓存 set-cookie、鉴权头这类会话相关字段。
3. 幂等键由客户端生成，恶意复用同一 key 刷接口怎么办 → 幂等键与 userId 加 path 绑定校验，不匹配直接 400，同 key 高频请求单独计数告警。
