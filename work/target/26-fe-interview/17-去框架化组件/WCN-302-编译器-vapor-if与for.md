---
title: [WCN-302] Vapor/Solid 编译器对控制流（if/for）的编译处理？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-302：Vapor/Solid 编译器对控制流（if/for）的编译处理？
**答**：
- if：编译为条件块节点（anchor 注释节点定位），条件 computed 驱动块的创建/销毁。
- for：keyed 循环——编译为「索引→节点」映射，增删只动局部（diff 逻辑运行时库提供）。
- 嵌套作用域：每层控制流创建独立作用域（依赖收集隔离）。
- 错误模式：在循环内解构 item（丢失响应）——编译器报错提示用 props 函数访问。

```javascript
<For each={items()}>{(item) => <Card item={item} />}</For>
// 编译：keyed diff + 每项独立作用域
// item 是响应式代理，Card 内 item.title 的读取建立 item.title 订阅
r
```
