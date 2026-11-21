---
title: [MFW-272] Action 的并发写冲突与 ABA 场景
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-272：并发写与 ABA

**答**:
- ABA 场景：库存 10→乐观扣 1→他人补货回 10→第二个请求以为没变再扣——值相同但历史不同；纯值比较防不住
- 防线：版本号（monotonic version）或条件更新（UPDATE ... WHERE qty = expected——CAS 语义在 SQL 层）——比较「版本」不是「值」
- UI 协同：409 冲突返回服务端最新态 → 客户端弹差异合并（ZSM-294 同款协议落到 Action）——不让用户盲目重试覆盖他人
- 幂等键配合：同表单重复提交（网络重试）用同一 opId——服务端按 opId 去重（首次结果缓存返回）——幂等与冲突控制是两件事都要

```javascript
const res = await prisma.order.updateMany({
  where: { id, version: input.baseVersion },        // CAS：版本比对
  data: { qty: newQty, version: { increment: 1 } },
})
if (res.count === 0) return { conflict: true, server: await fresh(id) }   // 409 带最新态
```
