---
title: [R19-336] 笔试：手写带 ETag/304 的 fetch 缓存封装
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-336：笔试：手写带 ETag/304 的 fetch 缓存封装
**题**：实现 `etagFetch(url)`：首次请求缓存 body 与 ETag；再次请求带 If-None-Match；304 命中返回缓存数据（不发全量）；服务端无 ETag 时退化为普通请求。

```javascript
const etagStore = new Map() // url -> { etag, body }
async function etagFetch(url, init) {
  const cached = etagStore.get(url)
  const res = await fetch(url, {
    ...init,
    headers: { ...init?.headers, ...(cached ? { 'If-None-Match': cached.etag } : {}) }
  })
  if (res.status === 304 && cached) return cached.body // 协商缓存命中
  const body = await res.json()
  const etag = res.headers.get('etag')
  if (etag) etagStore.set(url, { etag, body })
  return body
}
```
**评分点**：
- If-None-Match 条件请求 + 304 处理。
- 无 ETag 降级路径。
- 返回缓存 body 时不重复解析。
- 能扩展说明 WeakETag/强 ETag、Last-Modified 备选。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-103d4a83-02c6-4f8a-8ffa-13dccc5c3d7f-cwd'; fi
exit "$__zcode_status"
