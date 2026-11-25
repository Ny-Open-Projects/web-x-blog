---
title: [TST-975] 不是所有 AI 用例都值得信任——如何给它们做可靠性分级并区别使用？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-975：不是所有 AI 用例都值得信任——如何给它们做可靠性分级并区别使用？
**答**：
- 结论：分 L1~L4——L1 直接进阻塞门禁，L2 进普通门禁，L3 仅建议级，L4 隔离观察；级别由 flake 率、断言有效率、存活率综合判定。
- 动态升降级：连续 4 周稳定可升级；一旦 flake 或误报立即降级。
- 价值：既用好 AI 的覆盖广度，又不让不可信用例污染门禁信号。
- 追问钩子：一个 L3 用例连续 4 周零 flake，但从未检出过缺陷，能升级到 L1 吗？

```javascript
function gradeAIUseCase({ flakeRate, validity, survival, bugsFound }) {
  let level = 4;
  if (flakeRate <= 0.01 && validity >= 0.95 && survival >= 0.9 && bugsFound > 0) level = 1;
  else if (flakeRate <= 0.02 && validity >= 0.9 && survival >= 0.85) level = 2;
  else if (flakeRate <= 0.05 && validity >= 0.8) level = 3;
  return { level, policy: ['阻塞门禁','普通门禁','建议级','隔离观察'][level - 1] };
}
console.log(gradeAIUseCase({ flakeRate: 0.0, validity: 1, survival: 0.95, bugsFound: 0 }));
// { level:4, policy:'隔离观察' } — 稳定但零检出，不升 L1（故问题答案为「不能」）
```
