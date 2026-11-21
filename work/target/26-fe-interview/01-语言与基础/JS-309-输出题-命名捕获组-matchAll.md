---
title: [JS-309] 输出题：命名捕获组与 matchAll
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 正则]
type: 笔试题
---

## JS-309：输出题：命名捕获组与 matchAll

**题目**：写出 matchAll 返回结构与解构输出；命名组未匹配时的行为；replace 中的 $<name>。

**答**：
```javascript
const re = /(?<protocol>https?):\/\/(?<host>[\w.]+)(?::(?<port>\d+))?/g;
const text = 'a http://a.com x https://b.com:8080 y';

for (const { groups, groups: { protocol, host, port } } of text.matchAll(re)) {
  console.log(protocol, host, port ?? 'default');
}
// http a.com default
// https b.com 8080

console.log([...text.matchAll(re)].map(m => m.groups));
// [{protocol:'http',host:'a.com',port:undefined},{protocol:'https',host:'b.com',port:'8080'}]

// 未参与的命名组：undefined（不是 ''）
'no-url'.match(re)?.groups; // null（整体不匹配）

// replace 的 $<name> 与匿名 $1 混用
'2026-11-19'.replace(/(?<y>\d{4})-(\d{2})/, '$<y>年$2月'); // '2026年11月-19'
```

**评分点**：
- matchAll 返回迭代器（展开为数组），每项是 exec 式完整对象
- 可选命名组未匹配为 undefined（不是空串）——细节判分
- 解构嵌套（groups 再解构）的写法
- $<name> 与 $1 混用合法性
