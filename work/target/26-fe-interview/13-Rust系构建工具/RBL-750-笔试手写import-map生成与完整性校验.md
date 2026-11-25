---
title: [RBL-750] 笔试：手写 import map 生成器与完整性校验器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-750：笔试：手写 import map 生成器与完整性校验器

**答**：实现两部分。1) `generateMap(imports, urls)`：imports 为裸导入数组（含子路径如 'react/jsx-runtime'），urls: `Record<topPkg, url>`。规则：顶层包有映射 → 子路径映射为 `${pkgUrl}${subpath}`（'/' 连接）；无映射且无 scopes 匹配 → 抛错列出缺失。2) `validateMap(map, { allowCdn })`：校验每个 url：必须以 '/' 开头（自托管）或以 https:// 开头（第三方需 allowCdn=true）；含 '..' 抛错；返回 `{ problems, ok }`。边界：空 imports 返回空 map；重复包名合并（顶层映射一次）。

```javascript
function generateMap(imports, urls) {
  const map = {}; const missing = [];
  for (const spec of imports) {
    const [pkg, ...rest] = spec.split('/');
    const base = urls[pkg];
    if (!base) { missing.push(spec); continue; }
    map[spec] = rest.length ? `${base.replace(/\/$/, '')}/${rest.join('/')}` : base;
  }
  if (missing.length) throw new Error(`import map 缺失包映射: ${[...new Set(missing.map(s => s.split('/')[0]))].join(', ')}`);
  return { imports: map };
}

function validateMap(map, { allowCdn = false } = {}) {
  const problems = [];
  for (const [spec, url] of Object.entries(map.imports ?? map)) {
    if (url.includes('..')) { problems.push({ spec, issue: 'path-traversal', url }); continue; }
    const selfHosted = url.startsWith('/');
    const cdn = /^https:\/\/[\w.-]+/.test(url);
    if (!selfHosted && !(cdn && allowCdn))
      problems.push({ spec, issue: allowCdn ? 'invalid-url' : 'cdn-not-allowed', url });
  }
  return { problems, ok: problems.length === 0 };
}

// 自测
const urls = { react: '/vendor/react@18/index.mjs', lodash: '/vendor/lodash.mjs' };
let m = generateMap(['react', 'react/jsx-runtime', 'lodash'], urls);
console.log(m.imports.react === '/vendor/react@18/index.mjs');
console.log(m.imports['react/jsx-runtime'] === '/vendor/react@18/index.mjs/jsx-runtime');
console.log(m.imports.lodash === '/vendor/lodash.mjs');

let e; try { generateMap(['vue'], urls); } catch (x) { e = x; }
console.log(/缺失包映射.*vue/.test(e.message));

// 校验
console.log(validateMap(m).ok === true);                 // 全自托管
const cdnMap = { imports: { react: 'https://esm.sh/react@18' } };
console.log(validateMap(cdnMap).ok === false);           // 未允许 CDN
console.log(validateMap(cdnMap, { allowCdn: true }).ok === true);
const evil = { imports: { x: '/vendor/../secrets.mjs' } };
console.log(validateMap(evil).problems[0].issue === 'path-traversal');

console.log(Object.keys(generateMap([], urls).imports).length === 0);
```

**评分点**：
- 子路径映射拼接正确（顶层 URL + '/' + 子路径）；缺失包聚合报错（按顶层包去重）
- 校验三规则：自托管/CDN 白名单/路径穿越；allowCdn 开关语义清晰
- 边界：空 imports、url 规范化（尾斜杠）
- 能说清「import map 是版本协商与安全信任域的集中点」属于加分
