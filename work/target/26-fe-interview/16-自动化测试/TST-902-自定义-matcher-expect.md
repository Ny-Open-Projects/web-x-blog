---
title: [TST-902] 自定义 matcher（expect.extend）如何设计失败的 diff 展示才不误导？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-902：自定义 matcher（expect.extend）如何设计失败的 diff 展示才不误导？
**答**：
- 结论：自定义 matcher 的失败消息要「自解释」——写清比较语义（相等？包含？近似？）和容差，而不是复用通用 toBe 的措辞。
- 实现要点：matcher 返回 { pass, message }，message 用 this.utils.printExpected/printReceived 保持 Jest 风格颜色与格式化。
- 反模式：把对象 JSON.stringify 后比字符串——键序不同会假失败，且 diff 不可读。
- 追问钩子：你写了个 toBeCloseToPrice（金额分单位，容差 1 分），失败时怎样让新人一眼看懂是「超容差 1 分」而不是「两数不等」？

```javascript
expect.extend({
  toBeCloseToPrice(received, expected, tolerance = 1) {
    const pass = Math.abs(received - expected) <= tolerance;
    const hint = pass ? '金额在容差内' :
      `超出容差：差额=${Math.abs(received - expected)}分 > 允许=${tolerance}分`;
    return {
      pass,
      message: () => this.utils.matcherHint('toBeCloseToPrice') +
        `\n期望(分): ${this.utils.printExpected(expected)}\n` +
        `实际(分): ${this.utils.printReceived(received)}\n${hint}`,
    };
  },
});
expect(9901).toBeCloseToPrice(9900, 1); // pass
// expect(9905).toBeCloseToPrice(9900,1) 明确提示「差额5分 > 允许1分」
```
