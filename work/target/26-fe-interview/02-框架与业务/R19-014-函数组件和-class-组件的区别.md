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

**追问**：

1. 函数组件怎么模拟"只初始化一次的实例"？→ `useRef` 惰性初始化加 `useMemo`，但初始化逻辑要避免放在 render 里做有副作用的事；真要实例语义就用 ref 存一个对象。
2. class 的 `setState` 是异步的，函数组件呢？→ 都是批处理，但 class 的 `this.state` 在回调里读到的已合并结果，函数组件闭包里捕获的是当次快照，事件里连读两次都是旧值。
3. 现在还有哪些场景必须用 class 组件？→ 错误边界（`getDerivedStateFromError` 至今没有 hook 版本），以及需要继承第三方 class 基类的存量代码，其余都应迁到函数组件。
