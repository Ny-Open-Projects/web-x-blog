---
title: [FRP-368] 笔试：手写跨框架 store 适配器（React/Vue 双绑定）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-368：笔试：手写跨框架 store 适配器

**答**：给一个内核 store（get/set/sub），实现双框架绑定：① React 版 `useStoreReact(store, selector, equalityFn)`：基于 useSyncExternalStore 语义（快照缓存 + selector 比较防无效渲染）；② Vue 版 `useStoreVue(store, selector)`：customRef（读 track、变更 trigger）；③ 两者卸载清理（sub 的 dispose 调用）；④ selector 结果稳定性（引用比较失败时浅比较兜底选项）；⑤ 撕裂防护说明（React 侧为何必须快照化）。写出实现。

```javascript
// React 绑定
function useStoreReact(store, selector = (s) => s, equalityFn = Object.is) {
  const lastRef = useRef({ value: undefined, init: false });
  const getSnapshot = () => {
    const next = selector(store.get());
    if (!lastRef.current.init || !equalityFn(next, lastRef.current.value)) {
      lastRef.current = { value: next, init: true };   // 缓存: 引用稳定
    }
    return lastRef.current.value;
  };
  return useSyncExternalStore(store.sub, getSnapshot);   // 快照化防撕裂
}

// Vue 绑定
function useStoreVue(store, selector = (s) => s) {
  return customRef((track, trigger) => {
    const unsub = store.sub(() => trigger());            // 变更触发
    onScopeDispose(unsub);                               // 卸载清理
    return {
      get() { track(); return selector(store.get()); },  // 读时收集
      set(v) { store.set(v); },
    };
  });
}
// 撕裂防护: React 并发渲染中, 渲染期快照必须一致
// — useSyncExternalStore 保证 commit 前读到同一值; Vue 无并发渲染故 customRef 足够
```

**评分点**：
- React 侧快照缓存（selector 结果引用稳定，防死循环）
- equalityFn 扩展（浅比较防无关字段更新）
- Vue customRef 的 track/trigger 语义
- 双侧卸载清理与撕裂防护的框架差异说明
