---
title: [V3-030] Vue3 移除了 $on/$off，事件总线怎么做？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-030：Vue3 移除了 $on/$off，事件总线怎么做？
**答**：
- Vue3 实例不再是 EventEmitter，官方建议用 mitt、tiny-emitter 等独立库。
- mitt 用 Map 管理事件与处理器，支持通配符 \* 监听所有事件。
- 事件名建议用 TS 类型约束，避免魔法字符串。
- 必须在 onUnmounted 中 off，否则处理器泄漏、组件重复触发。

```typescript
// bus.ts —— Vue3 移除了 $on/$off，官方建议用 mitt 等库
import mitt from "mitt";

type Events = {
  "user-login": { id: number; name: string };
  "cart-updated": number; // 购物车数量
};

export const emitter = mitt<Events>();

// 任意组件中：
emitter.on("user-login", (payload) => console.log(payload.name));
emitter.on("*", (type, payload) => console.log(type, payload)); // 通配符监听
emitter.emit("cart-updated", 3);
emitter.off("user-login"); // 在 onUnmounted 中解绑，避免泄漏
```
