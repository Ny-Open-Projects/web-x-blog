---
title: [ALG-013] 路由跳转后要解析 `https://a.com/list?tag=front%20end&kw=a+b&tag=vue#top` 这样的 URL，正确处理 `%20`、`+` 编码与重复 key。手写 parseQuery？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-013：路由跳转后要解析 `https://a.com/list?tag=front%20end&kw=a+b&tag=vue#top` 这样的 URL，正确处理 `%20`、`+` 编码与重复 key。手写 parseQuery？
**答**：先取 `?` 到 `#` 之间的部分，按 `&` 拆分、每段按第一个 `=` 拆 key/value；还原时先把 `+` 换成空格再 `decodeURIComponent`；重复 key 用数组收集。时间 O(n)，空间 O(n)。

```javascript
function parseQuery(url) {
  const qs = url.slice(url.indexOf('?') + 1).split('#')[0];
  const res = {};
  if (!qs) return res;
  for (const pair of qs.split('&')) {
    if (!pair) continue;
    const eq = pair.indexOf('=');
    const rawK = eq === -1 ? pair : pair.slice(0, eq);
    const rawV = eq === -1 ? '' : pair.slice(eq + 1);
    const k = decodeURIComponent(rawK.replace(/\+/g, ' '));
    const v = decodeURIComponent(rawV.replace(/\+/g, ' '));
    if (k in res) res[k] = [].concat(res[k], v);
    else res[k] = v;
  }
  return res;
}
// => { tag: ['front end', 'vue'], kw: 'a b' }
```
