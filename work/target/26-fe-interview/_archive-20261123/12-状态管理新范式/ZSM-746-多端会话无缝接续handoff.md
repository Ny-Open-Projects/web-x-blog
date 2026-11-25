---
title: [ZSM-746] 多端会话无缝接续（handoff）：从手机切桌面的状态迁移
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-746：多端会话无缝接续（handoff）：从手机切桌面的状态迁移

**答**：
- 「手机看一半，桌面接着看」的状态迁移叫 handoff，需要迁移的是**会话上下文**而非全量状态：当前位置（滚动/页码/播放进度）、未完成草稿（表单/评论）、临时选择（多选集合）。迁移协议三步：1) 源端 `exportSession()` 产出会话快照（紧凑 JSON，<4KB，含 schemaVersion）；2) 传输（服务端中转的 handoff 通道或账号绑定的设备推送）；3) 目标端 `importSession()` 校验版本后恢复。
- 传输通道选型：**服务端中转**为主（源端上传会话快照 → 目标端拉取，账号维度单活跃会话槽）；不直连（两端可能不同网络）。快照存 Redis/DB 带 TTL（5 分钟过期——过期 handoff 无意义）。
- 恢复语义分级：位置类直接恢复（滚动到锚点、页码跳转）；草稿类**提示确认**（「检测到未完成的草稿，恢复？」——草稿可能已被源端继续编辑，静默覆盖危险）；选择类视业务（多选通常不迁移，会话语义变了）。
- 冲突与双活：handoff 期间源端还在编辑（用户切回）——「会话所有权」要显式转移（源端进入只读或提示已接管），防止两端同时写同一草稿。简单做法：快照带 `takenAt`，目标端导入后源端下次保存时收到「会话已转移」409。
- 追问钩子：handoff 与「多端同步」的区分——同步是持续的一致性（购物车），handoff 是一次性的上下文交接（会话快照）；别用同步协议做 handoff（过重），也别用 handoff 做同步（会丢）。

```javascript
// Handoff 协议
class SessionHandoff {
  #collectSnapshot() {
    return {
      schemaVersion: 2,
      takenAt: Date.now(),
      route: router.currentRoute.fullPath,
      scroll: { anchorId: getVisibleAnchorId() },        // 锚点而非像素（内容自适应）
      player: { mediaId: player.currentId, position: player.currentTime },
      draft: store.getState().commentDraft,               // 草稿类：目标端需确认
      selections: [...store.getState().multiSelect],      // 选择类：目标端可忽略
    }
  }

  async exportTo(deviceId) {
    const snap = { ...this.#collectSnapshot(), targetDevice: deviceId }
    const res = await api.handoff.upload(snap)            // 服务端中转（TTL 5min）
    return res.handoffId
  }

  async importFrom(handoffId) {
    const snap = await api.handoff.fetch(handoffId)
    if (Date.now() - snap.takenAt > 5 * 60000) throw new Error('EXPIRED')
    if (snap.schemaVersion !== CURRENT_SCHEMA) snap = migrateSession(snap)

    // 分级恢复
    router.push(snap.route)                                        // 位置：直接恢复
    scrollToAnchor(snap.scroll.anchorId)
    if (snap.player) player.seek(snap.player.mediaId, snap.player.position)
    if (snap.draft && Object.keys(snap.draft).length) {
      // 草稿：确认后恢复（防覆盖）
      if (await confirm('检测到未完成的草稿，是否恢复？')) {
        store.setState({ commentDraft: snap.draft })
      }
    }
    await api.handoff.acknowledge(handoffId)                // 源端标记转移
  }
}

// 源端的「会话转移」感知：下次保存收到 409
api.saveDraft(draft).catch(async (e) => {
  if (e.status === 409) {
    toast.info('此会话已在其他设备继续')
    store.setState({ commentDraft: null })          // 防双活写入
  }
})
```
