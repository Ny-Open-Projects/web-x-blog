---
title: [NODE-666] 文件上传服务端（分片/校验/存储直传）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-666：文件上传服务端怎么做？
**答**：
- 直传优先：大文件不走 Node 中转（对象存储直传——Node 只发签名 URL，SCN-FIN-494 签名直链）——Node 内存与带宽的最好保护。
- 分片协议：分片上传（每片签名 PUT + 完成合并校验——分片 hash 校验防错序/漏片）、断点续传（已传分片查询——客户端续传）。
- 服务端接收（小文件）：流式接收（req.pipe——不 whole-body 缓存内存，SCN-NODE-636 背压）、大小限制（content-length 预检 + 流中途超限断开）、类型校验（magic bytes 而非扩展名——伪造扩展防御）。
- 安全：签名 URL 短时效 + 绑定用户/大小/类型（签名即授权）、病毒扫描异步（上传后扫描——隔离区语义）。
- 追问钩子：为什么「magic bytes 校验」优于「扩展名/Content-Type 校验」——扩展名与 Content-Type 都是客户端声明（可伪造）；magic bytes 是文件内容特征（PNG 的 8 字节头），伪造成本高——上传安全的第一原则是「不信任客户端声明的任何元数据」。

```javascript
app.post('/upload/sign', auth(), async (req, res) => {
  const url = await oss.signPutObject({ key: `u/${req.user.id}/${uuid()}`,
    maxBytes: 10e6, contentType: req.body.type, expires: 300 });   // 签名绑定约束
  res.json({ url });
});
// 小文件流式接收
app.post('/upload', (req) => {
  if (+req.headers['content-length'] > 5e6) return req.destroy();   // 预检
  req.pipe(writeStream);                               // 流式（不进内存）
});
```
