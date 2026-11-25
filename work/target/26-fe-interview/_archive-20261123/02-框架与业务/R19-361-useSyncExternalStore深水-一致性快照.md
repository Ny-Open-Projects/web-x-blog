---
title: [R19-361] useSyncExternalStore 深水：一致性快照与撕裂防护
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-361：useSyncExternalStore 深水：一致性快照与撕裂防护

**答**：
- 存在意义：并发渲染下「读到撕裂的快照」问题——低优渲染中外部 store 变化，同一棵树读到新旧混合数据；useSyncExternalStore 保证 commit 前快照一致
- 三参数：subscribe（订阅外部 store）、getSnapshot（同步读当前值，必须稳定引用）、getServerSnapshot（SSR）——getSnapshot 返回缓存对象（不每次新建）否则无限重渲染
- tearing 防护机制：渲染期间检测快照变化 → 丢弃当前渲染重来（同步重渲染）；store 库（Redux/Zustand）都迁移到该 API
- 与 useEffect+setState 订阅的对比：后者有两帧延迟 + 撕裂风险——useSyncExternalStore 是「外部源接入 React」的官方正解
- useSyncExternalStoreWithSelector：.selector 版本支持选择器 + 相等性比较（Redux 的 useSelector 内核）

```javascript
// Zustand 集成内核
useStore(selector) {
  return useSyncExternalStoreWithSelector(
    store.subscribe,
    store.getState,
    store.getState,
    selector,
    equalityFn,        // 浅比较, 防无关字段更新触发重渲染
  );
}
```
