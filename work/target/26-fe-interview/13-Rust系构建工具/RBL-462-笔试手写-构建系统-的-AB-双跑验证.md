---
title: [RBL-462] 笔试：手写构建工具 AB 双跑验证
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-462：手写构建工具 AB 双跑验证
**答**：实现 `createShadowBuild(oldTool, newTool)`：1) PR 构建双跑：主路径用旧工具（用户无感），影子跑新工具；2) 产物对比：功能等价性（smoke 断言）+ 产物 diff 摘要（chunk 结构/体积）；3) 影子超时（3x 主路径时长）计为不兼容（防假通过）；4) 结果聚合：连续 N 个 PR 全通过 → canPromote（迁移决策依据）；5) 失败归因：diff 的第一个差异点定位（哪个 chunk/模块）。

```javascript
export function createShadowBuild(oldTool, newTool, { shadowTimeoutFactor = 3, promoteN = 20 } = {}) {
  const results = []
  let consecutiveOk = 0

  async function exec(project) {
    const main = await oldTool.build(project)                     // 主路径
    void (async () => {
      try {
        const shadow = await Promise.race([
          newTool.build(project),
          new Promise((_, rej) =>
            setTimeout(() => rej(new Error('shadow timeout')), main.timeMs * shadowTimeoutFactor)),
        ])
        const diff = compareArtifacts(main, shadow)
        const ok = diff.functional && diff.chunkDelta < 0.2       // 功能等价 + 结构差异可控
        results.push({ sha: project.sha, ok, diff: diff.summary })
        consecutiveOk = ok ? consecutiveOk + 1 : 0
      } catch (e) {
        results.push({ sha: project.sha, ok: false, reason: String(e.message) })
        consecutiveOk = 0
      }
    })()
    return main                                                   // 用户拿到旧工具结果
  }

  function compareArtifacts(a, b) {
    const aChunks = new Set(Object.keys(a.files)), bChunks = new Set(Object.keys(b.files))
    const onlyA = [...aChunks].filter((c) => !bChunks.has(c))
    const onlyB = [...bChunks].filter((c) => !aChunks.has(c))
    const sizeDelta = Object.values(b.files).reduce((s, f) => s + f.size, 0)
      - Object.values(a.files).reduce((s, f) => s + f.size, 0)
    return {
      functional: a.smokeTest.ok && b.smokeTest.ok,               // 冒烟等价
      chunkDelta: (onlyA.length + onlyB.length) / Math.max(aChunks.size, 1),
      summary: `onlyOld=[${onlyA.slice(0, 3)}] onlyNew=[${onlyB.slice(0, 3)}] Δsize=${sizeDelta}`,
    }
  }

  return { exec,
    canPromote: () => consecutiveOk >= promoteN,
    report: () => ({ total: results.length, ok: results.filter((r) => r.ok).length,
      lastFailure: results.findLast?.((r) => !r.ok) }) }
}
```
**评分点**：
- 主路径无感 + 影子异步（迁移零风险验证的标准结构）
- 三重判定（冒烟等价 + chunk 结构差异率 + 超时计失败——超时防假通过）
- consecutiveOk 连续窗口（canPromote 决策——不是通过一次就切）
- diff 摘要带首差异定位（chunk 集合差——归因入口）
