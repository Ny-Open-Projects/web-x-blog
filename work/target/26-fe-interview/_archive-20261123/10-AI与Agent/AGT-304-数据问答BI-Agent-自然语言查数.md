---
title: [AGT-304] 数据问答 Agent——自然语言查数（ChatBI）怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-304："上月华东 GMV 环比多少"这类数据问答 Agent 怎么做？

**答**:
- 管线：语义解析（问题→指标/维度/时间/过滤的结构化 DSL）→ SQL 生成（带 schema 上下文：表结构/指标口径/枚举值——口径字典是准确率关键）→ 执行（只读账号+行级权限+超时熔断）→ 呈现（数字+图表+SQL 透明可查）。
- 口径治理：业务指标口径（GMV 含不含退款）存指标字典并注入 prompt——口径错是 ChatBI 最大的事故源；同一指标不同部门口径冲突时显式列出选项让用户选。
- 防幻觉：数字全部来自查询引擎（AGT-267 数值治理），SQL 对用户透明可展开（可审计），结果带"口径说明+时间戳"；模糊问题（"最近表现怎么样"）触发澄清而非瞎猜维度。
- 评测：SQL 执行成功率、结果正确率（金标数据集）、澄清触发恰当率——ChatBI 用"能对上财务报表"的金标集做回归。

```javascript
async function chatBI(q, user) {
  const dims = await llm(`解析为 {metric, dim, time, filter}`,
    { q, metricDict: METRICS, schema: SCHEMA });
  if (dims.ambiguous) return clarify(dims.options);   // 口径/维度澄清
  const sql = await genSQL(dims, { readOnly: true,
    acl: rowACL(user) });                              // 行级权限
  const rows = await engine.run(sql, { timeout: 5e3 });
  return { answer: fmt(rows), sql, caliber: dims.metric.caliber };
}
```
