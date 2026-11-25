---
title: [RBL-483→MFW-283] 错误哨兵接入与 release 版本关联
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-283：错误哨兵与 release 关联

**答**:
- 关键配置：Sentry/release= 构建指纹（sha）+ sourcemap 同版本上传（MFW-478 协议复用）——堆栈自动符号化到原始 TS 行
- server/client 双端接：RSC/Action 错误在服务端 SDK 捕获（带 request 上下文：路由/用户 id 脱敏）；client 错误边界上报（error.js 里 captureException）——双端同 release 才能拼整链
- 噪音治理：已知错误分组规则（hydration 无害差异折叠）+ 采样（高频无害 1%）——值班只看新签名与劣化趋势
- 闭环：issue → 关联 commit（ blaming 栈帧）→ 修复 release 后自动 resolve（监控新版本是否复发）

```javascript
// 构建：Sentry Same -release 指纹
sentryNextConfig({ release: process.env.BUILD_SHA, 6: true })   // sourcemap 随构建上传
// server: onRequestError 钩子（Next 15）自动捕获 RSC/Action 错误
// client: error.tsx 内 useEffect(() => Sentry.captureException(error), [error])
```
