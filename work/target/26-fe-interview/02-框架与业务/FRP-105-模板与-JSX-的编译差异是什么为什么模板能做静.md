---
title: [FRP-105] 模板与 JSX 的编译差异是什么？为什么模板能做静态优化而 JSX 不能？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-105：模板与 JSX 的编译差异是什么？为什么模板能做静态优化而 JSX 不能？

**答**：
- 本质：**模板是受限 DSL**——不允许任意 JS，只有固定的表达形式（插值/指令/属性），编译器能**确定地**知道"这个位置永远是文本节点、这些属性是静态的"；**JSX 是 JS 的语法糖**，`<div a={cond ? x : y}>{fn()}</div>` 里一切都是运行时表达式，静态分析只能保守放弃。
- 模板的优化空间：静态提升、patchFlag、Block Tree、缓存 handler 全部依赖"结构编译期已知"；Vue3 的速度优势 = 模板限制换来的编译期信息。
- JSX 的空间：可以做到"编译期生成 h() 调用"，但**信息量止步于此**——无法保证 `props` 对象哪些字段动态（依赖 JS 全程序分析，跨组件/跨包分析不现实），所以 React 选择在运行时做（reconciler、memo、selector）。
- 中间路线：Vue 支持写 render 函数/h()（放弃优化），Solid/Svelte 证明"更受限的组件模型 + 编译器"能两全，但代价见 FRP-104。

```javascript
// 简化实验，帮助理解静态分析能力的边界
// ===== 模板（可静态分析）=====
// <div class="box"><span>static</span><i>{{ msg }}</i></div>
function compileTemplateSafe() {
  // 编译器确定地知道：
  // 1. div 的 class 是字符串字面量 -> 静态属性，永不 diff
  // 2. span 子树纯静态 -> 可提升为常量
  // 3. i 的内容是唯一动态表达式 -> patchFlag TEXT，diff 只碰 textContent
  return {
    hoisted: '<span>static</span>',
    patchFlags: { i: 1 /* TEXT */ },
    staticProps: { div: { class: 'box' } },
  };
}

// ===== JSX（不可静态分析）=====
function App({ msg, cond }) {
  return <div class={cond ? 'a' : 'b'}><span>{'static'}</span><i>{msg}</i></div>;
}
// 编译器视角（只能得到这个程度）：
function compileJSX(msg, cond) {
  return h('div',
    { class: cond ? 'a' : 'b' },        // 三元 -> 只能当"整体动态"，无法判定结果是否相等
    h('span', null, 'static'),           // 看似静态，但调用点可能传变量/副作用
    h('i', null, msg));                  // 同上
}
// 'static' 字面量在 JSX 里理论上可提，但：
// 1. React 组件 children 可能是带 key 的列表/map 结果，形态不定
// 2. 跨文件分析（props 传递链）成本不可控
// 结论：JSX 编译器只能保守生成均匀的 h() 调用，优化全部后置到运行时
console.log(JSON.stringify(compileTemplateSafe()));
console.log('JSX 产物', compileJSX('x', true).type); // div：无任何标记信息
```
