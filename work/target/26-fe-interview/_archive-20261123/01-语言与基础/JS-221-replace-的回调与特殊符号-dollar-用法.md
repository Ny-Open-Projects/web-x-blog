---
title: [JS-221] replace 的回调与特殊符号 $1/$&/$` 用法
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 正则]
type: 面试题
---

## JS-221：replace 的回调与特殊符号用法

**答**：
- 特殊符号：`$1` 组引用、`$<name>` 命名组、`$&` 整个匹配、`` $` `` 匹配前的串、`$'` 匹配后的串、`$$` 字面 $
- 回调签名：`(match, p1, p2, ..., offset, string)`——需要逻辑计算替换值时必用；命名组在最后一个参数 groups 里
- 典型场景：模板引擎（{{name}} 替换）、数字转中文、HTML 转义
- 陷阱：替换串中用户输入含 `$&` 会被解释——作为「替换串」传入时必须转义 `$$`

```javascript
// 模板引擎
const tpl = '你好 {{name}}，你有 {{count}} 条消息';
tpl.replace(/\{\{(\w+)\}\}/g, (_, key) => data[key]);

// offset 的用处：给命中处加位置标记
'abab'.replace(/a/g, (m, offset) => `${m}#${offset}`); // a#0ba#2b

// 用户输入进替换串要转义 $
const userText = '$&$&';
'a'.replace('a', userText.replace(/\$/g, '$$$$')); // 输出字面 $&$&
```
