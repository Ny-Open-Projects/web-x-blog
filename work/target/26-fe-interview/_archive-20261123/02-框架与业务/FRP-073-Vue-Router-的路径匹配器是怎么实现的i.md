---
title: [FRP-073] Vue Router 的路径匹配器是怎么实现的？`:id` 这类动态段如何变成正则？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-073：Vue Router 的路径匹配器是怎么实现的？`:id` 这类动态段如何变成正则？

**答**：
- 路由注册时把 `path` 编译成**正则 + 参数名列表**（源码用 path-to-regexp 思想）：`:id` 转成命名捕获组 `([^/]+)`，`*` 通配转 `(.*)`，静态段原样拼接。
- 查找时遍历 matcher 的 record（按**评分排序**：静态段 > 动态段 > 通配符，`/users/new` 优先于 `/users/:id`），第一个 `match(location)` 成功的返回 `{ params, matched }`。
- `parsePath` 先把 query/hash 拆掉再做匹配；匹配出的捕获组按顺序填进 params 对象。
- 手写要点：路径分词（`/` 分割）、每段决定"静态/参数/可选/通配"、生成正则、match 时解构捕获组。

```javascript
// 简化实现，帮助理解路径 -> 正则 -> match 的编译过程
function compilePath(path) {
  const params = [];
  const pattern = path
    .replace(/\/:([^/]+)/g, (_, name) => {           // :id -> 命名捕获组
      params.push(name);
      return '/([^/]+)';
    })
    .replace(/\*$/, () => {                          // * -> 通配捕获
      params.push('pathMatch');
      return '(.*)';
    });
  return { regex: new RegExp(`^${pattern}$`), params };
}

function createRouterMatcher(routes) {
  const matchers = routes
    .map((r) => ({ record: r, ...compilePath(r.path) }))
    // 评分：路径越"静态"越靠前，/users/new 优先于 /users/:id
    .sort((a, b) =>
      (b.record.path.split('/').filter((s) => !s.startsWith(':')).length) -
      (a.record.path.split('/').filter((s) => !s.startsWith(':')).length));

  function resolve(location) {
    const [pathname] = location.split('?');
    for (const m of matchers) {
      const result = pathname.match(m.regex);
      if (!result) continue;
      const params = {};
      m.params.forEach((name, i) => (params[name] = decodeURIComponent(result[i + 1])));
      return { matched: m.record, params };          // 返回匹配记录与动态参数
    }
    return null;
  }
  return { resolve, addRoute: (r) => matchers.unshift({ record: r, ...compilePath(r.path) }) };
}

const matcher = createRouterMatcher([
  { path: '/', component: 'Home' },
  { path: '/users/new', component: 'UserForm' },
  { path: '/users/:id', component: 'User' },
  { path: '/(.*)', component: 'NotFound' },
]);

console.log(matcher.resolve('/users/42'));   // matched User, params { id: '42' }
console.log(matcher.resolve('/users/new').matched.component); // UserForm：静态优先
console.log(matcher.resolve('/whatever').matched.component);  // NotFound：通配兜底
```
