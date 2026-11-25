---
title: [MFW-892] 笔试：手写内容寻址的 Merkle 哈希计算器（产物树指纹）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-892：笔试：手写内容寻址的 Merkle 哈希计算器（产物树指纹）

**答**：
- 结论：把产物目录组织成 merkle tree——文件哈希作为叶，目录哈希由子节点哈希组合得出；根哈希代表整棵产物树，任一字节变化都会改变根。
- 关键：叶节点按路径排序后拼接哈希，保证顺序无关；目录哈希 = 子节点哈希的稳定拼接再哈希。
- 追问钩子：merkle 树相比「所有文件拼一起哈希」好在哪？——能定位到具体变化的文件（增量比对），而非整树重传。

```javascript
function hash(s) { let h = 5381; for (const c of s) h = ((h << 5) + h + c.charCodeAt(0)) >>> 0; return h.toString(16); }

function merkle(files) {
  // files: { 'a.js': 'content', 'css/b.css': 'content2' }
  const dirs = new Map();       // dir -> [fileHash]
  for (const [path, content] of Object.entries(files)) {
    const dir = path.includes('/') ? path.slice(0, path.lastIndexOf('/')) : '';
    if (!dirs.has(dir)) dirs.set(dir, []);
    dirs.get(dir).push({ name: path, hash: hash(content) });
  }
  const layer = {};
  for (const [dir, entries] of dirs) {
    entries.sort((a, b) => a.name.localeCompare(b.name));   // 稳定排序
    layer[dir || '.'] = hash(entries.map(e => e.name + ':' + e.hash).join('|'));
  }
  const root = hash(Object.keys(layer).sort().map(d => d + ':' + layer[d]).join('|'));
  return { root, layer };
}
// 自测：内容变化 → 根哈希变化
const r1 = merkle({ 'a.js': 'v1' });
const r2 = merkle({ 'a.js': 'v2' });
console.log(r1.root !== r2.root);                    // true
```

**评分点**：
- 叶节点按路径稳定排序，保证顺序无关
- 目录哈希由子节点哈希组合，根哈希代表整棵树
- 能定位变化文件（增量比对），任一字节变化改变根哈希
- 边界：空目录、根目录命名、同名不同目录处理（加分）
