---
title: [MFW-806] 怎么给 Server Action 设计「事务内缓存旁路」机制（标记与降级）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-806：怎么给 Server Action 设计「事务内缓存旁路」机制（标记与降级）

**答**：
- 结论：用请求级/事务级标志 IN_TX，所有读封装检测它：事务内直接穿透到 DB（bypass cache），事务外正常走缓存，这样决策读永远拿当前快照。
- 配合：写路径在 commit 后主动 revalidateTag，把旁路读到的新值回填缓存，避免下次又读旧。
- 追问钩子：旁路会不会击穿缓存？——只影响事务内少量决策读，且可异步回填；不是全站关缓存。

```javascript
const als = new AsyncLocalStorage();

function inTx() { return !!als.getStore()?.bypass; }

function smartRead(cacheRead, dbRead) {
  return (...args) => inTx() ? dbRead(...args) : cacheRead(...args);
}

// 读封装：事务内穿透，事务外走缓存
const readSku = smartRead(
  (id) => unstable_cache(() => db.sku.find(id), ['sku'], { tags: ['sku'] })(),
  (id) => db.sku.find(id)
);

async function withBypass(tx, fn) {
  return als.run({ bypass: true }, () => fn(tx));
}

async function update(id, patch) {
  const tx = await db.begin();
  try {
    return await withBypass(tx, async () => {
      const cur = await readSku(id);               // 穿透 → 当前快照
      await tx.update(id, patch);
      await tx.commit();
    });
  } finally { revalidateTag('sku'); }
}
```
