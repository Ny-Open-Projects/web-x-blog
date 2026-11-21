---
title: [BLD-106] make 和 seal 两阶段分别负责什么？为什么这样拆分？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-106：make 和 seal 两阶段分别负责什么？为什么这样拆分？
**答**：
- **make 阶段是异步的、IO 密集**：从 entry 出发 factorize（resolve 路径）→ read+loader（build）→ parse（收集依赖）→ 递归处理依赖，产出完整 ModuleGraph；结束标志是 `compilation.finish()`（所有依赖闭包收齐）。
- **seal 阶段是同步的、CPU 密集**：buildChunkGraph 分 chunk → 一系列 optimize 钩子（optimizeChunks、concatenateModules、mangleExports、moduleIds）→ codeGeneration 逐模块产码 → createHash → emitAssets，产出最终 assets。
- 拆分意义：make 面向"源码与依赖"（可并行、可持久缓存、与产物形态无关）；seal 面向"产物形态"（分包策略、优化、hash 都在这）。loader/parse 报错在 make 查，体积/分包问题在 seal 查。
- 缓存分界：filesystem 缓存命中时 make 可跳过未变模块的 build，但 seal 每次全量重跑——这也是"缓存命中后仍要几百 ms"的原因。

```javascript
// 两阶段计时探针：面试中"你怎么证明瓶颈在 make 还是 seal"就靠这个
class PhaseTimingPlugin {
  apply(compiler) {
    const t = {};
    compiler.hooks.compilation.tap('PhaseTiming', (compilation) => {
      compilation.hooks.addEntry.tap('PhaseTiming', () => { t.make ??= 0; t.makeStart ??= process.hrtime.bigint(); });
      compilation.hooks.finishModules.tap('PhaseTiming', () => {
        t.make = Number(process.hrtime.bigint() - t.makeStart) / 1e6; // make 耗时 ms
      });
      compilation.hooks.seal.tap('PhaseTiming', () => { t.sealStart = process.hrtime.bigint(); });
      compilation.hooks.afterSeal.tap('PhaseTiming', () => {
        t.seal = Number(process.hrtime.bigint() - t.sealStart) / 1e6;
      });
    });
    compiler.hooks.done.tap('PhaseTiming', () => {
      console.log(`[phase] make=${t.make?.toFixed(0)}ms seal=${t.seal?.toFixed(0)}ms`);
      // 经验判读：make 高 → IO/loader/模块数问题（上缓存/换 esbuild-loader）
      //          seal 高 → 模块总量大导致压缩/分包/minimize 慢（查 Terser、splitChunks 规模）
    });
  }
}
module.exports = PhaseTimingPlugin;
```
