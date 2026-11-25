---
title: [XP-191] Electron 打包与分发：electron-builder 多平台
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-191：Electron 打包与分发：electron-builder 多平台

**答**：
- 题目：Electron 打包——electron-builder 多平台产物（macOS dmg/pkg + 公证、Windows NSIS + 签名、Linux AppImage/deb）、自动更新元数据。
- 思路：electron-builder.yml 配置（各平台 target/签名/公证）；macOS 公证（notarytool，无公证则 Gatekeeper 拦截）；Windows 签名（防 SmartScreen 拦截）。
- 评分点：多平台配置；macOS 公证；Windows 签名。

```javascript
# electron-builder.yml
appId: com.example.app
mac:
  target: [dmg, zip]                                             # zip 供自动更新
  category: public.app-category.productivity
  identity: Developer ID Application: XXX                        # 签名
  notarize: true                                                  # 公证（Gatekeeper）
win:
  target: nsis
  certificateSubjectName: XXX                                     # 代码签名（防 SmartScreen）
linux:
  target: [AppImage, deb]
# CI 流程：build → sign → notarize → 上传更新服务器 → 发布 latest.yml（自动更新元数据）
```
