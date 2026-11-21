---
title: [ALG-143] 微前端子应用注册时路由写法混乱：`/a/b/../c/./d/`、`//a//c`。如何实现路由 normalize（简化路径，LeetCode 71 场景化）？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-143：微前端子应用注册时路由写法混乱：`/a/b/../c/./d/`、`//a//c`。如何实现路由 normalize（简化路径，LeetCode 71 场景化）？
**答**：栈处理：按 `/` 拆段，空段与 `.` 忽略，`..` 弹栈（回上级），其余入栈；最后拼 `/` + 栈内容。注意 `/../` 开头弹空栈要忽略（到根了）。O(n)。

```javascript
function normalizePath(path) {
  const stack = [];
  for (const seg of path.split('/')) {
    if (seg === '' || seg === '.') continue; // 空段与当前目录忽略
    if (seg === '..') {
      if (stack.length) stack.pop();         // 回上级；已在根则忽略
    } else {
      stack.push(seg);
    }
  }
  return '/' + stack.join('/');
}
// normalizePath('/a/b/../c/./d/') => '/a/c/d'
// normalizePath('/../a') => '/a'
// 场景：qiankun 注册子应用 activeRule 前统一规范化
```
