---
title: [RBL-459] 笔试：手写 Runbook 自动生成器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-459：手写 Runbook 自动生成器
**答**：实现 `generateRunbook(incidentHistory, checks)`：1) 从事故历史提取高频故障模式（错误签名聚类 top5 → 每类生成 Runbook 草稿：症状/诊断命令/处置）；2) 诊断命令自动生成（错误类型对应的 check 脚本调用——checks 注册表）；3) 处置步骤从「历史成功处置」提取（同签名事故的处置动作统计——多数派步骤）；4) 人工审校标记（自动生成内容必须人工确认后生效——置信度分级）；5) 输出 markdown（Runbook 条目）+ 未覆盖故障模式清单（Runbook 空白区提示）。

```javascript
function signature(err) { return `${err.code ?? 'unknown'}#${err.message.slice(0, 50)}` }

export function generateRunbook(incidentHistory, checks) {
  const clusters = new Map()
  for (const inc of incidentHistory) {
    const sig = signature(inc.error)
    if (!clusters.has(sig)) clusters.set(sig, [])
    clusters.get(sig).push(inc)
  }

  const entries = [], uncovered = []
  for (const [sig, incidents] of clusters) {
    if (incidents.length < 3) { uncovered.push({ sig, count: incidents.length }); continue }   // 低频不生成
    const resolutions = incidents.filter((i) => i.resolution)
    const steps = modeOf(resolutions.map((r) => r.resolution.steps))     // 多数派处置步骤
    const check = checks[sig.split('#')[0]]
    entries.push({
      signature: sig, occurrences: incidents.length,
      draft: [
        `## 症状：${sig}（近 ${incidents.length} 次）`,
        `诊断：${check ? `\`./scripts/${check.script}\`` : '人工检查（暂无自动脚本）'}`,
        `处置步骤：`, ...steps.map((s, i) => `${i + 1}. ${s}`),
        `升级：>2 次复发 → 平台值班`,
      ].join('\n'),
      needsReview: true,                                               // 人工审校标记
    })
  }
  return { entries, uncovered,
    md: entries.map((e) => e.draft).join('\n\n') + (uncovered.length
      ? `\n\n> 未覆盖模式：${uncovered.map((u) => u.sig).join(', ')}（样本不足）` : '') }
}

function modeOf(lists) {
  const counts = new Map(lists.map((l) => [JSON.stringify(l), l]))
  return [...counts.entries()].sort((a, b) => b[1] - a[1])[0]?.[1] ?? []
}
```
**评分点**：
- 聚类驱动（错误签名聚类 → 高频模式才生成——数据驱动而非空想）
- 处置步骤多数派提取（历史成功处置统计——不是编造）
- 人工审校门（needsReview 标记——自动生成不直接生效）
- 未覆盖清单（Runbook 空白区可见——知识库完整性视角）
