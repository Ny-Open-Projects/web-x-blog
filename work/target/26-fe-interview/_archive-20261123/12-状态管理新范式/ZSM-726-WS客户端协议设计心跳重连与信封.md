---
title: [ZSM-726] WebSocket 客户端协议设计：信封格式、心跳与退避重连
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-726：WebSocket 客户端协议设计：信封格式、心跳与退避重连

**答**：
- 消息信封（协议第一层）：`{ v, type, seq, ts, ack, payload }`——v 协议版本（两端不兼容时降级）、seq 单调序号（接收方去重+缺口检测）、ack（对需要可靠投递的消息回执）、type 路由到处理器。信封统一让「日志/重放/版本协商」有统一抓手。
- 心跳双端职责：客户端每 25s ping，**40s 未收到任何消息判定假死**主动断开重连（NAT 超时一般 60s，25s 心跳安全）；服务端同样监测客户端心跳，超时踢连接。心跳也是网络质量探针（RTT 上报做慢连接降级）。
- 重连策略：指数退避 + 全抖动（`delay = min(cap, base * 2^n) * random(0.5, 1.5)`），立即重试只给「显式被踢」以外的首次；重连成功后**进入追平阶段**（带 lastSeq 请求缺口补发）再恢复业务订阅——「先追平再放行」防止追平期间的业务事件与新事件乱序。
- 状态机化连接：`idle → connecting → open → backoff → reconnecting`，暴露给 UI（「已断线重连中」横幅）；页面 visibility 隐藏时切「降频模式」（停心跳，仅保持连接或干脆断开，恢复时重连追平）。
- 追问钩子：WS 与 HTTP 请求的竞态——WS 更新与 HTTP 响应都可能改同一状态，用「版本号/时间戳」裁决或统一走一个入口（WS 更新也封装成 action，与 HTTP 回调同层竞争）。

```javascript
// WS 客户端骨架
class WsClient {
  #ws = null
  #seq = 0
  #lastSeq = 0
  #pingTimer = null
  #backoff = 1
  #handlers = new Map()
  state = 'idle'                 // idle|connecting|open|reconnecting
  #pendingAcks = new Map()

  connect(url, { lastSeq = 0 } = {}) {
    this.state = this.#backoff > 1 ? 'reconnecting' : 'connecting'
    const ws = this.#ws = new WebSocket(`${url}?since=${lastSeq}`)   // 连接即带缺口信息
    ws.onopen = () => {
      this.state = 'open'
      this.#backoff = 1
      this.#startHeartbeat()
      this.onReady?.()           // 上层触发「追平完成前的守门逻辑」
    }
    ws.onmessage = (e) => this.#onMessage(JSON.parse(e.data))
    ws.onclose = () => { this.#stopHeartbeat(); this.#scheduleReconnect(url) }
    ws.onerror = () => ws.close()
  }

  #onMessage(msg) {
    if (msg.type === 'pong') return
    if (msg.seq != null) {
      if (msg.seq <= this.#lastSeq) return          // 重复去重
      if (msg.seq > this.#lastSeq + 1) this.onGap?.(this.#lastSeq, msg.seq)   // 缺口检测
      this.#lastSeq = msg.seq
    }
    if (msg.ack) {
      const p = this.#pendingAcks.get(msg.ack)
      if (p) { clearTimeout(p.timer); p.resolve(msg.payload); this.#pendingAcks.delete(msg.ack) }
      return
    }
    this.#handlers.get(msg.type)?.(msg.payload)
  }

  send(type, payload, { needAck = false } = {}) {
    const msg = { v: 2, type, seq: ++this.#seq, ts: Date.now(), payload }
    if (needAck) {
      msg.ack = crypto.randomUUID()
      return new Promise((resolve, reject) => {
        const timer = setTimeout(() => { this.#pendingAcks.delete(msg.ack); reject(new Error('ack timeout')) }, 5000)
        this.#pendingAcks.set(msg.ack, { resolve, timer })
        this.#ws.send(JSON.stringify(msg))
      })
    }
    this.#ws.send(JSON.stringify(msg))
  }

  #startHeartbeat() {
    this.#pingTimer = setInterval(() => this.send('ping', null), 25000)
  }
  #scheduleReconnect(url) {
    const delay = Math.min(30000, 1000 * 2 ** this.#backoff++) * (0.5 + Math.random())   // 全抖动
    setTimeout(() => this.connect(url, { lastSeq: this.#lastSeq }), delay)               // 重连带 lastSeq 追平
  }
}
```
