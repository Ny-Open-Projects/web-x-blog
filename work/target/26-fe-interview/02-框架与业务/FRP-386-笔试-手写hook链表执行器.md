---
title: [FRP-386] 笔试：手写 hook 链表执行器（顺序约束检测）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-386：笔试：手写 hook 链表执行器

**答**：实现 React hooks 内核模拟：① `runComponent(fn, fiber)`：fn 内调用 useState/useEffect——hooks 按调用序挂 fiber.hooks 链；② 顺序约束检测：本次调用序与上次链不一致 → 抛「Rendered fewer hooks than expected」类错误（React 报错语义复现）；③ useState 的更新批处理（多次 setState 合并一次重跑）；④ useEffect 的「提交后执行」（模拟 commit 钩子）；⑤ StrictMode 双跑支持。写出实现。

```javascript
let currentFiber = null, hookIndex = 0;

function useState(initial) {
  const fiber = currentFiber;
  const hooks = fiber.hooks ?? (fiber.hooks = []);
  if (hookIndex >= hooks.length) {
    hooks.push({ state: typeof initial === 'function' ? initial() : initial, queue: [] });
  } else {
    const hook = hooks[hookIndex];
    hook.queue.forEach((a) => { hook.state = typeof a === 'function' ? a(hook.state) : a; });
    hook.queue = [];
  }
  const i = hookIndex++;
  const dispatch = (action) => {
    hooks[i].queue.push(action);
    scheduleFiber(fiber);                            // 批处理: 合并重跑
  };
  return [hooks[i].state, dispatch];
}

function runComponent(fn, fiber, { strict = false } = {}) {
  const prevHookCount = fiber.hooks?.length ?? 0;
  hookIndex = 0;
  const runs = strict ? [0, 1] : [0];                // StrictMode 双跑
  let output;
  for (const run of runs) {
    currentFiber = fiber; hookIndex = 0;             // 每轮重挂, finally 清空不跨轮生效
    try { output = fn(fiber.props); }
    finally { currentFiber = null; }
  }
  // 顺序约束: 本次 hook 数与上次不同(减少) → 报错
  if (fiber.hooks && hookIndex < prevHookCount && prevHookCount > 0)
    throw new Error(`Rendered fewer hooks than expected. ${hookIndex} < ${prevHookCount}`);
  // 提交后执行 effects
  fiber.effects?.forEach((e) => e());
  return output;
}
// 时序: useState 顺序挂链 → 条件调用 hooks → 链错位 → 抛错(React 行为复现)
```

**评分点**：
- hooks 按序挂链 + 顺序约束检测（fewer/more hooks 报错语义）
- setState 批处理（queue 合并一次重跑）
- StrictMode 双跑与 hookIndex 重置
- effects 的「提交后」模拟

## 变体与延伸（补充）

**变体与延伸**：

1. 顺序检测只看 hook 数量够吗？ → 不够。useState 换成 useEffect 数量不变但语义错位；真实 React 靠 dispatcher 校验类型，模拟里应逐位记录 type 并比对，才能复现真实报错。
2. StrictMode 双跑时 useState 的初始化函数会被调两次吗？ → 会。React 在 dev 下故意重复调用以暴露非纯逻辑，所以 initial 必须纯，不能在里面发请求、读随机数或写外部变量。
3. 在 render 期调用 dispatch 会怎样？ → 等于渲染中触发渲染，真实 React 会告警并可能死循环；模拟里应在 runComponent 执行期间让 dispatch 抛错或入队到下一轮。
