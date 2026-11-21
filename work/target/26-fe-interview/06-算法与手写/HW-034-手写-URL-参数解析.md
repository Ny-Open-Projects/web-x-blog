---
title: [HW-034] 手写 URL 参数解析
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-034：手写 URL 参数解析

**答**：
- 评分点：先定位 `?` 与 `#` 之间的 query 部分（hash 必须剔除）；`split('&')` 后每项 `split('=')`，**值可能含 `=`**（如 base64），要用第一个 `=` 分割而不是固定下标 1；`decodeURIComponent` 解码（注意 `+` 是空格的旧约定，`decodeURIComponent` 不处理 `+`，要手动 replace）；同名 key 合并成数组是加分实现；对照 `new URL(url).searchParams` / `URLSearchParams` 的原生能力。

```javascript
// ===== 5 分钟速写版 =====
function parseQuery(url) {
  const qs = url.split('?')[1]?.split('#')[0] || '';
  const result = {};
  qs.split('&').filter(Boolean).forEach(pair => {
    const idx = pair.indexOf('=');               // 第一个 = 是分隔符，值里可能有 =
    const key = decodeURIComponent(pair.slice(0, idx));
    const value = idx === -1 ? '' : decodeURIComponent(pair.slice(idx + 1));
    result[key] = value;
  });
  return result;
}
// parseQuery('https://a.com/list?tag=fe&page=2&q=a%3Db') → { tag: 'fe', page: '2', q: 'a=b' }

// ===== 标准完整版（含边界处理）=====
function parseQueryPro(url) {
  if (typeof url !== 'string') throw new TypeError('url must be a string');
  const queryStart = url.indexOf('?');
  if (queryStart === -1) return {};
  let qs = url.slice(queryStart + 1);
  const hashIdx = qs.indexOf('#');
  if (hashIdx !== -1) qs = qs.slice(0, hashIdx);   // 剔除 hash
  const decode = s => decodeURIComponent(s.replace(/\+/g, ' ')); // 旧约定：+ 代表空格
  const result = {};
  for (const pair of qs.split('&')) {
    if (!pair) continue;                            // 空项容错 a=1&&b=2
    const idx = pair.indexOf('=');
    const key = decode(idx === -1 ? pair : pair.slice(0, idx));
    const value = idx === -1 ? '' : decode(pair.slice(idx + 1));
    if (key in result) {
      result[key] = [].concat(result[key], value);  // 同名 key → 数组
    } else {
      result[key] = value;
    }
  }
  return result;
}
// 对应的序列化（反向，常连着考）：
function stringifyQuery(params) {
  return Object.entries(params)
    .flatMap(([k, v]) => Array.isArray(v)
      ? v.map(item => `${encodeURIComponent(k)}=${encodeURIComponent(item)}`)
      : [`${encodeURIComponent(k)}=${encodeURIComponent(v)}`])
    .join('&');
}
```

---
