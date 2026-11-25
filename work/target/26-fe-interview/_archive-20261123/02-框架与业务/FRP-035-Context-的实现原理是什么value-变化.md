---
title: [FRP-035] Context 的实现原理是什么？value 变化时如何精准通知消费者？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-035：Context 的实现原理是什么？value 变化时如何精准通知消费者？

**答**：
- `createContext` 创建 `{ $$typeof, _currentValue, Provider, Consumer }` 对象；Provider 渲染时把 value 写入 `_currentValue`。
- 消费侧（useContext）从当前 Fiber 沿 `return` 链**向上查找**最近的 Provider fiber（React 16.3+ 不再用栈游标，改为逐层向上 + 剪枝）。
- 精准通知：render 阶段 beginWork 时检查 `fiber.dependencies`（消费了哪些 context），Provider 的 value 变了就给**所有消费它的子孙 fiber** 打上 Update 标记，没有消费的子树被 bailout（跳过）。
- 性能要点：value 是新对象每次都通知所有消费者——大 context 应拆分或改用 selector 订阅（zustand/useSyncExternalStore）。

```javascript
// 简化实现，帮助理解 Context 查找与通知
const contextRegistry = new Map(); // Provider fiber -> value

function createContext(defaultValue) {
  const context = { $$typeof: Symbol('react.context'), _defaultValue: defaultValue };
  context.Provider = { $$typeof: Symbol('react.provider'), context };
  return context;
}

function pushProvider(providerFiber, value) {
  contextRegistry.set(providerFiber, value); // Provider render 时记录 value
}

function useContext(context) {
  let fiber = currentFiber;
  // 沿 return 链向上找最近的 Provider
  while (fiber) {
    if (fiber.type?.$$typeof === Symbol('react.provider') && fiber.type.context === context) {
      return contextRegistry.get(fiber);
    }
    fiber = fiber.return;
  }
  return context._defaultValue;
}

// 值变化时的传播（beginWork 内，示意）
function beginWorkWithProviderCheck(fiber, oldProps) {
  if (fiber.type?.$$typeof === Symbol('react.provider')) {
    const newValue = fiber.pendingProps.value;
    const oldValue = contextRegistry.get(fiber);
    if (!Object.is(oldValue, newValue)) {
      propagateContextChange(fiber, fiber.type.context); // 给消费者打标记
    }
    pushProvider(fiber, newValue);
  }
}
function propagateContextChange(providerFiber, context) {
  // 深入遍历子树，dependencies 里登记了该 context 的 fiber 强制更新
  // 未消费的兄弟子树被 bailout，不重新 render —— 这就是精准通知
}
```
