---
title: [ZSM-083] TanStack Query 的 networkMode 与离线排队：断网时查询和 mutation 各是什么行为？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-083：TanStack Query 的 networkMode 与离线排队：断网时查询和 mutation 各是什么行为？
**答**：
- networkMode 三档：online（默认，断网暂停请求）、offlineFirst（先试缓存/请求一次失败再暂停，配合 SW 场景）、always（不管网络直接发）。
- 断网时查询暂停并保持 isPaused；恢复联网后自动继续（配合 refetchOnReconnect 重取）。
- mutation 默认 online：断网时暂停**排队**，联网后按顺序重放——可用于「离线点赞/发消息」乐观列表。
- 离线重放的坑：mutationFn 依赖本地上下文（token、门店 id）在重放时可能已过期；重放前要校验，或用 retry/暂停开关控制。

```javascript
// 离线可发送的消息
const sendMsg = useMutation({
  mutationFn: api.send,
  networkMode: 'offlineFirst',   // 先尝试发一次
})
// 断网时 sendMsg.mutate(msg) 进入队列，联网自动重放
// 全局开关
const online = useIsOnline() // useOnlineStatus
if (!online) ui.showBanner('消息将在联网后送达')
```
