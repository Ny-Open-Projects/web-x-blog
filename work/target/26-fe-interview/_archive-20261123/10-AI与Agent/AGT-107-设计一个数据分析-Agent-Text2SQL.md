---
title: [AGT-107] 设计一个数据分析 Agent（Text2SQL + 图表渲染全链路）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-107：设计一个数据分析 Agent（Text2SQL + 图表渲染全链路）？
**答**：
- 链路：自然语言 → 生成分析方案（SQL + 图表 intent + 初步结论）→ 校验执行 → 真实结果回传修正结论 → 前端渲染图表。
- 安全红线：只允许 SELECT（正则白名单 + 只读数据库账号）、强制 LIMIT、禁 DDL/DML；表结构与字段注释进 prompt（schema link 是 Text2SQL 准确率关键）。
- 图表不指定死：模型输出 chart intent（类型/维度/度量），前端映射成 ECharts option——渲染职责在前端。
- 防编数字：结论必须基于回传的真实查询结果生成；SQL 报错把数据库错误信息回传重试一轮。

```typescript
import { z } from 'zod';

// Text2SQL + 图表渲染
const DB_SCHEMA = `
orders(id, user_id, amount, status, created_at) -- 订单表 status 取值 paid 或 refunded
users(id, name, region) -- 用户表`;

const AnalysisSchema = z.object({
  sql: z.string()
    .regex(/^\s*select/i)
    .refine((s) => !/\b(drop|delete|update|insert|alter|truncate)\b/i.test(s), '只允许 SELECT'),
  chart: z.object({ type: z.enum(['bar', 'line', 'pie']), xField: z.string(), yField: z.string(), title: z.string() }),
  conclusion: z.string(),
});

export async function analyzeQuestion(question: string, retrySql?: string, dbErr?: string) {
  const plan = await structuredLLM(
    [{
      role: 'user',
      content: `根据表结构生成分析方案。SQL 必须加 LIMIT 1000。
${retrySql ? `上一次 SQL 执行报错：${dbErr}，请修正这条 SQL：${retrySql}` : ''}
${DB_SCHEMA}
问题：${question}`,
    }],
    AnalysisSchema,
  );
  try {
    const rows = await readonlyDB.query(plan.sql);          // 只读账号执行
    // 真实结果回传修正结论，防止编数字
    const { conclusion } = await structuredLLM(
      [{
        role: 'user',
        content: `基于真实查询结果修正结论：
SQL：${plan.sql}
结果前 5 行：${JSON.stringify(rows.slice(0, 5))}
原结论：${plan.conclusion}`,
      }],
      z.object({ conclusion: z.string() }),
    );
    return { conclusion, sql: plan.sql, chartOption: toEchartsOption(plan.chart, rows) };
  } catch (e) {
    if (!retrySql) return analyzeQuestion(question, plan.sql, String(e)); // 报错回传重试一轮
    throw e;
  }
}

function toEchartsOption(c: z.infer<typeof AnalysisSchema>['chart'], rows: Record<string, unknown>[]) {
  return {
    title: { text: c.title },
    xAxis: { type: 'category', data: rows.map((r) => r[c.xField]) },
    yAxis: { type: 'value' },
    series: [{ type: c.type, data: rows.map((r) => r[c.yField]) }],
  };
}
```
