---
title: [MFW-803] Server Action 提交成功后 router.refresh 却读到旧数据，可见性竞态怎么解
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-803：Server Action 提交成功后 router.refresh 却读到旧数据，可见性竞态怎么解

**答**：
- 结论：commit 与 refresh 是两次独立 HTTP 往返，refresh 可能落在副本延迟窗口里读到旧快照；写请求响应必须携带「读己之写」凭据（版本/时间戳），刷新请求带上它强制读主或等待追平。
- 落地：action 返回 { ok, afterTs }；客户端 refresh 时把 afterTs 放进 header；读路径识别该 header 选主库/强一致副本。
- 追问钩子：为什么不直接 await 副本同步？——跨区无统一 ACK，等待会把 P99 拉爆；凭据路由是「按需强一致」替代「全局强一致」。

```javascript
// Server Action：提交后返回写入时间戳作为凭据
async function saveProfile(formData) {
  'use server';
  const ts = await db.user.update({ ... });       // 返回本次写入的逻辑时间
  revalidateTag('profile');
  return { ok: true, afterTs: ts };
}

// 客户端：把凭据随刷新请求带上
async function onSaved(res) {
  const r = await fetch('/api/snapshot', {
    headers: { 'x-after-write': String(res.afterTs) }
  });
  const data = await r.json();                    // 保证读到 >= afterTs 的版本
  router.refresh();
}

// 读路径：凭据存在且副本落后 → 回落主库
async function readProfile(req) {
  const after = Number(req.headers.get('x-after-write') || 0);
  const replicaTs = await replica.ts();
  const db = replicaTs >= after ? replica : primary;
  return db.user.find(/* ... */);
}
```
