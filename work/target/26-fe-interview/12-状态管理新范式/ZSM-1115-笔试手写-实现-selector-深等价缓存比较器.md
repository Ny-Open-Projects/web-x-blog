---
title: [1115] 笔试手写：实现 selector 深等价缓存比较器
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, Zustand]
type: 笔试题
---

## 1115：笔试手写：实现 selector 深等价缓存比较器

**答**：实现 deepEqualSelector(selector)：包装 selector，输出值与上次缓存做深等价比较（原始值 === 快路径；对象逐键；数组逐项；Date 按时间戳；循环引用用 seen 双集合）。相等则返回上次引用（不触发重渲染），不等返回新值。提供 clear() 重置缓存。

```js
function deepEqualSelector(selector) {
  let cache = { has: false, value: undefined };
  const eq = (a, b, sa = new Set(), sb = new Set()) => {
    if (a === b) return true;
    if (typeof a !== 'object' || typeof b !== 'object' || !a || !b) return false;
    if (a instanceof Date && b instanceof Date) return +a === +b;
    if (sa.has(a) || sb.has(b)) return a === b; // 循环引用：同一对象视为相等
    sa.add(a); sb.add(b);
    const ka = Object.keys(a), kb = Object.keys(b);
    if (ka.length !== kb.length) return false;
    return ka.every(k => eq(a[k], b[k], sa, sb));
  };
  return {
    run(state) {
      const next = selector(state);
      if (cache.has && eq(cache.value, next)) return cache.value; // 引用稳定
      cache = { has: true, value: next };
      return next;
    },
    clear: () => { cache = { has: false, value: undefined }; },
  };
}
```

**评分点**：
- === 快路径在前（绝大多数比较在此终止）
- 循环引用用双 seen 集合（单向 seen 会误判自嵌套）
- 相等返回旧引用——这是防重渲染的本质
- 能讨论：深比较的代价，适用「selector 返回新数组/对象」且比较便宜的子树
