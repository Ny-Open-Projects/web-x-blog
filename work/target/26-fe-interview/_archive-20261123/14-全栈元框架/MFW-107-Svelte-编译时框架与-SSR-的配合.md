---
title: [MFW-107] Svelte 作为编译时框架，对 SSR/水合有什么独特影响？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-107：Svelte 作为编译时框架，对 SSR/水合有什么独特影响？
**答**：
- Svelte 在**编译期**消解框架运行时：没有 vdom diff，输出的是直接的 DOM 操作代码。SSR 侧同样编译成字符串拼接逻辑，模板就是最终真相，运行时开销只剩极小的水合引导。
- 水合成本优势：React 要把整棵组件树（JSX 运行时）发到浏览器才能水合；Svelte 组件已被编译，客户端 bundle 更小，水合更快——对 LCP/TBT 是结构性优势。
- 响应式模型差异：`export let data` + 声明式赋值，没有 useState/useEffect 心智；SSR 场景下「服务端渲染 → 客户端激活」不需要 hooks 约束规则。
- 代价：生态与 RSC 式「零客户端 JS 数据流」不同——SvelteKit 的数据仍要序列化下发复水（devalue），不像 RSC 那样服务端组件不出现在客户端包里。

```svelte
<!-- 编译期响应式：无 hooks、无 vdom -->
<script>
  export let data;            // load 注入
  let count = 0;              // 编译器识别赋值 -> 触发更新
  $: doubled = count * 2;     // 响应式声明，编译为依赖追踪
</script>

<button on:click={() => count++}>{count}</button>
<p>双倍：{doubled}</p>

{#each data.items as item (item.id)}  <!-- keyed each，编译成循环 -->
  <li>{item.name}</li>
{/each}
```

```
编译产物心智模型（示意）：
React:   组件函数 -> vdom 树 -> reconcile -> DOM
Svelte:  组件函数 -> 编译期生成的 DOM 指令序列（create/update/destroy 分段）
SSR:     同一份模板编译为字符串拼接 + 水合指令，天然同构
```
