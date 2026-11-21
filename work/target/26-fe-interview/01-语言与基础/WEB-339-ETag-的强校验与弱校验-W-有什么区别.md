---
title: [WEB-339] ETag 的强校验与弱校验（W/）有什么区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-339：ETag 的强校验与弱校验（W/）有什么区别？
**答**：
- 强 ETag：字节级完全一致才算相同（"33a6..."）；弱 ETag 加 W/ 前缀：语义等价即可（压缩后、空格差异容忍）。
- 静态资源用内容哈希当强 ETag；动态接口（如渲染的 HTML）常用弱校验，容忍服务器渲染差异。
- 坑：负载均衡多机 ETag 算法不一致 → 304 命中率暴跌，需统一哈希算法或关掉机器指纹参与。

```javascript
const etagStrong = buf => '"' + sha1(buf) + '"';
const etagWeak = buf => 'W/"' + sha1(normalize(buf)) + '"';  // 忽略空白/压缩差异
// 请求: If-None-Match: W/"abc123"
function match(reqEtag, cur) {
  return reqEtag.replace(/^W\//, '') === cur.replace(/^W\//, '');
}
console.log('多机部署 ETag 不统一是 304 率低的头号原因');
```
