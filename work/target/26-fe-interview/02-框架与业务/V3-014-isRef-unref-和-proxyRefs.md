---
title: [V3-014] isRef、unref 和 proxyRefs 的原理与应用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-014：isRef、unref 和 proxyRefs 的原理与应用？
**答**：
- isRef 判断值是否为 ref；unref 是语法糖：`isRef(v) ? v.value : v`。
- 两者让组合函数兼容 `T | Ref<T>` 入参，是 VueUse 全家桶的基础模式。
- proxyRefs 是 toRefs 的反向操作：访问/写入时自动解包 ref。
- setup 返回值、reactive 对象内嵌 ref 的自动解包都由 proxyRefs 机制完成。

```typescript
import { isRef, unref, ref, computed } from "vue";
import type { Ref } from "vue";

// 组合函数兼容两种入参：number 或 Ref<number>
function useDouble(source: number | Ref<number>) {
  return computed(() => unref(source) * 2);
}

const n = ref(4);
useDouble(n).value; // 8
useDouble(2).value; // 4

// proxyRefs：setup 返回对象在模板中自动解包 .value 的原因（示意实现）
function proxyRefs(target: Record<string, unknown>) {
  return new Proxy(target, {
    get(t, key) {
      return unref(t[key]); // 访问时自动 .value
    },
    set(t, key, value) {
      const old = t[key];
      if (isRef(old) && !isRef(value)) {
        (old as Ref<unknown>).value = value; // 旧值是 ref 且新值不是，写入 .value
        return true;
      }
      t[key] = value;
      return true;
    },
  });
}
```

## 第三章 computed、watch 与 watchEffect
