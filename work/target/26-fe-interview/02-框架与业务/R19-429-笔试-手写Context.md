---
title: [R19-429] 笔试：手写 Context（Provider/Consumer 与 bailout 击穿）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## R19-429：笔试：手写 Context

**答**：实现 createContext：① Provider：value 存 fiber 上下文链（读时向上查），value 变化强制子树重渲染（击穿 bailout）；② useContext：沿 fiber.return 向上找最近的 Provider；③ 默认值（无 Provider 时）；④ 渲染期一致性（同次渲染内 value 快照不变）；⑤ Consumer render-prop 形式。写出实现。

```javascript
function createContext(defaultValue) {
  const ctx = {
    $$context: true,
    defaultValue,
    Provider({ value, children }) {
      // 渲染时把 value 压入当前 fiber 的 context 栈
      pushContext(ctx, value);                       // 渲染子树前
      const result = children;                        // 子树渲染(readContext 向上查)
      popContext();                                   // 渲染后
      return result;
      // value 变化 → Provider fiber 的 props 变 → beginWork 不 bailout
      // → 强制子树重渲染(击穿 memo)
    },
  };
  return ctx;
}

function useContext(ctx) {
  const fiber = currentFiber;
  let f = fiber;
  while (f) {
    if (f.contextValues?.has(ctx)) return f.contextValues.get(ctx);  // 最近 Provider
    f = f.return;                                    // 向上查找
  }
  return ctx.defaultValue;
}

function readContext(ctx) {
  // 渲染期注册依赖: Provider value 变化时通知该 fiber 重渲染
  const fiber = currentFiber;
  const provider = findProvider(fiber, ctx);
  provider?.dependents.add(fiber);                   // 依赖注册(精准重渲染优化)
  return useContext(ctx);
}
```

**评分点**：
- Provider 压栈/弹栈的查找链实现
- useContext 沿 return 向上最近命中
- value 变化击穿 bailout 的机制说明
- 默认值与渲染期一致性（快照）
