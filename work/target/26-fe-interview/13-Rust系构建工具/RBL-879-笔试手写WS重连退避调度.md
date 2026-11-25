---
title: [RBL-879] 笔试：手写 WS 重连退避调度（指数退避 + 抖动 + 消息缓冲重放）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-879：笔试：手写 WS 重连退避调度（退避 + 抖动 + 重放）

**答**：实现 `createWsClient({ connect, schedule, { baseMs, maxMs, jitter } })`。注入 connect（返回 Promise<conn>，conn 有 send/close；可失败模拟断线）、schedule(fn, delayMs)（定时注入）。规则：1) connect 失败 → 计算退避 delay = min(base × 2^n, max) × jitter 系数（注入 rng：×(0.5+rand)，jitter=false 则 ×1）→ schedule 重连；2) 成功连接：重放缓冲区消息（FIFO）并清空，重置退避计数；3) `send(msg)`：连接中直发，断线中缓冲（上限 100，超出丢弃最旧并记 drop 计数）；4) `close()`：停止重连（后续 send 全部缓冲或抛错——按 close 后状态忽略）；5) 返回 `{ send, close, state() }`（state: attempts/dropped/queued）。边界：maxMs 封顶；连续失败退避重置于成功后。

```javascript
function createWsClient(connect, schedule, { baseMs = 1000, maxMs = 30000, jitter = true, rng = Math.random, queueCap = 100 } = {}) {
  let queue = [], attempts = 0, dropped = 0, closed = false, conn = null;
  const tryConnect = async () => {
    if (closed) return;
    try {
      conn = await connect();
      attempts = 0;                                      // 成功重置退避
      const replay = queue.splice(0, queue.length);
      replay.forEach(m => conn.send(m));
    } catch {
      attempts++;
      const factor = jitter ? 0.5 + rng() : 1;
      const delay = Math.min(baseMs * 2 ** attempts, maxMs) * factor;
      schedule(tryConnect, Math.round(delay));
    }
  };
  tryConnect();
  return {
    send(msg) {
      if (closed) return 'closed';
      if (conn) { conn.send(msg); return 'sent'; }
      if (queue.length >= queueCap) { queue.shift(); dropped++; }
      queue.push(msg);
      return 'queued';
    },
    close() { closed = true; conn?.close?.(); conn = null; },
    state: () => ({ attempts, dropped, queued: queue.length, connected: !!conn }),
  };
}

// 自测
let scheduled = [];
let failCount = 2;
const connect = async () => {
  if (failCount > 0) { failCount--; throw new Error('down'); }
  return { send: (m) => sent.push(m), close: () => {} };
};
const sent = [];
const c = createWsClient(connect, (fn, ms) => scheduled.push({ fn, ms }),
  { baseMs: 1000, maxMs: 8000, jitter: false });

console.log(c.state().connected === false && c.state().attempts === 1);
console.log(scheduled[0].ms === 2000);                   // base×2^1

// 断线缓冲
console.log(c.send({ id: 1 }) === 'queued');
console.log(c.send({ id: 2 }) === 'queued');

// 重连成功重放
await scheduled[0].fn();
console.log(c.state().connected === true);
console.log(sent.map(m => m.id).join(','));              // 1,2（FIFO 重放）
console.log(c.state().queued === 0 && c.state().attempts === 0);

// 连接中直发
console.log(c.send({ id: 3 }) === 'sent' && sent[2].id === 3);

// close 后
c.close();
console.log(c.send({ id: 4 }) === 'closed');
```

**评分点**：
- 指数退避 + max 封顶正确；jitter 可关（测试确定性 rng 注入）；成功后重置 attempts
- 缓冲重放 FIFO、容量上限丢弃最旧并计数；连接中直发/断线缓冲的语义分明
- close 后 send 返回状态不抛错（幂等清理）
- 能说清「重连风暴的惊群必须 jitter 打散，分布式时钟同步是灾难随机化是解药」属于加分
