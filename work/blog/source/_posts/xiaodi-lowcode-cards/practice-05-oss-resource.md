---
title: 阿里云 OSS 资源体系：上传、删除与 CDN 域名
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, OSS, 资源]
---

## 阿里云 OSS 资源体系：上传、删除与 CDN 域名

**动机**：图片/视频大资源托管 OSS，减轻应用服务器存储与带宽压力。

上传链路：multer 拿 file → `uploadToAliOss`：文件名转 UTF-8 防中文乱码 → 拼对象 key（`upload_files/原名-时间戳.扩展名`）→ `put` 上传 → 删本地临时文件 → 正则替换 OSS 默认域名为自有 CNAME 域名。接口 `POST /resources/upload`，`FileInterceptor('file')` + `@UploadedFile()` + `@Body()` type；上传成功后把返回 URL 落库（resources 表：id/url/account_id/type/name）让前端按记录取资源。

删除链路三步：剔除自定义域名 → 保留文件名+后缀（即对象 key）→ `decodeURI` 解码；`res.status===204` 判成功。接口 `DELETE /resources` 用 Query 传记录 id，service 四步 = 查存在→删 OSS→按 id+account_id 删库→返回。注意顺序隐患：查存在未带 account_id、先删 OSS 后删库，存在越权删他人文件的 IDOR 面（修复：查单即带 account_id，未命中按 404 处理）——**OSS 与 DB 同步清理**，删库不删 OSS 就是存储泄漏。

安全红线：AccessKeySecret 只展示一次要保存好；**必须换真实密钥**否则资源传到他人账户（课程实测提醒）；密钥只走环境变量不入镜像。

前端配套：FormData 上传（headers multipart/form-data）、上传成功必须重新拉列表、视频缩略图用 OSS 截第一帧参数。

出处「课程25 · 17-1~17-5、18-1~18-2、27-8」
