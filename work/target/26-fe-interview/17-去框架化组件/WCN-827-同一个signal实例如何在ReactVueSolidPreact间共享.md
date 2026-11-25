---
title: [WCN-827] 同一个 signal 实例如何在 React/Vue/Solid/Preact 之间共享？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-827：同一个 signal 实例如何在 React/Vue/Solid/Preact 之间共享？

**答**：
- 结论先行：跨框架共享 signal 的关键是「统一底层原语 + 各框架薄适配层」——用 TC39 兼容的 signal（如 `signal-polyfill` 或 `@preact/signals-core`）作公共源，各框架只做「读取并触发本框架更新」的桥接。
- 为什么能共享：这些库的 signal 都是「对象引用 + get/set + 依赖追踪」，本身不绑定任何框架的渲染；框架适配层负责在 signal 变化时调用自己的更新机制（React 用 `useSyncExternalStore`，Vue 用 `ref` 包装，Solid 直接当 signal 用）。
- 各框架桥法：React 用 `useSignalValue(s)` = `useSyncExternalStore(s.subscribe, () => s.value)`；Vue 用 `customRef` 把 signal 包装成 ref；Solid/Preact 原生兼容，几乎零成本。
- 边界：相等性语义、批量时机、SSR 行为各框架可能不同——共享时要统一「在哪个层级 flush」「值比较策略」，否则会出现两个框架看到不一致的中间态。
- 追问钩子：面试官会问「React 里改了 signal，Vue 组件会立刻更新吗」——答：会，因为共享同一个 signal 实例，写入触发所有订阅者；但要靠各框架的适配层都正确订阅，且调度时机协调好。

```javascript
// 公共 signal 源（框架无关）
import { signal } from '@preact/signals-core';
export const sharedCount = signal(0);

// React 适配层：useSyncExternalStore 桥接
import { useSyncExternalStore } from 'react';
function useSignalValue(s) {
  const subscribe = useCallback(cb => s.subscribe(() => cb()), [s]); // 简化示意
  return useSyncExternalStore(subscribe, () => s.value);
}
// React 组件：const n = useSignalValue(sharedCount);
// Vue 组件：const n = customRef((track, trigger) => ({
//   get() { track(); return sharedCount.value; },
//   set(v) { sharedCount.value = v; trigger(); },
// }));
// 任一框架 sharedCount.value++ → 所有框架订阅者同步更新
```
