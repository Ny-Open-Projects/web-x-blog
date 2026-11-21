---
title: [R19-014] 函数组件和 class 组件的区别？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-014：函数组件和 class 组件的区别？
**答**：
- 函数组件没有 this 问题，逻辑可以聚合在单个 effect 中；class 组件的关联逻辑被生命周期方法拆散。
- 复用方式不同：函数组件靠自定义 Hook，class 组件靠 HOC/render props，嵌套层级更深。
- 函数组件每次渲染都是一次"快照"，props 和 state 在当次渲染中不可变；class 里 this 随时可变，容易读到新值。
- React 的新特性（Hooks、并发、Server Components 生态）都围绕函数组件展开。

```jsx
import { Component, useEffect, useState } from 'react';

// class 组件：this 绑定繁琐，逻辑被生命周期拆散
class TimerClass extends Component {
  state = { now: Date.now() };

  componentDidMount() {
    this.timer = setInterval(() => this.setState({ now: Date.now() }), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timer);
  }

  render() {
    return <span>{this.state.now}</span>;
  }
}

// 函数组件：启动与清理写在同一个 effect 里
function TimerHook() {
  const [now, setNow] = useState(Date.now());

  useEffect(() => {
    const timer = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(timer);
  }, []);

  return <span>{now}</span>;
}
```
