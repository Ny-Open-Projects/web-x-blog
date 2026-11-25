---
title: [RBL-439] 笔试：手写构建存储配额管理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-439：手写构建存储配额管理
**答**：实现 `createQuotaManager(root, { limitBytes })`：1) `usage()`：目录树大小统计（du 语义——递归 stat 聚合，缓存目录大小）；2) 写入前配额检查：预计写入超限 → 触发 LRU 清理（RBL-431）后再检查；仍超 → 拒绝写入（返回 quota 错误，调用方降级不缓存）；3) 软硬限：软限 80% 告警 + 预清理、硬限 100% 拒绝；4) 按域配额（各任务缓存独立配额防单任务吃光）；5) `report()` { usage, limit, perDomain, topConsumers }。

```javascript
import fs from 'node:fs'
import path from 'node:path'

export function createQuotaManager(root, { limitBytes, domains = {} } = {}) {
  function du(dir, depth = 0) {
    let total = 0
    const perFile = []
    for (const name of fs.readdirSync(dir)) {
      const full = path.join(dir, name)
      const st = fs.statSync(full)
      if (st.isDirectory()) total += du(full, depth + 1).total
      else { total += st.size; perFile.push({ path: full, size: st.size }) }
    }
    return { total, perFile }
  }

  function usage() {
    const { total, perFile } = du(root)
    const perDomain = {}
    for (const [domain, sub] of Object.entries(domains)) {
      try { perDomain[domain] = du(path.join(root, sub)).total } catch { perDomain[domain] = 0 }
    }
    return { total, perDomain, topConsumers: perFile.sort((a, b) => b.size - a.size).slice(0, 10) }
  }

  async function canWrite(bytes) {
    let { total } = usage()
    if (total + bytes <= limitBytes) return { ok: true, level: total / limitBytes > 0.8 ? 'soft' : 'ok' }
    // 软限触发清理（调用方接入 evictCache）
    return { ok: false, needFree: total + bytes - limitBytes, level: 'hard' }
  }

  return { usage, canWrite, report: () => ({ ...usage(), limit: limitBytes,
    pct: +(usage().total / limitBytes * 100).toFixed(1) }) }
}
```
**评分点**：
- du 语义实现（递归聚合）；topConsumers 定位大文件
- 软硬限分级（80% 预清理 / 100% 拒绝——避免突然写入失败）
- 按域配额（防单任务吃光共享配额）
- 拒绝时的降级语义（调用方退化为不缓存而非失败——配额是旁路保护）
