---
title: [BAS-192] 正则的命名捕获组和 lookaround 怎么写？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-192：正则的命名捕获组和 lookaround 怎么写？
**答**：
- 命名捕获组 `(?<name>...)`，结果在 match 的 groups 里取，比数组下标可读性高得多。
- lookahead `(?=...)` 匹配后面是某模式的位置，lookbehind `(?<=...)` 匹配前面是某模式的位置；`!` 版本是否定。
- 断言只"看"不"吃"字符：匹配结果里不包含断言部分，常用于提取定界符之间的内容。

```javascript
const re = /(?<year>\d{4})-(?<month>\d{2})/;      // 命名捕获组
const m = '2026-11-01'.match(re);
console.log(m.groups.year, m.groups.month);        // 2026 11

console.log('$99'.match(/(?<=\$)\d+/)[0]);         // 99 —— 后行断言，不匹配 $ 本身
console.log('99元'.match(/\d+(?=元)/)[0]);         // 99 —— 先行断言，不匹配 元
console.log('abc'.match(/(?<!a)b/));               // null —— 否定后行断言
```
