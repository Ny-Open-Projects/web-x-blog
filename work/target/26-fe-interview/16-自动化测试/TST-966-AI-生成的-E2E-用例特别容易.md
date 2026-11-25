---
title: [TST-966] AI 生成的 E2E 用例特别容易 flaky，怎么量化它的「flake 率」并设门禁？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-966：AI 生成的 E2E 用例特别容易 flaky，怎么量化它的「flake 率」并设门禁？
**答**：
- 结论：flake 率 = 同一 commit 重复运行 N 次中「结果不一致」的比例，必须隔离网络/时间等外部噪声后测量，否则测的是环境不是 AI。
- 做法：对 AI 用例在固定环境下重复 10 次，统计通过/失败波动；flake 率 >5% 的用例自动打回或降级为「建议」。
- 归因：AI 常见 flaky 源于硬编码等待、脆弱 selector、依赖真实数据。
- 追问钩子：AI 用例 flake 率 8%，但你怀疑是测试环境不稳而非用例本身，怎么设计实验区分？

```javascript
function measureFlakeRate(results) { // results: true/false 数组
  if (results.length < 2) return 0;
  const pass = results.filter(Boolean).length;
  const flaky = pass > 0 && pass < results.length;
  return +(flaky ? 1 - Math.max(pass, results.length - pass) / results.length : 0).toFixed(2);
}
// 更稳健：多次重复中「结果不一致」的比例
function flakeRatio(runs) { // runs: [batch1, batch2, ...]，每批是布尔数组
  if (!runs.length) return 0;
  const inconsistent = runs.filter(r => new Set(r).size > 1).length;
  return +(inconsistent / runs.length).toFixed(2);
}
console.log(measureFlakeRate([true, true, false, true])); // 0.25（1/4 失败）
console.log(flakeRatio([[true,true],[true,false],[true,true]])); // 0.33
// 门禁：flakeRatio > 0.05 → 打回 AI 用例
```
