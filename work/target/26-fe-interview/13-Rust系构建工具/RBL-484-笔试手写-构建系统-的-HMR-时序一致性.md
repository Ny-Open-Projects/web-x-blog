---
title: [RBL-484] 笔试：手写 HMR 时序一致性守卫
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-484：手写 HMR 时序一致性守卫
**答**：实现 `createHmrSequencer(ws)`：1) 问题：多次编辑产生多个 HMR update——客户端应用顺序必须与服务端生成顺序一致（乱序 = 状态不一致）；2) 序号协议：update 带 seq，客户端按 seq 严格递增应用（gap 检测——丢包则请求全量刷新）；3) 快速编辑合并：同一文件的连续编辑合并为一次 update（防抖 + 末值）；4) stale update 丢弃：客户端正在应用 update N 时收到 N+1——排队不丢弃（每个 update 都有效）；5) 断线重连：seq 恢复协议（重连后请求当前版本快照）。

```javascript
export function createHmrSequencer() {
  let serverSeq = 0

  function makeUpdate(payload) {
    return { seq: ++serverSeq, payload, ts: Date.now() }
  }
  // 快速编辑合并：同一文件窗口内只发末值
  const pending = new Map()
  function scheduleUpdate(file, payload, { windowMs = 80 } = {}) {
    pending.set(file, payload)
    setTimeout(() => {
      if (!pending.has(file)) return
      const p = pending.get(file)
      pending.delete(file)
      ws.send(JSON.stringify(makeUpdate(p)))
    }, windowMs)
  }

  // 客户端侧
  function createClientHandler(fullReload) {
    let lastSeq = 0
    const buffer = []
    return {
      onMessage(update) {
        buffer.push(update)
        buffer.sort((a, b) => a.seq - b.seq)
        while (buffer.length && buffer[0].seq === lastSeq + 1) {
          const u = buffer.shift()
          lastSeq = u.seq
          applyUpdate(u.payload)                                  // 严格递增应用
        }
        if (buffer.length && buffer[0].seq > lastSeq + 1) {
          fullReload()                                            // gap → 全量刷新
          lastSeq = buffer[buffer.length - 1].seq
          buffer.length = 0
        }
      },
      reconnect: () => { lastSeq = 0; fullReload() },             // 重连 → 快照
    }
  }
  function applyUpdate(p) { /* 模块热替换执行 */ }
  return { makeUpdate, scheduleUpdate, createClientHandler, get seq() { return serverSeq } }
}
```
**评分点**：
- seq 严格递增协议（乱序缓冲/gap 检测——传输层不可靠的补偿）
- 同文件快速编辑合并（末值语义——编辑风暴治理）
- gap → 全量刷新（局部更新不可修复时降级——正确性优先于流畅）
- 重连快照恢复（seq 跨连接重置的处理）
