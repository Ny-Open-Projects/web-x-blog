---
title: [V3-394] 笔试：手写 useDebounceFn composable（含组件卸载自动清理）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-394：笔试：手写 useDebounceFn composable（含组件卸载自动清理）
**题**：实现 `useDebounceFn(fn, wait)`：返回防抖函数；支持 cancel/flush 方法；组件卸载时自动 cancel（不漏触发）；onScopeDispose 实现自动清理。

```javascript
import { onScopeDispose, getCurrentScope } from 'vue'
function useDebounceFn(fn, wait = 300) {
  let timer = null
  const debounced = (...args) => {
    if (timer) clearTimeout(timer)
    timer = setTimeout(() => { timer = null; fn(...args) }, wait)
  }
  debounced.cancel = () => { if (timer) { clearTimeout(timer); timer = null } }
  debounced.flush = () => { if (timer) { clearTimeout(timer); timer = null; fn() } }
  if (getCurrentScope()) onScopeDispose(() => debounced.cancel()) // 组件卸载自动清理
  return debounced
}
// 用法：const search = useDebounceFn(q => fetchList(q), 300)
```
**评分点**：
- timer 生命周期管理正确（cancel/flush 均清 timer）。
- 用 onScopeDispose + getCurrentScope 做卸载清理，且在非组件上下文调用不报错。
- flush 触发 pending 调用。
- 说明卸载后触发 debounced 不会再执行（timer 被清但新调用仍会建 timer——能答出这个边界加分）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-60f5f368-d21a-445b-8d5c-de89934c5fe8-cwd'; fi
exit "$__zcode_status"
