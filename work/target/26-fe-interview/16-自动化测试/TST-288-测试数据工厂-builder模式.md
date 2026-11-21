---
title: [TST-288] 测试数据工厂的 builder 模式如何设计？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-288：测试数据工厂的 builder 模式如何设计？
**答**：
- 链式 builder：GoodsBuilder.aGoods().withPrice(100).inPromotion().build()——默认值合法，只显式覆盖关心的字段。
- 默认值策略：合理默认 + 关键字段唯一（sku 带序号）避免用例间耦合。
- 变体工厂：预设变体（aSeckillGoods/aOutOfStockGoods）封装常用组合，减少用例样板。
- 工厂与 schema 同源：类型从 API schema 生成，防止工厂字段过期。

```javascript
export class GoodsBuilder {
  private v: Partial<Goods> = { sku: `SKU-${seq++}`, price: 100, status: 'online' };
  withPrice(p: number) { this.v.price = p; return this; }
  soldOut() { this.v.status = 'soldout'; return this; }
  build(): Goods { return { ...defaults, ...this.v }; }
}
// 用例：GoodsBuilder.aGoods().withPrice(0.01).build()
r
```
