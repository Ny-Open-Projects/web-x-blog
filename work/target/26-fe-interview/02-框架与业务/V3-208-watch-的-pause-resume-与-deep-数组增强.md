---
title: [V3-208] Vue 3.5 watch 的 pause/resume 与 deep 数组增强是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-208：Vue 3.5 watch 的 pause/resume 与 deep 数组增强是什么？
**答**：
- `pause()/resume()`：实例级暂停/恢复 watcher，暂停期间依赖照常记录但不触发回调，恢复时若有脏变更会补触发一次。
- 场景：批量导入数据时暂停所有表单校验 watcher，导入完统一 resume，避免每行导入触发 N 次校验。
- deep 数组：`watch(source, cb, { deep: [a, b] })`——对数组里的每个源做深层监听，替代多个 watch 叠加。
- 语义区分：`deep: true` 对整个 source 深遍历；`deep: [obj1, obj2]` 只对指定项深，粒度可控性能更好。
- 追问钩子：pause 恢复后触发几次？——只按最新状态触发一次（类似 debounce 的合并语义），不会把暂停期间每次变更都重放。

```javascript
import { watch, reactive } from 'vue';
const form = reactive({ a: { deep: 1 }, b: { deep: 2 } });
// 3.5：只对 a、b 深监听，粒度可控
watch([() => form.a, () => form.b], (v) => save(v), {
  deep: [form.a, form.b],
});
const { pause, resume } = watch(() => form.a.deep, sync);
// 批量导入期间静默
pause();
bulkImport(bigData); // 期间 sync 不执行
resume();            // 恢复且只触发一次，用最新值
```
