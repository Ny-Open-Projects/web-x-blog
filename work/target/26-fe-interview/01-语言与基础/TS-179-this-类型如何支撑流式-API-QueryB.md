---
title: [TS-179] this 类型如何支撑流式 API（QueryBuilder）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-179：this 类型如何支撑流式 API（QueryBuilder）？
**答**：
- 返回类型写 `this` 而不是类名：链式调用后保留"真实实例类型"，继承链不塌缩。
- 需要"改变泛型状态"的链式方法（select 后 Row 变窄）返回新实例类型；不改变状态的方法返回 this。
- 两者搭配：状态型方法负责收窄，this 型方法保证子类方法不丢。

```typescript
class QueryBuilder<Row extends object = Record<string, unknown>> {
  protected filters: string[] = [];

  // 状态型：返回收窄后的新类型
  select<K extends keyof Row>(...keys: K[]): QueryBuilder<Pick<Row, K>> {
    return this as unknown as QueryBuilder<Pick<Row, K>>;
  }

  // this 型：不改状态，保留真实类型
  where(field: keyof Row, op: string, value: unknown): this {
    this.filters.push(`${String(field)} ${op} ?`);
    return this;
  }

  build(): { sql: string } {
    return { sql: this.filters.join(" AND ") };
  }
}

class SoftDeleteQuery<Row extends object> extends QueryBuilder<Row> {
  withDeleted(): this { // this 多态：链式后仍是 SoftDeleteQuery
    return this;
  }
}

const q = new SoftDeleteQuery<{ id: number; name: string }>()
  .withDeleted()
  .where("id", "=", 1); // 类型仍是 SoftDeleteQuery<...>，后续方法不丢
```
