---
title: [WCN-754] 编译器里的作用域提升与闭包优化是怎么回事？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-754：编译器里的作用域提升与闭包优化是怎么回事？

**答**：
- 结论：模板编译为渲染函数时，把不依赖响应式状态的常量提到函数外（模块作用域），减少每次渲染的闭包含量与重复创建；对访问外层变量的内部函数做「逃逸分析」，能内联就内联。
- 副作用：提升的常量必须真正无状态（不含 prop/state 引用），否则会跨实例共享导致 bug；编译器通过 patchFlag 标记哪些节点可提升。
- 追问钩子：把含 `Math.random()` 的表达式提升了会怎样？考察「有副作用/非纯表达式不可提升」的判定。

```javascript
// 编译前：render() { return h('div', { class: 'hd' }, [txt.value]) }
const HOISTED_CLASS = { class: 'hd' };            // 提升到模块作用域
function render(txt) {
  return { tag: 'div', props: HOISTED_CLASS, children: [txt] }; // 复用常量 props
}
// 反例：不可提升（每次结果不同）
function bad() { return { id: Math.random() }; }  // 有副作用，禁止提升
console.log(render('hi'), bad());
```
