---
title: [DP-259] 源码识别：Vue Vapor/Svelte 编译器源码中的直译策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-259：源码识别：Vue Vapor/Svelte 编译器源码中的直译策略？
**答**:
- 策略对比：VDOM 路线（React）"运行时 diff"vs 编译直译路线（Svelte/Vue Vapor）"把响应式更新编译成具体 DOM 操作"——同一问题两种策略路线。
- 静态提升：Svelte 编译期分析"哪些节点永不更新"→ 原样输出；动态节点才生成更新函数（update(t1, 'text')）。
- 观察者编译化：响应式信号直接绑到 DOM 更新指令（effect(() => node.textContent = value)），无虚拟 DOM 中间层。
- 识别要点：能说出两条路线的代价——直译路线包体积小但动态性弱（运行时结构变化难处理），VDOM 路线灵活但 diff 开销。

```javascript
// Svelte 编译产物心智模型
// 源码：<h1>{title}</h1><p>静态段落</p>
// 产物：
// let t1;                                   // 只有动态节点有句柄
// function update(ctx, dirty) {
//   if (dirty & /*title*/ 1 && t1.textContent !== ctx.title) t1.textContent = ctx.title;   // 直译更新
// }
// create_fragment() {
//   const h = element('h1'); t1 = text(ctx.title);
//   append(h, t1); append(h2, '静态段落');   // 静态节点编译为字面量
//   return { c, m, update };                  // 生命周期钩子由编译器生成
// }
// Vue Vapor：effect(() => { el.textContent = title.value }) —— 信号直绑 DOM，跳过 vdom
```
