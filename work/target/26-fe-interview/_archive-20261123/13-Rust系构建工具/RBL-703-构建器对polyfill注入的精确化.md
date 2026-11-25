---
title: [RBL-703] Polyfill 注入的精确化：usage 模式、按 chunk 注入与体积成本
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-703：Polyfill 注入的精确化：usage 模式、按 chunk 注入与体积成本

**答**:
- polyfill 注入三模式：1) entry 模式（全量 polyfill 进入口——简单但体积大，core-js 全量 100KB+）；2) usage 模式（扫描代码实际使用的特性，按需注入——精确但要求静态可分析）；3) 按目标兜底（browserslist 决定是否需要注入）。现代构建器默认 usage 精确化，体积与兼容性的最优交点。
- usage 模式的精度边界：动态特性使用（`obj[fnName]()` 调到 Array.prototype.flat）静态分析抓不到——保守策略是「语法级 polyfill 精确、API 级 polyfill 允许白名单兜底」；core-js 的 corejs: 'usage' 就是这个思路。
- 按 chunk 注入的成本权衡：polyfill 只注入「实际用到特性的 chunk」比「统一入口注入」省体积，但带来「chunk 间重复」（多个 chunk 各注入一份 core-js 模块）——解法是 polyfill 模块也参与 chunk 分割（共享 polyfill chunk），让复用与精确兼得。
- 版本锁定：polyfill 注入要 pin 版本（core-js 3 的 minor 也会变行为），lockfile 锁定 + 构建器输出「polyfill 清单」（用了哪些 polyfill、来自哪个特性、注入到哪些 chunk）——可审计。
- 追问钩子：为什么「entry 全量注入」仍在生产环境常见？——多个 chunk 的动态加载路径让 usage 模式的「漏 polyfill」变成线上白屏（比体积大更致命）；金融类稳定性优先场景选 entry 全量 + es5 降级包双保险——精确化是优化不是教条。

```javascript
// usage 精确注入
function injectPolyfills(chunk, targets, { mode = 'usage' } = {}) {
  const used = collectUsedFeatures(chunk.code);          // 语法+API 特性
  const needed = used.filter(f => !supportedBy(targets, f));
  if (!needed.length) return chunk.code;
  const imports = needed.map(f => `import 'core-js/modules/${f}';`);
  return imports.join('\n') + '\n' + chunk.code;         // usage 精确
}
// 共享 polyfill chunk
function hoistPolyfills(chunks) {
  const counts = countPolyfills(chunks);                 // polyfill -> 引用 chunk 数
  const shared = Object.entries(counts)
    .filter(([, n]) => n >= 3)                           // 3 个以上 chunk 共用 -> 提共享 chunk
    .map(([f]) => f);
  for (const chunk of chunks)
    chunk.code = stripPolyfills(chunk.code, shared);
  chunks.unshift({ name: 'polyfill', code: shared.map(toImport).join('\n') });
}
// 输出审计清单
console.log(JSON.stringify({ polyfills: shared, chunks: chunks.map(c => c.name) }));
```
