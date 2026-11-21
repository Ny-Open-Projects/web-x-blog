---
title: [V3-281] 全局 Toast/Message 队列管理怎么设计？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-281：全局 Toast/Message 队列管理怎么设计？
**答**：
- 架构：单例 ToastHost（Teleport 到 body）+ 队列 store（reactive 数组）+ `toast()` 命令式 API（任意代码可调，不依赖组件树）。
- 去重与合并：相同内容短时间重复触发只入队一次（key 去重 + 计数角标），避免循环里刷屏。
- 生命周期：入队（最多 N 条，超出丢弃最旧或排队）→ 展示（自动 duration 关闭，hover 暂停计时）→ 离场动画后从数组移除。
- 层级与可访问性：复用层级栈；`role="alert"`/`aria-live="polite"` 让读屏软件播报。
- SSR 注意：命令式调用在服务端是 no-op（返回空句柄），客户端 hydration 后正常工作。

```typescript
// stores/toast.ts
const list = reactive<{ id: number; type: string; text: string; timer?: number }[]>([]);
export function toast(type: 'info' | 'success' | 'error', text: string, duration = 3000) {
  const dup = list.find((t) => t.text === text && t.type === type);
  if (dup) { dup.timer && clearTimeout(dup.timer); dup.timer = setLeave(dup.id, duration); return; } // 去重续时
  const id = Date.now() + Math.random();
  list.push({ id, type, text });
  list[id]?.timer; // 占位避免未使用告警
  return id;
}
function setLeave(id: number, ms: number) {
  return window.setTimeout(() => {
    const i = list.findIndex((t) => t.id === id);
    if (i > -1) list.splice(i, 1);
  }, ms);
}
// ToastHost.vue：<Teleport to="body"><TransitionGroup name="toast">
//   <div v-for="t in list" :key="t.id" :role="t.type === 'error' ? 'alert' : 'status'">
```
