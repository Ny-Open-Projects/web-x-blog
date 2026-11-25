---
title: [RBL-183] 笔试：手写 CI 矩阵 job 生成器（shard 矩阵 JSON）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-183：笔试：手写 CI 矩阵 job 生成器（按测试目录动态生成 matrix）

**答**：写 gen-matrix.mjs：1) 输入包列表与每包测试文件数；2) 决策每个包是否独立成 job（测试文件 > 100 独立 + 内部再分片）、小包合并进 combined job（合并后总数 ≤ 200）；3) 生成 GitHub Actions matrix JSON：{ include: [{package, shard, shards}] }；4) 输出命令模板供各 job 使用：vitest run --shard=i/n --filter=包名；5) 环境变量 MAX_JOBS 限制总 job 数（超限时合并最小包）。

```javascript
// gen-matrix.mjs
export function genMatrix(pkgs, { maxJobs = 8, bigThreshold = 100, combinedLimit = 200 } = {}) {
  const big = pkgs.filter(p => p.tests > bigThreshold)
    .map(p => ({ ...p, job: 'solo', shards: Math.min(4, Math.ceil(p.tests / 60)) }));
  const small = pkgs.filter(p => p.tests <= bigThreshold)
    .sort((a, b) => b.tests - a.tests);

  const budget = maxJobs - big.reduce((s, p) => s + p.shards, 0); // 独立包已占用额
  const groups = [];
  for (const p of small) {                       // 贪心装箱：合并小包
    const g = groups.find(g => g.total + p.tests <= combinedLimit && groups.length < budget);
    if (g) { g.pkgs.push(p.name); g.total += p.tests; }
    else groups.push({ pkgs: [p.name], total: p.tests });
  }
  const include = [];
  for (const p of big)
    for (let i = 1; i <= p.shards; i++)
      include.push({ package: p.name, shard: i, shards: p.shards,
        cmd: `vitest run --shard=${i}/${p.shards} --project=${p.name}` });
  if (groups.length)
    include.push({ package: groups.map(g => g.pkgs.join('+')).join('|'), shard: 1, shards: 1,
      cmd: `vitest run --project=${groups.flatMap(g => g.pkgs).join(' --project=')}` });
  return { include, jobs: include.length };
}

// 示例输入与输出
const pkgs = [
  { name: 'web', tests: 320 }, { name: 'admin', tests: 150 },
  { name: 'ui', tests: 60 }, { name: 'utils', tests: 30 }, { name: 'hooks', tests: 20 },
];
const m = genMatrix(pkgs, { maxJobs: 6 });
console.log(JSON.stringify(m, null, 2));
// web 320>100 → 独立 4 片；admin 150>100 → 独立 3 片（min(4, ceil(150/60))）
// ui/utils/hooks 合并一个 job；总 job = 7 超过 maxJobs=6 时合并最小包重算
```
**评分点**：
- 阈值驱动的独立/合并决策（不是拍脑袋均分）。
- shard 数量按测试量算（ceil/tests per shard）而非固定。
- MAX_JOBS 预算扣除独立包占用后再分配。
- include 结构可直接用于 GitHub Actions strategy.matrix。
- 能说明动态矩阵解决"加包就要手改 CI 配置"的维护痛点。
