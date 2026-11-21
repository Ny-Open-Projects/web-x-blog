---
title: [SCN-121] App 内 H5 离线包上线后部分用户未命中、仍在走网络，如何排查？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-121：App 内 H5 离线包上线后部分用户未命中、仍在走网络，如何排查？
**答**：
- 命中链路分四环逐一排查：请求拦截是否注册并覆盖该域名 → 包是否下载完成且版本比对通过 → URL 匹配规则是否覆盖（hash 路由、query、大小写差异）→ 完整性校验（manifest md5）是否通过。
- 常见根因：包未下载完用户就进了页面（需要等待或回退网络）、版本号比对逻辑对灰度包不生效。
- 前端埋点上报命中状态与未命中明细（区分原因），让"命中率"变成可观测指标，按 App 版本下钻定位。

```javascript
// 离线包命中上报：区分未命中原因，定位问题环节
window.addEventListener('load', () => {
  const entries = performance.getEntriesByType('resource');
  const checks = entries
    .filter((e) => /\.(js|css)(\?|$)/.test(e.name))
    .map((e) => ({
      url: e.name,
      // App 拦截器返回本地文件时 transferSize 为 0 且有实际内容
      hit: e.transferSize === 0 && e.decodedBodySize > 0,
      size: e.decodedBodySize,
    }));
  const hitRate = checks.filter((c) => c.hit).length / (checks.length || 1);

  report({
    type: 'offline-package',
    hitRate,
    appVersion: window.NativeBridge?.getVersion(),     // 区分 App 版本兼容问题
    packageVersion: window.__OFFLINE_PKG__?.version,   // 离线包管理器注入
    misses: checks.filter((c) => !c.hit).slice(0, 10), // 未命中明细供逐条归因
  });
});
```
