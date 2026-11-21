---
title: [JS-222] exec 与 match 的区别：全局下行为差异
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 正则]
type: 面试题
---

## JS-222：exec 与 match 的区别

**答**：
- 非全局：两者几乎一致（match = exec 的便捷版），返回完整匹配信息
- 全局差异：str.match(re) 一次性返回**所有匹配内容的数组**（无组信息）；re.exec 循环返回**逐个完整匹配对象**（含组）
- 选择：只要内容 → match 全局版；要组信息/位置 → matchAll 或 exec 循环
- matchAll（推荐）：返回迭代器，不推进 lastIndex 的坑自动规避，配合解构好用

```javascript
const s = 'a1b22c333';
// 全局 match：只有内容
s.match(/\d+/g);              // ['1', '22', '333']
// exec 循环：有组与 index
const re = /(\d+)/g;
let m;
while ((m = re.exec(s))) console.log(m[1], m.index);
// matchAll：现代推荐
[...s.matchAll(/(\d+)/g)].map(x => ({ v: x[1], i: x.index }));
```
