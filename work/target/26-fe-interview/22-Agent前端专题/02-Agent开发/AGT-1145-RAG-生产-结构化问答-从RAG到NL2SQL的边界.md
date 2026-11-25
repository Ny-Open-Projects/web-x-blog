---
title: [1145] 「查今年 Q3 华东区销售额」这类问题该走 RAG 还是 NL2SQL
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, NL2SQL]
type: 面试题
---

## 1145：「查今年 Q3 华东区销售额」这类问题该走 RAG 还是 NL2SQL

**答**：
- 边界判断：问题问「事实在文档里」→ RAG；问「数据在库里」→ NL2SQL（文本转 SQL 查数仓）；两者混着来是事故源（让 RAG 检索「销售额」会命中旧报表文档给出过时数字）。
- 意图路由层：识别「查数」意图（时间+指标+维度的结构）路由到 NL2SQL，识别「知识」意图走 RAG；路由错误率要进评估。
- NL2SQL 的安全边界：只读账号 + 生成的 SQL 过审查（禁 DML/DDL、强制 LIMIT、表白名单），结果异常（行数爆炸）熔断。
- 追问钩子：NL2SQL 答数错了比 RAG 严重得多（看起来权威），怎么治理？——数字类回答必须附「SQL + 执行时间」溯源，且关键指标走「预定义指标口径」而非自由生成 SQL。

```ts
function route(q) {
  if (/销售额|订单数|同比|Q[1-4]/.test(q) && hasMetricStructure(q)) return nl2sql(q);
  return rag(q);
}
async function nl2sql(q) {
  const sql = await llm(nl2sqlPrompt(q, schemaDigest));
  const checked = sqlGuard(sql, { readOnly: true, tables: WHITELIST, forceLimit: 100 });
  const rows = await dw.query(checked);
  return cite(q, rows, { sql: checked, at: new Date() });   // 数字必须可溯源
}
```
