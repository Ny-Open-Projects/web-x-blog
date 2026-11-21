---
title: [BLD-107] seal 阶段内部顺序：buildChunkGraph、codeGeneration、emitAssets 各做什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-107：seal 阶段内部顺序：buildChunkGraph、codeGeneration、emitAssets 各做什么？
**答**：
- `Compilation.seal()` 顺序：`hooks.seal` → **buildChunkGraph**（依据 entrypoints、ImportDependency 分配 chunk 与 chunkGroup）→ optimize 链（optimizeChunks 供 splitChunks 钩子、optimizeModuleOrder、concatenateModules、moduleIds/chunkIds）→ `beforeModuleHash`。
- **codeGeneration**：对每个 module 调各自的 generator（JS 模块由 JavascriptModulesPlugin 的 Generator 包装为 `__webpack_require__` 形态），结果存 `compilation.codeGenerationResults`，同时汇总 runtimeRequirements 供 Runtime 模块使用。
- **createHash → processAssets**：内容 hash（contenthash 就在这定）后进入 `compilation.hooks.processAssets`（webpack5 资源处理统一入口，minimizer、压缩、manifest 插件全挂在这），最后 `hooks.afterProcessAssets → emitAssets` 经 `compiler.hooks.emit` 写盘。
- 扩展抓手：改产物用 processAssets（选 OptimizeChunkAssets 之后的 stage），改模块产码用 `compilation.hooks... JavascriptModulesPlugin` 的 renderModule/renderChunk。

```javascript
// 在 seal 内部的正确位置动手：processAssets 分 stage 的完整示例
const Compilation = require('webpack/lib/Compilation');

class SealInternalsDemoPlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('Demo', (compilation) => {
      // ① buildChunkGraph 之后可读：chunk 结构已定
      compilation.hooks.afterChunks?.tap('Demo', (chunks) => {
        console.log('chunks 已分配：', [...chunks].map((c) => c.name ?? c.id));
      });

      // ② processAssets 分 stage：顺序敏感，插错 stage 会互相覆盖
      compilation.hooks.processAssets.tap(
        { name: 'Demo', stage: Compilation.PROCESS_ASSETS_STAGE_ADDITIONS },
        (assets) => {
          // ADDITIONS：在 minimizer 之前追加产物（如生成 manifest.txt）
          const report = Object.entries(assets)
            .map(([n, a]) => `${n}: ${a.size()}B`).join('\n');
          compilation.emitAsset('build-report.txt', compilation.compiler.webpack.sources.RawSource.from(report));
        }
      );

      compilation.hooks.processAssets.tap(
        { name: 'DemoHeaders', stage: Compilation.PROCESS_ASSETS_STAGE_OPTIMIZE_SIZE + 10 },
        (assets) => {
          // OPTIMIZE_SIZE 之后：压缩已完成，适合做产物审计、注入 banner、SRI
          for (const [name, asset] of Object.entries(assets)) {
            if (name.endsWith('.js')) {
              console.log(`[minified] ${name} ${asset.size()}B`);
            }
          }
        }
      );
    });
  }
}
module.exports = SealInternalsDemoPlugin;
```
