---
title: [MFW-781] 乐观锁在 Action 中的实现
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-781：乐观锁在 Action 中的实现

**答**:
- 乐观锁（OCC）在 Action 中的实现：1) **version 字段**（每条记录带 version——update 时 WHERE version = 当前版本 → 更新成功 version++；版本不匹配 = 他人已修改 → 409 conflict；2) **action 层的冲突处理**（updateProfile(data, version) → WHERE version=version → 0 行更新 = 冲突 → 返回 409 + 当前数据（client 重新加载）；3) **悲观锁的对比**（SELECT FOR UPDATE——阻塞直到锁释放（并发吞吐低）vs 乐观锁（不阻塞——冲突时重试 RBL-567）；「乐观锁的优势 = 无锁竞争（读多写少场景吞吐高）」。
- client 侧的冲突 UI：409 → 提示「已被他人修改」→ 重新加载 → 用户决定合并/覆盖——「冲突解决的用户交互」。
- 追问钩子：为什么「乐观锁」比「悲观锁」更适合 Server Actions？——Action 的写操作短事务（毫秒级——悲观锁的阻塞窗口极短但连接占用）；乐观锁 = 无锁等待（冲突时才处理——多数操作无冲突）；「读写比例」：读多写少（乐观锁优势——读不被锁阻塞）vs 写冲突频繁（悲观锁可能更简单——避免频繁重试）；Server Actions 的典型场景（用户编辑——单人冲突率低）适合乐观锁。

```typescript
'use server';
export async function updateProfile(
  id: string, data: ProfileInput, expectedVersion: number
) {
  const session = await auth();
  const result = await db.$queryRaw`
    UPDATE users SET name = ${data.name}, version = version + 1
    WHERE id = ${id} AND version = ${expectedVersion}
    RETURNING id, version`;
  if (!result.length) {
    // 版本不匹配：他人已修改
    const current = await db.users.find(id);
    return { conflict: true, currentVersion: current.version, currentData: current };
  }
  return { ok: true, version: result[0].version };
}
// client 冲突处理
'use client';
function ProfileEditor({ user }) {
  const [conflict, setConflict] = useState(null);
  return <form action={async (fd) => {
    const result = await updateProfile(user.id, data, user.version);
    if (result.conflict) {
      setConflict(result.currentData);                   // 显示冲突：重新加载后编辑
    }
  }}>...</form>;
}
```
