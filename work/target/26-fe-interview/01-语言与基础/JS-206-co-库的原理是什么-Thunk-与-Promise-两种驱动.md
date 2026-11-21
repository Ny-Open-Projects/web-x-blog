---
title: [JS-206] co 库的原理：Thunk 与 Promise 两种驱动
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 生成器]
type: 面试题
---

## JS-206：co 库的原理：Thunk 与 Promise 两种驱动

**答**：
- co（TJ 的异步控制库）：自动驱动生成器——每次 next 拿到 yield 出来的值，若是 Promise 就等它 resolve 再把结果传回 next
- 递归驱动器 20 行代码就是 co 的内核：`gen.next().value.then(v => step(v))`
- 两种「让 yield 出去的值带结果」的方式：Promise（通用）与 Thunk（柯里化的回调函数，早期 Node 生态）
- 意义：co 是 async/await 的前身——理解 co = 理解 await 的运行时语义

```javascript
function co(gen) {
  return new Promise((resolve, reject) => {
    const g = gen();
    const step = (val) => {
      const { value, done } = g.next(val);
      if (done) return resolve(value);
      Promise.resolve(value).then(step, reject); // 结果传回下一个 next
    };
    step();
  });
}
co(function* () {
  const user = yield fetchUser();      // 暂停等 Promise
  const orders = yield fetchOrders(user.id);
  return orders;
});
```
