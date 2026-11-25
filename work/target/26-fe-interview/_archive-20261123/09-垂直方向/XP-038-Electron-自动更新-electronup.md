---
title: [XP-038] Electron 自动更新（electron-updater）全流程怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-038：Electron 自动更新（electron-updater）全流程怎么设计？
**答**：
- 流程：启动后台 `checkForUpdates` → 比对版本 → `downloadUpdate`（断点续传、差分更新 delta）→ 校验签名 → `quitAndInstall`（通常等用户确认或下次启动静默装）。
- 发布通道：`latest.yml/mac.yml` 元数据 + 分通道（latest/beta/alpha），按用户设置 `setFeedURL` 切换。
- 平台差异：Windows 走 NSIS/squirrel + 代码签名校验；macOS `Squirrel.Mac` + zip，需公证（notarize）否则 Gatekeeper 拦截；Linux AppImage/deb 自管理。
- 工程细节：更新期间业务可用（下载在后台）；失败重试与退避；强制更新场景在渲染层阻断；灰度按 latest.yml 分流或自建更新服务按设备发不同版本。
- 自建服务：electron-updater 支持 generic provider 指向自家 CDN/接口，可完全掌控灰度与埋点。

```yaml
# electron-builder.yml —— 自动更新配套
appId: com.example.app
publish:
  provider: generic          # 自建更新源（也可 github/s3）
  url: https://update.example.com/desktop
  channel: latest
nsis:
  differentialPackage: true  # Windows 差分更新
mac:
  hardenedRuntime: true      # 公证前置要求
  notarize: true             # 自动公证，未公证的 dmg 用户会拒装
  identity: Developer ID Application: Example Inc
```

```javascript
// main.ts —— 更新编排
import electronUpdater from 'electron-updater';
const { autoUpdater } = electronUpdater;

autoUpdater.autoDownload = false;                       // 手动控制下载节奏
autoUpdater.on('update-downloaded', async ({ version }) => {
  const { response } = await dialog.showMessageBox(win, {
    message: `新版本 ${version} 已就绪，是否立即重启安装？`, buttons: ['稍后', '立即更新'],
  });
  if (response === 1) autoUpdater.quitAndInstall();      // 或记录标记，下次启动静默安装
});
autoUpdater.on('error', (e) => report('updater.error', e)); // 退避重试由业务编排
app.whenReady().then(() => autoUpdater.checkForUpdates());  // 启动后静默检查，不打扰使用
```
