---
title: [FRP-178] React Compiler 的自动 memoization 是什么原理（编译期数据流分析）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-178：React Compiler 的自动 memoization 是什么原理（编译期数据流分析）？

**答**：
- React Compiler（原 React Forget）在**构建期**分析组件/hook 的数据流，自动插入等价于 useMemo/useCallback/自动依赖的缓存代码——开发者不再手写 memo。
- 核心是**依赖追踪的编译期化**：编译器把组件转成 SSA 形式，计算每个值依赖哪些输入（props/state/外部读取），把"依赖不变则复用"表达为编译产物。
- 产物形态：JSX 嵌入 `_c(dependencies, () => jsx(...))` 帮助函数——运行时做 `Object.is` 依赖比对，全等则返回缓存的元素树。
- 边界：编译器**只对符合 React 规则的代码**生效——可变全局、按调用顺序变化的逻辑会被跳过（保守策略，不改变语义只跳过优化）；ESLint 插件负责提前暴露违规。

```javascript
// 简化实现，帮助理解 React Compiler 产物
// —— 源码（无任何手写 memo） ——
// function TodoList({ todos, query }) {
//   const filtered = todos.filter(t => t.text.includes(query));
//   return (
//     <ul>
//       {filtered.map(t => <Todo key={t.id} todo={t} />)}
//     </ul>
//   );
// }

// —— 编译产物（简化示意） ——
function TodoList(t32) {
  const $ = useMemoCache(4);                       // 槽位数组的缓存池
  const { todos, query } = t32;

  let filtered;
  if (
    $[0] !== todos ||                              // 依赖比对：编译期算出的依赖集
    $[1] !== query
  ) {
    filtered = todos.filter(t => t.text.includes(query));
    $[0] = todos; $[1] = query; $[2] = filtered;   // 写入缓存槽
  } else {
    filtered = $[2];                               // 依赖没变：直接复用上次结果
  }

  let t0;
  if ($[3] !== filtered) {                         // JSX 也是值：依赖不变复用元素树
    t0 = jsx('ul', { children: filtered.map(t => jsx(Todo, { todo: t }, t.id)) });
    $[3] = filtered;
  } else {
    t0 = $[3];
  }
  return t0;
}

// —— _c/useMemoCache 的运行时 ——
function useMemoCache(size) {
  const fiber = currentFiber;
  const slot = fiber.memoizedState ??= { cache: new Array(size).empty };
  return slot.cache;   // 缓存挂在 fiber 上：组件卸载即释放，与 hooks 同生命周期
}

// —— 编译器侧的分析步骤（概念） ——
// 1. 转换为 SSA：每次赋值都是新变量，值与产生它的表达式一一对应
// 2. 计算依赖：filtered 依赖 [todos, query]；JSX 依赖 [filtered]
// 3. 保守性检查：读到可变全局/调用顺序依赖 -> 放弃该段优化（不缓存，保持原语义）
// 4. 生成缓存代码：上述 if ($[..] !== ...) 模式
// 效果等价于手写 useMemo(() => ..., [todos, query]) + memo(Todo) 的组合，但零手写、永不漏依赖
```

## 二十七、手写进阶综合
