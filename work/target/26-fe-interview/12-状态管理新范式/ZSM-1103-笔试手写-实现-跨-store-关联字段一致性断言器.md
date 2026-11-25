---
title: [1103] 笔试手写：实现 跨 store 关联字段一致性断言器
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## 1103：笔试手写：实现 跨 store 关联字段一致性断言器

**答**：两个 store 有关联不变量：cartStore.total === sum(cartStore.items.price) 且 userStore.isLoggedIn 时 orderStore.lastOrder 必须存在。实现 assertInvariants(snapshot)：snapshot 为 { cart, user, order } 三 store 快照，逐一断言不变量，违规输出违规项与定位（哪个 store 的哪个字段引发）。返回 { ok, violations }。

```js
function assertInvariants(snapshot) {
  const v = [];
  const { cart, user, order } = snapshot;
  const sum = cart.items.reduce((s, i) => s + i.price, 0);
  if (cart.total !== sum)
    v.push({ rule: 'total=sum(items)', culprit: `cart.total=${cart.total}`, expect: sum });
  if (user.isLoggedIn && !order.lastOrder)
    v.push({ rule: 'login⇒lastOrder', culprit: 'order.lastOrder missing' });
  if (!user.isLoggedIn && order.lastOrder)
    v.push({ rule: 'logout⇒no lastOrder', culprit: 'order.lastOrder exists' });
  return { ok: v.length === 0, violations: v };
}
```

**评分点**：
- 不变量写成显式规则（可枚举可扩展）
- culprit 定位到具体字段（可排查性）
- 双向断言（登录⇒存在、登出⇒不存在）
- 能讨论：断言在测试环境抛错、生产环境上报的分级策略
