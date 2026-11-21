---
title: [JS-238] findLast 与 findLastIndex：场景
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-238：findLast 与 findLastIndex

**答**：
- 从数组尾部向前查找第一个满足条件的元素/下标（ES2023）
- 替代的反模式：[...arr].reverse().find()（多复制一次）或手写倒序循环
- 高频场景：日志「最后一条错误」、列表「最后一个未完成项」、时间序列「最近一次达标」
- 与 slice(-n) 的区别：findLast 是条件查找而非截取；两者组合常见（先截取再查找）

```javascript
const logs = [
  { level: 'info', msg: 'a' },
  { level: 'error', msg: 'x' },
  { level: 'info', msg: 'b' },
  { level: 'error', msg: 'y' },
];
logs.findLast(l => l.level === 'error');        // { level: 'error', msg: 'y' }
logs.findLastIndex(l => l.level === 'error');   // 3
```
