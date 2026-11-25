---
title: [RBL-451] 笔试：手写 SBOM 生成器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-451：手写 SBOM 生成器
**答**：实现 `generateSBOM(lockfile, pkgJson)`：1) 从 lockfile 解析依赖树（含传递依赖）——去重（同包单条目）；2) 输出 CycloneDX 简化格式：`{ components: [{ name, version, purl, licenses?, scope }] }`——scope 区分 direct/transitive；3) purl 标准格式（pkg:npm/name@version）；4) 与产物关联：bundle 里实际打包的依赖标记（stats 联动——SBOM 标「in-bundle」）；5) 差异对比：两次 SBOM diff（新引入/移除/升级——CVE 响应时定位受影响产物）。

```javascript
export function generateSBOM(lockfile, pkgJson, bundleStats) {
  const components = new Map()                                 // name@version → 条目
  const direct = new Set(Object.keys(pkgJson.dependencies ?? {}))

  function walk(deps, scope) {
    for (const [name, info] of Object.entries(deps ?? {})) {
      const version = info.version ?? info.requires?.version ?? 'unknown'
      const key = `${name}@${version}`
      if (!components.has(key))
        components.set(key, { name, version, purl: `pkg:npm/${name.replace('/', '%2f')}@${version}`,
          scope, licenses: info.license ? [info.license] : undefined })
      if (info.dependencies) walk(info.dependencies, 'transitive')   // 传递依赖递归
    }
  }
  walk(lockfile.packages ? toTree(lockfile) : lockfile.dependencies, 'direct')

  // in-bundle 标记
  const bundled = new Set(bundleStats?.packages ?? [])
  const list = [...components.entries()].map(([key, c]) => ({
    ...c, 'in-bundle': bundled.has(c.name) || bundled.has(key),
  }))

  return { bomFormat: 'CycloneDX', specVersion: '1.4',
    metadata: { tools: [{ vendor: 'build-system', name: 'sbom-gen', version: '1.0' }] },
    components: list.sort((a, b) => a.name.localeCompare(b.name)) }
}

function toTree(lockfile) {
  // pnpm lockfile packages → 扁平树简化
  const out = {}
  for (const [key, info] of Object.entries(lockfile.packages ?? {})) {
    const name = key.replace(/\/.+$/, '')
    out[name] = { version: info.version, dependencies: info.dependencies }
  }
  return out
}

export function diffSBOM(a, b) {
  const da = new Map(a.components.map((c) => [c.purl, c]))
  const db = new Map(b.components.map((c) => [c.purl, c]))
  return {
    added: [...db.keys()].filter((k) => !da.has(k)),
    removed: [...da.keys()].filter((k) => !db.has(k)),
    changedScope: [...da.keys()].filter((k) => db.has(k) && da.get(k).scope !== db.get(k).scope),
  }
}
```
**评分点**：
- purl 标准格式（scoped 包 / 转义）
- scope 区分 direct/transitive；in-bundle 联动（SBOM 要回答「产物里有什么」不只是「依赖树有什么」）
- 递归传递依赖 + 去重（同包单条目）
- diffSBOM 服务 CVE 响应（新引入定位受影响产物——SBOM 的存在意义）
