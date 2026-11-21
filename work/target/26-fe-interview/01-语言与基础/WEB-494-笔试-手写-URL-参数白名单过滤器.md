---
title: [WEB-494] 笔试：手写 URL 参数白名单过滤器
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-494：笔试：手写 URL 参数白名单过滤器

**题目**：实现 `sanitizeUrlParams(url)`：只保留白名单参数；值做类型校验（id 必须 1-64 位数字、keyword 去除危险字符）；过滤后不改变其余路径，返回干净 URL。

**答**：
```javascript
const WHITE = {
  id: v => /^\d{1,64}$/.test(v),
  page: v => /^\d{1,4}$/.test(v) && +v <= 9999,
  keyword: v => v.length <= 50 && !/[<>"'`]/.test(v),
  sort: v => ['asc', 'desc'].includes(v),
};

function sanitizeUrlParams(url) {
  const u = new URL(url);
  const clean = new URLSearchParams();
  for (const [k, v] of u.searchParams) {
    if (!WHITE[k]) continue;            // 白名单外丢弃
    if (!WHITE[k](v)) continue;         // 校验不过丢弃
    clean.append(k, v);
  }
  u.search = clean.toString();
  return u.toString();
}

sanitizeUrlParams('https://e.com/list?id=123&evil=<script>&page=2');
// 'https://e.com/list?id=123&page=2'
```

**评分点**：
- 白名单模式（而非黑名单过滤），这是安全题的关键判分点
- 每个参数独立类型校验器，字符串按语义约束（枚举/长度/字符集）
- 用 URL 对象解析而非正则切分，处理编码边界
- 不改写路径与 hash，最小侵入
