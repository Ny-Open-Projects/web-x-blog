---
title: [MP-077] miniprogram-ci 如何自动化上传与预览？（高频）
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-077：miniprogram-ci 如何自动化上传与预览？（高频）
**答**：
- miniprogram-ci 是官方 Node 库/CLI：用**上传密钥**（后台下载，配 IP 白名单）代替开发者工具扫码，实现 CI 自动化。
- 核心能力：`upload`（提版本）、`preview`（生成真机预览二维码，可推送）、`pack-npm`、`analytic` 体验分析。
- 典型流水线：lint → build → packNpm → upload（robot 编号区分机器）→ preview 二维码发群里。

```javascript
// ci/upload.js
const ci = require('miniprogram-ci')
const project = new ci.Project({
  appid: 'wx1234567890',
  type: 'miniProgram',
  projectPath: './dist',
  privateKeyPath: './private.wx.key'   // 后台下载的上传密钥
})
await ci.upload({ project, version: '1.2.0', desc: 'CI 上传', robot: 3 })
await ci.preview({ project, robot: 3, qrcodeFormat: 'image', qrcodeOutputDest: './preview.jpg' })
```
