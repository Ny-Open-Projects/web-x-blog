---
title: [AIC-239] AI 生成 property-based 测试（如 fast-check）的效果如何？适合什么场景？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-239：AI 生成 property-based 测试（如 fast-check）的效果如何？适合什么场景？
**答**：
- AI 很擅长写属性测试：性质描述（不变量）由人给，生成与收缩 AI 能自动完成。
- 适合：纯函数、解析器、序列化、金额计算、状态机——性质清晰的领域。
- 不适合：依赖外部世界的 IO、UI 组件渲染断言。
- 关键输入是「性质清单」：如「序列化再反序列化等于原值」「任何输入不抛 uncaught」。

```javascript
import fc from 'fast-check';
it('金额计算性质：分→元→分 恒等', () => {
  fc.assert(fc.property(fc.integer({ min: 0, max: 1e9 }), cents =>
    expect(toFen(toYuan(cents))).toBe(cents)));
});
it('解析器性质：非法输入不崩溃', () => {
  fc.assert(fc.property(fc.string(), s => { parseCoupon(s); })); // 不抛 uncaught
});
r
```
