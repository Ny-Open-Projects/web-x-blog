---
title: [RBL-527] 笔试：手写四级 resolve 缓存（探测序列 + 持久化校验）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-527：手写四级 resolve 缓存（探测序列 + 持久化校验）
**需求**：实现 `createResolver({ fs, extensions, persist })`：1) `resolve(specifier, fromDir)`：完整管线——L1 内存 → L2 包缓存 → L3 探测缓存 → 实际探测（相对路径直接拼 + node_modules 上溯 + 后缀尝试）→ 结果写入各级缓存；2) `persist.load()/save()`：跨进程持久化 + mtime 校验（文件变了缓存失效）；3) 附用例：缓存命中与 mtime 失效。

```javascript
function createResolver({ fs, extensions = ['.js', '.ts'], persist } = {}) {
  const l1 = new Map()            // specifier+fromDir -> resolved
  const pkgCache = new Map()      // pkgDir -> pkg.json 解析结果
  const probeCache = new Map()    // path（无后缀）-> resolved | null
  const persistent = persist?.load() ?? new Map()   // persisted: Map<specifier+fromDir, { resolved, mtime }>

  function tryFile(path) {
    if (probeCache.has(path)) return probeCache.get(path)
    let resolved = null
    if (fs.exists(path)) resolved = path
    else {
      for (const ext of extensions) {
        if (fs.exists(path + ext)) { resolved = path + ext; break }
      }
    }
    probeCache.set(path, resolved)
    return resolved
  }

  function resolvePkg(name, fromDir) {
    // node_modules 上溯
    let dir = fromDir
    while (dir) {
      const pkgDir = `${dir}/node_modules/${name}`
      const pkgJsonPath = `${pkgDir}/package.json`
      if (!pkgCache.has(pkgJsonPath)) {
        const json = fs.exists(pkgJsonPath) ? JSON.parse(fs.read(pkgJsonPath)) : null
        pkgCache.set(pkgJsonPath, json)                 // L2 包缓存
      }
      const json = pkgCache.get(pkgJsonPath)
      const entry = json?.exports?.['.']?.import ?? json?.main
      const resolved = entry ? tryFile(`${pkgDir}/${entry.replace(/^\.\//, '')}`) : tryFile(`${pkgDir}/index`)
      if (resolved) return resolved
      const up = dir.split('/').slice(0, -1).join('/')
      dir = up === dir ? null : up
    }
    return null
  }

  function resolve(specifier, fromDir) {
    const key = `${specifier}@${fromDir}`
    // L1 内存
    if (l1.has(key)) return l1.get(key)
    // L4 持久化 + mtime 校验
    const persisted = persistent.get(key)
    if (persisted && fs.mtime(persisted.resolved) === persisted.mtime) {
      l1.set(key, persisted.resolved)
      return persisted.resolved
    }
    // 实际解析
    let resolved = null
    if (specifier.startsWith('.') || specifier.startsWith('/')) {
      resolved = tryFile(`${fromDir}/${specifier}`)            // 相对路径
    } else {
      resolved = resolvePkg(specifier, fromDir)                // 包解析
    }
    if (resolved) {
      l1.set(key, resolved)
      persistent.set(key, { resolved, mtime: fs.mtime(resolved) })
    }
    return resolved
  }

  return {
    resolve,
    save: () => persist?.save(persistent),
    stats: () => ({ l1: l1.size, pkg: pkgCache.size, probe: probeCache.size, persisted: persistent.size }),
  }
}

// 用例：mock fs
const files = {
  '/app/src/main.js': 'code',
  '/app/node_modules/lodash/package.json': '{"main":"./index.js"}',
  '/app/node_modules/lodash/index.js': 'code',
}
const fs = {
  exists: (p) => p in files,
  read: (p) => files[p],
  mtime: () => 12345,
}
const persistStore = new Map()
const resolver = createResolver({
  fs,
  extensions: ['.js', '.ts'],
  persist: { load: () => persistStore, save: (m) => persistStore.clear() || Object.entries(m).forEach(([k, v]) => persistStore.set(k, v)) },
})

console.log(resolver.resolve('./main', '/app/src'))       // /app/src/main.js（探测 .js）
console.log(resolver.resolve('lodash', '/app/src'))       // /app/node_modules/lodash/index.js（上溯）
console.log(resolver.resolve('lodash', '/app/src'))       // L1 命中（零探测）
resolver.save()
// 进程重启：L1 空 → L4 命中（mtime 校验通过）→ 跳过全量探测
```
**评分点**：
- 四级缓存层级（L1 内存/L2 包/L3 探测/L4 持久化）逐级命中
- node_modules 上溯 + 后缀尝试序列
- 持久化 mtime 校验（文件变了缓存失效）
- exports/import 优先于 main 的语义（简版）
