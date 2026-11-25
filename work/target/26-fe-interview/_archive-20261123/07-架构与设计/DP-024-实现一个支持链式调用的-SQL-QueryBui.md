---
title: [DP-024] 实现一个支持链式调用的 SQL QueryBuilder？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-024：实现一个支持链式调用的 SQL QueryBuilder？
**答**：
- 链式调用 + 建造者：每个方法返回新实例或自身，最后 `build()` 产出结果。
- 加分实现：不可变 builder——每个方法返回克隆后的新 builder，可以安全地"分叉"复用基础查询。
- 关键点：维护子句的组装顺序（select→from→where→orderBy→limit）、条件数组化支持多次 where（AND 拼接）。
- 面试常追问"每次返回新对象和返回 this 的取舍"：返回 this 性能好但可变；返回新实例不可变、可缓存复用。

```javascript
class QueryBuilder {
  constructor(parts = {}) { this.parts = parts; }
  #next(patch) { return new QueryBuilder({ ...this.parts, ...patch }); } // 不可变分叉

  table(t) { return this.#next({ table: t }); }
  select(...cols) { return this.#next({ cols }); }
  where(cond) { // 多次 where 视为 AND
    return this.#next({ conds: [...(this.parts.conds || []), cond] });
  }
  orderBy(col, dir = 'asc') { return this.#next({ orderBy: { col, dir } }); }
  limit(n) { return this.#next({ limit: n }); }

  build() { // 装配：固定子句顺序
    const p = this.parts;
    const sql = [
      `SELECT ${(p.cols || ['*']).join(', ')}`,
      `FROM ${p.table}`,
      p.conds?.length ? `WHERE ${p.conds.join(' AND ')}` : '',
      p.orderBy ? `ORDER BY ${p.orderBy.col} ${p.orderBy.dir.toUpperCase()}` : '',
      p.limit ? `LIMIT ${p.limit}` : '',
    ].filter(Boolean).join(' ');
    return sql + ';';
  }
}
// 基础查询可复用（不可变带来的能力）
const baseUserQuery = new QueryBuilder().table('users').select('id', 'name');
console.log(baseUserQuery.where('age > 18').orderBy('id').limit(10).build());
// SELECT id, name FROM users WHERE age > 18 ORDER BY id ASC LIMIT 10;
console.log(baseUserQuery.where('vip = 1').build()); // 基础查询未被污染
// SELECT id, name FROM users WHERE vip = 1;
```

---

## 五、结构型：适配器/装饰器/代理
