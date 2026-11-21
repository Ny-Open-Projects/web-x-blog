---
title: [ZSM-354] WS 断线重连后客户端状态重建的三种策略
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-354：WS 断线重连后客户端状态重建的三种策略

**答**:
- 策略一：快照重建（重连拉全量）——简单可靠，适合状态小的房间/面板；策略二：seq 续传（服务端从断点 seq 补发事件）——实时性好，要求服务端缓冲；策略三：失效重拉（把相关 Query invalidate）——复用现有缓存体系，粒度粗
- 选择依据：状态体积（大 → 续传/失效）、一致性要求（强 → 快照）、离线时长（长 → 直接快照）
- 混合默认：短断线用 seq 续传，长断线/校验失败升级快照——按离线时长阈值切换
- 重建期间 UI：显示「同步中」而非直接展示半新半旧；重建完成前禁止新的本地写入（防旧事件覆盖新操作）

```javascript
ws.onopen = async () => {
  const gap = Date.now() - disconnectedAt
  if (gap < 30_000 && lastSeq) send({ type: 'resume', fromSeq: lastSeq })   // 续传
  else await rebuildFromSnapshot()                                          // 快照
  setSyncing(false)
}
// 重建期写保护：syncing 时提交按钮禁用
```
