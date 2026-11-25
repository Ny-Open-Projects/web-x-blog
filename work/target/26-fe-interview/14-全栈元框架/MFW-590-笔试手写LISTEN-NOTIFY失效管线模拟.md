---
title: [MFW-590] 笔试：手写 LISTEN-NOTIFY 失效管线模拟
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-590：笔试：手写 LISTEN-NOTIFY 失效管线

**答**：实现 `createInvalidationPipeline({ listener, revalidateEndpoint, tagMap, secret })`。listener 注入：`on(channel, cb) => void`（模拟 pg LISTEN）；revalidateEndpoint 注入：`(tags) => Promise`（模拟调 Next 端点）。tagMap: `Record<table, (payload) => string[]>`（表 → tag 列表函数）。规则：1) 通知到达：解析 payload `{ table, id, op }` → tagMap[table](payload) → tags；2) 重试：revalidate 失败 → 指数退避重试 3 次（1s/2s/4s）；3) 重试耗尽 → 死信队列（deadLetters 数组 + onDeadLetter 回调——失效丢失的兜底：人工/定时补偿）；4) 通知去重（同 payload 1s 内重复 = 一次失效——事件风暴保护 RBL-874 去抖）。返回 `{ deadLetters, processed }`。

```javascript
function createInvalidationPipeline({ listener, revalidateEndpoint, tagMap, secret = '', now = Date.now } = {}) {
  const deadLetters = []; let processed = 0;
  const dedupe = new Map();                              // payloadHash -> ts
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  async function revalidateWithRetry(tags) {
    for (let attempt = 0; attempt < 3; attempt++) {
      try { await revalidateEndpoint(tags); return true; }
      catch { if (attempt < 2) await sleep(1000 * 2 ** attempt); }
    }
    return false;
  }
  listener.on('product_changes', async (raw) => {
    const payload = JSON.parse(raw);
    const key = JSON.stringify(payload);
    const last = dedupe.get(key);
    if (last && now() - last < 1000) return;             // 1s 去重
    dedupe.set(key, now());
    const tags = tagMap[payload.table]?.(payload) ?? [];
    if (!tags.length) return;
    const ok = await revalidateWithRetry(tags);
    if (ok) processed++;
    else { deadLetters.push({ payload, tags }); onDeadLetter?.({ payload, tags }); }
  });
  return { get deadLetters() { return deadLetters; }, get processed() { return processed; } };
}

// 自测
const calls = []; let failFirst = true;
const pipeline = createInvalidationPipeline({
  listener: { on: (ch, cb) => listenerCb = cb },
  revalidateEndpoint: async (tags) => {
    if (failFirst) { failFirst = false; throw new Error('next down'); }   // 首次失败→重试成功
    calls.push(tags);
  },
  tagMap: { products: (p) => [`product:${p.id}`, 'products'] },
});
let listenerCb;
pipeline; // 触发注册
listenerCb(JSON.stringify({ table: 'products', id: 42, op: 'UPDATE' }));
await sleep(50);
console.log(pipeline.processed === 1 && calls.length === 1);
console.log(calls[0].join(',') === 'product:42,products');

// 去重：1s 内重复通知
const before = pipeline.processed;
listenerCb(JSON.stringify({ table: 'products', id: 42, op: 'UPDATE' }));
await sleep(10);
console.log(pipeline.processed === before);              // 去重不重复失效

// 重试耗尽 → 死信
let deadCbCalled = null;
const p2 = createInvalidationPipeline({
  listener: { on: (ch, cb) => cb(JSON.stringify({ table: 'products', id: 99 })) },
  revalidateEndpoint: async () => { throw new Error('down'); },
  tagMap: { products: (p) => [`product:${p.id}`] },
});
await sleep(5000);                                       // 等重试完成（1+2+4=7s 太长——用短重试测试可注入 sleep）
// 注：真实测试注入短 sleep 或假 timer；此处示意
```

**评分点**：
- 通知 → tag 映射（表变更 → 缓存失效的完备性——RBL-577 触发源映射）
- 指数退避重试 + 死信队列（失效丢失的兜底——静默失效防线 RBL-956）
- 1s 去抖（事件风暴保护——CDC 风暴的失效合并）
- 能说清「失效管线是新数据到用户的最后一段——丢失 = 静默旧数据，死信补偿是必要兜底」属于加分
