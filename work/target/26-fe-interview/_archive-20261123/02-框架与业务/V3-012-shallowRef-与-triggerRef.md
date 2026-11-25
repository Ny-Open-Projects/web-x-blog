---
title: [V3-012] shallowRef 与 triggerRef 的用途是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-012：shallowRef 与 triggerRef 的用途是什么？
**答**：
- shallowRef 只有 `.value` 被整体替换时才触发更新，内部数据不是响应式。
- 适合大数组、大对象、地图实例、第三方图表实例等重资源，避免深层代理开销。
- 内部变更后想强制更新，调用 triggerRef 手动触发依赖。
- 这也是"不可变数据风格"的性能优化路径：永远整体替换。

```vue
<script setup lang="ts">
import { shallowRef, triggerRef } from "vue";

const bigList = shallowRef<Array<number>>([]);

// 整体替换会触发更新
bigList.value = Array.from({ length: 10000 }, (_, i) => i);

// 内部变更不会触发更新
bigList.value.push(10001);

// 强制触发更新（避免整包替换大数组的开销）
triggerRef(bigList);
</script>
```
