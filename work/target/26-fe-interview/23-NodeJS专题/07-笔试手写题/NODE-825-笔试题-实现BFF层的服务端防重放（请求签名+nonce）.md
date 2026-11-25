---
title: [NODE-825] 笔试题——实现 BFF 防重放（nonce + 时间窗 + 签名）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-825：手写防重放

**需求与边界**：
- 需求：服务端防重放（SCN-NODE-752 服务端版）——① nonce 去重（Redis SETNX——SCN-NODE-752）；② 时间窗（±5min——nonce TTL 闭合）；③ 签名覆盖（method+path+body 摘要——SCN-联想-752 规范化）；④ 窗口时钟漂移（多实例——容忍声明）。
- 边界：① nonce 存储的 TTL 与窗口一致（SCN-联想-752 闭合语义）；② 高并发 nonce 写入的性能（批量 SETNX/pipeline——SCN-NODE-674）；③ 防重放与幂等的分工（防重放挡网络层重放；幂等挡业务重试——两层语义不同，SCN-NODE-709）。

**答**：
```javascript
function antiReplay({ windowMs = 5 * 60_000 } = {}) {
  return async (req, res, next) => {
    const { ts, nonce, sign } = req.headers;
    if (Math.abs(Date.now() - +ts) > windowMs)
      return res.status(401).json({ code: 'TS_EXPIRED' });   // 时间窗（SCN-联想-752）
    const digest = sha256(canonicalBody(req));           // 规范化摘要
    const expected = hmac(SECRET, `${req.method}|${req.path}|${ts}|${nonce}|${digest}`);
    if (!timingSafeEqual(expected, sign))                // 恒时比较（SCN-联想-752）
      return res.status(401).json({ code: 'SIGN_INVALID' });
    const ok = await redis.pipeline()
      .set(`nonce:${nonce}`, 1, 'PX', windowMs, 'NX')
      .expire(`nonce:${nonce}`, windowMs).exec();        // pipeline 批量（SCN-NODE-674）
    if (!ok[0]) return res.status(401).json({ code: 'REPLAY' });   // nonce 去重
    next();                                              // 注意：防重放 ≠ 幂等（SCN-NODE-709 分工）
  };
}
```

**评分点**:
- 时间窗 + nonce TTL 闭合（SCN-联想-752 窗口语义）。
- timingSafeEqual + 规范化摘要（SCN-联想-752）。
- pipeline 批量 nonce（性能——SCN-NODE-674）。
- 防重放与幂等分工声明（SCN-NODE-709 两层语义）。
