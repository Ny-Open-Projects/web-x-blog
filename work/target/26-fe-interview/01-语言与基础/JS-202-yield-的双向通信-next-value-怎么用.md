---
title: [JS-202] yield 的双向通信：next(value) 怎么用
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 生成器]
type: 面试题
---

## JS-202：yield 的双向通信：next(value) 怎么用

**答**：
- yield 表达式有返回值：`next(value)` 传入的 value 就是「上一个 yield 表达式的求值结果」——生成器可接收外部输入
- 方向梳理：yield 右边的值「从生成器出去」（next 返回的 value），next 参数「从外部进来」赋给 yield 表达式
- 第一次 next 的参数被丢弃（没有正在等待的 yield）；throw() 让生成器在 yield 处抛错——异常双向注入
- 应用：状态机交互、协程式的「请求-响应」驱动（co 库把异步结果传回 yield 表达式）

```javascript
function* echo() {
  const a = yield '提问1';   // next('hello') 后 a === 'hello'
  const b = yield `你说了${a}`;
  return b;
}
const g = echo();
console.log(g.next());            // { value: '提问1', done: false }
console.log(g.next('hello'));     // { value: '你说了hello', done: false }
console.log(g.next('end'));       // { value: 'end', done: true }
```
