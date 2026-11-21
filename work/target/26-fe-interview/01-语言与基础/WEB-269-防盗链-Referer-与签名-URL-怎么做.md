---
title: [WEB-269] 防盗链：Referer 与签名 URL 怎么做？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-269：防盗链：Referer 与签名 URL 怎么做？

**答**：
- Referer 白名单：CDN 配置只允许自家域名引用，空 Referer 与黑名单域名拒绝。弱点：Referer 可伪造（仅防小白）、老隐私设置会剥离 Referer。
- 签名 URL（防盗链链）：`https://cdn.xx.com/v.mp3?sign=hash(path+expire+secret)&expire=1699...`，过期即失效，泄露也可控时间窗口；视频/付费资源主流方案。
- 生效方式：前端向业务服务请求带签名的临时 URL（服务端持有 secret 签发），再拿 URL 请求 CDN；CDN 边缘校验签名。
- 进阶：IP 频控、UA 校验、HLS 切片 + 每 segment 独立签名 token（视频防盗核心）。

```javascript
// 前端拿签名 URL 播放付费视频
const { url } = await fetch(`/api/media/${id}/playurl`).then(r => r.json());
// url: https://cdn.xx.com/seg1.ts?sign=abc&expire=1700000000&uid=42
video.src = url;
// 服务端签发: sign = md5(secret + path + expire + uid)
// CDN 边缘: 校验 expire 未过期且 hash 匹配
```
