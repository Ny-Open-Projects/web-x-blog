---
title: [WCN-087] Svelte 的 runes 是什么？与 Signals 体系是什么关系？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-087：Svelte 的 runes 是什么？与 Signals 体系是什么关系？

**答**：
- Svelte 5 引入 runes：`$state`（响应式变量）、`$derived`（派生）、`$effect`（副作用）、`$props`、`$bindable`。信号语义以编译器魔法变量形式出现——写起来像普通变量。
- 与 Signals 关系：`$state`/`$derived`/`$effect` 与 signal/computed/effect 一一对应；Svelte 5 底层也有一套类似 signals 的运行时实现（深层的 proxy + 订阅），编译器负责消除样板代码。
- 差异：Svelte 依赖编译期转换（`let x = $state(0)` 编译成 signal 读写），依赖追踪仍发生在运行时，但代码层面完全隐形；Signals 标准提案追求"运行时显式 API"。
- `$derived` 是惰性的；`$effect` 返回清理函数；`$state` 深层对象用 proxy，数组/对象修改自动响应（Vue reactive 语义）。
- 迁移注意：runes 要求组件文件显式声明，老的 `let` 自动响应式（Svelte 4）不再隐式生效——赋值即响应的语义被收窄为显式 rune。

```svelte
<!-- Svelte 5 runes -->
<script>
  let count = $state(0);
  let double = $derived(count * 2);      // 惰性派生
  $effect(() => {                         // 追踪 count/double
    document.title = `${double}`;
    return () => {};                      // 清理函数
  });
</script>
<button onclick={() => count++}>{double}</button>
```
