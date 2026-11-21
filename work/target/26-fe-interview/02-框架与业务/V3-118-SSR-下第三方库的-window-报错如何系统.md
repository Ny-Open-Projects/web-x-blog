---
title: [V3-118] SSR 下第三方库的 window 报错如何系统性解决？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-118：SSR 下第三方库的 window 报错如何系统性解决？
**答**：
- 报错根源：模块顶层访问 window/document，Node 环境没有这些全局对象。
- 守卫模式：封装统一的 `isServer` 判断，入口访问一律前置守卫；守卫逻辑收口在一个 env 模块，不要散落 typeof window。
- 动态导入模式：重库（echarts、编辑器）在客户端生命周期或事件回调里 `await import()`，SSR 构建不触碰其顶层代码。
- 备选：shim 假对象、构建别名替换等侵入手段，能不用就不用。

```typescript
// utils/env.ts —— 统一环境守卫，收口所有 window 判断
export const isServer = typeof window === "undefined";
export const isClient = !isServer;

// 重库动态导入：只在客户端加载，SSR 构建不会解析其顶层 window 依赖
export async function loadECharts() {
  if (isServer) return null;
  return import("echarts");
}

// 存储类 API 统一加守卫
export function readLocalStorage(key: string): string | null {
  if (isServer) return null;
  return window.localStorage.getItem(key);
}

// 组件内天然安全的位置：onMounted 只在客户端执行
// onMounted(async () => {
//   const echarts = await loadECharts(); // 此处访问 window 一定安全
//   const chart = echarts!.init(chartRef.value!);
//   chart.setOption(option);
// });
```
