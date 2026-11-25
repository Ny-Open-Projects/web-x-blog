---
title: [NODE-791] 笔试题——实现签名 URL 生成与续签（短时效 + 绑定）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-791：手写签名 URL

**需求与边界**：
- 需求：签名 URL（SCN-FIN-494）——① 短时效签名（HMAC——到期失效）；② 参数绑定（userId/key/操作类型——换用户不可用）；③ 续签（下载中断续签——同参数新签名）；④ 防泄露（URL 不进日志/不进前端缓存——SCN-FIN-509）。
- 边界：① 签名参数完整（操作类型限定 GET/PUT——签名即授权范围）；② 续签的权限校验（续签也要鉴权——不能拿旧 URL 无限续）；③ 一次性 URL（下载链接单次——重放拒绝）。

**答**：
```javascript
function signUrl({ key, userId, op, ttl = 300_000, once = false }) {
  const exp = Date.now() + ttl;
  const sig = hmac(SECRET, `${key}|${userId}|${op}|${exp}${once ? '|' + crypto.randomUUID() : ''}`);
  return { url: `/files/${key}?u=${userId}&op=${op}&e=${exp}&s=${sig}`, exp, once };
}
function verifySignedUrl(req) {
  const { key, u, op, e, s } = req.query;
  if (Date.now() > +e) throw new Error('URL_EXPIRED');      // 过期
  const expect = hmac(SECRET, `${key}|${u}|${op}|${e}`);
  if (!timingSafeEqual(expect, s)) throw new Error('URL_FORGED');   // 防伪造
  if (once && usedSet.has(s)) throw new Error('URL_REPLAYED');      // 一次性：重放拒绝
  if (+u !== req.user?.id) throw new Error('USER_MISMATCH');        // 用户绑定
  markUsed(s, once);                                   // 单次标记
}
// 续签：鉴权后新签名（SCN-FIN-494）
app.post('/files/renew', auth(), (req, res) => res.json(signUrl({ ...req.body, userId: req.user.id, ttl: 300_000 })));
```

**评分点**:
- 短时效 HMAC + 参数绑定（用户/操作——签名即授权）。
- timingSafeEqual + 一次性重放拒绝。
- 续签鉴权（不能拿旧 URL 无限续——SCN-FIN-494）。
- URL 不进日志（SCN-FIN-509 脱敏联动）。
