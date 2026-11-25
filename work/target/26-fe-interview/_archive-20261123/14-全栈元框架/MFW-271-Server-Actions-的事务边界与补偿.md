---
title: [MFW-271] Server Action 的事务边界与补偿设计
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-271：Action 事务边界与补偿

**答**:
- Action 不是事务容器：一个 Action 内多次外部调用（DB + 支付 + 邮件）无法原子——按 Saga 思路拆：核心写库本地事务（原子），外部副作用走「可靠事件 + 幂等消费」（outbox 模式）
- outbox 最小实现：业务写与事件记录同事务落库 → 后台/触发器投递事件 → 消费端幂等键去重——「先落意图再执行」替代分布式事务
- 补偿路径：已扣款但发货失败 → 反向 Action（退款）自动触发 + 人工兜底队列——补偿也要幂等与可重入
- 用户侧一致性：部分成功时 UI 语义（「已提交，发货确认中」）——不要把分布式未定态伪装成全成/全败

```javascript
export async function placeOrder(items) {
  'use server'
  await prisma.$transaction([
    prisma.order.create({...}),                                // 核心原子写
    prisma.event.create({ data: { type: 'CHARGE', payload, status: 'PENDING' } }),   // outbox 同事务
  ])
  // worker：PENDING 事件 → 调支付（幂等键=eventId）→ 成功标 SENT / 失败重试→死信
}
```
