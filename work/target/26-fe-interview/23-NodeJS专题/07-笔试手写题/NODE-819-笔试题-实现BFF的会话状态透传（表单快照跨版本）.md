---
title: [NODE-819] 笔试题——实现 BFF 会话状态透传（版本切换表单不丢）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-819：手写会话透传

**需求与边界**：
- 需求：版本切换会话保护（SCN-OPS-218/744）——① 会话状态快照端点（客户端断开/版本对齐刷新前保存——SCN-OPS-218 表单）；② 快照恢复（新版本加载后恢复——schema 兼容转换，SCN-OPS-646 迁移器）；③ 快照 TTL 与加密（敏感表单——SCN-FIN-515 最小存活）；④ 冲突处理（多 Tab 快照覆盖——last-write-wins + 提示）。
- 边界：① 快照 schema 版本（旧版本快照新版本恢复——字段迁移）；② 敏感字段不进快照（密码类——SCN-FIN-515）；③ 快照服务端存储的加密（payload 加密——SCN-FIN-515 加密上传）。

**答**：
```javascript
app.post('/session/snapshot', auth(), async (req, res) => {
  const { data, schemaVer } = sanitize(req.body);      // 敏感字段剔除（SCN-FIN-515）
  const encrypted = await encrypt(data);               // 加密存储（SCN-FIN-515）
  await redis.setex(`snap:${req.user.id}:${req.query.tab}`, 600, JSON.stringify({ encrypted, schemaVer }));
  res.end();
});
app.get('/session/snapshot', auth(), async (req, res) => {
  const snap = await redis.get(`snap:${req.user.id}:${req.query.tab}`);
  if (!snap) return res.json(null);
  const { encrypted, schemaVer } = JSON.parse(snap);
  const migrated = migrateSnapshot(await decrypt(encrypted), schemaVer, CURRENT_SNAP_VER);   // schema 迁移（SCN-OPS-646）
  res.json(migrated);
});
function migrateSnapshot(data, from, to) {             // 字段迁移器（SCN-OPS-646）
  for (let v = from; v < to; v++) data = SNAP_MIGRATIONS[v]?.(data) ?? data;
  return data;
}
```

**评分点**:
- 快照加密 + 敏感字段剔除（SCN-FIN-515 最小存活）。
- schema 版本迁移（SCN-OPS-646 迁移器——跨版本恢复）。
- TTL 600s（会话窗口——SCN-OPS-218 重入语义）。
- 多 Tab 键隔离（tab 维度——冲突显式）。
