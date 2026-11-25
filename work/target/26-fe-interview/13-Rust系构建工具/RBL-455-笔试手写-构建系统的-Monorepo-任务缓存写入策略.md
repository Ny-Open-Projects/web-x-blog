---
title: [RBL-455] 笔试：手写任务缓存写入策略（flaky 豁免 + 分级）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-455：手写任务缓存写入策略
**答**：实现 `decideCacheWrite(task, result)`：1) 判定要素：任务类型（build 可缓存 / test 条件可缓存 / lint 可缓存）、结果稳定性（test 通过但历史 flaky 率高 → 不写缓存）、确定输出（outputs 与声明一致）；2) 缓存等级：global（共享）/ team / local——按任务类型与分支决定；3) flaky 保护：近 7 天重试率 > 5% 的 test 任务结果禁入共享缓存（只写 local）；4) 大小预算：单条目 > 100MB 不入远程（传输成本 > 收益）；5) 输出 { write: boolean, tier, reason }（决策可解释）。

```javascript
export function decideCacheWrite(task, result, context) {
  // 1. 类型基线
  const typePolicy = { build: { shareable: true }, lint: { shareable: true }, test: { shareable: 'if-stable' } }
  const policy = typePolicy[task.type]
  if (!policy) return { write: false, tier: 'none', reason: `unknown task type ${task.type}` }

  // 2. 输出完整性
  if (!result.outputsMatchDeclaration)
    return { write: false, tier: 'none', reason: 'outputs mismatch declaration' }

  // 3. 大小预算
  const totalSize = result.outputSizes.reduce((a, b) => a + b, 0)
  if (totalSize > 100 * 1024 * 1024)
    return { write: false, tier: 'none', reason: `output ${totalSize} exceeds 100MB budget` }

  // 4. flaky 保护（test 专项）
  if (task.type === 'test') {
    if (context.flakyRate7d > 0.05)
      return { write: true, tier: 'local', reason: `flaky rate ${(context.flakyRate7d * 100).toFixed(1)}% — local only` }
    if (result.retried) return { write: false, tier: 'none', reason: 'passed after retry — uncertain result' }
  }

  // 5. 分支分级
  const tier = context.branch === 'main' && context.isCI ? 'global' : context.isCI ? 'team' : 'local'
  return { write: true, tier, reason: `${task.type} stable, branch ${context.branch}` }
}
```
**评分点**：
- 类型分级策略（test 条件可缓存——非确定性任务的特殊处理）
- flaky 双保险（历史重试率降级 local / 本次重试通过禁写——不确定结果不进共享层）
- 大小预算（超大条目传输成本 > 收益）
- 决策可解释（tier + reason——缓存策略审计的基础）
