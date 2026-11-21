---
title: [MP-283] 笔试：手写小程序 IM 消息列表页核心
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 笔试题
---

## MP-283：笔试：手写 IM 消息列表页核心
**题**：实现：消息分页加载（向上翻历史，scroll-into-view 保持位置）；WebSocket 消息按 msgId 去重插入；未读数管理（在底部时自动已读）；发送消息乐观展示（sending 态 + 失败重试）。

```javascript
Page({
  data: { messages: [], scrollTop: 0, intoView: '', unread: 0, draft: '' },
  seen: new Set(),
  async onLoad() { this.connectWs(); await this.loadLatest() },
  connectWs() {
    this.ws = wx.connectSocket({ url: WS_URL + '?token=' + wx.getStorageSync('token') })
    this.ws.onMessage(({ data }) => {
      const msg = JSON.parse(data)
      if (this.seen.has(msg.id)) return
      this.seen.add(msg.id)
      this.insertMessage(msg)
      if (this.atBottom) this.markRead([msg.id])
      else this.setData({ unread: this.data.unread + 1 })
    })
  },
  async insertMessage(msg) {
    const messages = [...this.data.messages, msg].sort((a, b) => a.ts - b.ts)
    this.setData({ messages, intoView: `msg-${msg.id}` }) // 锚点滚到底部
  },
  async loadHistory() {
    const prevHeight = this._listHeight
    const older = await api.getMessages({ before: this.data.messages[0]?.ts })
    this.setData({ messages: [...older.reverse(), ...this.data.messages] }, () => {
      this.setData({ intoView: `msg-${older[older.length - 1]?.id}` }) // 位置保持
    })
  },
  send() {
    const body = this.data.draft.trim()
    if (!body) return
    const tempId = `tmp-${Date.now()}`
    const optimistic = { id: tempId, body, status: 'sending', ts: Date.now(), mine: true }
    this.setData({ messages: [...this.data.messages, optimistic], draft: '' })
    api.sendMessage({ body, requestId: tempId })
      .then(() => this.setData({ [`messages[${this.data.messages.length - 1}].status`]: 'sent' }))
      .catch(() => this.setData({ [`messages[${this.data.messages.length - 1}].status`]: 'failed' }))
  }
})
```
**评分点**：
- msgId 去重（WS 重发场景）。
- 历史加载位置保持（scroll-into-view 锚点）。
- 乐观发送 + sending/failed 状态 + 路径级 setData。
- 未读管理（底部自动已读）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-059f966f-381c-41be-bc2e-e3d6dd5705d2-cwd'; fi
exit "$__zcode_status"
