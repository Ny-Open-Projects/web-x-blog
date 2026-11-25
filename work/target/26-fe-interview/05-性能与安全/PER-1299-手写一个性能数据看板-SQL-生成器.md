---
title: [PER-1299] 手写一个"性能数据看板 SQL 生成器"（防注入参数化）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1299：手写一个"性能数据看板 SQL 生成器"（防注入参数化）

**答**：
- 需求：implement boardQuery(params)。params 为 { page, metric, from, to, quantile }；白名单校验 metric ∈ {lcp, inp, cls}、quantile ∈ [0.5, 0.75, 0.9, 0.95]；page/from/to 参数化（$1 占位）；输出 { sql, params }；非法 metric/quantile 抛错。
- 边界：page 必填；时间默认最近 7 天；sql 只聚合不扫明细；quantile 格式化两位小数。
- 评分点：白名单校验；参数化；默认时间窗；聚合下推

```javascript
function boardQuery(params, now = Date.now()) {
  const METRICS = ['lcp', 'inp', 'cls'];
  const QS = [0.5, 0.75, 0.9, 0.95];
  if (!METRICS.includes(params.metric))
    throw new Error(`非法指标 ${params.metric}`);
  if (!QS.includes(params.quantile))
    throw new Error(`非法分位 ${params.quantile}`);
  if (!params.page) throw new Error('page 必填');
  const from = params.from ?? now - 7 * 86400_000;
  const to = params.to ?? now;
  return {
    sql: `SELECT toDate(ts) d, quantile(${params.quantile.toFixed(2)})(${params.metric}) v, count() n
          FROM perf WHERE page = $1 AND ts BETWEEN $2 AND $3
          GROUP BY d ORDER BY d`,
    params: [params.page, from, to],
  };
}
// 白名单指标防注入，参数化时间防拼接注入；
```

## 补充：评分点与变体

**评分点**：

- 值全部走参数化占位符，不拼接用户输入。
- 标识符（表名、列名）走白名单映射，不能参数化的位置单独校验。
- 时间范围与分页有上限，防全表扫描。
- 生成的 SQL 可打印可复现，便于审计。

**变体与延伸**：

1. 为什么标识符不能参数化？ → 预编译只支持值占位，标识符必须靠白名单。
2. 怎么验证真的防住注入？ → 单测喂恶意串，断言生成 SQL 不含该串且参数值原样绑定。
3. 多条件筛选怎么拼？ → 统一收集 condition 数组再 join，避免分支里手写字符串。
