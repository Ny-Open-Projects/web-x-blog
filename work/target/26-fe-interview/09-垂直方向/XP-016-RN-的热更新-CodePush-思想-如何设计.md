---
title: [XP-016] RN 的热更新（CodePush 思想）如何设计与实现？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-016：RN 的热更新（CodePush 思想）如何设计与实现？
**答**：
- 原理：RN 业务逻辑在 JS bundle 中，**替换 bundle 即更新逻辑**，原生壳与原生模块仍需发版；小程序/服务端渲染是另外两条热更新路线（对比见 XP-074）。
- 流程：启动 check 更新 → 下载差分/全量 bundle → 校验签名与哈希 → 写入 staging 目录 → 下次启动 `setJSBundle` 生效（或立即 reload）。
- 关键机制：**双 bundle 槽位**（current/staging）保证失败可回滚；**灰度发布**按设备分桶；**版本映射** bundle 必须与原生版本兼容（native version 匹配）。
- 安全：bundle 走 HTTPS + 签名校验，防中间人篡改；商店合规（Apple 需符合 3.3.2 条款，禁改原生行为）。
- 自建要点：差分算法（bsdiff/自研 chunk diff）+ CDN 分发 + 埋点全链路（下发/下载/应用/崩溃率回滚熔断）。

```javascript
// 自建热更新核心流程（CodePush 同构思想）
const manifest = await fetch('/ota/manifest?platform=ios&nv=3.2.0&cv=' + currentVer).then(r => r.json());
// manifest: { version, url, hash, size, nativeMin, nativeMax, rollout: 30 }

function shouldUpdate(m, deviceId) {
  if (!semverSatisfies(m.nativeMin, m.nativeMax, nativeVersion)) return false; // 原生版本兼容校验
  return parseInt(hash(deviceId), 16) % 100 < m.rollout;                        // 灰度分桶
}

async function applyUpdate(m) {
  const file = await downloadDiff(m.url);              // 1. 下载差分包
  await verify(file, m.hash, PUBLIC_KEY);              // 2. 验签 + 哈希校验
  await unzipTo(STAGING_DIR, file);                    // 3. 解压到 staging 槽位
  pendingRollbackGuard(m.version);                     // 4. 埋点 + 启动崩溃率熔断标记
  // 5. 下次启动原生侧：setJSBundle(stagingBundle) 后 reload；
  //    若新 bundle 启动 N 秒内连续崩溃 → 原生回滚 current 槽位并上报
}
```

---

## 三、Flutter 原理（017-025）
