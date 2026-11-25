---
title: [V3-524] 笔试：手写 customRef（防抖 ref 与异步校验 ref）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 语言特性]
type: 笔试题
---

## V3-524：笔试：手写 customRef

**答**：用 customRef 实现：① `debouncedRef(value, delay)`：写入后 delay 毫秒才真正更新并触发（输入联想场景）；② 读取始终返回最新已提交值（未提交的写不生效）；③ 组件卸载时 flush 挂起写（不丢最后一次输入）；④ `asyncValidatedRef(value, validator)`：写入先过异步校验，通过才提交，期间 isPending 状态暴露。写出实现。

```javascript
import { customRef, getCurrentScope, onScopeDispose } from 'vue';

function debouncedRef(value, delay = 200) {
  let timer, pending;
  return customRef((track, trigger) => {
    if (getCurrentScope())
      onScopeDispose(() => {                   // 卸载 flush
        clearTimeout(timer);
        if (pending != null) { value = pending; pending = null; }
      });
    return {
      get() { track(); return value; },
      set(nv) {
        pending = nv;
        clearTimeout(timer);
        timer = setTimeout(() => { value = nv; pending = null; trigger(); }, delay);
      },
    };
  });
}

function asyncValidatedRef(value, validator) {
  let committed = value, pending = null;
  const state = { isPending: false, error: null };
  return { ref: customRef((track, trigger) => ({
    get() { track(); return committed; },
    set(nv) {
      pending = nv; state.isPending = true; state.error = null; trigger();
      Promise.resolve(validator(nv)).then(ok => {
        if (pending === nv && ok) { committed = nv; state.isPending = false; trigger(); }
        else if (!ok) { state.error = 'invalid'; state.isPending = false; trigger(); }
      });
    },
  })), state };
}
// 用法: v-model="debouncedQuery" → 输入不卡, 请求按 300ms 节流
```

**评分点**：
- customRef 的 track/trigger 语义正确（get 中 track，提交后 trigger）
- 卸载 flush 防最后一次输入丢失
- 异步校验的 pending/committed 双值与竞态守卫（pending === nv）
- 与 watch+debounce 方案的对比（绑定侧自动节流）
