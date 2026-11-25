---
title: [TST-911] 自定义 matcher 的命名如何成为「活的文档」从而提升断言可诊断性？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-911：自定义 matcher 的命名如何成为「活的文档」从而提升断言可诊断性？
**答**：
- 结论：matcher 名应表达「业务语义 + 比较关系」，如 toBeSettledWithin(2)、toHaveStockAbove(0)，读失败日志的人不用看实现就懂规则。
- 命名三段式：主语（toBe/toHave）+ 业务量（Coupon/Stock）+ 关系（Within/Above/Equal），单位写进名字或消息。
- 反模式：toOK、toRight 这类玩家私有缩写，失败时只有作者看得懂。
- 追问钩子：团队里出现 20 个自定义 matcher，你怎么防止它们变成另一种「方言」反而增加理解成本？

```javascript
// 好的命名：业务语义 + 比较关系 + 单位线索
expect(order.priceCents).toBeWithinCents(expected, 1);
expect(sku.stock).toHaveStockAbove(0);
expect(ship.deadline).toBeSettledWithinHours(24);

expect.extend({
  toBeWithinCents(received, expected, tolerance = 1) {
    const pass = Math.abs(received - expected) <= tolerance;
    return { pass, message: () => pass ? '金额在容差内' :
      `金额(分)超出容差：期望 ${expected}±${tolerance}，实际 ${received}` };
  },
  toHaveStockAbove(received, min) {
    return { pass: received > min, message: () =>
      `库存需 > ${min}，实际 ${received}（${received <= 0 ? '已售罄' : '不足'}）` };
  },
});
```
