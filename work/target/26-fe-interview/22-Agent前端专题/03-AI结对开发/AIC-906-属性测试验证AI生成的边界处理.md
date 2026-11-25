---
title: [AIC-906] AI 生成的商品库存扣减函数，如何用「属性测试」发现它漏掉的边界，而不是靠举几个例子？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-906：AI 生成的商品库存扣减函数，如何用「属性测试」发现它漏掉的边界，而不是靠举几个例子？
**答**：
- 属性测试的思想是验证「不变量」而非穷举用例：定义对任意输入都应成立的性质（如扣减后库存 ≥0、扣减量 ≤ 当前库存），让工具自动生成上千组输入。
- 对 AI 代码尤其有效，因为 AI 常漏边界（负数、超卖、并发），属性测试用随机输入把它「逼」出来。
- 一旦发现反例要「缩小」（shrink）：把失败的复杂输入简化为最小复现，便于定位与反馈给 AI 修复。
- 追问钩子：能区分「基于例子的测试」与「基于性质的测试」，并说出性质比例子更能覆盖未知边界的候选人，测试思维更成熟。

```typescript
// 简易属性测试：随机生成输入验证不变量
function checkProperties(fn, trials = 1000) {
  for (let i = 0; i < trials; i++) {
    const stock = Math.floor(Math.random() * 1000);
    const n = Math.floor(Math.random() * 1000) - 50; // 含负数
    const after = fn(stock, n);
    const invariant = after >= 0 && after <= stock &&
      (n < 0 ? after === stock : after === stock - Math.min(n, stock));
    if (!invariant) return { pass:false, counterexample:{ stock, n, after } };
  }
  return { pass:true };
}
// 让 AI 生成的扣减函数
const deduct = (stock, n) => Math.max(0, stock - n);
console.log(checkProperties(deduct)); // 负数 n 时 after>stock，反例被抓出
```
