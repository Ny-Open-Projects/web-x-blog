---
title: [RBL-277] 构建期的代码质量门禁（lint 产物）怎么做
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-277：构建期的代码质量门禁怎么做

**答**:
- 三类门禁：产物级（体积预算/重复依赖检测/hash 稳定性快照）、内容级（禁止 eval/new Function、console 残留、debugger、TODO 计数）、结构级（chunk 数量/关键路径深度）
- 时机：构建后 pre-release 门禁（失败阻断），或 PR 级 diff 门禁（增量体积涨超阈值阻断）——门禁越晚误伤越少
- 白名单治理：例外必须显式声明（如某 chunk 预算放宽，带 issue 链接），定期清理过期白名单
- 与分析联动：门禁报告附归因（哪个包涨的）——阻断时开发者能立即定位

```javascript
// 产物内容门禁示例（processAssets）
if (/\bdebugger\b/.test(code)) throw new Error(`debugger 残留: ${name}`)
if (/console\.log\(/.test(code) && !allowConsole) warnings.push(name)
// 体积门禁
if (gzipSize > budget[name]) throw new Error(`${name} 超预算 ${gzipSize} > ${budget[name]}`)
```
