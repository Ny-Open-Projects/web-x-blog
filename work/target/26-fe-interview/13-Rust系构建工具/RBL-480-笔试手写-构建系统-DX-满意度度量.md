---
title: [RBL-480] 笔试：手写构建 DX 满意度度量
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-480：手写构建 DX 满意度度量
**答**：实现 `createDxTracker()`：1) 客观指标：dev server 启动时长、HMR 延迟、CI 等待时间、构建失败重试率（一次过的比例——DX 代理指标）；2) 主观指标：周期性问卷（NPS/痛点开放题——客观指标覆盖不到的感受面）；3) 指标与体验关联校验：客观改善后 NPS 是否跟随（不跟随时找被忽略的痛点）；4) 痛点归因：问卷开放题 → LLM 聚类（人工标注校准）→ 痛点榜单；5) 输出季度 DX 报告（趋势 + top 痛点 + 行动项）。

```javascript
export function createDxTracker() {
  const objective = []       // { at, devStartMs, hmrMs, ciWaitMs, firstTryPass }
  const surveys = []         // { at, nps, painPoints: string[] }

  function trackDev(o) { objective.push({ ...o, at: Date.now() }) }
  function addSurvey(s) { surveys.push({ ...s, at: Date.now() }) }

  function correlation() {
    // 客观指标改善后 NPS 是否跟随（按季度对比）
    const quarters = groupByQuarter([...objective])
    const npsByQuarter = groupByQuarter(surveys)
    const mismatches = []
    for (const q of Object.keys(quarters)) {
      const obj = quarters[q], nps = npsByQuarter[q]
      if (!nps) continue
      const objImproved = avg(obj.map((o) => o.devStartMs)) < avg(obj.map((o) => o.devStartMs)) // 简化：趋势
      const npsImproved = nps.length && nps[nps.length - 1].nps > nps[0].nps
      if (objImproved !== npsImproved) mismatches.push({ quarter: q, note: '客观改善但 NPS 未跟随 → 有未覆盖痛点' })
    }
    return mismatches
  }

  function clusterPainPoints(surveyTexts, clusterFn) {
    // LLM 聚类（clusterFn 注入——可测试性）：返回 [{ theme, count, samples }]
    return clusterFn(surveyTexts.map((s) => s.painPoints).flat())
  }

  function quarterlyReport(clusterFn) {
    const last90 = Date.now() - 90 * 86400_000
    const obj = objective.filter((o) => o.at > last90)
    return {
      devStartP50: pctile(obj.map((o) => o.devStartMs), 0.5),
      hmrP50: pctile(obj.map((o) => o.hmrMs), 0.5),
      firstTryPassRate: obj.length ? obj.filter((o) => o.firstTryPass).length / obj.length : null,
      npsTrend: surveys.filter((s) => s.at > last90).map((s) => s.nps),
      mismatches: correlation(),
      topPainPoints: clusterPainPoints(surveys.filter((s) => s.at > last90), clusterFn).slice(0, 5),
    }
  }

  return { trackDev, addSurvey, quarterlyReport, correlation }
}
const avg = (a) => (a.length ? a.reduce((x, y) => x + y, 0) / a.length : 0)
const pctile = (a, p) => { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(s.length * p)] : null }
function groupByQuarter(items) {
  const out = {}
  for (const i of items) { const q = new Date(i.at).getFullYear() * 4 + Math.floor(new Date(i.at).getMonth() / 3); (out[q] ??= []).push(i) }
  return out
}
```
**评分点**：
- 客观+主观双轨（firstTryPass 是 DX 最佳代理指标——「要不要重试」是体验核心）
- 关联校验（客观改善 NPS 不跟随 → 找被忽略痛点——度量的自校验）
- LLM 聚类 + 人工校准（开放题量化——主观指标的可操作化）
- 季度报告闭环（趋势 + 痛点 + 行动项）
