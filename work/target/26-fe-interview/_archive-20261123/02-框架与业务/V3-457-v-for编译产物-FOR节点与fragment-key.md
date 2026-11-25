---
title: [V3-457] v-for 编译产物：FOR 节点与 item/index 解构
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-457：v-for 编译产物：FOR 节点与 item/index 解构

**答**：
- FOR 节点结构：`{ type: FOR, source, value, key, index, child }`——source 是列表表达式，value/key/index 是解构出的循环变量
- codegen 产物：`_renderList(source, (item, index, key) => ...)` 返回 fragment（vnode 数组）——运行时 renderList 对数组/对象/数字三种 source 分别处理（数字 = 计数循环）
- key 编译：`:key` 表达式作为第三个参数传入并设为 vnode key——「key 必须放 v-for 同层」的编译层依据；缺 key 时走「就地复用」patch 策略
- 嵌套 v-for：child 节点本身又是一个 FOR——递归结构，编译器按嵌套生成多层 renderList
- 深水点：v-for 内的模板引用/作用域插槽作用域——循环变量是「子作用域」，编译器把它们放进渲染函数参数而非外层闭包（这也是编译器 vs 运行时模板的关键差异）

```javascript
// template: <li v-for="(item, i) in list" :key="item.id">{{ item.name }}</li>
// 产物:
_renderList(list, (item, i) => ({
  key: item.id,
  _createVNode('li', null, _toDisplayString(item.name))
}))
```
