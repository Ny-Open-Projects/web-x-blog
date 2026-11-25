---
title: [MFW-813] RSC 分页渲染时用户下了单，翻页出现重复/丢失行，怎么用快照游标解决
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-813：RSC 分页渲染时用户下了单，翻页出现重复/丢失行，怎么用快照游标解决

**答**：
- 结论：offset 分页在数据集被并发写改变时会重复/漏行；改用 keyset（游标）分页并把「快照版本」随游标传递，让后续页在同一逻辑快照上读。
- 落地：首页返回 { items, cursor, snapshotTs }；下一页带 cursor + snapshotTs，查询按 id 游标 + 版本上界（MVCC 快照读）。
- 追问钩子：快照太老被 GC 怎么办？——回退「当前快照 + 数据已变化」提示，或限制可回溯窗口。

```javascript
// ❌ offset 分页：并发插入新行 → 下一页重复
async function pageByOffset(page, size) {
  return db.items.orderBy('createdAt').offset(page*size).limit(size);
}

// ✅ keyset + 快照：游标定位 + 版本上界
async function pageByCursor(cursor, snapshotTs, size) {
  const c = cursor ? decode(cursor) : { id: null };
  return db.items.where(builder => {
      if (c.id) builder.where('id', '<', c.id);     // 稳定定位
      builder.where('createdAt', '<=', snapshotTs); // 同一快照
    })
    .orderBy('id', 'desc').limit(size);
}

// RSC 首页携带快照版本给客户端
async function ListPage() {
  const ts = await db.currentSnapshotTs();
  const items = await pageByCursor(null, ts, 20);
  return <List items={items} cursor={encode({ id: items.at(-1).id })} ts={ts} />;
}
```
