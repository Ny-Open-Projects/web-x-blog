---
title: [AIC-206] 规则文件太多导致上下文爆掉，怎么管理 rules 的 token 预算？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-206：规则文件太多导致上下文爆掉，怎么管理 rules 的 token 预算？
**答**：
- 给规则定预算：always 层 < 2k tokens，全部命中规则总和 < 8k tokens（约模型窗口 10%）。
- 规则瘦身三板斧：删重复（引用代替复制）、压缩措辞（要点式）、降层级（长规范拆到 glob 层按需注入）。
- 监控每次请求实际注入的规则 token 数，超预算告警。
- 价值密度评估：每条规则记录「命中后违规率变化」，低价值的降级或删除。

```javascript
function ruleBudget(rules: Array<{ name: string; body: string }>, max = 8000) {
  const cost = rules.map(r => ({ name: r.name, tk: Math.ceil(r.body.length / 3) }));
  const total = cost.reduce((s, c) => s + c.tk, 0);
  if (total > max) {
    // 超预算：按 token 降序输出裁剪建议
    return { over: true, cut: cost.sort((a, b) => b.tk - a.tk).slice(0, 3) };
  }
  return { over: false, total };
}
r
```
