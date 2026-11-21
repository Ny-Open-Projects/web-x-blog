---
title: [BAS-042] 回调、Promise、async/await 是什么关系？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-042：回调、Promise、async/await 是什么关系？
**答**：
- 回调是最原始的异步方案，多层嵌套形成回调地狱，错误只能在每层处理。
- Promise 用链式 then/catch 把异步扁平化，状态一旦改变不可逆。
- async/await 是 Promise 的语法糖：同步写法、try/catch 捕错，底层仍是微任务。

```javascript
// 回调风格：getUser(id, (err, user) => ...)
// Promise 链：
getUser(id)
  .then((user) => getOrders(user.id))
  .then((orders) => console.log(orders))
  .catch(handleError);
// async/await：
async function load(id) {
  try {
    const user = await getUser(id);
    return await getOrders(user.id);
  } catch (e) {
    handleError(e);
  }
}
```

## 五、HTTP 与网络速答
