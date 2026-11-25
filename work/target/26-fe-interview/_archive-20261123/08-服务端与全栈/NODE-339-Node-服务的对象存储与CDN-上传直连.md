---
title: [NODE-339] Node 服务的对象存储与 CDN 上传直连架构如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-339：Node 服务的对象存储与 CDN 上传直连
**答**:
- 直传模式：Node 只做"签发与登记"——校验业务参数 → 生成上传凭证（STS 临时凭证或 PostObject 签名，限定 key 前缀/大小/类型/过期）→ 前端直传 OSS → 回调（OSS 回调 Node 登记 + 校验真实大小/类型）→ 返回 CDN 域名 URL。文件字节流不过应用服务器。
- 安全设计：key 规则化（业务前缀 + 哈希文件名，防路径穿越与覆盖）、大小/类型服务端最终校验（魔数）、私有读签名 URL（有效期 + 行为绑定）、回调验签（防伪造回调刷记录）。
- CDN 配合：上传后 URL 走 CDN 域、图片处理参数（x-oss-process 缩略）与缓存策略（immutable 哈希名）、回源防盗链。
- 大文件：分片（Multipart Upload）+ 分片进度登记，失败续传；Node 端记录分片状态供查询。
- 可靠性：回调丢失兜底（定时对账未完成上传）；上传成功但登记失败的幂等键设计。
```javascript
// 签发直传凭证（阿里云 OSS 伪码）
app.post('/api/upload/credential', async (req) => {
  const { biz, size } = req.body;
  const key = `${biz}/${dayjs().format('YYYYMM')}/${crypto.randomUUID()}`;
  return oss.signPost({ key, expire: 60, maxSize: size,
    conditions: [['content-length-range', 1, size], ['starts-with', '$key', `${biz}/`]] });
});
// OSS 回调 → verifySign → 登记 DB → 幂等键 uploadId
```
