---
title: [ALG-142] 权限系统路径匹配：`api/*/read` 的 `*` 匹配单个路径段，`api/**` 的 `**` 匹配任意多层。如何实现这个通配符匹配？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-142：权限系统路径匹配：`api/*/read` 的 `*` 匹配单个路径段，`api/**` 的 `**` 匹配任意多层。如何实现这个通配符匹配？
**答**：按 `/` 拆段后递归：`**` 匹配任意段数（包括 0 段，所以要枚举 k 从 j 到末尾）；`*` 只匹配一段（任意字符但不能跨界）；普通段要求完全相等。可加 memo 缓存 (i, j) 状态防指数回溯，最坏 O(n × m)。前端场景也可编译成正则一次复用。

```javascript
function pathMatch(pattern, path) {
  const ps = pattern.split('/'), xs = path.split('/');
  function match(i, j) {
    if (i === ps.length) return j === xs.length;      // 模式耗尽：路径也须耗尽
    if (ps[i] === '**') {
      for (let k = j; k <= xs.length; k++) {          // ** 吞 0 段到全部段
        if (match(i + 1, k)) return true;
      }
      return false;
    }
    if (j === xs.length) return false;                // 路径耗尽但模式没耗尽
    return (ps[i] === '*' || ps[i] === xs[j]) && match(i + 1, j + 1);
  }
  return match(0, 0);
}
// pathMatch('api/*/read', 'api/docs/read')  => true
// pathMatch('api/*/read', 'api/a/b/read')   => false（* 只匹配一段）
// pathMatch('api/**',     'api/a/b/c')      => true
```
