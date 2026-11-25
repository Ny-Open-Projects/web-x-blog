---
title: [950] 笔试手写：实现 N/N+1 补偿金计算器
date: 2026-11-17
categories: [软技能与求职]
tags: [前端面试, 面试题, 裁员谈判]
type: 面试题
---

## 950：笔试手写：实现 N/N+1 补偿金计算器

**答**：实现 severance({ monthlyAvg, workYears, months, base })：工作年限 workYears 满 1 年计 1 个月，满 6 个月不满 1 年计 0.5，不满 6 个月计 0——N = floor(workYears) 按规则累计；月工资基数取「离职前 12 个月平均应发工资」monthlyAvg，高于当地社平 3 倍则按 3 倍封顶且年限最多 12 年。实现函数返回 { n, capped, amount }；再算 N+1（额外 +1 个月代通知金，不封顶限制）。

```js
function severance({ monthlyAvg, workYears, cap3x = Infinity }) {
  const base = Math.min(monthlyAvg, cap3x);          // 3 倍社平封顶
  let years = 0;
  const whole = Math.floor(workYears);
  const frac = workYears - whole;
  years = Math.min(whole, 12);                        // 封顶后年限最多 12 年
  if (frac >= 0.5) years += 0.5;                      // 满 6 个月 +0.5
  const n = years;
  return { n, capped: monthlyAvg > cap3x || whole > 12,
    amount: +(n * base).toFixed(2) };
}
// N+1：代通知金按上月工资，不参与封顶
function severanceN1(x, noticePay) {
  const s = severance(x);
  return { ...s, n1Amount: +(s.amount + noticePay).toFixed(2) };
}
console.log(severance({ monthlyAvg: 40000, workYears: 3.6, cap3x: 30000 }));
// { n: 3.5, capped: true, amount: 105000 }  (3年+0.5年=3.5, 按3万封顶)
console.log(severanceN1({ monthlyAvg: 20000, workYears: 2, cap3x: 30000 }, 20000));
// { n: 2, capped: false, amount: 40000, n1Amount: 60000 }
```

**评分点**：
- 年限折算规则正确（满6月+0.5、不满6月为0）
- 双封顶逻辑：基数封顶 3 倍社平 + 年限封顶 12 年，且封顶联动（capped 标记）
- N+1 的代通知金不参与封顶（常见混淆点）
- 能讨论：金额应以「应发工资」含奖金津贴计、协商高于法定是谈判空间而非违法

