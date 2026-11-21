---
title: [MP-024] Component 构造器的高级选项 observers / lifetimes 怎么用？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-024：Component 构造器的高级选项 observers / lifetimes 怎么用？
**答**：
- `observers`：监听 data 与 properties 的任意字段，支持 `'a, b'` 多字段与 `'obj.**'` 通配符，适合派生数据（替代手动 watch）。
- `lifetimes`：组件生命周期 `created → attached → ready → moved → detached`，写在 lifetimes 字段里优先级高于构造器顶层同名定义。
- 页面生命周期放 `pageLifetimes`（show/hide/resize），监听所在页面状态。

```javascript
Component({
  properties: { a: Number, b: Number },
  observers: {
    'a, b'(a, b) { this.setData({ sum: (a || 0) + (b || 0) }) },
    'obj.**'(obj) { console.log('obj 任意字段变化', obj) }
  },
  lifetimes: {
    attached() { console.log('进入节点树') },
    ready()   { console.log('布局完成，可查节点') },
    detached(){ console.log('移除：清定时器') }
  },
  pageLifetimes: {
    show() { console.log('所在页面显示') }
  }
})
```
