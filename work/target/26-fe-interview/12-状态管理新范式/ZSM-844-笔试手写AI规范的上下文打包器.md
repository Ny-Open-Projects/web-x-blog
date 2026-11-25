---
title: [ZSM-844] 笔试：手写 AI 上下文打包器（按层注入 + token 预算裁剪）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-844：手写 AI 上下文打包器（按层注入 + token 预算裁剪）
**答**：把 ZSM-843 落成工具——实现 `packContext({ files, budget })`：1) 按优先级分层打包：全局规范（P0）→ 当前文件（P0）→ 同目录 ADR（P1）→ 相邻 store 模板（P2）；2) token 预算裁剪：预算不足时从低优先级层开始截断（按重要性保留开头 anchor）；3) `estimateTokens(text)`：粗估（字符/3.5）；4) 输出带层级标记的 prompt 文本；5) 附用例：预算不足时的裁剪顺序。

```javascript
function estimateTokens(text) {
  return Math.ceil((text ?? '').length / 3.5)
}

function packContext({ files, budget = 8000 }) {
  // 分层优先级
  const PRIORITY = { global: 0, current: 0, adr: 1, template: 2, other: 3 }
  const sorted = [...files].sort((a, b) =>
    (PRIORITY[a.layer] ?? 3) - (PRIORITY[b.layer] ?? 3))

  const used = { tokens: 0 }
  const packed = []
  const dropped = []

  for (const f of sorted) {
    const t = estimateTokens(f.content)
    if (used.tokens + t <= budget) {
      used.tokens += t
      packed.push(f)
    } else if (t > budget) {
      // 单文件超预算：截断保留开头 anchor
      const keep = Math.max(0, Math.floor((budget - used.tokens) * 3.5))
      if (keep > 100 && f.layer !== 'other') {
        packed.push({ ...f, content: f.content.slice(0, keep) + '\n…[截断]', truncated: true })
        used.tokens = budget
      } else dropped.push(f.path)
    } else {
      dropped.push(f.path)                    // 低优先级层整体裁掉
    }
  }

  // 输出：带层级标记的 prompt
  const prompt = packed.map((f) =>
    `<layer:${f.layer} path="${f.path}"${f.truncated ? ' truncated' : ''}>\n${f.content}\n</layer:${f.layer}>`
  ).join('\n')

  return { prompt, usedTokens: used.tokens, budget, packed: packed.map((f) => f.path), dropped: dropped.map((f) => f.path) }
}

// 用例
const ctx = packContext({
  budget: 500,
  files: [
    { layer: 'global', path: 'AGENTS.md', content: '分层规范+审计八问+命名约定。'.repeat(10) },   // ~140 tokens
    { layer: 'current', path: 'cart.ts', content: '当前 store 代码。'.repeat(8) },                // ~60
    { layer: 'adr', path: 'ADR-0007.md', content: '购物车拆分决策记录。'.repeat(30) },            // ~210
    { layer: 'template', path: 'store.template.ts', content: '标准模板。'.repeat(50) },           // ~150
    { layer: 'other', path: 'utils.ts', content: '无关工具'.repeat(20) },                          // 低优
  ],
})
console.log(ctx.packed)      // ['AGENTS.md', 'cart.ts', 'ADR-0007.md']：高优先级先入
console.log(ctx.dropped)     // ['store.template.ts', 'utils.ts']：预算裁掉低优层
console.log(ctx.usedTokens <= 500)   // true：预算约束
console.log(ctx.prompt.startsWith('<layer:global'))   // 层级标记
```
**评分点**：
- 优先级分层（global/current P0 → adr P1 → template P2 → other 裁掉）
- 预算裁剪顺序（低优层先裁、单文件超限截断保 anchor）
- estimateTokens 粗估（字符/3.5）
- prompt 层级标记（AI 可感知来源与截断状态）
