---
title: [RBL-409] 笔试：手写构建缓存 key 生成器（多源指纹聚合）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-409：手写构建缓存 key 生成器
**答**：实现 `cacheKey(task, inputs)`：1) inputs：`{ files: Map<path, contentHash>, env: {}, config: object, toolVersion, depOutputs: Map<pkg, hash> }`；2) key = sha(稳定序列化所有输入)——对象键排序、数组保序、Map 键排序；3) 分层 key：`{ tier1: toolVersion, tier2: config+env, tier3: files+depOutputs }`——分层支持「工具不变仅文件变」的快速失效定位；4) 相同输入必同 key（跨机器）；5) `explain(keyA, keyB)` 找出两 key 首个不同的层级（缓存 miss 归因）。

```javascript
import crypto from 'node:crypto'
const sha = (s) => crypto.createHash('sha256').update(s).digest('hex')

function stable(v) {
  if (v instanceof Map)
    return '{' + [...v.entries()].sort(([a], [b]) => (a < b ? -1 : 1))
      .map(([k, x]) => `${JSON.stringify(k)}:${stable(x)}`).join(',') + '}'
  if (Array.isArray(v)) return '[' + v.map(stable).join(',') + ']'
  if (v && typeof v === 'object')
    return '{' + Object.keys(v).sort()
      .map((k) => `${JSON.stringify(k)}:${stable(v[k])}`).join(',') + '}'
  return JSON.stringify(v)
}

export function cacheKey(task, inputs) {
  const tiers = {
    tier1: sha(stable({ task, toolVersion: inputs.toolVersion })),
    tier2: sha(stable({ config: inputs.config, env: inputs.env })),
    tier3: sha(stable({ files: inputs.files, depOutputs: inputs.depOutputs })),
  }
  return { full: sha(stable(tiers)), tiers }
}

export function explain(a, b) {
  for (const tier of ['tier1', 'tier2', 'tier3'])
    if (a.tiers[tier] !== b.tiers[tier]) return { divergedAt: tier }
  return { divergedAt: a.full !== b.full ? 'combination' : 'identical' }
}
```
**评分点**：
- 稳定序列化四规则（对象排序/数组保序/Map 排序/原始值 JSON）
- 分层 key 设计（miss 归因到层——explain 依赖分层）
- explain 找首异层（工具变/配置变/文件变的快速定位）
- 跨机器一致性（序列化不含环境相关内容——路径/时间戳禁入）
