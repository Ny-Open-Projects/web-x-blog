---
title: [RBL-446] 笔试：手写 Registry 镜像切换器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-446：手写 Registry 镜像切换器
**需求**：实现 `createRegistryFailover(registries)`：1) registries：`[{ name, url, priority }]`；2) 健康探测：定期 ping（/-/ping 端点）→ 不可用标记降级；3) install 时按优先级选 registry：主不可用切镜像；4) 切换事件记录（哪个包在哪个 registry 拿的——溯源）；5) 回主恢复：主恢复后逐步回切（避免全量回切风暴——按比例）；6) 一致性提示：镜像与主可能不同步（新包在镜像缺失）→ 主可用时优先主。

```javascript
export function createRegistryFailover(registries) {
  const health = new Map(registries.map((r) => [r.name, true]))
  const switchLog = []
  let primaryWeight = 1                                       // 回切比例

  async function probe(reg) {
    try {
      const res = await fetch(`${reg.url}/-/ping`, { signal: AbortSignal.timeout(3000) })
      health.set(reg.name, res.ok)
      return res.ok
    } catch { health.set(reg.name, false); return false }
  }

  function pick() {
    const sorted = [...registries].sort((a, b) => a.priority - b.priority)
    const primary = sorted[0]
    // 主健康时按回切权重逐步回主
    if (health.get(primary.name) && Math.random() < primaryWeight) return primary
    return sorted.find((r) => health.get(r.name)) ?? primary   // 最健康的可用源
  }

  async function install(pkg, installFn) {
    const reg = pick()
    try {
      const result = await installFn(reg.url, pkg)
      switchLog.push({ pkg, registry: reg.name, at: Date.now() })
      return result
    } catch (e) {
      health.set(reg.name, false)                              // 失败降级标记
      const fallback = registries.find((r) => r.name !== reg.name && health.get(r.name))
      if (!fallback) throw e
      switchLog.push({ pkg, registry: fallback.name, reason: 'failover' })
      return installFn(fallback.url, pkg)
    }
  }

  return { probe: () => Promise.all(registries.map(probe)), pick, install,
    log: () => switchLog,
    setRecoverWeight: (w) => (primaryWeight = w) }             // 回切比例调参
}
```
**评分点**：
- 优先级选择 + 健康探测（ping 超时标记降级）
- 回切防风暴（权重逐步回主——全量回切打爆主源）
- 溯源日志（每包来源可查——镜像不一致排查依据）
- 一致性提示（镜像可能缺新包——主可用优先主）
