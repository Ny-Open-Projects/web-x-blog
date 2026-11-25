---
title: [MFW-654] 笔试：手写 URL 规范化器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-654：笔试：手写 URL 规范化器

**答**：实现 `canonicalize(url, { stripParams, paramOrder })`。规则：1) 路径规范化：尾部斜杠去除、`//` 压缩、`../`/`./` 解析（RBL-898 normalize 扩展）；2) query 参数：stripParams 列表内的参数删除（utm_* 追踪参数——缓存键统一）；paramOrder 白名单排序（白名单内按声明序、白名单外按字典序——规范化顺序）；3) 重复参数保留第一个（cat=a&cat=b → cat=a）；4) 空 query（?）去除；5) 返回规范化 URL。边界：纯 query 无路径（?a=1——错误 URL 原样）；带 hash 的 URL（hash 保留）；相对路径。

```javascript
function canonicalize(url, { stripParams = [], paramOrder = [] } = {}) {
  const [rawPath, rawQuery = '', hash = ''] = url.split(/([?#])/).reduce((acc, part, i) => {
    if (part === '?' || part === '#') acc.push(part);
    else acc[acc.length - 1] += part;
    return acc;
  }, ['']);
  // 路径规范化
  let path = rawPath.split('/').filter(s => s && s !== '.')
    .reduce((acc: string[], seg) => seg === '..' ? (acc.pop(), acc) : (acc.push(seg), acc), [])
    .map(s => s.replace(/\/{2,}/g, '/')).join('/');
  path = '/' + path;
  // query 规范化
  const sp = new URLSearchParams(rawQuery);
  const entries = [...sp.entries()];
  const deduped = new Map();
  for (const [k, v] of entries)
    if (!deduped.has(k)) deduped.set(k, v);              // 重复保留第一个
  for (const k of stripParams) deduped.delete(k);        // strip
  // 排序：白名单序优先，其余字典序
  const keys = [...deduped.keys()].sort((a, b) => {
    const ia = paramOrder.indexOf(a), ib = paramOrder.indexOf(b);
    if (ia !== -1 && ib !== -1) return ia - ib;
    if (ia !== -1) return -1;
    if (ib !== -1) return 1;
    return a.localeCompare(b);
  });
  const qs = keys.map(k => `${k}=${deduped.get(k)}`).join('&');
  return `${path}${qs ? '?' + qs : ''}${hash ? '#' + hash : ''}`;
}

// 自测
// 路径规范化
console.log(canonicalize('/a/b/../c//d/') === '/a/c/d');
// strip 追踪参数
console.log(canonicalize('/p?utm_source=x&id=1', { stripParams: ['utm_source'] }) === '/p?id=1');
// 白名单排序
r = canonicalize('/p?sort=price&cat=elec&q=x',
  { paramOrder: ['cat', 'sort', 'q'] });
console.log(r === '/p?cat=elec&sort=price&q=x');
// 非白名单字典序
r = canonicalize('/p?zebra=1&apple=2', {});
console.log(r === '/p?apple=2&zebra=1');
// 重复参数保留第一个
console.log(canonicalize('/p?cat=a&cat=b') === '/p?cat=a');
// 空 query 去除
console.log(canonicalize('/p?') === '/p');
// hash 保留
console.log(canonicalize('/p?id=1#sec', {}) === '/p?id=1#sec');
// ../ 解析
console.log(canonicalize('/a/b/../c') === '/a/c');
```

**评分点**：
- 路径规范化完整（../、.、双斜杠、尾斜杠——RBL-898 扩展）
- query 三层：strip（追踪参数）/去重（保留首）/排序（白名单序优先）；hash 保留
- 边界（空 query/纯 query/相对路径的容错）；规范化让缓存键统一（RBL-582 键规范化）
- 能说清「URL 规范化 = 缓存键统一 + SEO canonical 的基础——追踪参数进缓存键 = 缓存碎片化」属于加分
