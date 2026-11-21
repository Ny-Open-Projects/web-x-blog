---
title: [NODE-171] 设计一个图片服务（上传/处理/防盗链）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-171：设计一个图片服务（上传/处理/防盗链）？
**答**：
- 链路：签名直传（NODE-126，文件不过业务服务器）→ 上传回调触发处理流水线（队列异步）→ 多尺寸 + webp 生成 → CDN 分发。
- 处理用 sharp（NODE-080 有专题）：缩略图按预定义尺寸生成；长尾尺寸用"CDN 缓存按需变换"（x-oss-process 风格）。
- 防盗链三层：**URL 签名**（HMAC + 过期时间 + 处理参数进签名防篡改）、Referer 白名单、限额防刷。
- 安全：MIME/魔数校验、大小限制、路径含 uid 防越权覆盖、EXIF 隐私剥离。

```javascript
app.post('/api/images/sign', auth, async (ctx) => {
  const { name, size, mime } = ctx.request.body;
  if (!ALLOW_MIME.has(mime) || size > 10 * 1024 * 1024) ctx.throw(400); // 白名单
  const key = `img/${ctx.state.uid}/${randomUUID()}${path.extname(name)}`; // 防越权覆盖
  ctx.body = {
    uploadUrl: oss.signatureUrl(key, { method: 'PUT', expires: 600 }),
    cdnUrl: `${IMG_CDN}/${key}`,
  };
});

// 防盗链：签名 URL（处理参数进签名）
function signedImgUrl(key, { w, h, ttlSec = 3600 } = {}) {
  const expires = Math.floor(Date.now() / 1000) + ttlSec;
  const sig = crypto.createHmac('sha1', CDN_SECRET)
    .update(`${key}-${w ?? 0}-${h ?? 0}-${expires}`).digest('base64url');
  return `${IMG_CDN}/${key}?w=${w ?? ''}&h=${h ?? ''}&e=${expires}&s=${sig}`;
}

// 处理流水线：上传回调 → 队列 → sharp 多尺寸
processQueue.add('resize', { key }, { attempts: 3 });
// worker：sharp(src).resize(w).webp({ quality: 80 }) → 逐尺寸上传 → 元数据入库
```
