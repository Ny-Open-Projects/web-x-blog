---
title: [DP-030] 什么是 AOP 思想？手写 before/after 织入埋点（高频压轴）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-030：什么是 AOP 思想？手写 before/after 织入埋点（高频压轴）
**答**：
- AOP（面向切面）：把日志、埋点、鉴权、性能统计等"横切关注点"从业务代码中剥离，动态织入函数执行的前后。
- 前端经典实现：`Function.prototype.before/after`——不修改原函数源码，在调用链上包裹。
- 与装饰器关系：装饰器是 AOP 的声明式语法糖，before/after 是 AOP 的函数式原语。
- 价值：埋点需求变化（换 SDK、改参数）不影响业务函数；业务函数也可单独测试。

```javascript
// AOP 原语：before/after 织入，不侵入原函数
Function.prototype.before = function (beforeFn) {
  const self = this;
  return function (...args) {
    const patched = beforeFn.apply(this, args); // 前置切面可改参数
    return self.apply(this, patched === undefined ? args : patched);
  };
};
Function.prototype.after = function (afterFn) {
  const self = this;
  return function (...args) {
    const result = self.apply(this, args);
    afterFn.call(this, result);                 // 后置切面可消费结果
    return result;
  };
};

// 业务函数：干净，不含任何埋点代码
function submitOrder(order) {
  console.log('提交订单', order.id);
  return { ok: true, orderId: order.id };
}

// 织入埋点（前置）与上报（后置）
const trackedSubmit = submitOrder
  .before((order) => {
    tracker('click_submit', { orderId: order.id, ts: Date.now() });
    // 可选：校验失败返回 null 时可中止，这里演示改参
    return [{ ...order, from: 'pc' }];
  })
  .after((result) => {
    tracker('submit_done', { ok: result.ok });
  });
function tracker(event, data) { console.log('[埋点]', event, data); }

trackedSubmit({ id: 'A1' });
// [埋点] click_submit {orderId: 'A1', ts: ...}
// 提交订单 A1
// [埋点] submit_done {ok: true}

// 无侵入的另一直接写法：包装函数（等价于上面的组合）
const withTrack = (fn, event) => (...args) => { tracker(event, {}); return fn(...args); };
const t2 = withTrack(submitOrder, 'click_submit_alt');
t2({ id: 'A2' });
```
