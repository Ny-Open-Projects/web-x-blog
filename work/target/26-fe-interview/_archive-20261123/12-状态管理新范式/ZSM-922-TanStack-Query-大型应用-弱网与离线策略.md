---
title: [922] 弱网/离线场景下 TanStack Query 的策略
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 离线]
type: 面试题
---

## 922：弱网/离线场景下 TanStack Query 的策略

**答**：
- 读策略：offlineFirst networkMode（有缓存先用、网络失败不立即报错）+ 长 staleTime 域（登录后预热核心数据，离线也能干活）。
- 写策略：mutation 的 pauseOffline——离线 mutation 进队列，恢复网络后重放；重放的幂等（idemKey）必须配套（队列语义是 at-least-once）。
- 状态可视：离线队列状态给用户可见（「3 个操作待同步」——未告知的离线队列是用户困惑之源）；networkStatus 驱动 UI 徽标。
- 冲突处理：离线重放遇到服务端已变化（版本冲突 409）——走冲突 UI（覆盖/放弃/合并三选），不静默失败。

```ts
const m = useMutation({
  mutationFn: v => submit({ ...v, idemKey: v.localId }),  // 重放幂等
  networkMode: 'offlineFirst',
});
// 恢复网络：由在线监听触发
window.addEventListener('online', () => qc.resumePausedMutations());
```

