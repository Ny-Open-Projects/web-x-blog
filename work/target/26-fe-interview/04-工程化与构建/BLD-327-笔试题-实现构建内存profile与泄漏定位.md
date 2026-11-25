---
title: [BLD-327] 笔试题——实现构建内存 profile 与泄漏定位？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-327：手写内存定位

**需求与边界**：
- 需求：构建 OOM 的定位（SCN-BLD-253）——① 堆采样（构建过程定时 heapUsed 记录——增长曲线）；② 保留树分析（heap snapshot 的 retained size Top——谁持有最多内存）；③ 泄漏假设生成（插件 AST 缓存/sourcemap sourcesContent/模块图——SCN-BLD-253 三嫌疑）；④ 验证脚本（禁用嫌疑插件重跑对比内存）。
- 边界：① 采样在 worker 进程也要覆盖（主进程 OOM 常见但 worker 也可能）；② snapshot 对比（两次 snapshot 的 diff——增长部分）；③ 建议带证据（retained size 数值）。

**答**：
```javascript
async function memoryProfile(buildFn, { samples = 20 } = {}) {
  const series = [];
  const sampler = setInterval(() => {
    const mu = process.memoryUsage();
    series.push({ t: Date.now(), heap: mu.heapUsed });
    if (series.length > 1 && monotonicGrowth(series))          // 单调增长 = 泄漏嫌疑
      warn('heapUsed 单调增长——疑似泄漏');
  }, 2000);
  try {
    await buildFn();
  } finally { clearInterval(sampler); }
  // 堆快照 diff（增长部分）
  const snap1 = await takeHeapSnapshot();
  await buildFn();                                     // 再跑一轮
  const snap2 = await takeHeapSnapshot();
  const growth = diffSnapshots(snap1, snap2)           // 增长对象 Top
    .sort((a, b) => b.retainedSize - a.retainedSize).slice(0, 10);
  // 三嫌疑验证
  const hypotheses = [
    { name: 'plugin-ast-cache', test: () => disablePluginCaches() },
    { name: 'sourcemap-content', test: () => disableSourcesContent() },
    { name: 'module-graph', test: () => buildWithSharding() },
  ];
  for (const h of hypotheses) {
    const before = process.memoryUsage().heapUsed;
    await h.test(async () => await buildFn());
    const after = process.memoryUsage().heapUsed;
    if (before - after > 100e6)                        // 内存降 100MB+ = 命中
      return { culprit: h.name, savedMB: Math.round((before - after) / 1e6) };
  }
  return { series, growth };
}
```

**评分点**:
- 增长曲线 + 单调检测（泄漏嫌疑——SCN-BLD-253）。
- 快照 diff（增长对象 retained Top）。
- 三嫌疑假设验证（禁用对比——证据驱动定位）。
- worker 覆盖意识 + 建议带数值证据。

## 变体与延伸（补充）

**变体与延伸**：

1. 怎么区分真泄漏与高水位？ → 强制多次 GC 后 heapUsed 仍单调增长才算泄漏，否则只是缓存水位，误判会导致无效优化。
2. heap snapshot 怎么看？ → 取构建前后两个时间点做对比，看 retained size 增量与对象构造栈，定位到具体 loader 或插件。
3. loader 泄漏怎么定位？ → 在 hook 前后各采一次 heapUsed 差值，再用 snapshot 过滤该 loader 闭包里的对象，看是否持有模块源码或 AST，缓存常是元凶，插件级闭包最容易积压。
