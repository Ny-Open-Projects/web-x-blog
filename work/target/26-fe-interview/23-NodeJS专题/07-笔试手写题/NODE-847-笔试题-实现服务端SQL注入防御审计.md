---
title: [NODE-847] 笔试题——实现 SQL 注入防御审计（参数化校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-847：手写 SQL 防御

**需求与边界**：
- 需求：SQL 注入审计（SCN-NODE-719）——① 参数化查询强制（拼接 SQL 检测——CI 扫描 + 运行时审计）；② 动态表名/列名的白名单（标识符白名单——不能参数化的部分）；③ 运行时审计（异常 SQL 模式告警——SCN-NODE-747）；④ ORM 的逃生舱审计（raw query 的白名单清单）。
- 边界：① CI 扫描（源码字符串拼接 SQL 检测——SCN-ENG-235）；② 运行时检测（query 拦截——用户输入出现在 SQL 位置）；③ 白名单管理（标识符白名单变更审计——SCN-OPS-219）。

**答**：
```javascript
// 运行时审计：拦截 raw query
db.on('query', (q) => {
  if (q.sql.includes('${') || q.sql.includes('` + '))   // 模板拼接特征
    alert({ type: 'SQL_CONCAT_SUSPECT', sql: q.sql, stack: captureStack() });
  const userTokens = extractUserInputTokens(q.bindings);
  if (userTokens.some(t => /('|;|--|\bunion\b|\bdrop\b)/i.test(t) && appearsAsIdentifier(q.sql, t)))
    alert({ type: 'SQL_INJECT_SUSPECT' });             // 用户输入出现在标识符位置
});
// CI 扫描（SCN-ENG-235）
for (const file of sourceFiles)
  for (const m of file.match(/db\.query\(`[^`]*\$\{/g))   // 模板串拼接
    fail(`SQL 拼接: ${file}:${m}`);
// 标识符白名单（动态表名）
const ALLOWED_TABLES = new Set(['orders', 'goods']);
function safeTable(name) { if (!ALLOWED_TABLES.has(name)) throw new Error('TABLE_BLOCKED'); return name; }
```

**评分点**:
- 双层防御（CI 源码扫描 + 运行时审计——SCN-ENG-235）。
- 标识符白名单（动态表名——不能参数化的部分显式管理）。
- 用户输入位置检测（标识符位置 vs 参数位）。
- 白名单变更审计（SCN-OPS-219）。
