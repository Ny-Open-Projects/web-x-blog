---
title: [TST-679] prompt 本身怎么测试（模型升级导致的漂移）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-679：prompt 本身怎么测试（模型升级导致的漂移）？

**答**：
- 结论：把 prompt 当代码——建 golden 数据集（输入→期望输出），每次改 prompt 或换模型都跑回归。
- 测试维度：格式合规、关键字段正确、边界输入不崩、成本与延迟预算。
- 模型版本锁定，升级先在影子流量对比，指标达标再切换。
- 追问钩子：同一 prompt 不同 temperature 结果差异大，你怎么稳定输出？

```javascript
function evaluatePrompt(prompt, cases, callModel) {
  return Promise.all(cases.map(async c => {
    const out = await callModel(prompt, c.input);
    return {
      id: c.id,
      formatOk: c.schema.every(k => k in out),
      exact: JSON.stringify(out) === JSON.stringify(c.expected),
    };
  })).then(rows => ({
    passRate: rows.filter(r => r.exact).length / rows.length,
    formatRate: rows.filter(r => r.formatOk).length / rows.length,
  }));
}
```
