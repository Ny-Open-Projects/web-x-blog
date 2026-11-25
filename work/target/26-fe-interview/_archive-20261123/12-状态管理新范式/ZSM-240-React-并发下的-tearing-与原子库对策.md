---
title: [ZSM-240] React 并发渲染下的 tearing 是什么原子库怎么防
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-240：React 并发渲染下的 tearing 是什么，原子库怎么防

**答**：
- tearing（撕裂）：一次更新里不同组件在同一渲染批次读到不同版本的外部 store 状态，导致 UI 内部不一致
- 根因：外部 store 是同步全局值，React 并发渲染分片执行时时间片之间外部状态又变了；React 18 提供 `useSyncExternalStore` 让读取与版本绑定，库层接入即免疫
- Jotai/Valtio/Zustand 均已基于 useSyncExternalStore 实现：getSnapshot 必须返回稳定值（同一版本两次调用同引用），getServerSnapshot 处理 SSR
- 自写订阅库时的检查点：snapshot 缓存（不要每次返回新对象）+ 版本号比较 + transition 内不触发外部写入

```javascript
// 库的底层形态（简化）
const subscribe = (cb) => store.sub(cb)
const getSnapshot = () => store.get(atom)   // 必须引用稳定
useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot)
```
