---
title: [TST-208] 如何实测并优化分片负载均衡？给出一个贪心装箱方案。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-208：如何实测并优化分片负载均衡？给出一个贪心装箱方案。
**答**：
- 用 JSON reporter 收集每个用例耗时，按时长降序贪心分给「当前最轻」的分片。
- 把分片结果生成 shard 清单（testDir 过滤），供 CI 各分片消费。
- 优化目标：最大分片时长最小化（makespan），贪心近似即可。
- 每次代码变更后重新生成清单（用例增减会破坏均衡）。

```javascript
function balance(durations: Array<{ id: string; ms: number }>, shards: number) {
  const bins = Array.from({ length: shards }, () => ({ total: 0, ids: [] as string[] }));
  for (const d of [...durations].sort((a, b) => b.ms - a.ms)) {
    const b = bins.reduce((m, x) => x.total < m.total ? x : m);
    b.total += d.ms; b.ids.push(d.id);
  }
  return bins; // 生成各分片要跑的用例清单
}
r
```
