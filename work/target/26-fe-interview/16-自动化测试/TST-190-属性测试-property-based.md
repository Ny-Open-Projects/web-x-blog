---
title: [TST-190] 属性测试（property-based testing）是什么？fast-check 在前端怎么用？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-190：属性测试（property-based testing）是什么？fast-check 在前端怎么用？
**答**：
- 定义：示例测试写「输入 A 期望 B」，属性测试写「对所有满足 X 的输入，性质 P 必须成立」——框架自动生成成百上千组随机输入（可缩到最小失败用例），专找你没想到的边界（空串、超长、负零、Unicode、NaN）。工具：fast-check（支持 Vitest/Jest）。
- 常用属性模式：① 往返不变性 `decode(encode(x)) === x`（序列化/加密/压缩）；② 不变式（排序后元素集合不变、金额计算结果 ≥ 0）；③ 幂等性 `f(f(x)) === f(x)`（规范化函数）；④ 对照实现（简单实现 vs 优化实现结果一致）；⑤ 元性质（shuffle 不改元素、长度不变）。
- 前端适用场景：工具库（日期解析、金额计算、diff/树操作）、状态更新函数、表单校验器。不适合：依赖环境/时间的 UI 交互（生成不了有意义属性）。
- 工程化：不进 PR 门禁（运行时间长），每夜跑或发布前跑；`fc.configureGlobal({ numRuns: 100 })` 控制规模；发现的最小失败用例固化为常规示例测试（防回归）。
- 追问钩子：和 test.each 参数化什么区别？——each 是人挑的例子（有限的想象），property 是机器生成的域（覆盖你没想象的输入），互补不替代。

```javascript
import fc from 'fast-check';
import { parseTemplate, stringifyTemplate } from './template';

test('属性：序列化往返不变', () => {
  fc.assert(fc.property(
    fc.record({ name: fc.string(), count: fc.integer({ min: 0 }) }),
    (tpl) => expect(parseTemplate(stringifyTemplate(tpl))).toEqual(tpl), // 任意输入都成立
  ));
});

test('属性：金额折扣函数永不为负、不超过原价', () => {
  fc.assert(fc.property(
    fc.integer({ min: 0, max: 10_000_00 }),   // 单位：分
    fc.integer({ min: 0, max: 100 }),
    (price, percent) => {
      const out = applyDiscount(price, percent);
      expect(out).toBeGreaterThanOrEqual(0);
      expect(out).toBeLessThanOrEqual(price);
    },
  ));
});

test('属性：shuffle 后元素集合不变', () => {
  fc.assert(fc.property(
    fc.array(fc.integer()),                       // 任意数组
    (arr) => expect([...shuffle(arr)].sort()).toEqual([...arr].sort()),
  ));
});
```
