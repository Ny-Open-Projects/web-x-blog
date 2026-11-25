---
title: [V3-168] composable 测试怎么搭环境（withSetup 工具）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-168：composable 测试怎么搭环境（withSetup 工具）？
**答**：
- composable 依赖组件上下文（onMounted、provide/inject）时，裸调用会报错；需要包一个临时组件挂载后调用。
- withSetup 工具：创建临时 App，把 composable 放进 setup 执行，把返回值存到变量再挂载。
- 测试要点：挂载后才能测生命周期钩子；provide/inject 依赖用 global.provide 注入；卸载触发 onUnmounted 验证清理逻辑。
- 纯逻辑 composable（不依赖上下文的）直接当普通函数测即可，不需要 withSetup。

```typescript
// test-utils/withSetup.ts + composables/__tests__/useMouse.spec.ts
import { createApp, defineComponent, h, type App } from "vue";

// 工具：把 composable 包进临时组件执行，拿到返回值
export function withSetup<T>(composable: () => T, options?: { provide?: Record<string, unknown> }): {
  result: T;
  app: App;
} {
  let result!: T;
  const app = createApp(
    defineComponent({
      setup() {
        result = composable(); // 在真实组件上下文里执行
        return () => h("div"); // 必须返回渲染函数，否则告警
      },
    })
  );
  Object.entries(options?.provide ?? {}).forEach(([k, v]) => app.provide(k, v));
  app.mount(document.createElement("div"));
  return { result, app };
}

// ---------- 被测 composable ----------
// composables/useOnline.ts
import { ref, onMounted, onUnmounted } from "vue";
export function useOnline() {
  const online = ref(navigator.onLine);
  const update = () => (online.value = navigator.onLine);
  onMounted(() => window.addEventListener("online", update));
  onUnmounted(() => window.removeEventListener("online", update));
  return { online };
}

// ---------- 测试 ----------
import { describe, it, expect, vi } from "vitest";
import { useOnline } from "@/composables/useOnline";

describe("useOnline", () => {
  it("在线事件触发时状态更新", () => {
    const { result, app } = withSetup(() => useOnline());
    expect(result.online.value).toBe(true);

    // 模拟离线事件
    Object.defineProperty(navigator, "onLine", { value: false, configurable: true });
    window.dispatchEvent(new Event("offline"));
    expect(result.online.value).toBe(false);

    app.unmount(); // 触发 onUnmounted，验证监听清理不报错
  });

  it("依赖 provide 的 composable 可注入测试值", () => {
    const { result } = withSetup(() => inject("theme") as string, {
      provide: { theme: "dark" },
    });
    expect(result).toBe("dark");
  });
});

import { inject } from "vue";
```
