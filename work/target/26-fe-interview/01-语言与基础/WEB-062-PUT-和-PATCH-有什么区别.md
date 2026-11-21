---
title: [WEB-062] PUT 和 PATCH 有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-062：PUT 和 PATCH 有什么区别？
**答**：
- PUT 是整体替换：客户端发送资源的完整表示，服务器用请求体整个覆盖目标资源；请求体不含的字段会被清掉，且必须幂等。
- PATCH 是部分更新：只携带变更的字段或补丁文档，服务器在原资源上应用补丁；重复执行是否幂等取决于补丁语义。
- 实践中多数 REST API 用 JSON 直接表达"部分字段"，严格语义可用 `application/json-patch+json` 或 `application/merge-patch+json`。
- 面试要点：PUT 的 Content-Type 是资源类型，PATCH 的 Content-Type 是"补丁类型"，两者语义层完全不同。

```javascript
// PUT：发送完整资源，未携带的 title 会被覆盖为空
await fetch('https://api.example.com/articles/42', {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ content: '全新正文' }), // title 字段将被置空
});

// PATCH：只发变更部分
await fetch('https://api.example.com/articles/42', {
  method: 'PATCH',
  headers: { 'Content-Type': 'application/merge-patch+json' },
  body: JSON.stringify({ content: '只改正文，其他字段保持不变' }),
});

// 严格 JSON Patch：一组操作指令，天然表达精确变更
await fetch('https://api.example.com/articles/42', {
  method: 'PATCH',
  headers: { 'Content-Type': 'application/json-patch+json' },
  body: JSON.stringify([
    { op: 'replace', path: '/title', value: '新标题' },
    { op: 'add', path: '/tags/-', value: 'http' },
  ]),
});
```
