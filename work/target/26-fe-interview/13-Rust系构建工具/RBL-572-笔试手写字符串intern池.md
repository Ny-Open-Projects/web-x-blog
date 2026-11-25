---
title: [RBL-572] 笔试：手写线程安全的字符串 Intern 池（含容量与统计）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-572：笔试：手写线程安全的字符串 Intern 池（含统计与上限）

**答**：实现 `createPool({ maxEntries })`：`intern(s)` 返回稳定 id（同串同 id，幂等）；`get(id)` 反查；`stats()` 返回 `{ entries, hits, misses }`（hits=重复 intern 次数，misses=新 intern 次数）；超过 maxEntries 后新字符串不再驻存，返回 -1。要求 intern 为 O(1) 均摊；`get` 越界返回 undefined；负 id/非字符串入参抛 TypeError。

```javascript
function createPool({ maxEntries = Infinity } = {}) {
  const map = new Map(); const vec = [];
  let hits = 0, misses = 0;
  return {
    intern(s) {
      if (typeof s !== 'string') throw new TypeError('intern: string required');
      const known = map.get(s);
      if (known !== undefined) { hits++; return known; }      // 幂等：同串同 id
      if (vec.length >= maxEntries) return -1;                 // 上限保护
      const id = vec.length;
      map.set(s, id); vec.push(s); misses++;
      return id;
    },
    get(id) {
      if (!Number.isInteger(id) || id < 0 || id >= vec.length) return undefined;
      return vec[id];
    },
    stats() { return { entries: vec.length, hits, misses }; },
  };
}

// 自测
const p = createPool({ maxEntries: 3 });
const a = p.intern('/src/a.js'), b = p.intern('/src/a.js'), c = p.intern('/src/b.js');
p.intern('/src/c.js'); const d = p.intern('/src/d.js');       // 超上限 -> -1
// 断言：
// a === b（同串同 id）；d === -1；
// p.get(a) === '/src/a.js'；p.get(99) === undefined；p.get(-1) === undefined
// p.stats() = { entries: 3, hits: 1, misses: 3 }
let threw = false;
try { p.intern(42); } catch (e) { threw = e instanceof TypeError; }
// 断言：threw === true
```

**评分点**：
- 幂等性正确（同串同 id）且 hits/misses 统计口径清晰
- maxEntries 超限返回 -1 而非抛错（调用方可降级为普通字符串），且不破坏已有驻存
- get 的边界处理完整（越界/负数/非整数 -> undefined）
- intern O(1) 均摊（Map），get O(1)（数组下标）——能说出 trade-off（表全局驻存的泄漏边界）
