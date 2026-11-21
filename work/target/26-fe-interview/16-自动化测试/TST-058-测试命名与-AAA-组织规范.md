---
title: [TST-058] 单测的命名规范与 AAA 组织结构怎么定？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-058：单测的命名规范与 AAA 组织结构怎么定？
**答**：
- 命名：it 用「条件 → 期望结果」的完整句子（“输入已过期的 token 时返回 401 错误码”）；describe 按被测单元/场景分层；禁止 `test1`、`测试正常情况` 这类无信息名。
- AAA 结构：Arrange（准备数据与依赖）→ Act（执行被测动作）→ Assert（断言结果），一条 it 只走一轮 AAA、断言一个行为焦点。
- 可读性细节：Act 语句单独一行且显眼（很多团队注释 // act）；断言里不用魔法值，期望值用字面量写出（toBe(180) 而不是 toBe(expected) 变量回填）；Arrange 里的 mock 设置与用例无关的部分放 beforeEach。
- 失败可读性：命名 + 断言信息要能让人不看被测代码就知道哪坏了；expect(x).toBe(y) 优于 if(!x) throw。
- 追问钩子：命名即文档——好的测试文件读下来就是被测模块的「行为说明书」，这也是评审测试 PR 的核心标准。

```javascript
describe('CouponService.apply', () => {
  // Arrange 公共部分上提
  const makeCoupon = (type, value) => ({ type, value, active: true });

  it('满减券在订单金额达到门槛时扣减固定金额', async () => {  // 条件 → 结果
    // arrange
    const cart = makeCart([{ price: 300, qty: 1 }]);
    // act
    const result = applyCoupon(cart, makeCoupon('FULLCUT', 50));
    // assert
    expect(result.total).toBe(250);       // 期望值字面量，失败一眼看出
  });

  it('未达到满减门槛时返回门槛不足错误且金额不变', async () => {
    const cart = makeCart([{ price: 30, qty: 1 }]);
    const result = applyCoupon(cart, makeCoupon('FULLCUT', 50));
    expect(result.error).toBe('THRESHOLD_NOT_MET');
    expect(result.total).toBe(30);
  });
});
```
