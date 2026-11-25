---
title: [1146] 笔试手写：实现 SQL 安全守卫（只读/白名单/LIMIT）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, RAG, 安全]
type: 笔试题
---

## 1146：笔试手写：实现 SQL 安全守卫（只读/白名单/LIMIT）

**答**：实现 sqlGuard(sql, { tables, forceLimit=100 })：拒绝非 SELECT 语句；校验 FROM/JOIN 涉及的表都在白名单（简单正则提取表名）；无 LIMIT 时自动追加 LIMIT；含注释（-- 或 /*）直接拒绝（防注释注入）。返回 { ok, sql } 或 { ok: false, reason }。

```js
function sqlGuard(sql, { tables, forceLimit = 100 } = {}) {
  const s = sql.trim().replace(/;\s*$/, '');
  if (!/^select\s/i.test(s)) return { ok: false, reason: '只读仅允许 SELECT' };
  if (/--|\/\*/.test(s)) return { ok: false, reason: '含注释，拒绝' };
  // 提取 FROM/JOIN 后的表名
  const refs = [...s.matchAll(/\b(?:from|join)\s+([`\w.]+)/gi)].map(m => m[1].replace(/`/g, ''));
  const bad = refs.filter(t => !tables.includes(t));
  if (bad.length) return { ok: false, reason: '表不在白名单: ' + bad.join(',') };
  if (!/\blimit\s+\d+/i.test(s)) return { ok: true, sql: s + ' LIMIT ' + forceLimit };
  return { ok: true, sql: s };
}
const T = ['sales', 'orders'];
console.log(sqlGuard('SELECT * FROM sales', { tables: T }).sql);      // 追加 LIMIT
console.log(sqlGuard('DROP TABLE sales', { tables: T }).ok);          // false
console.log(sqlGuard('SELECT * FROM users', { tables: T }).reason);   // 白名单
```

**评分点**：
- 非 SELECT 拒绝 + 多语句（分号后仍有内容）可讨论处理
- 表名提取正则覆盖 FROM/JOIN，反引号处理
- 注释拒绝防「SELECT 1 --DROP」类注入
- 能讨论局限：正则守卫挡不住子查询别名等复杂形态，生产用 SQL parser（AST 校验）+ 只读账号双保险

