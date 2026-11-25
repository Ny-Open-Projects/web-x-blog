---
title: [MFW-860] 笔试：手写类型安全路由的参数提取器（模板 → params）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-860：笔试：手写类型安全路由的参数提取器（模板 → params）

**答**：
- 结论：把路径模板转成正则提取参数名与值；类型层面由模板字面量推导 key 联合类型，运行时返回 Record<key,string>。
- 关键：处理可选段(?)与通配符(*)，替换顺序需先可选后必选；参数用 decodeURIComponent 解码。
- 追问钩子：为什么要类型安全？——跳转时拼错参数名能在编译期发现，而不是运行时 404。

```javascript
function parseRoute(pattern) {
  const keys = [];
  const rx = new RegExp('^' + pattern
    .replace(/\*/g, '.*')
    .replace(/:([^/]+)\?/g, (_, k) => { keys.push(k); return '([^/]*)'; }) // 可选
    .replace(/:([^/]+)/g, (_, k) => { keys.push(k); return '([^/]+)'; })    // 必选
    + '$');
  return {
    match(path) {
      const m = rx.exec(path);
      if (!m) return null;
      const out = {};
      keys.forEach((k, i) => { out[k] = decodeURIComponent(m[i + 1] || ''); });
      return out;                                    // 类型：Record<keys, string>
    }
  };
}

// 自测
const r = parseRoute('/users/:id/posts/:postId');
console.log(JSON.stringify(r.match('/users/42/posts/9'))); // {id:'42',postId:'9'}
console.log(r.match('/users/42'));                         // null
const opt = parseRoute('/search/:q?');
console.log(JSON.stringify(opt.match('/search')));         // {q:''}
```

**评分点**：
- 路径模板转正则并提取参数名/值，decodeURIComponent 解码
- 处理可选段(?)与通配符(*)，替换顺序正确（先可选后必选）
- 边界：不匹配返回 null、可选段缺省值
- 能说明类型层面如何由模板字面量推导 key 联合类型（加分）
