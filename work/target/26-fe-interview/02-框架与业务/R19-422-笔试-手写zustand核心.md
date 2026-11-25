---
title: [R19-422] 笔试：手写 zustand 核心（create + selector + 浅比较）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 状态管理]
type: 笔试题
---

## R19-422：笔试：手写 zustand 核心

**答**：实现 `create(createState)`：① createStore：{ getState, setState, subscribe, destroy }；② setState 支持 partial 合并与函数式，且「值没变不通知」（浅比较 merged）；③ React hook：useStore(selector, equalityFn)——基于手写 useSyncExternalStore，selector 结果用 equalityFn（默认 Object.is，可选 shallow）防无关更新；④ middleware 简版：persist（JSON 存储）与 devtools 钩子。写出实现。

```javascript
function createStore(createState) {
  let state;
  const listeners = new Set();
  const setState = (partial, replace) => {
    const next = typeof partial === 'function' ? partial(state) : partial;
    if (!Object.is(next, state)) {
      const merged = replace ? next : { ...state, ...next };
      // 浅比较: 所有字段相等则不通知
      const changed = Object.keys(merged).some(k => !Object.is(merged[k], state?.[k]));
      if (changed) {
        const prev = state;
        state = merged;
        listeners.forEach(l => l(state, prev));
      }
    }
  };
  const getState = () => state;
  const subscribe = (l) => { listeners.add(l); return () => listeners.delete(l); };
  state = createState(setState, getState);
  return { setState, getState, subscribe };
}

function create(createState) {
  const store = createStore(createState);
  const useStore = (selector = (s) => s, equalityFn = Object.is) => {
    const getSnap = () => selector(store.getState());
    // 简化: 每次渲染读 selector + 订阅比较
    return useSyncExternalStoreShim(
      store.subscribe,
      () => {                                   // 缓存 selector 结果防不稳定快照
        lastSel = getSnap();
        return lastSel;
      },
    );
  };
  useStore.getState = store.getState;
  useStore.setState = store.setState;
  return useStore;
}
const shallow = (a, b) => Object.keys(a).length === Object.keys(b).length
  && Object.keys(a).every(k => Object.is(a[k], b[k]));
// 用法: useStore(s => ({ a: s.a, b: s.b }), shallow)
```

**评分点**：
- setState 浅比较不通知（避免无效渲染）
- selector + equalityFn 的细粒度订阅
- 快照缓存防不稳定 getSnapshot
- middleware（persist）扩展点
