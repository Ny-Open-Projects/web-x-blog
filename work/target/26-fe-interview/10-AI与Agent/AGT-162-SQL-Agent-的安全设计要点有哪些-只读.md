---
title: [AGT-162] SQL Agent 的安全设计要点有哪些（只读/白名单/限额）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-162：SQL Agent 的安全设计要点有哪些（只读/白名单/限额）？
**答**：
- 数据库层防线是第一优先：独立只读账号（仅 SELECT 权限）、连接级 `statement_timeout`、查询结果行数与字节双限额——模型再失控也改不了库、拖不垮库。
- 模型层防线：Text2SQL 的输入仅提供白名单表的 schema 摘要（列名+注释+样例行），禁止 `SHOW TABLES` 全量暴露；生成的 SQL 必须过静态校验器——只允许 SELECT、禁止多语句、禁止注释截断、LIMIT 强制注入。
- 执行分级：探索性查询（EXPLAIN/小样本）自动执行，聚合大查询走预估行数判断，超过阈值要求用户确认或自动加时间范围约束。
- 溯源与审计：每次查询记录「问题→SQL→行数→耗时」，回答附上 SQL 让用户可自查，错误结果可回溯到具体语句。

```typescript
// SQL Agent 安全执行层：静态校验 + 只读执行 + 双限额
import { z } from 'zod';

export function validateSql(sql: string): { ok: boolean; reason?: string } {
  const s = sql.trim().replace(/;+\s*$/, '');
  if (/;/.test(s)) return { ok: false, reason: '禁止多语句' };
  if (!/^select\s/i.test(s) && !/^with\s[\s\S]+select\s/i.test(s)) return { ok: false, reason: '仅允许 SELECT/WITH 查询' };
  if (/\b(insert|update|delete|drop|alter|truncate|grant|create)\b/i.test(s)) return { ok: false, reason: '包含被禁止的关键字' };
  if (/(--|#|\/\*)/.test(s)) return { ok: false, reason: '禁止注释符（防注释截断注入）' };
  if (!/\blimit\s+\d+/i.test(s)) return { ok: true, reason: 'LIMIT 缺失' }; // 标记需注入
  return { ok: true };
}

export async function safeQuery(userQuestion: string, generatedSql: string) {
  const v = validateSql(generatedSql);
  if (v.ok === false) throw new Error(`SQL 校验失败：${v.reason}`);
  const finalSql = v.reason === 'LIMIT 缺失' ? `${generatedSql.replace(/;+\s*$/, '')} LIMIT 100` : generatedSql;

  const result = await pool.query({
    text: `SET LOCAL statement_timeout = '10s'; ${finalSql}`,   // 连接级超时
    rowMode: 'array',
  });
  if (result.rows.length > 1000) throw new Error('结果超限，请缩小查询范围'); // 行数限额
  audit({ question: userQuestion, sql: finalSql, rows: result.rows.length }); // 全量审计
  return result.rows.slice(0, 100);
}

// Schema 注入模板：只给白名单表与脱敏样例
export function schemaPrompt(allowedTables: string[], schema: Record<string, any>): string {
  const tables = allowedTables.map((t) => {
    const cols = schema[t].columns.map((c: any) => `${c.name}（${c.comment ?? c.type}）`).join(', ');
    return `表 ${t}：${cols}。样例行：${JSON.stringify(schema[t].samples[0] ?? {})}`;
  }).join('\n');
  return `可用表如下，禁止使用其他表：\n${tables}\n生成 PostgreSQL 只读查询。`;
}
const pool = { query: async (x: any) => ({ rows: [] as any[] }) };
const audit = (x: unknown) => { void x; };
```
