---
title: [JS-245] using 与显式资源管理提案：Symbol.dispose
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-245：using 与显式资源管理（explicit resource management）

**答**：
- using：块级作用域的资源声明——离开作用域自动调用 Symbol.dispose（try/finally 的语法糖，Python with 的 JS 版）
- 实现接口：对象实现 `Symbol.dispose` 方法（清理逻辑）；异步资源用 `await using` + Symbol.asyncDispose
- 价值：把「忘了 close/clear/abort」类资源泄漏消灭在语法层——数据库连接、文件句柄、AbortController
- 支持方式：TypeScript 5.2+ 转译；原生引擎落地推进中
- 与 GC 的分界：dispose 管「显式资源」（确定性时机），GC 管「内存」（不确定时机）——面试必须分清

```typescript
class DbConn {
  constructor(private conn: Connection) {}
  [Symbol.dispose]() { this.conn.close(); }
}
async function query() {
  using conn = new DbConn(pool.connect()); // 离开作用域自动 close，异常也保证
  return await conn.query('SELECT 1');
}
```
