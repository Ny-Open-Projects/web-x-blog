---
title: [ZSM-311] 浏览器前进/后退与 bfcache 下状态怎么恢复
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-311：浏览器前进/后退与 bfcache 下状态怎么恢复

**答**:
- bfcache（往返缓存）：页面进历史栈时整页快照（含 JS 内存），返回时直接恢复——store 内存态天然保留，但要注意 pagehide/persisted 判断与重新激活事件
- 关键坑：恢复后服务端数据可能已变（Query 缓存陈旧），`pageshow` 事件里 `event.persisted === true` 时触发失效/重连（WS 断了要重连）
- 非 bfcache 路径（正常刷新）：URL 是唯一恢复源，这就是「可恢复状态进 URL」的根本原因
- 实践清单：pageshow 恢复连接（WS/轮询）、重新校验会话、刷新时间敏感缓存、resumePausedMutations

```javascript
window.addEventListener('pageshow', (e) => {
  if (e.persisted) {                         // 从 bfcache 恢复
    queryClient.invalidateQueries({ stale: true })   // 陈旧缓存后台刷新
    reconnectWS()
    queryClient.resumePausedMutations()
  }
})
```
