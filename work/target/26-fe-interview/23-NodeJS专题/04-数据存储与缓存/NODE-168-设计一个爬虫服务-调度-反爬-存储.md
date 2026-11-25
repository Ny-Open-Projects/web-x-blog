---
title: [NODE-168] 设计一个爬虫服务（调度/反爬/存储）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-168：设计一个爬虫服务（调度/反爬/存储）？
**答**：
- 三层：**调度**（优先级队列 + 去重集合）→ **抓取**（并发控制 + UA 池 + 限速）→ **存储**（结构化抽取 + url 唯一键幂等入库）。
- 合规底线：遵守 robots.txt、对单站限速（limiter 5 QPS）、UA 可识别、隐私数据只存摘要。
- 反爬对策分级：限频（遵守 Retry-After）、验证码（接入打码或人工）、登录态（cookie 池轮换）、封 IP（代理池 + 退避）。
- 稳定性：任务可恢复（队列持久化）、失败重试 + 死信、抓取内容 hash 去重防重复存储。

```javascript
const { Queue, Worker } = require('bullmq');
const crawlQueue = new Queue('crawl', { connection: redis });
const seen = new Set(); // url 去重（量大换 Redis SADD / BloomFilter）

async function schedule(url, depth) {
  if (seen.has(url)) return;
  seen.add(url);
  await crawlQueue.add('fetch', { url, depth }, { priority: depth }); // 浅层优先
}

new Worker('crawl', async (job) => {
  const { url, depth } = job.data;
  if (await robotsDisallowed(url)) return;                 // robots 合规
  const res = await fetch(url, {
    headers: { 'user-agent': UA_POOL.random(), accept: 'text/html' },
    signal: AbortSignal.timeout(8000),
  });
  if (res.status === 429) {                                 // 尊重限频
    await sleep((+res.headers.get('retry-after') || 5) * 1000);
    throw job.retry();
  }
  const html = await res.text();
  await bulkUpsert(extract(html));                          // url 唯一键幂等入库
  if (depth < 3) for (const link of extractLinks(html)) await schedule(link, depth + 1);
}, { concurrency: 10, limiter: { max: 5, duration: 1000 } }); // 单站限速 5 QPS
```
