---
title: [RBL-404] 笔试：手写构建产物 manifest 生成器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-404：手写构建产物 manifest 生成器
**需求**：实现 `generateManifest(assets, meta)`：1) assets：文件树（path→content）；2) 生成 `{ version, files: { path: { hash, size } }, entry, envHash }`；3) hash 用内容 sha256（basename 前 8 位作为文件名后缀的重命名映射：old→hashed）；4) entry 为入口 html 引用替换（html 里的产物路径替换为 hashed 路径）；5) envHash 来自 meta.env 清单（参与指纹）；6) 递归目录遍历支持。

```javascript
import crypto from 'node:crypto'
import path from 'node:path'

function walk(tree, prefix = '', out = {}) {                // tree: 嵌套对象或字符串内容
  for (const [name, v] of Object.entries(tree)) {
    const p = prefix ? `${prefix}/${name}` : name
    if (typeof v === 'string') out[p] = v
    else walk(v, p, out)
  }
  return out
}

export function generateManifest(assetsTree, meta = {}) {
  const files = walk(assetsTree)
  const renames = {}
  const fileMeta = {}
  for (const [p, content] of Object.entries(files)) {
    const hash = crypto.createHash('sha256').update(content).digest('hex').slice(0, 8)
    const ext = path.extname(p)
    const hashed = p.replace(ext, `.${hash}${ext}`)
    renames[p] = hashed
    fileMeta[hashed] = { hash, size: Buffer.byteLength(content) }
  }
  // entry html 引用替换
  if (files['index.html']) {
    let html = files['index.html']
    for (const [old, nw] of Object.entries(renames)) html = html.replaceAll(old, nw)
    fileMeta[renames['index.html']] = { hash: fileMeta[renames['index.html']].hash,
      size: Buffer.byteLength(html) }
    files['index.html'] = html
    renames['index.html'] = renames['index.html']
  }
  const envHash = crypto.createHash('sha256')
    .update(JSON.stringify(meta.env ?? [])).digest('hex').slice(0, 8)
  return { version: meta.version ?? Date.now(), envHash, files: fileMeta, renames }
}
```
**评分点**：
- 递归树遍历（支持嵌套目录）；hash 用内容 sha256（8 位截断约定明确）
- html 引用替换与替换后大小更新（manifest 与实际一致）
- envHash 参与指纹（漏 env 是指纹错误主因）
- renames 映射（部署/回滚/对账的消费依据）
