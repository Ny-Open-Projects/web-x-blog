---
title: [NODE-835] 笔试题——实现接口防爬限流（维度组合 + 行为信号）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-835：手写防爬限流

**需求与边界**：
- 需求：防爬限流（SCN-NODE-641/联想-569）——① 维度组合限流（IP/用户/UA/端点——SCN-NODE-641）；② 行为信号辅助（无 dwell/连续均匀间隔——SCN-联想-590 特征）；③ 分级处置（限速→验证→封禁——SCN-联想-586 轮换）；④ 白名单（搜索引擎爬虫——合法 UA 白名单）。
- 边界：① 特征信号的权重量化（多特征弱证据加权——SCN-联想-597）；② 封禁的申诉通道（SCN-联想-563）；③ 动态阈值（攻击期收紧——SCN-联想-573 开关矩阵）。

**答**：
```javascript
function antiCrawler(req) {
  const dims = { ip: req.ip, user: req.user?.id, ua: req.headers['user-agent'] };
  if (SEARCH_BOTS.has(dims.ua)) return next();         // 合法爬虫白名单
  for (const [dim, val] of Object.entries(dims)) {
    const r = limiter.check(`${dim}:${val}:${req.route.path}`);   // 维度组合（SCN-NODE-641）
    if (!r.allowed) return escalate(dim, r);           // 分级处置（SCN-联想-586）
  }
  const behavior = behaviorScore(req);                 // 行为特征（SCN-联想-597 加权）
  if (behavior.machineHint && Math.random() < 0.5)
    return captchaChallenge(req);                      // 疑似：验证升级（SCN-联想-565 分级）
  next();
}
function escalate(dim, r) {
  const strikes = strikeCount(dim, r);
  if (strikes < 3) return res.status(429).set('Retry-After', r.waitMs / 1000).end();
  return banTemporarily(dim, r, { duration: 30 * 60_000 });   // 分级封禁（SCN-联想-590 指数惩罚）
}
```

**评分点**:
- 维度组合限流（SCN-NODE-641）+ 合法爬虫白名单。
- 行为特征加权（弱证据——SCN-联想-597）+ 分级处置（限速→验证→封禁——SCN-联想-586）。
- 动态阈值（攻击期收紧——SCN-联想-573）。
- 申诉通道意识（SCN-联想-563）。
