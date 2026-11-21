---
title: [WCN-283] Svelte 5 runes（$state/$derived/$effect）的编译实现？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-283：Svelte 5 runes（$state/$derived/$effect）的编译实现？
**答**：
- runes 是编译器指令：$state 声明编译为信号节点，$derived 编译为 computed，依赖自动收集（编译期静态分析 + 运行时兜底）。
- 与 Svelte 4 区别：4 是编译期定向更新（无运行时信号）；5 引入运行时信号（跨组件/动态场景），编译期仍是优化层。
- 细粒度粒度控制：深层对象用 $state 代理，属性级订阅。
- 编译器校验：非响应式上下文读 runes、跨组件传普通值导致丢响应——编译期报错。

```javascript
<script>
let count = $state(0);
let double = $derived(count * 2);
$effect(() => console.log(double));
</script>
<button onclick={() => count++}>{double}</button>
r
```
