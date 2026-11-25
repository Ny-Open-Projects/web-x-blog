---
title: [JS-228] 闭包捕获大对象怎么优化：提前置 null
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 内存]
type: 面试题
---

## JS-228：闭包捕获大对象怎么优化

**答**：
- 问题：回调闭包捕获了整块数据（如完整响应 JSON），但只用到其中一个字段——整块被闭包钉住无法回收
- 优化一：解构出需要的字段再进闭包（捕获小对象）——最常用、零成本
- 优化二：用完置 null——释放闭包链上的引用（对 let/var 生效；const 不行）
- 优化三：改传值不传环境——把数据转成参数传入（消除闭包依赖）
- 注意 V8 优化：未被使用的上下文变量可能被引擎优化掉，但别赌——显式控制作用域才是工程纪律

```javascript
function process(res) {
  const { items } = res;      // 只留需要的字段
  return () => render(items); // 闭包只钉住 items，res 整体可回收
}
// 用完释放
let bigData = await load();
const summary = compute(bigData);
bigData = null;               // bigData 可回收，summary 已算完
```
