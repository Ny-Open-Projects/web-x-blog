---
title: [AIC-745] 如何用差分测试验证 AI 重构的正确性
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-745：如何用差分测试验证 AI 重构的正确性

**答**：
- 结论先行：差分测试 = 让「重构前」和「重构后」两个版本对同一批输入产生相同输出，用行为等价性替代逐行审查——特别适合 AI 发起的大范围重构，人不可能逐行看完。
- 做法：1) 保留旧实现的引用（golden）；2) 构造覆盖边界的输入集；3) 同时跑新旧版本对比输出；4) 任何差异都要有解释（是预期行为改变还是 bug）。
- 难点：引入随机性/时间/外部状态的模块难直接对比，要注入确定性时钟和 mock。
- 追问钩子：差分测试能通过是否等于重构正确？——不等于，输入集若不覆盖关键路径，差异就发现不了；覆盖率决定差分的可信度。

```javascript
// 差分测试：新旧实现同输入比对
function diffTest(oldFn, newFn, inputs) {
  const diffs = [];
  for (const input of inputs) {
    const a = oldFn(input), b = newFn(input);
    if (JSON.stringify(a) !== JSON.stringify(b)) diffs.push({ input, old: a, new: b });
  }
  return { passed: diffs.length === 0, diffs, coverage: inputs.length };
}
const oldCalc = x => x * 2;                       // 重构前
const newCalc = x => x + x;                       // 重构后（等价）
console.log(diffTest(oldCalc, newCalc, [0, 1, 5, -3]).passed); // true
const buggy = x => x * 2 + (x > 10 ? 1 : 0);      // 引入边界 bug
console.log(diffTest(oldCalc, buggy, [1, 20]).diffs.length);   // 1
```
