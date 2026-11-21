---
title: [JS-119] URLSearchParams 的用法与手写 query 处理工具
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-119：URLSearchParams 的用法与手写 query 处理工具

**答**：
- URLSearchParams 自动处理编码解码、`+` 号空格、重复键，比 split('&') 手写解析健壮得多。
- get 取第一个值，getAll 取全部，has 判断存在（无值键返回空串）。
- toString 输出时自动编码，可直接拼到 url 后面；空值/undefined 过滤要在构建前做。
- `location.search` 只含 `?` 后部分；hash 路由时要自行解析 hash 中的 query。

```javascript
const qs = new URLSearchParams('a=1&a=2&name=%E5%BC%A0%E4%B8%89&flag');
console.log(qs.get('a'));     // '1'  — 只取第一个
console.log(qs.getAll('a'));  // ['1', '2']
console.log(qs.has('flag'));  // true
console.log(qs.get('flag'));  // ''   — 存在但无值
console.log(qs.get('name'));  // '张三' — 自动解码

// 修改与输出
qs.append('kw', 'a=1');            // 自动编码
console.log(qs.toString());        // a=1&a=2&name=...&flag=&kw=a%3D1

// 从对象构建：过滤空值是常见需求
function buildQuery(obj) {
  return new URLSearchParams(
    Object.entries(obj).filter(([, v]) => v !== undefined && v !== null && v !== '')
  ).toString();
}
console.log(buildQuery({ page: 1, kw: '手机 拍照', tag: null }));
// page=1&kw=手机+拍照（+ 表示空格）

// 解析当前页面（含 hash 路由场景）
function getQuery(search) {
  return Object.fromEntries(new URLSearchParams(search));
}
console.log(getQuery('?id=1&type=vip')); // { id: '1', type: 'vip' } — 全是字符串
```
