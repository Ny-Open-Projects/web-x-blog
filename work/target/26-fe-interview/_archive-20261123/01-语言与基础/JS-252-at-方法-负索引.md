---
title: [JS-252] at() 方法与负索引
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-252：at() 方法与负索引

**答**：
- at(i)：支持负索引（-1 是最后一个）——`arr.at(-1)` 替代 `arr[arr.length - 1]`
- 作用对象：Array、String、TypedArray——字符串取最后字符 `str.at(-1)` 同样好用
- 越界返回 undefined（与 [] 取值一致）；i 非整数会截断
- 与 slice(-1)[0] 的对比：at 语义更直白，无额外数组分配
- 来源：相对索引提案（ES2022）——小 API 但极高频

```javascript
const arr = [1, 2, 3];
arr.at(-1);        // 3
arr.at(-4);        // undefined
'abc'.at(-1);      // 'c'
// 滚动列表取最新项
const last = messages.at(-1);
```
