---
title: [WCN-758] 模板指令（v-if/v-for）通常如何编译为运行时代码？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-758：模板指令（v-if/v-for）通常如何编译为运行时代码？

**答**：
- 结论：v-if 编译为三元表达式/条件块（`condition ? renderA() : renderB()`），v-for 编译为 `list.map((item,i)=>...)` 并带 key；编译器把指令转换为纯 JS 渲染逻辑，运行时不解析指令。
- v-if 与 v-for 同节点时有优先级（Vue2 for 先、Vue3 if 先），影响可访问的变量；编译期据此调整嵌套顺序。
- 追问钩子：为什么 v-if 和 v-for 不建议写在同一元素？考察「优先级不明确 + 每次循环都判断」的性能与可读性问题。

```javascript
// 模板：<li v-for="(item,i) in list" :key="item.id" v-if="item.show">{{item.name}}</li>
// 编译产物（Vue3：if 优先）：
function render(list) {
  return list
    .filter((item) => item.show)                    // v-if 提升为过滤（注意作用域差异）
    .map((item, i) => ({ tag: 'li', key: item.id, children: [item.name] }));
}
console.log(render([{ id: 1, name: 'A', show: true }, { id: 2, name: 'B', show: false }]));
```
