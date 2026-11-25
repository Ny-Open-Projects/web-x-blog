---
title: [BLD-175] 构建任务并行与资源分配：CI 机器规格与并行度怎么定？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-175：构建任务并行与资源分配：CI 机器规格与并行度怎么定？
**答**：
- 并行度 = min(CPU 核数, 任务类型瓶颈)：webpack/seal 是 CPU 密集（压缩、Terser 线程数 `parallel: os.cpus().length - 1`）、loader/resolve 是 IO 密集（可高并发）；过并行反而因上下文切换与内存 GC 变慢。
- CI 规格经验值：webpack 大型项目 4C8G 起步（Terser 内存峰值可达 2-4GB）；Rspack/esbuild 类原生工具 2C 即可高吞吐（多进程模型不同）；并发 job 数 × 单 job 峰值内存 < 机器内存 × 0.8（OOM 是 CI 失败头号原因）。
- 任务编排：monorepo 用 turbo 的 `--concurrency` 控制（默认 CPU 数）；`NODE_OPTIONS=--max-old-space-size=6144` 显式抬堆上限；按"耗时 × 内存"分桶调度（长任务给大规格 runner，短任务并发多个）。
- 观测先行：先跑 `--profile` 拿每任务耗时与内存基线，再定规格——直接拍脑袋加机器是最贵的方案。

```javascript
// scripts/parallel-tuning.js：并行度压测脚本（确定 CI 规格用）
const os = require('os');
const { execSync } = require('child_process');

async function bench(concurrency, maxOldSpace) {
  const env = {
    ...process.env,
    NODE_OPTIONS: `--max-old-space-size=${maxOldSpace}`,
    TURBO_CONCURRENCY: String(concurrency),
  };
  execSync('rm -rf node_modules/.cache apps/*/node_modules/.cache', { cwd: process.cwd() });
  const t0 = Date.now();
  execSync(`pnpm turbo build --concurrency=${concurrency}`, {
    env, stdio: ['ignore', 'ignore', 'inherit'],
  });
  const ms = Date.now() - t0;
  console.log(`concurrency=${concurrency} heap=${maxOldSpace}MB → ${ms}ms`);
  return ms;
}
// 实测矩阵：从 os.cpus().length 到 2x 扫一遍，找拐点
(async () => {
  const cpus = os.cpus().length;
  for (const c of [2, cpus, cpus * 2]) {
    await bench(c, 4096);
  }
})();
// 结论模板：16C runner 上 turbo --concurrency=8 最快（更高并发 Terser 内存争用反降速）
// 单 job 内存峰值 3.2GB → 选 4C8G 规格 × 3 并发 job，机器利用率 74%
```

## 追问（补充）

**追问**：

1. 并行度越高越好吗？ → 不是，每条并行线程有独立堆内存，超过物理核数之后会因内存换页与调度争抢反而变慢，压缩阶段尤其明显。
2. CI 机器规格怎么定？ → 按 P95 构建耗时和峰值 RSS 反推，取 workers = min(核数, 可用内存 / 单线程峰值)，再留一成余量给系统。
3. 怎么判断瓶颈在 CPU 还是 IO？ → 看构建期 CPU 利用率与 load 均值，压缩和转译会吃满 CPU，装依赖与读写缓存才是 IO 密集，两者扩容方向不同。
