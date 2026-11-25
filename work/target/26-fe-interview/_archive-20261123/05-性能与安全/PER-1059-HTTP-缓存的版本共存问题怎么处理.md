---
title: [PER-1059] HTTP 缓存的"版本共存"问题怎么处理
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1059：HTTP 缓存的"版本共存"问题怎么处理

**答**：
- 问题：HTML 与静态资源发布不同步——新 HTML 引用的新资源未就绪，或旧 HTML 引用的旧资源已被清理。
- 铁律：先部署资源后发布 HTML（资源部署先于引用它的 HTML）；旧资源保留期 ≥ HTML 缓存最长寿命。
- CDN purge 顺序：purge HTML 前确保新资源全量就绪；灰度期间新旧资源并存。
- 事故案例：发布脚本先删旧资源再传新资源，窗口期用户拿到 404——改为"只增不删 + 定期清理"。

```javascript
// 发布编排（CI 脚本示意）
async function release(buildDir) {
  await uploadAssets(buildDir);                  // 1. 先传资源（含新 hash）
  await verifyAssets(buildDir);                  // 2. 抽样校验 200 与 hash
  await deployHTML(buildDir);                    // 3. 再发 HTML
  await cdnPurge('/index.html');                 // 4. 清 HTML 缓存
}
async function verifyAssets(dir) {
  for (const f of manifestOf(dir)) {
    const r = await fetch(CDN + f.path, { method: 'HEAD' });
    if (r.status !== 200) throw new Error(`资源未就绪 ${f.path}`);
  }
}
```
