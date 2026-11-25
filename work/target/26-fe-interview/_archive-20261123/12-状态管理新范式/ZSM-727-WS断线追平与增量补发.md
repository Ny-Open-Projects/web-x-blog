---
title: [ZSM-727] WS 断线追平：lastSeq 缺口补发的三种策略与兜底
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-727：WS 断线追平：lastSeq 缺口补发的三种策略与兜底

**答**：
- 断线期间的事件不能丢（消息/状态变更），重连后按 lastSeq 补发。三种策略：1) **服务端缓冲重放**——服务端为每个连接缓存最近 N 条（或按用户全局缓冲带 TTL），重连带 `?since=lastSeq` 服务端重放缺口；2) **增量接口拉取**——WS 只做信号，缺口通过 HTTP 增量接口（`GET /events?since=`）补，缓冲压力转移到存储层；3) **状态快照对账**——缺口大或无法补发时直接全量拉当前状态覆盖（放弃中间过程，终局一致）。
- 策略选择依据：缺口大小与事件语义。小缺口（<50 条）重放；大缺口但事件可聚合（如列表变更）走快照对账；事件有独立存储（消息表）走增量接口。**混合策略是常态**：`gap <= 50 ? replay : snapshot`。
- 追平期间的入口封闭：重放/拉取完成前，新事件进「暂存队列」不直接 apply——追平数据与新事件按 seq 合并去重后按序应用，保证顺序。实现：追平阶段把 lastSeq 推进到最新，期间到达的事件带更高 seq，缓冲区排序应用。
- 幂等与去重：重放的事件可能已部分应用过（断线前收到一半）——所有状态应用必须幂等（以 id/seq 去重），追平重复无害。
- 追问钩子：追平失败的兜底——服务端缓冲已淘汰（TTL 过期）返回 410 Gone，客户端直接走全量刷新（invalidate 所有活跃缓存 + 重置游标），UI 提示「数据已刷新」。

```javascript
// 追平协调器
class CatchUpCoordinator {
  #buffer = []          // 追平期间暂存的新事件
  #catchingUp = false

  async onReconnect(client, since) {
    const gap = client.serverLastSeq - since
    this.#catchingUp = true

    try {
      if (gap <= 50) {
        await this.#replay(client, since)                     // 策略1：重放
      } else if (await this.#hasIncrementalApi()) {
        await this.#fetchIncremental(client, since)           // 策略2：增量接口
      } else {
        await this.#snapshot(client)                          // 策略3：快照对账
      }
    } catch (e) {
      if (e.status === 410) {                                 // 缓冲已淘汰：全量兜底
        await this.#fullRefresh()
      } else throw e
    }

    this.#catchingUp = false
    // 应用暂存：按 seq 去重排序
    const buffered = this.#buffer.splice(0)
      .sort((a, b) => a.seq - b.seq)
      .filter((e) => e.seq > since)
    buffered.forEach((e) => apply(e))
  }

  onLiveEvent(event) {
    if (this.#catchingUp) {
      this.#buffer.push(event)      // 追平期间：暂存不 apply
    } else {
      apply(event)
    }
  }

  async #replay(client, since) {
    // 服务端重放：连接建立后服务端主动推缺口（?since=lastSeq）
    await waitFor(() => client.serverCaughtUp)    // 服务端补完信号
  }

  async #fetchIncremental(client, since) {
    const { events } = await api.getEvents({ since })
    events.forEach(apply)
  }

  async #snapshot(client) {
    const snap = await api.getSnapshot()
    store.setState(snap, true)                    // 全量覆盖
  }
}
```
