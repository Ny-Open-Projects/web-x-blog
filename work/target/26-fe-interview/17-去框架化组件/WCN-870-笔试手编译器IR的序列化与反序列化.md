---
title: [WCN-870] 笔试：手写编译器 IR 的「序列化与反序列化」（跨进程/缓存）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-870：笔试：手写编译器 IR 的「序列化与反序列化」（跨进程/缓存）

**题目**：编译器 IR 节点形如 `{ type, props: {...}, children: [...] }`，其中 props 可能含函数（如 `expr: () => count * 2`）、Set、Map、undefined、循环引用（节点间互相引用）。实现 `serializeIR(root)` 与 `deserializeIR(data)`。要求：① 函数序列化成源码字符串（用 `fn.toString()`），反序列化时用 `new Function` 还原（注意安全边界：仅用于可信 IR）；② Set/Map 转成带类型标记的数组，还原时重建；③ undefined、NaN、Infinity 用标记保留（不能丢成 null）；④ 循环引用用 id 引用表处理（每个节点赋 id，引用处写 `{__ref:id}`）；⑤ 输出为可 JSON.stringify 的普通对象。边界：共享节点（非循环但多次引用）也用引用还原为同一对象；反序列化后节点结构完整可用。

**答**：

```javascript
function serializeIR(root) {
  const seen = new Map(); let nextId = 1;
  function enc(v) {
    if (typeof v === 'function') return { __fn: v.toString() };
    if (v === undefined) return { __undef: true };
    if (typeof v === 'number' && !Number.isFinite(v)) return { __num: String(v) };
    if (v instanceof Set) return { __set: [...v].map(enc) };
    if (v instanceof Map) return { __map: [...v].map(([k, val]) => [enc(k), enc(val)]) };
    if (v && typeof v === 'object') {
      if (seen.has(v)) return { __ref: seen.get(v) };
      const id = nextId++; seen.set(v, id);
      const out = {};
      for (const [k, val] of Object.entries(v)) out[k] = enc(val);
      out.__id = id;
      return out;
    }
    return v;
  }
  return enc(root);
}
function deserializeIR(data) {
  const refs = new Map();
  function dec(v) {
    if (!v || typeof v !== 'object') return v;
    if ('__ref' in v) return refs.get(v.__ref);
    if ('__fn' in v) return new Function('return (' + v.__fn + ')')(); // 仅可信 IR
    if ('__undef' in v) return undefined;
    if ('__num' in v) return Number(v.__num);
    if ('__set' in v) return new Set(v.__set.map(dec));
    if ('__map' in v) return new Map(v.__map.map(([k, val]) => [dec(k), dec(val)]));
    const node = {}; for (const [k, val] of Object.entries(v)) if (k !== '__id') node[k] = dec(val);
    if (v.__id) refs.set(v.__id, node);
    return node;
  }
  return dec(data);
}
const ir = { type: 'Expr', props: { deps: new Set(['count']), expr: () => 1, missing: undefined }, children: [] };
const restored = deserializeIR(serializeIR(ir));
console.log(restored.props.expr(), restored.props.deps.has('count')); // 1, true
```

**评分点**：
- 函数/Set/Map/特殊数值用类型标记正确编解码（IR 语义保真）。
- 循环/共享引用用 id 引用表，还原为同一对象（关键难点）。
- undefined/NaN/Infinity 不丢（JSON 天生缺陷的补救）。
- 注明函数还原的安全边界（仅可信 IR），有安全意识。
