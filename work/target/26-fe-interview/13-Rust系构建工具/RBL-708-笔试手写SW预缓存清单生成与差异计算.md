---
title: [RBL-708] 笔试：手写 SW 预缓存清单生成与差异计算器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-708：笔试：手写 SW 预缓存清单生成与差异计算器

**答**：实现两个函数。1) `swManifest(manifest)`：manifest: `{ files: Array<{ name, role, hash?, content? }> }`。规则：排除 role==='service-worker' 与 .map 文件；条目 `{ url: '/' + name, revision }`（hash 存在用 hash，否则用注入 sha(content)；content 也缺则 revision 用 name 本身）。2) `swDiff(oldList, newList)`：返回 `{ add: string[], remove: string[], update: string[] }`——url 不在旧清单 → add；在旧但 revision 变 → update；在旧不在新 → remove。三个数组都按 url 排序。边界：旧清单为空（全 add）；新清单为空（全 remove）。

```javascript
function swManifest(manifest, { sha = (s) => 'h_' + s } = {}) {
  return manifest.files
    .filter(f => f.role !== 'service-worker' && !f.name.endsWith('.map'))
    .map(f => ({
      url: '/' + f.name,
      revision: f.hash ?? (f.content != null ? sha(f.content) : f.name),
    }))
    .sort((a, b) => a.url < b.url ? -1 : 1);
}

function swDiff(oldList = [], newList = []) {
  const oldMap = new Map(oldList.map(e => [e.url, e.revision]));
  const newMap = new Map(newList.map(e => [e.url, e.revision]));
  const add = [], update = [], remove = [];
  for (const [url, rev] of newMap) {
    if (!oldMap.has(url)) add.push(url);
    else if (oldMap.get(url) !== rev) update.push(url);
  }
  for (const url of oldMap.keys())
    if (!newMap.has(url)) remove.push(url);
  const s = (a) => [...a].sort();
  return { add: s(add), update: s(update), remove: s(remove) };
}

// 自测
const manifest = { files: [
  { name: 'index.html', role: 'entry-html', content: '<html>' },
  { name: 'sw.js', role: 'service-worker', hash: 'swH' },           // 排除
  { name: 'main.js.map', role: 'asset', hash: 'm1' },               // 排除
  { name: 'main.abc.js', role: 'chunk', hash: 'abc' },
  { name: 'logo.png', role: 'asset' },                              // 无 hash 无 content
] };
let m = swManifest(manifest);
console.log(JSON.stringify(m));
// ["/index.html"(h_<html>), "/logo.png"(logo.png), "/main.abc.js"(abc)]——sw 与 map 被排除

const oldM = [
  { url: '/index.html', revision: 'h_old' },
  { url: '/main.abc.js', revision: 'abc' },
  { url: '/removed.js', revision: 'r1' },
];
const newM = [
  { url: '/index.html', revision: 'h_new' },
  { url: '/main.abc.js', revision: 'abc' },
  { url: '/added.js', revision: 'a1' },
];
const d = swDiff(oldM, newM);
console.log(d.add.join(','));                            // /added.js
console.log(d.update.join(','));                         // /index.html
console.log(d.remove.join(','));                         // /removed.js

console.log(swDiff([], newM).add.length === 3);          // 全 add
console.log(swDiff(oldM, []).remove.length === 3);       // 全 remove
```

**评分点**：
- 清单排除规则正确（sw.js 与 sourcemap 排除是防更新循环的关键）；revision 三级取值（hash > content sha > name）
- diff 三分类正确且输出排序；旧空/新空边界
- 能说清「清单含 sw.js 会造成每次发布的全量缓存重建」属于加分
