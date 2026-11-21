---
title: [RBL-298] Rspack 产物完整性校验（sourcemap 与 runtime）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-298：Rspack 产物完整性校验

**答**:
- 校验清单：sourcemap 引用完整（.js 都有 .map 且 sourceMappingURL 正确）、chunk 引用闭合（html/script 的 chunk 都存在于 manifest）、publicPath 拼接正确（绝对/相对一致性）、CSS 里的 url() 资源齐全
- 实现时机：emit 后（afterEmit 钩子）做全量校验，失败即 fail 构建——发布前的最后防线，成本秒级
- sourcemap 验证抽样：随机取若干映射点验证 map 源坐标与源码内容匹配（防 map 断链悄悄发生）
- 输出：校验报告 artifact（清单 + 结果），失败项带具体文件定位

```javascript
compiler.hooks.afterEmit.tap('Integrity', (compilation) => {
  const manifest = JSON.parse(assets['manifest.json'].source())
  for (const chunk of Object.values(manifest)) {
    if (!assets[chunk.js]) throw new Error(`chunk missing: ${chunk.js}`)
    if (assets[chunk.js].source().includes('sourceMappingURL=') && !assets[chunk.js + '.map'])
      throw new Error(`sourcemap missing: ${chunk.js}`)
  }
})
```
