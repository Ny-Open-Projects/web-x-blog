---
title: [OPT-083] useSyncExternalStore 自定义 store 怎么实现 selector 级订阅？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 笔试题, 12]
type: 笔试题
---

## OPT-083：useSyncExternalStore 自定义 store 怎么实现 selector 级订阅？

**答**：
- `useSyncExternalStore(subscribe, getSnapshot)` 是 React 18 的外部 store 标准接口：订阅变化 + 原子读取快照，天然避免 tearing。
- 性能关键在 **selector**：组件只订阅自己用到的切片（getSnapshot 返回切片），切片不变不重渲，等价 Redux 的 useSelector。
- 注意 getSnapshot 必须**返回稳定引用**（缓存切片结果），否则每次渲染都拿到新对象导致无限重渲。
- 适合中大型应用自建轻量 store（几十行）替代全局 state 管理库的重渲染风暴问题。

```jsx
// 一一对应：mini store + useSyncExternalStore 的 selector 订阅
// store.js —— 30 行实现：外部 store + 切片缓存
function createStore(initial) {
  let state = initial;
  const listeners = new Set();
  return {
    getState: () => state,
    setState(patch) {
      state = typeof patch === 'function' ? patch(state) : { ...state, ...patch };
      listeners.forEach((l) => l()); // 通知所有订阅者，组件靠 selector 决定要不要重渲
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
  };
}
export const store = createStore({ keyword: '', list: [], theme: 'dark' });

// useStore(selector)：selector 结果用引用相等做缓存，切片不变不触发重渲
export function useStore(selector) {
  return useSyncExternalStore(store.subscribe, () => {
    const slice = selector(store.getState());
    return slice; // selector 必须返回原始值或稳定引用
  });
}

// 组件只订阅自己关心的切片
function ThemeButton() {
  const theme = useStore((s) => s.theme); // keyword/list 变化时本组件不重渲
  return <button className={theme}>切换主题</button>;
}
function SearchResults() {
  const list = useStore((s) => s.list); // 只被 list 影响
  return <ul>{list.map((it) => <Row key={it.id} item={it} />)}</ul>;
}
// 搜索输入时 store.setState({ keyword }) -> 两个组件的切片均未变 -> 零重渲染
```
