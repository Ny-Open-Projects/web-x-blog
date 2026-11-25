---
title: [TST-905] 断言消息里的「期望 vs 实际」怎样写才可读？金额/时间/枚举各有何讲究？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-905：断言消息里的「期望 vs 实际」怎样写才可读？金额/时间/枚举各有何讲究？
**答**：
- 结论：期望与实际要「同类型、同单位、带业务含义」——金额统一到分并标注单位，时间统一到 ISO，枚举打印名字而非数字。
- 金额：禁止浮点直接比，用整数分；失败信息写「期望 99.00 元 / 实际 99.01 元（差 1 分）」。
- 时间：带时区，避免 UTC 与本地时间混用造成的假失败；用同一时钟源。
- 追问钩子：断言「优惠券在 23:59:59 过期」，测试机在 UTC、服务在 UTC+8，失败信息怎么写才能暴露是时区问题而不是券本身错了？

```javascript
function yuan(cents) { return `${(cents / 100).toFixed(2)} 元`; }
function assertPrice(receivedCents, expectedCents) {
  if (receivedCents !== expectedCents) {
    const diff = receivedCents - expectedCents;
    throw new Error(
      `价格断言失败：期望 ${yuan(expectedCents)}，实际 ${yuan(receivedCents)}，` +
      `差额 ${diff > 0 ? '+' : ''}${yuan(Math.abs(diff))}`
    );
  }
}
function assertISO(received, expected) {
  const r = new Date(received).toISOString(), e = new Date(expected).toISOString();
  if (r !== e) throw new Error(`时间断言失败：期望 ${e}(UTC)，实际 ${r}(UTC)`);
}
assertPrice(9901, 9900); // 差额 +0.01 元（+1 分）
assertISO('2026-11-23T15:59:59Z', '2026-11-23T15:59:59+08:00');
```
