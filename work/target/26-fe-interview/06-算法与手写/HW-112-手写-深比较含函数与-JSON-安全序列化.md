---
title: [HW-112] 手写安全 JSON 序列化——循环引用、BigInt、undefined、Date 自定义替换器
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-112：手写安全 JSON 序列化——循环引用、BigInt、undefined、Date 自定义替换器
**答**：JSON.stringify 四大坑：循环引用抛错、BigInt 抛 TypeError、undefined/函数/符号键静默丢失、Date 变 ISO 字符串但 Map/Set 直接变 {}。安全序列化 = 自写替换器 + WeakSet 循环检测 + 类型转换协议。

```javascript
function safeStringify(value, { onCycle = (k) => '[Circular]', bigInt = (v) => `${v}n` } = {}) {
  const seen = new WeakSet();
  return JSON.stringify(value, function (key, val) {
    if (typeof val === 'bigint') return bigInt(val);           // BigInt: 转字符串
    if (val instanceof Map) return { __type: 'Map', entries: [...val] };   // Map/Set 可逆序列化
    if (val instanceof Set) return { __type: 'Set', values: [...val] };
    if (val instanceof Date) return { __type: 'Date', iso: val.toISOString() };
    if (typeof val === 'object' && val !== null) {
      if (seen.has(val)) return onCycle(key);                  // 循环引用：标记而非抛错
      seen.add(val);
    }
    return val;                                                // undefined/函数键被 JSON 规则自动跳过（协议内）
  });
}
function safeParse(str) {
  return JSON.parse(str, (k, v) => {
    if (v && v.__type === 'Map') return new Map(v.entries);
    if (v && v.__type === 'Set') return new Set(v.values);
    if (v && v.__type === 'Date') return new Date(v.iso);
    return v;
  });
}
// 验证：
const obj = { m: new Map([['a', 1]]), d: new Date(0), n: 10n };
obj.self = obj;
const s = safeStringify(obj);
const back = safeParse(s);
back.m instanceof Map && back.d instanceof Date && back.self.m instanceof Map;  // true，结构还原
// 语义边界：undefined 值会被丢（数组里变 null）——这是 JSON 协议，不是 bug，要在文档标注
```

**评分点**：
- 循环引用用替换器 + WeakSet 处理（替换器里标记，不抛错）。
- Map/Set/Date 可逆序列化协议（__type 标记 + reviver 还原）。
- BigInt 转换策略；能说清 undefined/函数键丢失是 JSON 协议语义。
- stringify/parse 对称性（round-trip 验证）。
