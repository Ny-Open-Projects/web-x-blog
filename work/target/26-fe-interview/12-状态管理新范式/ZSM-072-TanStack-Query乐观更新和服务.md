---
title: [ZSM-072] 乐观更新在多标签页/多设备并发下怎么保证一致？失效兜底策略怎么设计？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-072：乐观更新在多标签页/多设备并发下怎么保证一致？失效兜底策略怎么设计？
**答**：
- 乐观值只是本端假设；多端并发时服务端才是唯一权威。策略=「乐观提体验 + 失效对真相」：onSettled 必invalidate，不依赖 onError 才对齐。
- 请求序号/版本号：mutation 携带 baseVersion，服务端检测冲突返回 409，前端回滚并提示合并（IM 消息、协作文档场景）。
- Query 级辅助：refetchOnWindowFocus（切回窗口对齐真相）、广播 manager（多标签页共享 QueryClient 缓存与失效）。
- 兜底底线：乐观更新失败率高的接口（弱网）降级为悲观；对用户可感知的回滚要给提示，不能静默闪变。

```javascript
// 冲突检测式乐观更新
onMutate: async ({ id, baseVersion }) => {
  /* ...快照与乐观写... */
},
onError: (e, v, ctx) => {
  qc.setQueryData(['docs', v.id], ctx.prev)
  if (e.status === 409) openConflictDialog(e.serverVersion) // 版本冲突走人工合并
},
onSettled: () => qc.invalidateQueries({ queryKey: ['docs'] }), // 无论如何对齐服务端
```
