---
title: [ALG-170] 两个并发流程同时"读 localStorage 购物车 → push → 写回"，后写的覆盖先写的（丢更新）。如何用 Promise 链实现一个 async 互斥锁？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-170：两个并发流程同时"读 localStorage 购物车 → push → 写回"，后写的覆盖先写的（丢更新）。如何用 Promise 链实现一个 async 互斥锁？
**答**：把共享状态串行化：锁内部维护一条 Promise 链（`chain`），每个 lock 调用排在链尾执行（`chain.then(() => fn())`）；同时把本次执行结果（吞掉错误后）接回链尾，保证前一个失败不阻断后续。获得锁的执行是"读改写"原子段。时间 O(排队长度) 均摊 O(1)。

```javascript
function createMutex() {
  let chain = Promise.resolve(); // 用 Promise 链当任务队列
  return function lock(fn) {
    const run = chain.then(() => fn());  // 排在队尾，前一个完成才轮到
    chain = run.catch(() => {});         // 吞错误：单个任务失败不阻断后续
    return run;                          // 调用方仍能拿到结果/异常
  };
}
// 场景：购物车读改写原子化，防止并发丢更新
const mutex = createMutex();
const addToCart = item => mutex(async () => {
  const cart = JSON.parse(localStorage.getItem('cart') || '[]');
  cart.push(item);                       // 读 -> 改 -> 写 在同一临界区内
  localStorage.setItem('cart', JSON.stringify(cart));
  return cart.length;
});
// 并发调用 addToCart(a); addToCart(b); 顺序执行，两次都生效
```

## 十九、安全相关算法

> ALG-171 ~ ALG-176：XSS 白名单过滤、水印防篡改、签名时间窗、混淆编码、安全随机、时序安全比较。前端安全算法的共同认知：前端只是第一道防线，权威校验永远在后端。
