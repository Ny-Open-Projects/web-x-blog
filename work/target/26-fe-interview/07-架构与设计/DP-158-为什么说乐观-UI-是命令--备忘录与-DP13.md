---
title: [DP-158] 为什么说乐观 UI 是"命令 + 备忘录"？与 DP-135 的差异点在哪？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-158：为什么说乐观 UI 是"命令 + 备忘录"？与 DP-135 的差异点在哪？（高频）
**答**：
- 备忘录：操作前对"受影响的局部状态"拍快照（不是全量 store），回滚 = 恢复快照，O(1) 且精确。
- 命令：每个操作是 `{ do, undo }` 闭包/对象，发起即执行 do 并入栈；服务器确认成功则丢弃（或转正式记录），失败执行 undo。
- 与 DP-135（回滚队列）的分工：135 关注"多条乐观操作的排队与一致性"，本题关注"单条操作的快照与撤销原语"，二者可叠加（队列的每条 entry 用本条的快照回滚）。

```javascript
// 原语层：局部快照 + do/undo 命令
function withOptimistic(store) {
  const apply = (cmd) => {
    const snapshot = structuredClone(store.slice());          // 备忘录：局部快照
    cmd.do(store);
    return {
      async confirm(request) {
        try { const server = await request(); cmd.merge?.(store, server); return server; }  // 成功：用服务端真值覆盖
        catch (e) { store.replace(snapshot); toastError(e); throw e; }                      // 失败：恢复快照
      },
    };
  };
  return { apply };
}
const opt = withOptimistic(store);
// 场景1：点赞
const ticket1 = opt.apply({
  do: (s) => { const p = s.posts.find((x) => x.id === id); p.liked = true; p.likes++; },
});
ticket1.confirm(api.like(id));
// 场景2：编辑 + 重命名（命令可带 merge，消除乐观值与服务端值的偏差）
const ticket2 = opt.apply({
  do: (s) => { const doc = s.docs.find((d) => d.id === docId); doc.title = '新标题'; doc.saving = true; },
  merge: (s, server) => { const doc = s.docs.find((d) => d.id === docId); doc.updatedAt = server.updatedAt; doc.saving = false; },
});
await ticket2.confirm(api.rename(docId, '新标题'));           // 成功后 saving=false，updatedAt 用服务端
```
