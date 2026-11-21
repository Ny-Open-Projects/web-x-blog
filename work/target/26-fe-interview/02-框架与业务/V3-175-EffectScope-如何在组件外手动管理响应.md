---
title: [V3-175] EffectScope 如何在组件外手动管理响应式作用域？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-175：EffectScope 如何在组件外手动管理响应式作用域？
**答**：
- effectScope 收集其内部创建的 effect/computed/watch，scope.stop() 一次性全部销毁——组件卸载时源码就是这么清理的。
- 组件外创建响应式系统（跨 tab 工具、Node 脚本、单例 store 库）必须手动 scope，否则 watch 永不释放造成内存泄漏。
- 嵌套 scope：子 scope 随父 scope 一起 stop；detached 参数让子作用域独立存活。
- composable 里若在组件外被调用（如全局单例），用 getCurrentScope + onScopeDispose 注册清理，等价于组件里的 onUnmounted。

```typescript
// src/reactive/scope-demo.ts —— 组件外手动管理响应式
import {
  reactive, computed, watch, watchEffect, effectScope, getCurrentScope, onScopeDispose,
} from "vue";

// 场景：跨页面共享的全局配置中心（组件外创建）
export function createConfigStore() {
  // 必须用 scope 包住：否则这里的 watch 永远不会被回收
  const scope = effectScope();

  const state = reactive({ theme: "light", locale: "zh-CN", menus: [] as string[] });
  const isDark = computed(() => state.theme === "dark");

  scope.run(() => {
    // 这些副作用全部登记进 scope
    watchEffect(() => document.documentElement.dataset.theme = state.theme);
    watch(() => state.locale, (v) => console.log("locale changed", v));

    // 在 scope 内注册清理回调（组件外等价于 onUnmounted）
    if (getCurrentScope()) {
      onScopeDispose(() => console.log("config store 已销毁，清理监听"));
    }
  });

  return {
    state,
    isDark,
    destroy: () => scope.stop(), // 一键销毁所有副作用
  };
}

// 用法：HMR 或单页应用重建 store 时调用 destroy，避免旧 watch 残留
// export const configStore = createConfigStore();
// if (import.meta.hot) import.meta.hot.dispose(() => configStore.destroy());

// detached：子作用域独立于父作用域
// const parent = effectScope();
// parent.run(() => {
//   const child = effectScope(true); // detached：parent.stop() 不会停掉 child
//   child.run(() => watch(state, cb));
// });
```
