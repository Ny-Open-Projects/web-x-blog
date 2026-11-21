---
title: [RBL-255] monorepo 任务缓存的 Output 校验怎么做
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-255：monorepo 任务缓存的 Output 校验怎么做

**答**:
- 缓存恢复后校验三件事：声明文件齐全（outputs 通配符展开后逐个存在）、内容 hash 与记录一致、关键入口可解析
- outputs 声明漂移：构建实际产出但未声明 → 恢复缺文件——CI 侧「实际输出 vs 声明输出」diff 检测，漂移即告警
- 部分校验策略：全量 hash 校验成本高——抽样校验 + 关键入口必检；校验失败丢弃缓存回退重跑
- 校验成本账：缓存恢复省 60s，校验花 2s 并行 IO——值得

```javascript
async function verifyOutputs(record, dir) {
  const declared = await expandGlobs(record.outputs, dir)
  for (const f of declared) {
    const hash = await hashFile(path.join(dir, f))
    if (!record.hashes[f]) return { ok: false, reason: `undeclared output: ${f}` }   // 漂移检测
    if (record.hashes[f] !== hash) return { ok: false, reason: `hash mismatch: ${f}` }
  }
  return { ok: true }
}
```
