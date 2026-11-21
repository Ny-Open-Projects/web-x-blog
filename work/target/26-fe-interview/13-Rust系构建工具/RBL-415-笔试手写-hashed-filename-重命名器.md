---
title: [RBL-415] 笔试：手写 hashed filename 重命名与引用重写
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-415：手写 hashed filename 重命名器
**需求**：实现 `hashRename(files, { pattern })`：1) files：`Map<path, content>`；2) 重命名：`main.js → main.a1b2c3d4.js`（内容 sha256 前 8 位，替换扩展名前插入）；3) 引用重写：JS/CSS/HTML 内对旧路径的引用替换为新路径（字符串精确匹配 + 相对路径解析归一）；4) 两轮收敛：重命名后产物引用链二次校验（所有引用指向存在的文件）；5) 返回 { renamed: Map<old, new>, files: 新 Map, brokenRefs: [] }。

```javascript
import crypto from 'node:crypto'
import path from 'node:path'

const EXT_RE = /(\.[a-z]+)(\?.*)?$/

export function hashRename(files) {
  const renamed = new Map()
  for (const [p, content] of files) {
    const hash = crypto.createHash('sha256').update(content).digest('hex').slice(0, 8)
    const dir = path.dirname(p), ext = path.extname(p)
    const base = path.basename(p, ext)
    renamed.set(p, path.join(dir, `${base}.${hash}${ext}`))
  }
  const out = new Map()
  const broken = []
  for (const [oldPath, content] of files) {
    const newPath = renamed.get(oldPath)
    let next = content
    // 引用重写：归一相对路径 → 绝对映射
    for (const [from, to] of renamed) {
      if (from === oldPath) continue
      const rel = normalizeRef(oldPath, from)
      if (next.includes(rel)) next = next.replaceAll(rel, normalizeRef(newPath ?? to, from))
    }
    out.set(newPath, next)
  }
  // 二轮校验：所有引用存在
  for (const [p, content] of out) {
    const refs = content.match(/(?:\.\/|\.\.\/|\/)?[\w./-]+\.(?:js|css|png|woff2)/g) ?? []
    for (const r of refs) {
      const resolved = path.resolve(path.dirname(p), r)
      if (!out.has(resolved) && !isExternal(r)) broken.push({ from: p, ref: r })
    }
  }
  return { renamed, files: out, brokenRefs: broken }
}

function normalizeRef(target, from) {
  let rel = path.relative(path.dirname(from), target)
  if (!rel.startsWith('.')) rel = './' + rel
  return rel
}
const isExternal = (r) => r.startsWith('http') || r.startsWith('//')
```
**评分点**：
- hash 插入位置正确（扩展名前）；内容 hash（非路径/时间）
- 引用重写用「相对路径归一」后匹配（绝对路径比对会漏相对引用）
- 二轮校验引用闭合（brokenRefs 输出——引用重写遗漏可检测）
- 外链排除（http// 开头不重写）
