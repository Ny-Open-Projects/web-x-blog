---
title: [MFW-808] 笔试：手写 Outbox 投递 worker（至少一次投递的幂等对账）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-808：笔试：手写 Outbox 投递 worker（至少一次投递的幂等对账）

**答**：
- 结论：worker 从 outbox 取待发消息，用「消息 id 作为幂等 key」发送，成功后标记；用 inFlight 去重防并发重入，失败按次数重试并进死信。
- 关键：markSent 失败会造成重复投递，必须靠消费端幂等 key 把「至少一次」收敛为「恰好一次效果」。
- 追问钩子：重试上限到了怎么办？——进死信队列 + 告警，而不是无限重试拖垮下游。

```javascript
function createOutboxWorker({ loadPending, send, markSent, retryMax = 3 }) {
  const inFlight = new Set();
  async function tick() {
    const rows = await loadPending(100);
    await Promise.all(rows.map(async (m) => {
      if (inFlight.has(m.id)) return;             // 并发去重
      inFlight.add(m.id);
      try {
        if (m.attempts >= retryMax) {
          await markSent(m.id, 'dead'); return;   // 死信
        }
        await send({ key: m.id, payload: m.payload }); // 幂等 key
        await markSent(m.id, 'sent');
      } catch (e) {
        await markSent(m.id, 'pending', m.attempts + 1);
      } finally { inFlight.delete(m.id); }
    }));
  }
  return { tick };
}

// 自测：模拟一条消息，verify 幂等 key 与状态流转
const box = [{ id: 'o1', payload: {}, attempts: 0, state: 'pending' }];
const w = createOutboxWorker({
  loadPending: async () => box.filter(m => m.state === 'pending'),
  send: async (m) => console.log('send', m.key),
  markSent: async (id, s, a) => { box[0].state = s; if (a) box[0].attempts = a; }
});
w.tick().then(() => console.log(box[0].state));   // sent
```

**评分点**：
- outbox 与业务同事务写入是原子性前提（需在面试中点出，笔试代码体现取 pending）
- 幂等 key = 消息 id，把至少一次投递收敛为恰好一次效果
- inFlight 去重防止同一消息在并发 tick 中重复处理
- 重试上限 + 死信 + markSent 失败靠幂等兜底，避免无限重试
