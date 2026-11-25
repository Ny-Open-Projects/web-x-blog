---
title: [OPT-060] 大 JSON（几十 MB）解析怎么优化？分片、Worker、流式怎么选？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-060：大 JSON（几十 MB）解析怎么优化？分片、Worker、流式怎么选？

**答**：
- 一个 30MB 的 `res.json()` 会阻塞主线程 200-800ms（低端机更久），且解析峰值内存约原文件 3-5 倍。
- 方案优先级：**接口端减量**（分页/字段裁剪）> **Worker 解析**（主线程零阻塞，实现简单）> **流式增量解析**（首屏先渲染，实现最复杂）。
- Worker 方案注意：postMessage 传回解析结果仍走结构化克隆，大对象同样耗时——应解析+裁剪都在 Worker 内完成，只回传业务需要的字段。
- 流式方案用 `response.body.getReader()` + 边界切分（如 NDJSON 每行一个 JSON），按行增量 parse，天然可配合虚拟列表。

```javascript
// 一一对应：大 JSON 的 Worker 解析 + NDJSON 流式两种方案
// worker.js —— 方案一：Worker 内解析并裁剪，只回传业务字段（克隆量最小）
self.onmessage = async (e) => {
  const res = await fetch(e.data.url);
  const big = await res.json();          // 阻塞发生在 Worker，主线程无感
  const slim = big.items.map((it) => ({  // 30MB -> 3MB，克隆成本同步降一个量级
    id: it.id, name: it.name, price: it.price,
  }));
  self.postMessage(slim);
};
// main.js
// const worker = new Worker('worker.js');
// worker.postMessage({ url: '/api/huge-list' });
// worker.onmessage = (e) => render(e.data);

// 方案二：NDJSON 流式增量解析，首条数据到达即可渲染
async function streamNdjson(url, onRow) {
  const reader = (await fetch(url)).body.getReader();
  const decoder = new TextDecoder();
  let buf = '';
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    const lines = buf.split('\n');
    buf = lines.pop(); // 最后一段可能不完整，留到下一轮
    for (const line of lines) onRow(JSON.parse(line)); // 每行独立小对象，无大阻塞
  }
  if (buf) onRow(JSON.parse(buf));
}
// streamNdjson('/api/huge-list?format=ndjson', (row) => appendVirtualRow(row));
```

## 追问（补充）

**追问**：

1. 分片会不会更慢？ → 总解析时间略增，但把长任务切成 50ms 以内的小段，交互不被阻塞，感知收益通常大于吞吐损失。
2. Worker 解析完怎么回传？ → 用 Transferable 转移 ArrayBuffer 而不是结构化克隆，避免主线程再拷贝一份大对象。
3. 流式解析适合什么数据？ → 超大数组或 NDJSON，边读边处理，内存峰值与总数据量解耦，但需要自己维护解析状态机，错误恢复也更麻烦，需要额外的校验与重试分支。
