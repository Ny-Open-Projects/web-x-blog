---
title: [TST-874] 笔试：手写一个「AI 测试 prompt 的效果回归测试」（prompt 变更前后对比）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-874：笔试：手写一个「AI 测试 prompt 的效果回归测试」（prompt 变更前后对比）
**答**：
- 需求：实现 promptRegression(cases, oldFn, newFn) —— 对每个 case 分别用旧/新 prompt 函数生成结果，对比是否退化。
- 规则：结果用 judge 函数打分（0-1）；新版本平均分低于旧版本 0.05 以上判为 regression，列出退化 case。
- 边界：cases 为空返回无回归；单次 judge 异常按 0 计；返回平均分与退化明细。

```javascript
function promptRegression(cases, oldFn, newFn, judge) {
  if (!cases.length) return { regression: false, avgOld: 0, avgNew: 0, degraded: [] };
  const safeJudge = (out) => { try { return judge(out); } catch { return 0; } };
  let sumOld = 0, sumNew = 0;
  const degraded = [];
  for (const c of cases) {
    const o = safeJudge(oldFn(c)), n = safeJudge(newFn(c));
    sumOld += o; sumNew += n;
    if (n < o - 0.05) degraded.push({ case: c.id, old: o, new: n });
  }
  const avgOld = sumOld / cases.length, avgNew = sumNew / cases.length;
  return {
    regression: avgNew < avgOld - 0.05,
    avgOld: Number(avgOld.toFixed(3)), avgNew: Number(avgNew.toFixed(3)),
    degraded,
  };
}
const cases = [{ id: 1, input: 'formatMoney' }, { id: 2, input: 'sum' }];
console.log(promptRegression(cases,
  c => `old:${c.input}`, c => `new:${c.input}`,
  s => s.includes('toBe') ? 1 : 0.4)); // 对比两版 prompt 生成质量
```
**评分点**：
- 对同一批 case 跑新旧版本并 judge 打分，对比设计正确。
- 退化阈值（0.05）判定 + 明细列出，可定位是哪些 case 退化。
- judge 异常按 0 计、空 cases 兜底，边界健壮。
- 能点出「prompt 变更必须跑回归，否则可能悄悄变差」这一工程化核心。
