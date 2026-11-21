---
title: [RBL-162] CI 测试分片：怎么把 40 分钟测试压到 10 分钟
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-162：CI 测试分片：怎么把 40 分钟测试压到 10 分钟

**答**：
- 思路：测试总量不变，但拆到 N 个并行 CI job；墙钟 = 最慢一片，所以分片要"均衡"，不是简单按文件数均分。
- 均衡策略：按历史耗时加权分片——收集每个测试文件上次耗时（CI 报告持久化），贪心装箱到各片使总时长接近；无历史数据时按文件大小/用例数粗估。
- 工具支持：vitest --shard=i/n --reporter=jest-summary、jest --listTests 拿清单自己分；bun test 没原生 shard 就脚本层分（见 RBL-130 思路）。
- flaky 对策：分片后某片失败不要整体重跑全部，用 --only-failed（ Nx）或脚本记录失败集重试单独文件。
- 追问钩子：分片数量不是越多越好——N 片 = N 次 runner 启动 + 依赖安装开销，实测找到"分片收益 > 启动开销"的拐点，大仓库一般 4~8 片。

```javascript
// scripts/shard-tests.mjs —— 耗时加权贪心分片
import { readFileSync, writeFileSync, existsSync } from 'node:fs';

const files = JSON.parse(readFileSync('test-files.json')); // ["a.test.ts", ...]
const history = existsSync('test-timings.json') ? JSON.parse(readFileSync('test-timings.json', 'utf8')) : {};
const dur = f => history[f] ?? 5; // 无历史按 5s 估

function shard(files, n) {
  const sorted = [...files].sort((a, b) => dur(b) - dur(a)); // 从大到小
  const bins = Array.from({ length: n }, () => ({ files: [], total: 0 }));
  for (const f of sorted) {
    const b = bins.reduce((min, x) => (x.total < min.total ? x : min)); // 放最轻的桶（LPT 贪心）
    b.files.push(f); b.total += dur(f);
  }
  return bins.map(b => b.files);
}
const n = Number(process.env.SHARDS ?? 4);
writeFileSync('shards.json', JSON.stringify(shard(files, n)));
// 各 job：SHARD=k vitest run $(node scripts/list-shard.js k)
// 结束后汇总每文件耗时写回 test-timings.json（缓存持久化），供下次加权。
```
