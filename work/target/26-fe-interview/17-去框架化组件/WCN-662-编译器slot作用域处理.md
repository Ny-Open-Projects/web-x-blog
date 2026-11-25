---
title: [WCN-662] 编译器如何处理 slot（作用域插槽）的编译？作用域如何传递？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-662：编译器如何处理 slot（作用域插槽）的编译？作用域如何传递？

**答**：
- 结论：slot 内容在「父组件作用域」编译，但可接收子组件通过 slot props 传入的参数；编译器把 slot 编译为函数 (props) => VNode。
- 做法：<slot :item="x"> 编译为 renderSlot(slots, 'default', { item: x })；父组件传入的 slot 模板编译为函数接收 props。
- 追问钩子：与普通 props 传 JSX 比有何优势？slot 保留响应式上下文且延迟渲染——考察对「作用域与渲染时机」的理解。

```javascript
// 模板：<Child><template #row="{ item }">{{ item.name }}</template></Child>
// 父组件编译：slot 编译为函数，接收子传入的 props
const slots = {
  row: ({ item }) => h('span', null, String(item.name)),
};
// 子组件编译：调用 slot 并传入作用域数据
function Child({ slots }, items) {
  return items.map(item =>
    slots.row({ item }) // 作用域通过参数传给父编译的函数
  );
}
console.log(Child({ slots }, [{ name: 'A' }]).length); // 1
```
