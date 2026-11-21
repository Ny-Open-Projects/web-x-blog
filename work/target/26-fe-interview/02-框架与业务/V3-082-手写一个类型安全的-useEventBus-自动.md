---
title: [V3-082] 手写一个类型安全的 useEventBus（自动 off）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-082：手写一个类型安全的 useEventBus（自动 off）？
**答**：
- 用泛型映射类型约束事件名与 payload 类型：`Events extends Record<string, unknown>`，emit/on 双端都受编译期检查。
- createEventBus 内部用 Map<string, Set<Function>> 存储订阅，同一事件多订阅者互不影响。
- useEventBus 订阅即返回，组件卸载时 onScopeDispose 自动 off，杜绝手写解绑造成的内存泄漏。
- 返回的 off 也可提前手动解绑。

```typescript
// composables/useEventBus.ts
import { onScopeDispose } from "vue";

export interface EventBus<Events extends Record<string, unknown>> {
  on<K extends keyof Events>(type: K, handler: (payload: Events[K]) => void): void;
  off<K extends keyof Events>(type: K, handler: (payload: Events[K]) => void): void;
  emit<K extends keyof Events>(type: K, payload: Events[K]): void;
}

export function createEventBus<Events extends Record<string, unknown>>(): EventBus<Events> {
  const map = new Map<keyof Events, Set<(payload: never) => void>>();
  return {
    on(type, handler) {
      if (!map.has(type)) map.set(type, new Set());
      map.get(type)!.add(handler as (payload: never) => void);
    },
    off(type, handler) {
      map.get(type)?.delete(handler as (payload: never) => void);
    },
    emit(type, payload) {
      map.get(type)?.forEach((handler) => (handler as (p: unknown) => void)(payload));
    },
  };
}

// 事件表：key 是事件名，value 是 payload 类型
interface AppEvents {
  "user:login": { id: number; name: string };
  "cart:changed": { count: number };
}

const bus = createEventBus<AppEvents>();

// 组件里使用：卸载自动解绑
export function useEventBus<K extends keyof AppEvents>(
  type: K,
  handler: (payload: AppEvents[K]) => void
) {
  bus.on(type, handler);
  onScopeDispose(() => bus.off(type, handler)); // 自动清理，防泄漏
  return () => bus.off(type, handler); // 也可提前手动解绑
}
```
