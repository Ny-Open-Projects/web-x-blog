---
title: [ALG-165] 面试趣味题：只用 setTimeout（不用比较排序）把一组非负整数排成升序。写出实现并说明它为什么不能用于生产？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-165：面试趣味题：只用 setTimeout（不用比较排序）把一组非负整数排成升序。写出实现并说明它为什么不能用于生产？
**答**：sleep 排序——按值定时，值小的定时器先醒先输出。复杂度 O(max(n))（时间维度），只能排非负整数、受定时器最小粒度与并发上限（Chrome 同域 setTimeout 链）限制，且值差距小于定时器精度时乱序。考察点是事件循环理解：所有定时器回调在各自到期后的宏任务轮次执行。

```javascript
const sleepSort = (arr, scale = 1) => new Promise(resolve => {
  const out = [];
  arr.forEach(n => {
    setTimeout(() => {
      out.push(n);                     // 值小的定时器先到期先输出
      if (out.length === arr.length) resolve(out);
    }, n * scale);                     // scale 放大间隔可缓解精度乱序
  });
});
// await sleepSort([5, 3, 8, 1, 9]) => [1, 3, 5, 8, 9]
// 不能用于生产：O(max 值) 时间、值小于定时器精度会乱序、只支持非负整数
// 价值在于展示 setTimeout 并发注册与宏任务轮次的理解
```
