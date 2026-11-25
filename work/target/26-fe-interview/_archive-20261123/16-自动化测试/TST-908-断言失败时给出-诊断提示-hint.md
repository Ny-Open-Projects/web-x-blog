---
title: [TST-908] 断言失败时给出「诊断提示」（hint）的价值如何量化？怎样的 hint 才算好？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-908：断言失败时给出「诊断提示」（hint）的价值如何量化？怎样的 hint 才算好？
**答**：
- 结论：好 hint 把「什么错了」推进到「多半因为什么、下一步查哪」，能缩短平均定位时间(MTTD)。
- 量化：对比加 hint 前后的 MTTD、同一失败重复排查次数、新人独立定位成功率。
- 写法：hint 要基于失败特征触发（如金额差恰好 1 分→提示币种单位；字段全 null→提示接口未联调）。
- 追问钩子：你怎么证明加 hint 不是「自嗨」——怎么设计对照实验说明它真降低了定位成本？

```javascript
function withHint(failure) {
  const hints = [];
  if (failure.diff === 1) hints.push('差额恰为最小单位：检查元/分换算或 Math.round 丢失精度');
  if (/null|undefined/.test(failure.actual)) hints.push('实际值为空：确认接口是否返回该字段、mock 是否过期');
  if (failure.path.includes('time')) hints.push('时间字段：确认测试机与服务时区一致（UTC vs UTC+8）');
  return { ...failure, hints: hints.length ? hints : ['无匹配规则，转人工排查'] };
}
const f = withHint({ path: 'price', expected: 9900, actual: 9901, diff: 1 });
console.log(f.hints); // ['差额恰为最小单位：检查元/分换算…']
```
