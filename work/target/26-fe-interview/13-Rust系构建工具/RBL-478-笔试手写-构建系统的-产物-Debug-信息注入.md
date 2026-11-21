---
title: [RBL-478] 笔试：手写产物 debug 信息注入（可观测的构建指纹）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-478：手写产物 debug 信息注入
**需求**：实现 `injectDebugInfo(bundle, meta)`：1) 注入运行时可读的构建指纹（版本/sha/构建时间戳/工具版本/envHash）——线上排查「用户跑的哪个版本」；2) 注入方式：全局对象（window.__BUILD__）+ 版本端点（/version.json 静态生成）；3) 稳定性权衡：时间戳破坏缓存 → 分离策略（产物不含时间戳，版本信息独立文件——hash 稳定与可追溯兼得）；4) sourcemap 关联：注入 bundleVersion 与 map 版本配对（监控符号化匹配）；5) 隐私边界：不注入机器名/用户路径。

```javascript
export function injectDebugInfo(bundle, meta) {
  const fingerprint = {
    version: meta.version,
    sha: meta.sha,
    tool: meta.toolVersion,          // 工具版本
    envHash: meta.envHash,
    bundleVersion: meta.bundleHash.slice(0, 8),   // 与 sourcemap 配对
    builtAt: undefined,              // 时间戳不进产物（缓存稳定性）——进独立版本文件
  }
  const runtimeSnippet = `window.__BUILD__=${JSON.stringify(fingerprint)};`

  // 独立版本文件（不参与 contenthash——每次发布更新）
  const versionFile = JSON.stringify({ ...fingerprint, builtAt: meta.builtAt, sourcemapVersion: meta.mapHash })

  // sourcemap 关联：map 文件内嵌 version 字段（监控按 bundleVersion 匹配 map）
  const mapWithVersion = { ...meta.sourcemap, x_bundleVersion: fingerprint.bundleVersion }

  // 隐私边界校验
  const leak = /\/(Users|home)\/[^/]+\//.test(JSON.stringify(fingerprint))
  if (leak) throw new Error('fingerprint 含用户路径（隐私泄露）')

  return { runtimeSnippet, versionFile, mapWithVersion }
}

// 线上排查链：用户报告 → /version.json 读 builtAt+sha → 与 CI 记录对账 → sourcemap 符号化
```
**评分点**：
- 缓存稳定性与可追溯分离（时间戳进独立版本文件不进产物——hash 分层的关键设计）
- sourcemap 版本配对（监控符号化按 bundleVersion 匹配——排查链完整）
- 隐私边界校验（用户路径禁入）
- 排查链路完整（/version.json → CI 对账 → 符号化）
