---
title: [FRP-063] cacheHandlers（内联事件缓存）解决什么问题？编译产物里的 `_cache[0] || (_cache[0] = ...)` 是怎么回事？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-063：cacheHandlers（内联事件缓存）解决什么问题？编译产物里的 `_cache[0] || (_cache[0] = ...)` 是怎么回事？

**答**：
- 问题：模板里的内联事件 `@click="count++"` 每次重渲染都会**生成一个新函数**作为 vnode 的 prop，子组件收到新 prop 引用就认为"变了"，导致**无效更新**（尤其配合 memo/props 浅比较时）。
- 编译器开启 cacheHandlers 后，handler 被编译成 `_cache[0] || (_cache[0] = ($event) => _ctx.count++)`：首次渲染创建并**缓存在组件实例上**，之后重渲染直接命中缓存拿到**同一个函数引用**。
- 内联表达式里访问 `_ctx`，正是为了让函数可以被缓存——闭包不捕获当次渲染变量，而改为运行时从 ctx 取值，天然规避了事件闭包的旧值问题。
- 在线工具里看到 `_cache` 数组即代表此优化开启（默认开启，`cacheHandlers: true`）。

```javascript
// 简化实现，帮助理解 handler 缓存对无效更新的消除
// 模板：<Child @inc="count++" />，两种编译产物对比
function compileTemplate(cache) {
  // 未开启缓存：每次 render 都创建新函数
  return function renderWithoutCache(_ctx) {
    return { type: 'Child', props: { onInc: () => _ctx.count++ } };
  };
}
function compileTemplateCached(cache) {
  // 开启缓存：函数只创建一次，引用恒定
  return function renderWithCache(_ctx) {
    return {
      type: 'Child',
      props: {
        onInc: cache[0] || (cache[0] = ($event) => _ctx.count++), // 首次创建后复用
      },
    };
  };
}

const ctx = { count: 0 };
const renderCached = compileTemplateCached([]);

const r1 = renderCached(ctx);
const r2 = renderCached(ctx);
console.log(r1.props.onInc === r2.props.onInc); // true：引用相同，子组件可跳过更新
r1.props.onInc();
console.log(ctx.count); // 1：函数运行时读 _ctx，闭包没有旧值问题

const renderPlain = compileTemplate([]);
console.log(renderPlain(ctx).props.onInc === renderPlain(ctx).props.onInc); // false：每次新函数
// 若 Child 内部对 props 做浅比较，false 意味着每次父渲染它都白白重渲染
```
