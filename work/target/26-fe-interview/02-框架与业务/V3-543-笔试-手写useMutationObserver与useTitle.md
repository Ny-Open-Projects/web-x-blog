---
title: [V3-543] 笔试：手写 useMutationObserver 与 useTitle
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## V3-543：笔试：手写 useMutationObserver

**答**：实现：① `useMutationObserver(targetRef, cb, options)`：观察 DOM 变化（childList/attributes/subtree 透传），target 动态变化重绑，卸载断开；② 防抖选项（debounce ms——DOM 高频变化合批）；③ `useTitle(newTitle, { template = '%s' })`：响应式更新 document.title，路由 meta 联动示例；④ observer 回调记录记录（MutationRecord）的裁剪说明。写出实现。

```javascript
export function useMutationObserver(targetRef, cb, { debounce: deb, ...options } = {}) {
  let mo = null;
  const handler = deb
    ? useDebounceFn((muts) => cb(muts, mo), deb)
    : cb;
  watch(targetRef, (el) => {
    mo?.disconnect();
    if (!el) return;
    mo = new MutationObserver(handler);
    mo.observe(el, options);
  }, { immediate: true, flush: 'post' });
  onScopeDispose(() => mo?.disconnect());
  return { stop: () => mo?.disconnect() };
}

export function useTitle(newTitle, { template = '%s' } = {}) {
  const title = ref(toValue(newTitle));
  watch(title, (t) => { document.title = t ? template.replace('%s', t) : document.title; },
    { immediate: true });
  watch(newTitle, (v) => title.value = toValue(v));
  return title;
}
// 路由联动:
watch(() => route.meta.title, (t) => useTitleShared(t));   // 单例 title ref
// 注意: MutationRecord 含节点引用, 回调长期持有会泄漏 — cb 内只取需要的信息
```

**评分点**：
- target 动态重绑（watch flush post 保证 DOM 就绪）
- 防抖合批（DOM 高频变化场景）
- MutationRecord 持有节点引用的泄漏提示
- useTitle 的 template 与外部输入源联动
