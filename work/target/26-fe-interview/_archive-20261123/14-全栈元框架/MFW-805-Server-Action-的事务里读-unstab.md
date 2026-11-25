---
title: [MFW-805] Server Action 的事务里读 unstable_cache 为什么会脏读，怎么破
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-805：Server Action 的事务里读 unstable_cache 为什么会脏读，怎么破

**答**：
- 结论：Data Cache / unstable_cache 的命中发生在事务快照之外——缓存的是上次填充的旧值，事务内读它等于绕过当前事务的隔离语义。
- 现象：事务已把库存 10→9，事务内再读缓存仍是 10，基于它判断「库存充足」会写出错数据。
- 追问钩子：那事务里能读什么？——只信任事务内连接（同 connection / 主库）读；缓存读只用于「非决策性展示」。

```javascript
const cachedStock = unstable_cache(
  (id) => db.stock.find(id), ['stock'], { tags: ['stock'] }
);

async function deduct(id, n) {
  'use server';
  const tx = await db.begin();
  // ❌ 脏读：缓存命中绕过事务快照，仍是旧值 10
  const shown = await cachedStock(id);

  // ✅ 决策读：穿透缓存，走同一事务连接
  const real = await tx.one('SELECT qty FROM stock WHERE id=? FOR UPDATE', [id]);
  if (real.qty < n) { await tx.rollback(); throw new Error('库存不足'); }
  await tx.exec('UPDATE stock SET qty=qty-? WHERE id=?', [n, id]);
  await tx.commit();
  revalidateTag('stock');                          // 提交后回填缓存
  return { shown, real };                          // shown 仅做展示
}
```
