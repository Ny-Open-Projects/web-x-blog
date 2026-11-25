---
title: [XP-039] Electron 打包与签名（electron-builder / macOS 公证 / Windows 签名）怎么做？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-039：Electron 打包与签名（electron-builder / macOS 公证 / Windows 签名）怎么做？
**答**：
- electron-builder 统一产出：Windows NSIS 安装包、macOS dmg/zip、Linux AppImage/deb，自动处理 asar、依赖裁剪、双架构（x64/arm64）。
- macOS 链路：Developer ID 代码签名 → **notarize 公证**（hardenedRuntime 必开）→ staple；缺公证时用户打开报"已损坏/无法验证"。
- Windows 链路：EV/OV 证书签名（EV 可直接过 SmartScreen 信誉）；`signAndEditExecutable` 在打包时签名，避免被篡改后再签。
- asar 与安全：asar 防用户手改代码但不是加密，敏感逻辑本就不该进客户端；native 模块按平台 rebuild（electron-rebuild）。
- CI 要点：证书走密钥管理（不落仓库）、arm64 与 x64 矩阵构建、产物含 latest.yml 供更新器消费。

```yaml
# electron-builder.yml —— 多平台打包矩阵（CI 消费）
appId: com.example.app
productName: ExampleApp
directories: { output: dist }
files: [ 'dist/**', 'package.json' ]
asar: true
mac:
  target: [ { target: dmg, arch: [x64, arm64] }, { target: zip, arch: [x64, arm64] } ] # zip 供 Squirrel 更新
  category: public.app-category.productivity
  hardenedRuntime: true
  entitlements: build/entitlements.mac.plist
  notarize: true
  identity: Developer ID Application: Example Inc (TEAMID)
win:
  target: [ { target: nsis, arch: [x64, arm64] } ]
  signingHashAlgorithms: [ sha256 ]
  certificateSubjectName: Example Inc        # CI 中用 EV 证书签名
linux:
  target: [ AppImage, deb ]
  category: Utility
# CI（GitHub Actions）矩阵：macos-latest 签名公证出 dmg/zip；windows-latest 出 NSIS；
# 产物 dist/latest.yml 上传 update.example.com 供 electron-updater 消费
```
