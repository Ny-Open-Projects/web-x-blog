---
title: [PER-804] 手写一个 setData 路径 diff 工具：对比新旧 state 生成最小路径更新集
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-804：手写一个 setData 路径 diff 工具：对比新旧 state 生成最小路径更新集

**答**：
- 需求：实现 diffState(oldState, newState)，输出最小路径更新集 { "a.b.c": value, "list[2].x": value }：标量变化输出路径赋值；数组先按引用对比，相等则跳过，不等则逐元素递归；对象递归下钻。删除的字段输出 null（约定置空）。
- 边界：循环引用检测（防栈溢出）；数组长度变化输出 length 路径 + 新元素；输出按键排序保证可测。
- 评分点：最小路径正确性（不产生冗余父路径）；数组元素级 diff；循环引用处理。

```javascript
function diffState(oldS, newS, path = '', out = {}, seen = new WeakSet()) {
  if (oldS === newS) return out;                                 // 引用相等：跳过
  if (typeof newS !== 'object' || newS === null || typeof oldS !== 'object' || oldS === null)
    return void (out[path || '.'] = newS);                       // 标量或类型变化
  if (seen.has(newS)) return out; seen.add(newS);                // 循环引用保护
  if (Array.isArray(newS)) {
    const oldArr = Array.isArray(oldS) ? oldS : [];
    for (let i = 0; i < newS.length; i++)
      diffState(oldArr[i], newS[i], `${path}[${i}]`, out, seen); // 元素级 diff
    if (newS.length !== oldArr.length) out[`${path}.length`] = newS.length;
    return out;
  }
  const keys = new Set([...Object.keys(oldS || {}), ...Object.keys(newS)]);
  for (const k of keys) {                                        // 对象递归下钻
    const p = path ? `${path}.${k}` : k;
    if (!(k in newS)) out[p] = null;                             // 删除 → 置空约定
    else diffState((oldS || {})[k], newS[k], p, out, seen);
  }
  return out;
}
// diffState({a:1,list:[{x:1}]}, {a:2,list:[{x:1},{x:2}]})
// => { 'a': 2, 'list[1]': {x:2}, 'list.length': 2 }
```
