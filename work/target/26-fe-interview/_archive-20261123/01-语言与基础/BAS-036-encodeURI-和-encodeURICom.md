---
title: [BAS-036] encodeURI 和 encodeURIComponent 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-036：encodeURI 和 encodeURIComponent 有什么区别？
**答**：
- encodeURI 编码整个 URL，保留结构字符（`:` `/` `?` `#` `&` `=`），只转义中文、空格等。
- encodeURIComponent 编码单个参数值，结构字符也一并转义，拼接 query 参数必须用它。
- 对应解码是 decodeURI / decodeURIComponent；表单编码里 `+` 代表空格，服务端要做转换。

```javascript
encodeURI('https://a.com/搜索?q=前端');   // 保留 :// ? = 等 URL 结构字符
encodeURIComponent('a=1&b=前端');         // 参数值里的 = 和 & 也被转义
const url = 'https://a.com/search?q=' + encodeURIComponent('前端 & 面试');
```
