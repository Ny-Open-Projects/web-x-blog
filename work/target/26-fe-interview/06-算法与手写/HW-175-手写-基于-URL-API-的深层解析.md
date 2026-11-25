---
title: [HW-175] 手写 URL 深层解析——相对路径解析、searchParams 数组语义、锚点与路由冲突处理
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-175：手写 URL 深层解析——相对路径解析、searchParams 数组语义、锚点与路由冲突处理
**答**：URL 工具封装：相对路径 → 绝对（URL 构造器 base 参数，代替手写拼接）；searchParams 的数组语义规范化（getAll vs 逗号——与 HW-152 的编码对称）；hash 与 history 路由冲突（hash 含路由时禁止业务使用锚点）；中文编码一致性（encodeURI vs encodeURIComponent 边界——整 URL 用 encodeURI、参数值用 encodeURIComponent）。

```javascript
function parseURL(input, base = location.href) {
  const u = new URL(input, base);                        // 相对路径自动解析（构造器兜底非法值需 try）
  const params = {};
  // 数组语义：同键多次 = 数组（?tag=a&tag=b）；单键逗号 = 数组（?tags=a,b）—— 统一为数组
  for (const key of new Set(u.searchParams.keys())) {
    const all = u.searchParams.getAll(key);
    params[key] = all.length > 1 ? all
      : (all[0]?.includes(',') ? all[0].split(',') : all[0]);
  }
  const isHashRouter = u.hash.startsWith('#/');           // hash 路由占用锚点
  return {
    path: u.pathname, params, hash: isHashRouter ? null : u.hash.slice(1),   // 路由 hash 不算业务锚点
    query: u.search,
    resolve(rel) { return new URL(rel, u).href; },        // 相对解析
    withParams(patch) {
      for (const [k, v] of Object.entries(patch)) {
        u.searchParams.delete(k);
        (Array.isArray(v) ? v : [v]).forEach((x) => v != null && u.searchParams.append(k, x));
      }
      return u.href;
    },
  };
}
// parseURL('goods/88?tag=a&tag=b', 'https://s.com/list/')
// => { path: '/list/goods/88', params: { tag: ['a','b'] }, ... }
// 陷阱清单：
// hash 路由站点的锚点语义冲突（#section 与 #/route 不可共存）
// encodeURIComponent('a b') => 'a%20b'（参数值）；encodeURI 保留 ? & =（整 URL）—— 用错则 & 被编码破坏结构
```

**评分点**：
- URL 构造器 base 解析相对路径（拒绝手写字符串拼接）。
- searchParams 数组语义统一（getAll 与逗号双格式归一）。
- hash 路由与锚点冲突的处理决策。
- encodeURI vs encodeURIComponent 边界陷阱说清——本题高频考点。
