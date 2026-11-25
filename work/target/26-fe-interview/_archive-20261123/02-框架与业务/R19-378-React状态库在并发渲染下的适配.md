---
title: [R19-378] React 状态库在并发渲染下的适配
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 状态管理]
type: 面试题
---

## R19-378：React 状态库在并发渲染下的适配

**答**：
- tearing 防护：库必须用 useSyncExternalStore（Redux 8/Zustand 4+）——旧版 setState 订阅在并发下撕裂
- update 批处理语义：React 18+ 自动批处理（包括 setTimeout/原生事件内的多次 setState）——库的 dispatch 多次调用合并为一次渲染
- selector 与相等性：细粒度 selector + 浅比较（防无关字段触发渲染）；不可变更新（结构共享）让浅比较有效
- transition 兼容：库的 setState 若总是同步优先级，Transition 场景失效——支持「带优先级的更新」（zustand 的 transient updates / startTransition 包装指导）
- 服务端状态库（React Query）与客户端状态库的分工：Query 管「缓存 + 竞态 + 重试」，Zustand 管「UI 态」——混用反模式盘点

```javascript
// zustand 并发适配要点
const useStore = create((set) => ({ count: 0 }));
// 选择器 + 默认 Object.is
const count = useStore((s) => s.count);
// transition 兼容:
startTransition(() => useStore.setState({ bigList: newList }));  // 库更新也走低优
```
