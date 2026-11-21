---
title: [NODE-327] Node 服务的上传链路安全？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-327：Node 服务的上传链路安全？
**答**:
- 校验链：类型白名单（MIME+magic number 双重，扩展名不可信）→ 大小限制 → 病毒扫描（异步）→ 内容审核（图片/视频）→ 通过才转正。
- 存储安全：文件名服务端生成（防路径穿越/覆盖）；独立域名（上传域与页面域分离防 XSS）；MIME 强制（Content-Type 不可用户控）。
- 直传方案：服务端签发临时凭证（STS/预签名 URL）→ 客户端直传 OSS → 回调确认——服务端不中转大文件（NODE-070 分片延伸）。
- 访问控制：私有桶 + 签名 URL 短时效；防盗链 Referer/签名。

```javascript
// magic number 校验 + 预签名直传
import { fileTypeFromBuffer } from 'file-type';
async function validateUpload(buf) {
  const type = await fileTypeFromBuffer(buf);        // 内容真实类型（不信扩展名）
  if (!ALLOWED.has(type?.mime)) throw new BizError('UNSUPPORTED');
  if (buf.length > 20 << 20) throw new BizError('TOO_LARGE');
  return type;
}
// 签发直传凭证
app.post('/upload/sign', async (ctx) => {
  const key = `uploads/${ctx.state.user.id}/${nanoid()}`;    // 服务端命名
  return oss.signPut(key, { expiresIn: 600, contentType: 'image/*', conditions: [['content-length-range', 1, 20 << 20]] });
});
// 客户端直传后 POST /upload/confirm { key } → 校验 + 落库（回调/轮询双确认）
```
