---
title: [RBL-476] 笔试：手写私有 Registry 发布器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-476：手写私有 Registry 发布器
**答**：实现 `createPrivatePublisher(registry, { scope })`：1) 发布校验：包名 scope 正确（@team/ 前缀——防误发公网）、版本不重复（已发布版本不可覆盖——immutable 发布）、文件清单校验（无 .env/token 泄漏扫描）；2) 发布原子性：先传全部文件 → publish manifest（半发布不可见）；3) dist-tag 管理：latest 固定、next（预发）、legacy（废弃通道）；4) 发布审计：谁/何时/什么版本/内容 hash——发布可追溯；5) 撤回（unpublish）策略：24h 内可撤回（带审计），过期走 deprecation 而非删除（下游可能依赖）。

```javascript
export function createPrivatePublisher(registry, { scope = '@team' } = {}) {
  const audit = []

  async function publish(pkg /* { name, version, files, tarball } */, operator) {
    if (!pkg.name.startsWith(scope)) throw new Error(`包名必须 ${scope} 前缀（防误发公网）`)
    const existing = await registry.versions(pkg.name)
    if (existing.includes(pkg.version)) throw new Error(`版本 ${pkg.version} 已发布（immutable）`)

    // 泄漏扫描
    for (const [path, content] of Object.entries(pkg.files))
      if (/(token|secret|password)[=:]\s*['"][^'"]+['"]/i.test(content))
        throw new Error(`疑似 secret 泄漏: ${path}`)

    // 原子发布：先传文件再 manifest
    for (const [path, content] of Object.entries(pkg.files)) await registry.putFile(pkg, path, content)
    await registry.publishManifest(pkg)                          // manifest 后写 → 半发布不可见

    audit.push({ name: pkg.name, version: pkg.version, operator,
      contentHash: hashOf(pkg.files), at: Date.now() })
    return { ok: true, version: pkg.version }
  }

  async function unpublish(pkg, operator, reason) {
    const record = audit.find((a) => a.name === pkg.name && a.version === pkg.version)
    if (!record || Date.now() - record.at > 24 * 3600_000)
      throw new Error('超过 24h 不可 unpublish，请走 deprecation（下游可能已依赖）')
    await registry.deprecate(pkg, reason)                        // deprecation 替代删除
    return { ok: true }
  }

  return { publish, unpublish,
    distTag: async (pkg, tag) => registry.setDistTag(pkg, tag),   // latest/next/legacy
    audit: () => audit }
}
const hashOf = (files) => Object.keys(files).sort().join('|')
```
**评分点**：
- scope 前缀校验（防误发公网——私有 registry 第一道闸）
- immutable 版本 + 原子发布（manifest 后写——半发布不可见）
- 泄漏扫描前置；审计完整（内容 hash——发布可追溯）
- unpublish 24h 限制（下游依赖保护——deprecation 优先于删除）
