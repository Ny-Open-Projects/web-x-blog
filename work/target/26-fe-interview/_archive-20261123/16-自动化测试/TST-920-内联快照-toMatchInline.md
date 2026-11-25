---
title: [TST-920] 内联快照（toMatchInlineSnapshot）与外置 .snap 文件如何取舍与治理？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-920：内联快照（toMatchInlineSnapshot）与外置 .snap 文件如何取舍与治理？
**答**：
- 结论：内联快照「与代码同框、review 直观」适合小而稳定的值；外置快照「不污染源码」适合大对象/多用例共享。
- 取舍维度：可读性（内联胜）、源码体积（外置胜）、批量更新（外置胜）、code review 可见性（内联胜）。
- 治理：混合策略——错误提示文案、小型 DTO 用内联；大 DOM 树、组件树用外置；禁止把 100 行 JSON 内联进源码。
- 追问钩子：内联快照让 PR diff 看起来很大，团队抱怨「测试代码比业务代码还多」，你怎么折中？

```javascript
// 内联：短小值，review 时和断言写在一起
expect(formatPrice(9900)).toMatchInlineSnapshot(`"99.00 元"`);

// 外置：大对象，源码干净
expect(renderCoupon(coupon)).toMatchSnapshot();

// 治理阈值：超过 N 行强制外置
function chooseSnapshotMode(value) {
  const len = JSON.stringify(value).length;
  return len <= 80 ? 'inline' : 'external';
}
console.log(chooseSnapshotMode({ price: 9900 }));        // inline
console.log(chooseSnapshotMode({ items: Array(50).fill(1) })); // external
```
