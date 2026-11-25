---
title: [RBL-413] 笔试：手写 bundle 分析器（包体积归因）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-413：手写 bundle 分析器
**答**：实现 `analyzeBundle(modules)`：1) modules：`[{ id, name(如 node_modules/lodash/clone.js), size, chunks: ['main'] }]`；2) 输出按「包→目录→文件」聚合的体积树（node_modules/lodash 总量、子路径占比）；3) 重复包检测：同包多版本（从 name 解析版本）→ 告警与浪费体积；4) 重复内容检测：不同模块 hash 相同（重复打包）→ 合并建议；5) gzip 估算输入可选（真实 gzip 更准）；6) 输出 top N 占比列表。

```javascript
import crypto from 'node:crypto'

const PKG_RE = /node_modules\/((?:@[^/]+\/)?[^@/]+)(?:@?([^/]+))?/

export function analyzeBundle(modules, { top = 20 } = {}) {
  const tree = {}                                   // pkg → { size, files: Map }
  const byContent = new Map()                       // contentHash → [module]
  const versions = new Map()                        // pkg → Set<version>

  for (const m of modules) {
    const m2 = { ...m, contentHash: m.contentHash ?? crypto.createHash('md5').update(String(m.id)).digest('hex') }
    const match = PKG_RE.exec(m2.name)
    if (match) {
      const [, pkg, ver] = match
      tree[pkg] ??= { size: 0, files: new Map() }
      tree[pkg].size += m2.size
      tree[pkg].files.set(m2.name, (tree[pkg].files.get(m2.name) ?? 0) + m2.size)
      if (ver) (versions.get(pkg) ?? versions.set(pkg, new Set()).get(pkg)).add(ver)
    }
    if (!byContent.has(m2.contentHash)) byContent.set(m2.contentHash, [])
    byContent.get(m2.contentHash).push(m2)
  }

  const total = modules.reduce((s, m) => s + m.size, 0)
  const topPkgs = Object.entries(tree)
    .map(([pkg, { size, files }]) => ({ pkg, size, pct: +(size / total * 100).toFixed(1), files: [...files.entries()].sort((a, b) => b[1] - a[1]).slice(0, 5) }))
    .sort((a, b) => b.size - a.size).slice(0, top)

  const duplicated = [...versions.entries()].filter(([, v]) => v.size > 1)
    .map(([pkg, v]) => ({ pkg, versions: [...v], waste: tree[pkg]?.size ?? 0 }))
  const duplicatedContent = [...byContent.values()].filter((g) => g.length > 1)
    .map((g) => ({ modules: g.map((m) => m.name), waste: g[0].size * (g.length - 1) }))

  return { total, topPkgs, duplicatedPkgs: duplicated, duplicatedContent }
}
```
**评分点**：
- 包名解析处理 scoped 包（@scope/pkg 正则）
- 三层归因：包聚合树 / 多版本重复（浪费体积）/ 同内容重复（不同路径同内容）
- pct 分母 = 总体积；top N 排序降序
- gzip 口径提示（size vs gzip 的选择要声明）
