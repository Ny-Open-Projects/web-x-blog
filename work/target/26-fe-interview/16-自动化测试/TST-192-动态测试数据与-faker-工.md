---
title: [TST-192] 测试数据怎么生成？faker、fixture 工厂与「数据真实性」的平衡
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-192：测试数据怎么生成？faker、fixture 工厂与「数据真实性」的平衡
**答**：
- 三层数据策略：① fixture 工厂（核心）——`makeUser(overrides)` 合成默认合法对象 + 局部覆写，测试只声明「与被测行为相关的字段」，无关字段用合理默认值（factory-builder 模式，见 TST-049）；② faker 动态生成——`faker.person.fullName()` 造「看起来真实」的多样化数据，用于格式化/截断/排序类测试；③ 真实脱敏数据——排查线上问题时导出的快照，作为回归基线（最有价值也最难造）。
- 真实性 vs 确定性的权衡：随机数据提高输入多样性但降低可复现性——解法是 seeded faker（固定 seed，见 TST-152）：同一次运行数据多样且可重放。
- 关键纪律：与断言相关的数据必须显式写在用例里（`makeOrder({ status: 'paid' })`），不允许「随机生成然后碰巧断言」；无关数据才交给工厂默认值——否则测试失败原因不可读。
- 边界数据显式化：超长字符串、emoji、空数组、最大值——这些「设计上就该被测」的输入写成共享常量（`EDGE_CASES`），别藏在随机里。
- 追问钩子：mock 数据与真实接口结构漂移怎么办？——工厂类型绑定接口类型（`satisfies GoodsResp`），接口改字段工厂编译报错，第一时间暴露。

```javascript
// fixture 工厂 + faker 混合
import { faker } from '@faker-js/faker';
faker.seed(42);                          // 固定种子：多样且可复现

export const makeOrder = (overrides = {}) => ({
  id: faker.string.uuid(),
  buyer: faker.person.fullName(),
  items: [makeItem()],
  status: 'pending',
  createdAt: '2026-11-01T10:00:00Z',     // 相关键固定，无关键默认
  ...overrides,                          // 测试关心的键显式覆写
});

// 用例：只声明相关字段
test('已支付订单显示发货按钮', () => {
  const order = makeOrder({ status: 'paid' });       // 相关：status
  render(<OrderCard order={order} />);
  expect(screen.getByRole('button', { name: '发货' })).toBeInTheDocument();
});

// 共享边界数据
export const EDGE_CASES = {
  empty: [], maxLength: '长'.repeat(1000), emoji: '🛒🎉', zero: 0,
};
```
