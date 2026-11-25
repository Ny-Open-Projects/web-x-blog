---
title: [TST-479] 笔试：AI 生成测试的入库闸门（三检）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-479：笔试：AI 生成测试的入库闸门（三检）。
**题目**：三检：① 真实执行通过 ② 断言期望值可追溯（含 source 标记）③ 变异抽检会红（注入已知 bug）。实现 `admitGate(candidate, deps)` 输出 `{admit, reasons}`。

```javascript
async function admitGate(c, { run, verifyTraceable, mutateCheck }) {
  const reasons = [];
  const r = await run(c.code);
  if (!r.passed) reasons.push(`执行未通过: ${r.error?.slice(0, 80)}`);
  if (!verifyTraceable(c.assertions)) reasons.push('断言期望值不可追溯（缺 source）');
  if (!mutateCheck(c.code)) reasons.push('变异抽检未红（断言力不足）');
  return { admit: reasons.length === 0, reasons };
}

```

**评分点**：
- 三检顺序执行且全过才 admit。
- traceability 缺 source 直接拒（不可追溯）。
- 变异抽检失败（测试没红）拒——假测试。
- reasons 汇总全部失败检（不只第一个）。
