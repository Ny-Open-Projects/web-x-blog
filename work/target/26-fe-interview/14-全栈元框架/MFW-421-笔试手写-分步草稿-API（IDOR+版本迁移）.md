---
title: [MFW-421] 笔试：手写分步草稿 API（IDOR 防线+版本迁移）
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-421：分步草稿 API
**答**：实现 `draftEndpoints(db, crypto, { ttlDays = 7, schemas } )`：1) POST /drafts → { id: 不透明随机串, stepUrls }（创建即归属）；2) PATCH /drafts/:id/step/:n → 归属校验（uid 不匹配 → 404 非 403——存在性不泄露）+ 步数据加密存储（AES-GCM per-draft key）+ schema 版本记录；3) GET 恢复 → 版本比对：相等直返/旧版走 migrate 链/新版（回滚发版）提示重填；4) 提交 → 全量聚合校验（步级通过≠整体合法：跨步依赖如 A 步国家=B 步税号格式）→ fieldErrors 带步号定位；5) GC（updatedAt > 7d 删除——含密钥销毁）。

```javascript
export function draftApi(db, { keyring } = {}) {
  return {
    'POST /drafts': auth(async (user) => {
      const id = crypto.randomBytes(16).toString('base64url')     // 不可枚举
      const dk = crypto.randomBytes(32)                            // per-draft 数据密钥
      await save({ id, uid: user.id, dk: kms.wrap(dk), v: SCHEMA_V, steps: {}, at: now })
      return { id }
    }),
    'PATCH /drafts/:id/step/:n': owng(async (user, id, step, payload) => {
      const d = await loadOwned(id, user.id)                       // uid 不匹配→404
      if (vStale(d.v)) return 409({ migrate: MIGRATIONS[d.v] })    // 版本三分支
      await saveStep(id, step, encryptAE SG(payload, unwrap(dk)), { stepTs: now })
    }),
    'POST /drafts/:id/submit': crossValidate(async (all) => {      // 聚合：跨步依赖
      const r = FULL_SCHEMA.safeParse(unfoldAll(steps))
      if (!r.success) return fieldErrorsWithStep(r)                // {step, path, message}
      await promoteToOrder(r.data); destroyDraft(id)               // 密钥销毁
    }),
  }
}
setInterval(gcDrafts, 3600_000)                                  // >7d 删（含密钥）
```
**评分点**：
- 404 代 403（存在性不泄露——IDOR 标准应答）+ 不透明 id（防枚举）
- per-draft 信封加密（密钥与密文分离存储；销毁=真删除）
- 版本三分支（等/旧迁移/新拒绝——回滚发版安全）
- 跨步聚合校验（步级各自通过≠整体合法——fieldErrors 带步号定位回跳 UI）
