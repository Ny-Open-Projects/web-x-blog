---
title: [RBL-205] 怎么写一个给 CI 用的构建信息 stats 插件
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-205：怎么写一个给 CI 用的构建信息 stats 插件

**答**:
- 用 `compiler.hooks.done.tap` 拿 stats，`stats.toJson({ modules: false, chunks: true })` 控制粒度（全量 modules 在大项目里巨大）
- 提取 CI 关心的字段：构建耗时、产物数与总体积（按类型分组）、error/warning 数、缓存命中（`stats.compilation.getCache` 命中率近似）
- 写文件用 `compiler.outputFileSystem.writeFile` 而不是 fs（保持与内存文件系统一致）；或者直接 node fs（CI 场景可以）
- 与体积门禁联动：插件内直接做 diff（读上一份 manifest 比对）并在超限时抛错阻断

```javascript
class CiStatsPlugin {
  apply(compiler) {
    compiler.hooks.done.tap('CiStats', (stats) => {
      const j = stats.toJson({ modules: false, chunks: true, assets: true })
      const byType = {}
      for (const a of j.assets ?? []) {
        const ext = a.name.split('.').pop()
        byType[ext] = (byType[ext] ?? 0) + a.size
      }
      const report = { time: j.time, errors: j.errors?.length, warnings: j.warnings?.length, byType }
      compiler.outputFileSystem.writeFile('build-report.json', JSON.stringify(report), () => {})
    })
  }
}
```
