---
title: [DP-293] 笔试题：手写 JSON 序列化（循环引用/BigInt/函数）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-293：笔试题：手写 JSON 序列化（循环引用/BigInt/函数）？
**答**：实现 jsonStringify(value)：1) 基本类型/数组/对象；2) 循环引用输出 "[Circular]" 不死循环；3) BigInt 抛错或转字符串（可配置）；4) 函数/undefined 语义与原生一致（对象内跳过、数组内变 null）；5) 转义控制字符。
**评分点**：
- 递归栈 path 用 Set 检测循环（当前祖先链，不是已访问全量）。
- undefined/函数在对象 vs 数组中的不同语义正确。
- 字符串转义（\n \t 引号）与 key 引号完整。
- 数组空槽/稀疏处理正确。
```javascript
function jsonStringify(value, { bigint = 'string' } = {}) {
  const seen = new Set();                                // 2) 当前祖先链
  const encode = (v) => {
    if (v === null) return 'null';
    switch (typeof v) {
      case 'number': return Number.isFinite(v) ? String(v) : 'null';
      case 'boolean': return String(v);
      case 'bigint': return bigint === 'string' ? JSON.stringify(v.toString()) : null;   // 3)
      case 'string': return JSON.stringify(v).replace(/\n|\t|\r/g, c => c === '\n' ? '\\n' : c === '\t' ? '\\t' : '\\r'); // 5)
      case 'undefined': case 'function': return null;    // 数组内 → null
      case 'object': {
        if (seen.has(v)) return '"[Circular]"';           // 循环引用
        seen.add(v);
        try {
          if (Array.isArray(v)) return '[' + v.map(x => encode(x) ?? 'null').join(',') + ']';  // 4)
          const pairs = Object.entries(v)
            .filter(([, val]) => typeof val !== 'function' && val !== undefined)  // 对象内跳过
            .map(([k, val]) => `${JSON.stringify(k)}:${encode(val)}`);
          return '{' + pairs.join(',') + '}';
        } finally { seen.delete(v); }                     // 回溯：只防祖先链
      }
      default: return 'null';
    }
  };
  return encode(value) ?? 'null';
}
// 用：const a = { b: undefined, c: () => {}, arr: [1, undefined, null] }; a.self = a;
// jsonStringify(a) → '{"arr":[1,null,null],"self":"[Circular]"}'
```
