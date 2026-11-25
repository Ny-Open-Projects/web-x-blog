---
title: [NODE-775] 笔试题——实现审计日志（append-only + 检索 + 防篡改）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-775：手写审计日志

**需求与边界**：
- 需求：审计日志（SCN-FIN-521/OPS-220）——① append-only 存储（不可改删——权限隔离：应用账号只有 INSERT 权限）；② 检索（按主体/时间/动作——SCN-FIN-625）；③ 防篡改哈希链（每条含前条 hash——链式证据，SCN-联想-631）；④ 敏感字段脱敏进审计。
- 边界：① 哈希链的验证任务（定期校验链完整性——断链告警）；② 审计写入与业务解耦（ALS 异步写——不阻塞业务，SCN-NODE-646）；③ 检索权限（审计只读角色——SCN-OPS-643）。

**答**：
```javascript
async function audit(entry) {
  const prev = await db.query('SELECT hash FROM audit ORDER BY id DESC LIMIT 1 FOR UPDATE');
  const hash = sha256(JSON.stringify({ ...entry, prev: prev?.hash ?? 'GENESIS' }));   // 链式哈希
  await db.insert('audit', { ...entry, prev: prev?.hash, hash });   // append-only（应用账号无 UPDATE/DELETE 权限）
}
// 链完整性验证（定期——SCN-联想-631）
async function verifyChain() {
  let prev = 'GENESIS';
  for (const e of await db.allAudit()) {
    const expect = sha256(JSON.stringify({ ...e.entry, prev }));
    if (e.hash !== expect) return alert({ type: 'CHAIN_BROKEN', at: e.id });   // 断链告警
    prev = e.hash;
  }
  return { intact: true };
}
// 检索权限：只读角色（SCN-OPS-643 审计角色）
app.get('/audit/search', requireRole('auditor'), async (req, res) =>
  res.json(await auditSearch(req.query)));             // 按主体/时间/动作
```

**评分点**:
- append-only 权限隔离（应用账号只有 INSERT——不可改删）。
- 哈希链防篡改 + 定期验证（断链告警——SCN-联想-631）。
- 检索权限审计角色（SCN-OPS-643）。
- 敏感字段脱敏进审计（SCN-NODE-698 联动）。
