---
title: [RBL-436] 笔试：手写构建产物树去重器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-436：手写构建产物树去重器
**答**：实现 `dedupeAssets(files)`：1) files：Map<path, content>；2) 相同内容（hash 相同）的多个路径 → 保留一个实体文件，其余替换为引用（或 symlink/软链接声明）；3) 引用语义选择：硬链接（同文件系统）vs 单实体+manifest 映射（跨域 CDN 用 URL 映射）；4) 节省体积统计（deduped bytes）；5) 引用安全：实体文件删除时引用文件不能悬空（保留策略：hash 索引文件生命周期 = 最长引用者）；6) 输出 { entities, references, savedBytes }。

```javascript
import crypto from 'node:crypto'
import fs from 'node:fs'

export function dedupeAssets(files, { strategy = 'symlink' } = {}) {
  const byHash = new Map()                     // hash → 实体路径
  const entities = new Map()                   // path → content（实体）
  const references = new Map()                 // path → entityPath
  let saved = 0

  for (const [p, content] of files) {
    const hash = crypto.createHash('sha256').update(content).digest('hex')
    if (!byHash.has(hash)) {
      byHash.set(hash, p)
      entities.set(p, content)
    } else {
      const entity = byHash.get(hash)
      references.set(p, entity)
      saved += content.length
      if (strategy === 'symlink' && typeof fs.symlinkSync === 'function') {
        // 落盘时：fs.symlinkSync(entity, p) —— 相对路径防绝对耦合
      }
    }
  }

  // 生命周期：实体删除 = 该 hash 的全部引用者都不存在时才可删
  const refCounts = new Map()
  for (const entity of references.values())
    refCounts.set(entity, (refCounts.get(entity) ?? 0) + 1)

  return { entities, references, savedBytes: saved, refCounts,
    canDelete: (entityPath) => !refCounts.get(entityPath) }       // 无引用才可删实体
}
```
**评分点**：
- hash 判重 + 引用替换语义（symlink/URL 映射两种策略与适用面）
- 节省统计（deduped bytes）
- 生命周期安全（实体删除受引用计数约束——悬空引用防护）
- 硬链接 vs symlink 的文件系统边界说明
