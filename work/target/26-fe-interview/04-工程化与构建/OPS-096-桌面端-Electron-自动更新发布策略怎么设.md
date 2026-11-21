---
title: [OPS-096] 桌面端（Electron）自动更新发布策略怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-096：桌面端（Electron）自动更新发布策略怎么设计？
**答**：
- 发布链路：CI 构建 + 打签名（macOS 公证/Windows 代码签名）→ 上传更新服务（GitHub Releases/自建 update server）→ 客户端 electron-updater 分阶段检查更新。
- 分阶段灰度：更新服务按比例/用户组放行 update 响应，先 5% 观察崩溃率（Sentry crash-free）再全量。
- 应急回滚：update server 下发旧版本号（staged rollout 收紧）+ 强制降级开关；已升坏的用户由服务端指回稳定版。
- 版本兼容：更新包必须兼容旧版本本地数据（migration），升级失败要有回退到上一版的自动恢复。

```yaml
# electron-builder.yml：自动更新发布配置
appId: com.example.mall-desktop
productName: MallDesktop
publish:
  provider: generic                 # 自建更新服务（可做分阶段灰度）
  url: https://updates.example.com/desktop/
  channel: stable                   # stable/beta 双通道
mac:
  identity: "Developer ID Application: Example Inc"   # 必须签名
  hardenedRuntime: true
  notarize: true                    # 公证，否则新版会被 Gatekeeper 拦
win:
  certificateSubjectName: "Example Inc"              # 代码签名
  signingHashAlgorithms: ["sha256"]
nsis:
  differentialPackage: true         # 增量更新，降低下载体积
# 发布流程（CI 中）：
#   1. electron-builder --publish always   构建签名并上传 update server
#   2. update server 灰度：staged 5%，观察 Sentry crash-free 率 > 99.5% 放量
#   3. 应急：update server 把 staged 收紧为 0 并对已升级用户下发回滚 manifest
```

```javascript
// main/update.js：electron-updater 接入（主进程）
import { autoUpdater } from 'electron-updater';

autoUpdater.autoDownload = false;          // 下载前询问用户（或静默+重启时机可选）
autoUpdater.allowDowngrade = true;         // 允许服务端下发旧版本实现回滚

autoUpdater.on('update-available', async (info) => {
  const ok = await askUser(`发现新版本 ${info.version}，是否更新？`);
  if (ok) autoUpdater.downloadUpdate();
});
autoUpdater.on('update-downloaded', () => {
  // 安全校验：更新包签名校验失败则拒绝并上报
  autoUpdater.quitAndInstall();
});
autoUpdater.on('error', (e) => reportError('updater_error', String(e)));

export function checkForUpdates() {
  autoUpdater.checkForUpdates().catch((e) =>
    reportError('update_check_fail', String(e)));
}
```
