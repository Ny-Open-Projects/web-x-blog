---
title: [V3-416] 笔试：手写 Nuxt Server API（鉴权 + 缓存 + 错误规范）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-416：笔试：手写 Nuxt Server API（鉴权 + 缓存 + 错误规范）
**题**：在 `server/api/goods/[id].get.ts` 中实现：从 cookie 鉴权（未登录 401）；读取商品数据走 Nitro 缓存（5 分钟，swr）；商品不存在返回 404（createError）；响应带 ETag，If-None-Match 命中返回 304。

```javascript
export default defineCachedEventHandler(async (event) => {
  const token = parseCookies(event).token
  if (!token || !verifyToken(token)) {
    throw createError({ statusCode: 401, statusMessage: 'Unauthorized' })
  }
  const id = getRouterParam(event, 'id')
  const goods = await getGoods(id) // 业务数据源
  if (!goods) throw createError({ statusCode: 404, statusMessage: 'Not Found' })
  const etag = `"${goods.version}"`
  if (getHeader(event, 'if-none-match') === etag) {
    setResponseStatus(event, 304)
    return '' // 304 无体
  }
  setHeader(event, 'ETag', etag)
  return { code: 0, data: goods }
}, { maxAge: 300, swr: true, name: 'goods', getKey: (e) => e.ctx.params.id })
```
**评分点**：
- defineCachedEventHandler + getKey 路由级缓存。
- createError 保持 HTTP 语义（401/404），前端可统一处理。
- ETag/304 流程完整（弱 ETag 版本号即可）。
- 304 返回空体这一细节。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-0c6b0a97-0d2b-416e-a67c-f2d461a96b92-cwd'; fi
exit "$__zcode_status"
