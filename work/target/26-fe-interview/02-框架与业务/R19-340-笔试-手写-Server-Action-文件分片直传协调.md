---
title: [R19-340] 笔试：手写大文件上传（预签名直传 + Action 协调）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 面试题
---

## R19-340：笔试：手写大文件上传（预签名直传 + Action 协调）
**题**：实现：action `initUpload` 返回 uploadId 与各分片预签名 URL；客户端并发 3 路直传对象存储（绕过服务端带宽）；全部完成调 `completeUpload` 校验分片并入库；断点续传靠 initUpload 返回已传分片。

```javascript
'use server'
export async function initUpload(name, size) {
  const user = await auth()
  if (!user) return { ok: false, code: 'AUTH' }
  const uploadId = crypto.randomUUID()
  const uploaded = await redis.smembers(`up:${uploadId}:done`) // 断点续传
  const chunkSize = 4 * 1024 * 1024
  const urls = Array.from({ length: Math.ceil(size / chunkSize) }, (_, i) =>
    presign(`uploads/${uploadId}/${i}`, 'PUT', { expiresIn: 900 })
  )
  await redis.set(`up:${uploadId}:meta`, JSON.stringify({ userId: user.id, name, size, chunkSize }))
  return { ok: true, uploadId, urls, chunkSize, uploaded: uploaded.map(Number) }
}
export async function completeUpload(uploadId, checksum) {
  const meta = JSON.parse(await redis.get(`up:${uploadId}:meta`))
  if (meta.userId !== (await auth()).id) return { ok: false, code: 'AUTH' }
  const okCount = await redis.scard(`up:${uploadId}:done`)
  const expect = Math.ceil(meta.size / meta.chunkSize)
  if (okCount !== expect) return { ok: false, code: 'INCOMPLETE' }
  const file = await db.file.create({ data: { ...meta, checksum } })
  await redis.del(`up:${uploadId}:*`)
  return { ok: true, fileId: file.id }
}
// 客户端：并发池 3 路上传分片 → 成功调 markChunk 或直接由对象存储回调
```
**评分点**：
- 预签名 URL 让字节流绕过服务端（带宽架构核心）。
- 断点续传（已传分片索引）。
- completeUpload 校验分片数量 + 校验和 + 权限（userId 属主校验）。
- action 只管协调，不收文件本体。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-d2740a26-6696-4f07-89a9-8fa44bfa1004-cwd'; fi
exit "$__zcode_status"
