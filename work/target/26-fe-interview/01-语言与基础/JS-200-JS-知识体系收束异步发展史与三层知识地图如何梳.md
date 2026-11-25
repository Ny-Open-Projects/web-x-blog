---
title: [JS-200] JS 知识体系收束？异步发展史与三层知识地图如何梳理？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-200：JS 知识体系收束？异步发展史与三层知识地图如何梳理？

**答**：
- 异步演进是一条"解决上一步痛点"的逻辑链：回调（嵌套地狱、错误分散）→ Promise（状态机 + 链式，统一错误通道）→ generator + 执行器（可中断但需手动驱动）→ async/await（同步写法的语法糖）→ 响应式流（RxJS/信号，面向持续变化的数据流）。
- 一次性异步用 await，持续异步（输入流、消息流）用响应式——演进不是替代而是分层，每层都有适用场景。
- 知识地图三层：语言核心（类型转换、作用域闭包、this 与原型、Promise 与事件循环、元编程、函数式）；浏览器（DOM 与事件、存储、网络、渲染原理、Web API）；工程化（模块化、构建、框架原理、性能、监控、规范设计）。
- 面试应答四层法：概念是什么 → 底层原理 → 能否手写 → 实际场景；每层都要有代码佐证，本文件 200 题即按此结构收束。
- 复习方法：把 200 题映射回三层地图，能讲出"概念/原理/手写/场景"四层的打勾，缺口即弱项清单。

```javascript
// 1. 回调时代：嵌套地狱，错误分散在每层
getUser(id, (err, user) => {
  if (err) return handle(err);
  getOrders(user, (err, orders) => {
    if (err) return handle(err);            // 每层都要写一遍错误处理
    getDetail(orders[0], (err, detail) => { // 越嵌越深，无法组合
      if (err) return handle(err);
      console.log(detail);
    });
  });
});

// 2. Promise 时代：链式拉平，错误通道统一
getUser(id)
  .then((user) => getOrders(user))
  .then((orders) => getDetail(orders[0]))
  .then((detail) => console.log(detail))
  .catch(handle);                           // 一处捕获全链错误

// 3. generator + 执行器：可中断，async/await 的前身
function* flow() {
  const user = yield getUser(id);
  const orders = yield getOrders(user);
  return yield getDetail(orders[0]);
}
run(flow()).then(console.log);              // run 即 JS-148 手写的自动驱动器

// 4. async/await：同步写法 + 原生 try/catch
(async () => {
  try {
    const user = await getUser(id);
    const orders = await getOrders(user);
    console.log(await getDetail(orders[0]));
  } catch (e) { handle(e); }
})();

// 5. 响应式流：面向"持续到来的数据"（RxJS 思想示意）
// input$.pipe(debounceTime(300), distinctUntilChanged(), switchMap(search))
//   .subscribe(renderResults);            // 输入流 → 搜索流 → 渲染

// 6. 三层知识地图（自检清单）
const knowledgeMap = {
  语言核心: ['类型与转换', '作用域与闭包', 'this 与原型', 'Promise 与事件循环', '元编程', '函数式'],
  浏览器: ['DOM 与事件', '存储', '网络 fetch', '渲染原理', 'Web API', '安全'],
  工程化: ['模块化', '构建工具', '框架原理', '性能优化', '错误监控', '规范设计'],
};
// 自检：每项都能讲出 概念/原理/手写/场景 四层即为掌握，讲不出的就是弱项
```

## 追问（补充）

**追问**：

1. async/await 与 generator 的本质关系？ → async 函数是 generator 加自动执行器再加 Promise 的语法糖，await 等价于 yield 后由引擎自动 next，所以手写执行器能解释其行为。
2. 响应式流补上了 await 的什么短板？ → await 只能拿到一次性结果，RxJS 面向持续到来的多值流，可组合、可取消、可做背压与节流。
3. await 之后的代码在事件循环哪个时机执行？ → 作为微任务在当前同步代码结束后立刻执行，早于下一次宏任务、渲染与定时器回调。
