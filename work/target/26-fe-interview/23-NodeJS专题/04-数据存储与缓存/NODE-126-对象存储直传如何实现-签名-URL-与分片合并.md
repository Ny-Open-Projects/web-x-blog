---
title: [NODE-126] 对象存储直传如何实现（签名 URL 与分片合并）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-126：对象存储直传如何实现（签名 URL 与分片合并）？
**答**：
- 直传价值：文件流不经过业务服务器，省带宽省内存；服务端只负责**发凭证 + 管元数据**。
- 小文件：预签名 PUT URL（限时 + 限操作），前端直传后回调（OSS callback）通知服务端入库。
- 大文件：init 拿 uploadId → 每个分片签独立 PUT URL → 前端并发传分片 → complete 合并；服务端校验分片数/总大小/etag。
- 安全三件事：路径含 uid 防越权覆盖、签名短时效、MIME 与大小白名单校验（配合 NODE-070 分片续传）。

```javascript
// 1. 分片初始化
const { uploadId } = await oss.initMultipartUpload(`video/${fileId}.mp4`);

// 2. 每个分片签发预签名 PUT URL，前端直传
function partUrl(fileKey, uploadId, partNumber) {
  return oss.signatureUrl(fileKey, {
    method: 'PUT',
    expires: 1800,                        // 签名 30 分钟有效
    subResource: { uploadId, partNumber },
  });
}

// 3. 合并前服务端校验
app.post('/api/upload/complete', auth, async (ctx) => {
  const { fileId, uploadId, parts } = ctx.request.body; // parts: [{ number, etag, size }]
  const total = parts.reduce((s, p) => s + p.size, 0);
  if (total > MAX_VIDEO || parts.length > 10000) ctx.throw(400, 'size/parts exceeded');
  // 可选：抽样 HEAD 分片校验 etag，防伪造
  await oss.completeMultipartUpload(`video/${fileId}.mp4`, uploadId, parts);
  await db.file.update({ where: { id: fileId }, data: { status: 'READY', total } });
  ctx.body = { url: `${CDN_HOST}/video/${fileId}.mp4` };
});
```

---

## 十五、安全深入
