---
title: [XP-101] Electron 自动更新的灰度通道怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-101：Electron 自动更新的灰度通道怎么设计？
**答**：
- 通道模型：`latest/alpha/beta` 多 channel（electron-builder 按通道产出 `latest-beta.yml` 等），用户设置或内部账号决定 channel；`allowPrerelease`/`setFeedURL` 动态切换。
- **灰度放量**：generic provider 下自建更新服务——按机器 GUID 哈希分桶，只对命中桶的客户端返回新版本 yml，其余返回稳定版；放量比例服务端可调，秒级止血。
- 更新流程纪律：下载在后台完成、重启时机用户可控（提示而非强弹）、` differentialDownload`（blockmap 差量）省带宽；更新包签名校验（macOS 公证 + Windows 签名）必须开启。
- 风控指标：更新成功率、更新后崩溃率对比（crash 上报带版本，超阈值服务端停止放量并回滚 yml 指针）——与 XP-083 热更风控、XP-137 发布体系同一套门禁。
- 本地开发与内测：企业内网 feed、staging channel 隔离，禁止内测包走生产 feed。

```javascript
// main/updater.js —— 通道 + 服务端灰度 + 安全校验
import { autoUpdater } from 'electron-updater';

const CHANNELS = ['latest', 'beta', 'alpha'];

export function initUpdater(opts) {
  const channel = opts.channel ?? 'latest';               // 用户设置/内部身份决定
  autoUpdater.channel = channel;
  autoUpdater.allowDowngrade = false;
  autoUpdater.autoDownload = true;                        // 后台静默下载
  autoUpdater.differentialPackage = true;                 // blockmap 差量下载

  // feed 指向自建更新服务：服务端按机器 GUID 分桶实现灰度
  autoUpdater.setFeedURL({
    provider: 'generic',
    url: `${process.env.UPDATE_BASE}/${channel}`,         // /latest /beta 按通道隔离
  });

  autoUpdater.on('update-downloaded', (info) => {
    // 用户可控时机：提示条"重启以更新"，绝不强弹强更
    mainWindow.webContents.send('update:ready', { version: info.version });
  });
  autoUpdater.on('error', (e) => log.error('updater', e));

  autoUpdater.checkForUpdates();                          // 启动延迟 30s 检查 + 每 4h 轮询
}

// 自建更新服务端（伪代码）：
//   GET /latest/latest.yml?guid=<machine-id>
//   bucket = murmur3(guid) % 100
//   release = bucket < rolloutPercent(current) ? newVersion : stableVersion
//   返回对应 yml；newVersion 崩溃率超阈值 → rolloutPercent 置 0（秒级止血）
// 安全：macOS 公证 + Windows 代码签名，autoUpdater 校验签名失败拒绝安装
```
