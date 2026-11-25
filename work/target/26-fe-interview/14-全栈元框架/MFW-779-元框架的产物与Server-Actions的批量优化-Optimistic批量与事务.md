---
title: [MFW-779] 乐观批量与事务
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-779：乐观批量与事务

**答**:
- 乐观批量的 UI 协议（RBL-706 批量操作的 UI 层）：1) **批量乐观**（全选删除——所有选中项立即消失（乐观移除）；server 事务成功 → 真值对齐；事务失败 → 全部恢复（RBL-707 all-or-nothing 的 UI 版）；2) **部分成功的 UI**（best-effort：成功的消失、失败的恢复+错误提示——逐条对应 RBL-707 的 results）；3) **批量乐观的状态管理**：useOptimistic 的数组操作（filter/map——批量删除/更新的乐观变换 RBL-741）。
- 事务语义与 UI 语义的对齐：all-or-nothing = 乐观全删→全恢复；best-effort = 乐观全删→部分恢复（每个 item 的状态 = 成功保留失败恢复）——「事务模式 → UI 乐观策略」的映射。
- 追问钩子：为什么「乐观批量的事务语义」比「逐条乐观」更复杂？——逐条乐观：每条独立（乐观状态互不影响——一条失败只回滚自己）；批量乐观：多条共享事务语义（全回滚/部分恢复——乐观状态的联动——一条失败影响整批的 UI 状态）；「批量乐观的粒度」：整批状态（all-or-nothing）vs 逐条状态（best-effort）——状态管理的复杂度从 O(1) 到 O(N)。

```tsx
'use client';
function BulkDelete({ items, selectedIds }) {
  const [optimisticItems, removeOptimistic] = useOptimistic(
    items,
    (cur, removeIds: string[]) => cur.filter(i => !removeIds.includes(i.id))   // 批量乐观移除
  );
  return (
    <form action={async (fd) => {
      removeOptimistic(selectedIds);                       // 全部乐观移除（UI 立即消失）
      const result = await bulkDeleteAction(selectedIds);
      if (!result.ok) {
        // all-or-nothing 失败：useOptimistic 自动回滚（revalidate 恢复）
        showError(`删除失败: ${result.error}`);
      } else if (result.failed?.length) {
        // best-effort 部分失败：失败的项会在 revalidate 后恢复
        showPartialError(result.failed);
      }
    }}>
      {optimisticItems.map(item => <Item key={item.id} item={item} />)}
      <button>删除 {selectedIds.length} 项</button>
    </form>
  );
}
```
