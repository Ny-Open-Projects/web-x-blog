---
title: [DP-102] 重构实战：订单流程的巨型 switch 如何升级为映射表与状态机？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-102：重构实战：订单流程的巨型 switch 如何升级为映射表与状态机？（高频）
**答**：
- switch 的坏味道：状态转移规则散落在各处，"哪些状态能发什么事件"无法一眼看出，非法转移（已取消还能发货）没有防线。
- 升级两步走：第一版映射表（事件 → 处理函数）消灭 switch；第二版补上"当前状态"维度成为状态机表（状态 × 事件 → 下一步 + 动作）。
- 状态机表的价值：转移合法性由表保证，action 集中放副作用，可视化/测试都容易；再进一步可换 xstate（DP-056）。

```javascript
// 重构前：每个按钮 handler 里各自 switch，规则重复且互相漂移
function onPayClick(order) {
  switch (order.status) {
    case 'pending': pay(order); order.status = 'paid'; break;
    case 'shipped': /* 有人在这里复制粘贴出了重复逻辑 */ break;
  }
}
function onCancelClick(order) {
  switch (order.status) {
    case 'pending': close(order); order.status = 'closed'; break;
    case 'paid':    refund(order); order.status = 'refunding'; break;  // 新加的，忘记同步到别处
  }
}
```

```javascript
// 重构后：状态机表 = 状态 × 事件 → next + action
const orderMachine = {
  pending: {
    pay:    { next: 'paid',      action: (o) => pay(o) },
    cancel: { next: 'closed',    action: (o) => close(o) },
  },
  paid: {
    ship:   { next: 'shipped',   action: (o) => createDelivery(o) },
    refund: { next: 'refunding', action: (o) => startRefund(o) },
  },
  shipped: { confirm: { next: 'done', action: (o) => addPoints(o) } },
};
function dispatch(order, event) {
  const node = orderMachine[order.status]?.[event];
  if (!node) throw new Error(`非法转移 ${order.status} + ${event}`);  // 防线：表之外的转移直接报错
  node.action(order);
  order.status = node.next;
  return order.status;
}
const order = { status: 'pending' };
dispatch(order, 'pay');     // paid
dispatch(order, 'ship');    // shipped
dispatch(order, 'cancel');  // Error 非法转移 shipped + cancel —— 已发货不能取消
```
