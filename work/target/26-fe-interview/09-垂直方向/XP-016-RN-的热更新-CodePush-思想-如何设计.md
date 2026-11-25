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

## 追问（补充）

**追问**：

1. 新 bundle 一启动就白屏，用户已经装上了怎么救 → setJSBundle 必须包在 try/catch 里，连续 2 次启动失败自动切回上一槽位，并把该 bundle 版本号拉黑不再下发，回滚不需要用户手动清数据。
2. 差分包下载中断或校验失败，会不会把 current 写坏 → 只往 staging 目录写，hash 与签名都通过才原子 rename 切指针，任何一步失败直接删 staging 保留 current。
3. 灰度 5% 用户更新后崩溃率翻倍，多久能止血 → 崩溃上报按 bundle 版本聚合，5 分钟内超过基线 1.5 倍即自动停发并加入黑名单，客户端下次启动回滚。
