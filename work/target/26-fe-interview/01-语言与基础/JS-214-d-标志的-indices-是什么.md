---
title: [JS-214] d 标志的 indices 是什么
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 正则]
type: 面试题
---

## JS-214：d 标志的 indices 是什么

**答**：
- d 标志（ES2022）：exec/match 结果多出 indices 数组——每个捕获组在原字符串中的起止位置
- 解决的问题：以前只有「组内容」，想知道「这段内容在原文的哪一段」必须自己 indexOf 重新定位（嵌套/重复内容时不可靠）
- 结构：m.indices[0] 是整体匹配区间，m.indices.groups.name 是命名组区间
- 应用：编辑器高亮、语法着色、错误定位——需要「位置」而非「内容」的场景

```javascript
const re = /(?<area>\d{3})-(?<num>\d{4})/d;
const m = re.exec('电话 010-1234 请拨打');
console.log(m.indices);            // [[3, 11], [3, 6], [7, 11]]
console.log(m.indices.groups.area); // [3, 6] —— 在原文中的区间
```
