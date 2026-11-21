---
title: [ARC-015] DDD 在前端如何做轻量级实践？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-015：DDD 在前端如何做轻量级实践？
**答**：
- 不必照搬聚合根/仓储全套，前端取三点：统一语言（术语与代码命名一致）、实体行为内聚（校验规则进实体而非散落组件）、值对象不可变。
- 收益集中在前端最痛的"表单/状态规则散落"：把业务规则从组件里捞出来，组件只剩渲染。
- 轻量边界：只对核心域做 DDD，支撑域仍用贫血模型 + 表单库。

```typescript
// 统一语言：代码命名即业务术语（不是 data1/list2）
// 值对象不可变 + 不变式内聚
class Money {
  private constructor(
    readonly amount: number,   // 分为单位，避免浮点误差
    readonly currency: 'CNY' | 'USD',
  ) {}
  static create(amount: number, currency: 'CNY' | 'USD'): Money {
    if (!Number.isInteger(amount)) throw new Error('金额必须为分（整数）');
    if (amount < 0) throw new Error('金额不可为负');
    return new Money(amount, currency);
  }
  add(other: Money): Money {           // 行为在实体上，而非组件里的 if/else
    if (other.currency !== this.currency) throw new Error('币种不一致');
    return Money.create(this.amount + other.amount, this.currency);
  }
  toYuanString(): string { return (this.amount / 100).toFixed(2); }
}
// 组件只做展示与交互：<Price value={total.toYuanString()} />
```
