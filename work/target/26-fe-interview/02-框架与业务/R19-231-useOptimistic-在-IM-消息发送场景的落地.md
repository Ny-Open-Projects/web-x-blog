---
title: [R19-231] IM 发消息场景怎么用 useOptimistic 落地？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-231：IM 发消息场景怎么用 useOptimistic 落地？
**答**：
- 乐观消息带本地临时 id + status: 'sending'，立即上屏在列表尾部；action 成功后服务端返回正式 id，队列清空、serverState 更新。
- 失败：消息回到「失败态」显示重发按钮（UI 层把回滚后的消息保留在草稿区，或依赖 serverState 中的 failed 记录）。
- 排序稳定性：乐观消息固定在队尾，不参与服务端消息的乱序排序，确认后归位。
- 并发：多条消息连续发送共用一个 action 入口，队列保证顺序；WebSocket 推送来的新消息在 serverState 层合并。
- 关键点：乐观层只管「我的发送」，收消息是另一条数据流，别混在一个 reducer。
