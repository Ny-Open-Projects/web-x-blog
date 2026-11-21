---
title: [NODE-340] Node 服务的文件下载鉴权与防盗链如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-340：文件下载鉴权与防盗链
**答**:
- 鉴权模型：下载走"鉴权 + 短时效签名 URL"两步——Node 校验用户权限（购买/会员/配额）后签发限定对象与过期时间的签名 URL（30s~5min），CDN/OSS 校验签名。鉴权不过应用服务器带宽。
- 防盗链分层：签名 URL（防直连传播）、Referer/UA 白名单（防简单爬虫）、限速限流（按用户/IP 下载频次与带宽配额）、行为风控（批量下载特征识别）。
- 敏感文件：下载审计日志（谁在何时下载了什么，ARC-073）、水印（图片/PDF 叠加用户标识，泄露可追责）、一次性 URL（防转发复用）。
- 大文件体验：Range 分段下载支持（断点续传）、Content-Disposition 命名、下载进度（前端 Range 探测 total）。
- 流式代理场景（必须经 Node 时，如鉴权逻辑复杂）：stream pipe + 背压（NODE-010），禁整文件 buffer 内存。
```javascript
app.get('/api/files/:id/download', async (req, res) => {
  const file = await db.file.findById(req.params.id);
  if (!await canDownload(req.user, file)) return res.status(403).end();
  const url = oss.signGet(file.key, { expires: 60, responseDisposition: `attachment; filename="${file.name}"` });
  audit('download', req.user.id, file.id);                     // 审计
  res.json({ url, expiresIn: 60 });                            // 前端拿签名 URL 直下
});
```
