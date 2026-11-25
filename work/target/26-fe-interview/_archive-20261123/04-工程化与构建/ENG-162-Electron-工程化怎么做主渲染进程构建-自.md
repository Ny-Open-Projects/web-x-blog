---
title: [ENG-162] Electron 工程化怎么做？主渲染进程构建 自动更新与打包签名？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-162：Electron 工程化怎么做？主渲染进程构建 自动更新与打包签名？
**答**：
- 进程分层构建：主进程 cjs 打包，渲染进程就是标准 vite 前端工程，preload 走 cjs + contextBridge 白名单暴露。
- 自动更新：electron-updater 对接自建更新服务，nsis differentialPackage 差量更新省带宽；更新逻辑只在主进程。
- 打包与签名：electron-builder 配多平台 target；macOS 公证与 Windows 证书全部走 CI secrets，未签名会被系统拦截。
- 安全基线：contextIsolation true、nodeIntegration false、preload 最小暴露，不图省事全开。

```yaml
# electron-builder.yml —— 打包 签名与自动更新配置
appId: com.corp.desktop
directories: { output: release }
files: ['dist/**', 'electron/main.js', 'electron/preload.js']
publish:
  provider: generic
  url: https://update.corp.com/desktop     # 自建更新服务 electron-updater 对接
mac:
  category: public.app-category.productivity
  hardenedRuntime: true
  notarize: true                            # 公证 CI 提供 APPLE_ID 相关 secrets
  entitlements: build/entitlements.mac.plist
win:
  certificateSubjectName: Corp Ltd          # 证书走 CI secrets
nsis:
  differentialPackage: true                 # 差量更新
# 主进程侧自动更新
# import { autoUpdater } from 'electron-updater'
# autoUpdater.checkForUpdatesAndNotify()
```
