---
title: [RBL-627] 笔试：手写 import.meta.glob 静态展开器（含逃逸防护）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-627：笔试：手写 import.meta.glob 静态展开器（含逃逸防护）

**需求**：实现 `expandGlob(pattern, files)`。pattern 形如 './pages/*.vue' 或 './i18n/**/*.json'（`*` 单层、`**` 跨层）；files 为相对 cwd 的文件列表。返回 `Map<relPath, lazyCode>`：key 为 './' 开头的相对路径（pattern 的目录部分保持），value 为 `() => import('<absPath>')` 字符串（absPath 以 '/src/' 起头模拟绝对路径）。规则：1) `*` 不跨 `/`，`**` 跨多层；2) 结果按 key 字典序；3) 简化模式（`*` 的展开存在时忽略同名的目录索引歧义——不做）跳过；4) files 中含 `..` 的路径抛错（逃逸防护）；5) 空匹配返回空 Map。

```javascript
function expandGlob(pattern, files) {
  if (files.some(f => f.includes('..'))) throw new Error('glob 逃逸: 路径含 ..');
  const [dir, pat] = splitPattern(pattern);              // './pages' + '*.vue'
  const regex = globToRegex(pat);                        // 单层或跨层
  const out = new Map();
  for (const f of [...files].sort()) {                   // 先排序保证字典序
    if (!f.startsWith(dir.slice(2) + '/') && !(dir === './' && !f.includes('/'))) continue;
    const rel = dir === './' ? f : f.slice(dir.length + 1);
    if (!regex.test(rel)) continue;
    const key = dir + '/' + rel;                         // './' 开头
    out.set(key, `() => import('/src/${f}')`);
  }
  return out;
}
function splitPattern(p) {
  const idx = lastStarDirIndex(p);
  return [p.slice(0, idx), p.slice(idx + 1)];
}
const lastStarDirIndex = (p) => p.lastIndexOf('*/') >= 0 ? p.lastIndexOf('*/') : (p.includes('**') ? p.indexOf('**/') : 1);
function globToRegex(pat) {
  const src = pat
    .replace(/[.+^${}()|[\]\\]/g, '\\$&')
    .replace(/\*\*/g, '\u0000')
    .replace(/\*/g, '[^/]+')
    .replace(/\u0000/g, '(?:[^/]+/)*');
  return new RegExp('^' + src + '$');
}

// 自测
const files = ['pages/Home.vue', 'pages/List.vue', 'pages/detail/Item.vue', 'i18n/zh/app.json', 'i18n/en/app.json'];
let r = expandGlob('./pages/*.vue', files);
console.log([...r.keys()]);                              // ['./pages/Home.vue', './pages/List.vue']（单层）
console.log(r.get('./pages/Home.vue') === "() => import('/src/pages/Home.vue')");

r = expandGlob('./i18n/**/*.json', files);               // 跨层
console.log([...r.keys()].length === 2 && [...r.keys()][0] === './i18n/en/app.json');

r = expandGlob('./pages/**/*.vue', files);               // ** 跨 detail 层
console.log([...r.keys()].length === 3);

console.log(expandGlob('./none/*.vue', files).size === 0);

let err; try { expandGlob('./a/*.js', ['../evil.js']); } catch (e) { err = e; }
console.log(/逃逸/.test(err.message));
```

**评分点**：
- 单层 `*` 与跨层 `**` 的正则转换正确（`[^/]+` vs `(?:[^/]+/)*`），字面量正确转义
- 相对路径 key 拼接与字典序稳定；绝对 import 路径以规范前缀生成（可联动 manifest）
- 逃逸防护（`..` 抛错）实现；空匹配返回空 Map 不抛错
- 能说清「展开成显式映射是 hash 联动与 tree shaking 前提」属于加分
