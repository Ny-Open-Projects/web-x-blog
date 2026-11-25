---
title: [DP-335] 笔试题：手写 URL 状态同步器（查询参数双向）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-335：笔试题：手写 URL 状态同步器（查询参数双向）？
**答**：实现 urlState：1) 读：searchParams → 状态对象（类型还原 number/boolean/array）；2) 写：状态变更 → replaceState（不产生历史条目，防后退爆炸）；3) 白名单字段；4) 浏览器前进/后退监听恢复。
**评分点**：
- 类型还原正确（'?a=1&page=2&tags=x,y' → { a: true, page: 2, tags: [...] }）。
- replaceState vs pushState 语义正确（筛选条件 replace，翻页 push 可选）。
- 白名单过滤防注入任意参数。
- popstate 监听恢复。
```javascript
function createUrlState(schema /* { page: 'number', tags: 'array', q: 'string' } */) {
  const read = () => {
    const sp = new URLSearchParams(location.search);
    const state = {};
    for (const [key, type] of Object.entries(schema)) {    // 3) 白名单
      const v = sp.get(key);
      if (v == null) continue;
      state[key] = type === 'number' ? +v : type === 'array' ? v.split(',').filter(Boolean)
        : type === 'boolean' ? v !== 'false' : v;
    }
    return state;
  };
  const write = (state, { push = false } = {}) => {        // 2)
    const sp = new URLSearchParams();
    for (const [k, v] of Object.entries(state))
      if (v != null && v !== '' && !(Array.isArray(v) && !v.length))
        sp.set(k, Array.isArray(v) ? v.join(',') : String(v));
    const url = `${location.pathname}?${sp}`;
    push ? history.pushState(null, '', url) : history.replaceState(null, '', url);
  };
  const onPop = (fn) => addEventListener('popstate', () => fn(read()));   // 4)
  return { read, write, onPop };
}
```
