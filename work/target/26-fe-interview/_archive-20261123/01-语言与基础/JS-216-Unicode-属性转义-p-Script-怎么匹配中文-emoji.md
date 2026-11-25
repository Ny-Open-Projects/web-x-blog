---
title: [JS-216] Unicode 属性转义 \p{Script}：匹配中文与 emoji
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 正则]
type: 面试题
---

## JS-216：Unicode 属性转义 \p{...}：匹配中文与 emoji

**答**：
- u 标志 + \p{属性=值}：按 Unicode 属性匹配——Script（文字系统）、General_Category、Emoji 等
- 中文：`\p{Script=Han}`；日语假名 `\p{Script=Hiragana}`；emoji：`\p{Extended_Pictographic}`
- 比 [\u4e00-\u9fa5] 强在：覆盖扩展汉字区（生僻字、兼容区），手写区间总有遗漏
- 组合：`\p{Letter}` 匹配所有语言的字母（国际化校验昵称时必备）
- 注意：必须带 u（或 v）标志，否则 \p 被当普通字符

```javascript
const cn = /[\p{Script=Han}]/u;
cn.test('汉字 ok');        // true
const emoji = /\p{Extended_Pictographic}/u;
emoji.test('👍👍');        // true
// 提取中英混排中的纯中文片段
'Hello 你好世界 end'.match(/\p{Script=Han}+/gu); // ['你好世界']
```
