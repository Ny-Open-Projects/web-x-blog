---
title: [HW-304] 手写一个 JSON 查询引擎：点路径与数组过滤语法
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-304：手写一个 JSON 查询引擎：点路径与数组过滤语法

**答**：
- 需求：实现 JSONQuery：语法 a.b[0].c、a[*].x（全量投影）、a[?(@.score>80)]（过滤，@ 代指当前元素）、a.b|length（管道取长度）；parse 编译为执行函数（可缓存复用）。
- 边界：路径不存在返回 undefined（不抛错）；过滤表达式支持 > < == 与字段访问；空数组投影返回 []。
- 评分点：编译缓存；@ 上下文；undefined 语义。

```javascript
function compileQuery(q) {
  const segs = q.split('.').map(s => {
    const arr = s.match(/^(\w+)?\[(.+)\]$/);
    if (arr) return { key: arr[1], selector: arr[2] };
    return { key: s };
  });
  return data => {
    let cur = data;
    for (const seg of segs) {
      if (seg.key) cur = cur?.[seg.key];
      if (cur == null) return undefined;
      if (seg.selector != null) {
        if (seg.selector === '*') cur = (Array.isArray(cur) ? cur : [cur]).map(x => x).flat();   // 全量投影
        else if (seg.selector.startsWith('?')) {                         // 过滤
          const expr = seg.selector.slice(2, -1);                       // @.score>80
          const m = expr.match(/@\.(\w+)\s*([><=!]+)\s*(.+)/);
          if (!m) throw new Error('bad-filter');
          const [, f, op, raw] = m;
          const val = isNaN(+raw) ? raw.replace(/['"]/g, '') : +raw;
          const cmp = { '>': (a, b) => a > b, '<': (a, b) => a < b,
            '==': (a, b) => a == b, '>=': (a, b) => a >= b, '<=': (a, b) => a <= b }[op];
          cur = cur.filter(x => cmp(x?.[f], val));
        } else cur = cur[+seg.selector];                                 // 索引
      }
    }
    return cur;
  };
}
const cache = new Map();
function query(q, data) {
  if (!cache.has(q)) cache.set(q, compileQuery(q));      // 编译缓存
  return cache.get(q)(data);
}
// query('users[?(@.age>18)].name', {users:[...]})
```
