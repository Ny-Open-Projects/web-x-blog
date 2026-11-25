---
title: [WEB-340] Last-Modified 只有秒级精度，会造成什么问题？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-340：Last-Modified 只有秒级精度，会造成什么问题？
**答**：
- 同一秒内多次修改 → Last-Modified 不变 → 浏览器 304 拿旧内容；大文件部分更新同理误判。
- 解决：ETag 为主（内容哈希），Last-Modified 兜底；HTTP/1.1 规定两者都有时 ETag 优先。
- mtime 不稳的场景（重新部署全量 touch 文件）会让 Last-Modified 全变 → 200 风暴，CDN 回源放大。

```javascript
// 协商优先级
const validate = (reqHeaders, file) => {
  if (reqHeaders['if-none-match']) {
    return reqHeaders['if-none-match'] === file.etag ? 304 : 200; // 先 ETag
  }
  if (reqHeaders['if-modified-since'] === file.lastModified) return 304;
  return 200;
};
console.log('秒级精度问题 → ETag 主校验，Last-Modified 辅助');
```
