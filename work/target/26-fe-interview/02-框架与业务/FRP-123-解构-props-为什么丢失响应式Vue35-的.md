---
title: [FRP-123] 解构 props 为什么丢失响应式？Vue3.5 的 reactive props destructure 是怎么解决的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-123：解构 props 为什么丢失响应式？Vue3.5 的 reactive props destructure 是怎么解决的？

**答**：
- `const { title } = props` 是**一次性读值**：局部变量拿到当时的字符串，之后 `props.title` 变化与它无关——响应式是"对象属性级"的，值离开对象就断链（reactive 同理，见 FRP-056）。
- Vue3.5 的解法在**编译期**：允许 `const { title = 'hi' } = defineProps(...)`，编译器把之后所有对局部变量 `title` 的**读取重写为 `props.title`**——运行时根本没有这个局部变量，自然不断链。
- 默认值 `= 'hi'` 被编译进运行时 props 声明（相当于 props 默认值），而非局部兜底。
- 本质：不是"让变量变成响应式"，而是**不产生变量**，用编译期的标识符替换保住属性访问路径。

```javascript
// 简化实现，帮助理解编译器的重写行为
// 源码（<script setup> 中）：
//   const { title = 'hi', count } = defineProps<{ title?: string; count: number }>()
//   console.log(title, count + 1)
//
// 编译产物等价于（伪代码）：
function compileDemo() {
  const props = definePropsRuntime({ title: { type: String, default: 'hi' }, count: Number });
  // 注意：没有 const title = ...，而是所有引用被重写
  console.log(props.title, props.count + 1);
}

// —— 手动模拟这个重写过程 ——
function transformDestructure(source) {
  // 1. 解析 const { a, b = def } = defineProps(...) 拿到解构名与默认值
  const names = parseDestructure(source); // ['title', 'count']
  // 2. 把函数体内对这些标识符的"读"替换为 props.xxx（写会报编译错误）
  let code = rewriteIdentifiers(source.body, names, (name) => `props.${name}`);
  // 3. 默认值合入运行时 props 声明
  const runtimeProps = mergeDefaults(source.propsDecl, source.defaults);
  return `const props = defineProps(${runtimeProps});\n${code}`;
}

function rewriteIdentifiers(body, names, map) {
  // 真实实现基于 AST 遍历，跳过 shadow 作用域（局部又声明同名变量的块）
  return body.replace(new RegExp(`\\b(${names.join('|')})\\b`, 'g'), (m) => map(m));
}

// 行为验证：解构后"变量"依然跟随 props 变化
const props = reactive({ title: 'a' });
const getTitle = () => props.title; // 编译重写后的形态
props.title = 'b';
console.log(getTitle()); // 'b' —— 仍是属性访问，不断链
// 而 const { title } = props 之后再读 title 永远是 'a'
```
