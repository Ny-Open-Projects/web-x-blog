---
title: [WCN-984] Signals + islands + SSR 结合：局部水合岛之间信号怎么共享快照
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-984：Signals + islands + SSR 结合：局部水合岛之间信号怎么共享快照

**答**：
- 结论先行：islands 各自独立水合，但共享状态（购物车数量/登录态）要跨岛同步——靠「SSR 快照下沉 + 各岛订阅同一 signal slice + 事件广播」，而非全局单例运行时。
- 快照下沉：服务端把共享信号序列化进 HTML（如 `window.__SNAPSHOT__` 或 script 标签），各岛 hydrate 时从快照初始化自己的 signal，保证首屏一致。
- 订阅切片：每个岛只订阅自己关心的 signal 字段（computed selector），避免一岛写全岛重渲染；写操作通过统一 store 派发。
- 跨岛同步：store 变更用 CustomEvent/BroadcastChannel 广播，其他岛的 slice 对应更新；或共用同一 signal 实例（若同 realm）。
- 追问钩子：面试官问「岛之间不同 realm（iframe）怎么同步」——答： BroadcastChannel/postMessage 传快照，各 realm 独立 store，靠版本号对齐。

```javascript
// SSR 快照下沉 + 各岛订阅 slice
const snapshot = JSON.parse(document.getElementById('__SNAP__').textContent);
// { cartCount: 3, user: 'Ada' }
function makeStore(s) {
  const listeners = new Set();
  return { get: k => s[k],
    set(k, v) { s[k] = v; listeners.forEach(f => f(k, v)); },
    subscribe(f) { listeners.add(f); } };
}
const store = makeStore({ ...snapshot });
// 购物车岛只订阅 cartCount
store.subscribe((k, v) => { if (k === 'cartCount') document.getElementById('badge').textContent = v; });
store.set('cartCount', 4); // 跨岛同步 badge
```
