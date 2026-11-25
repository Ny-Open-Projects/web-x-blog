---
title: [AGT-480] 笔试题——实现平台健康度评分（多维指标加权+趋势+告警）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-480：手写健康度评分：可用性/质量/成本/安全四维加权、趋势检测、分级告警

**需求与边界**：
- 输入：各维度原始指标；输出：健康分+趋势+告警。
- 边界要求：① 四维加权（质量与安全权重高——不是可用性一家独大）；② 各维归一化（不同量纲统一 0~100）；③ 趋势检测（连续下滑告警 vs 单点波动不告警）；④ 一票否决项（安全违规直接红色）。

**答**：
```javascript
function healthScore({ availability, quality, cost, security },
                     { history }) {
  // 1. 归一化（各维 0~100）
  const norm = {
    availability: availability.successRate * 100,
    quality: quality.acceptRate * 100,
    cost: Math.max(0, 100 - (cost.perTask / cost.budget) * 100),
    security: 100 - security.violations * 20,       // 每次违规 -20
  };
  // 2. 加权：安全与质量优先
  const WEIGHTS = { security: 0.3, quality: 0.3,
    availability: 0.25, cost: 0.15 };
  const total = Object.entries(WEIGHTS)
    .reduce((s, [k, w]) => s + norm[k] * w, 0);
  // 3. 一票否决：安全严重违规直接红
  const veto = security.criticalViolations > 0;
  const level = veto ? 'red' :
    total > 80 ? 'green' : total > 60 ? 'yellow' : 'red';
  // 4. 趋势：连续 3 点下滑才告警（防单点波动误报）
  const series = history.slice(-3).map(h => h.total);
  const downtrend = series.length === 3 &&
    series.every((v, i) => i === 0 || v < series[i - 1]);
  return {
    score: Math.round(total), level, veto,
    norm,
    trend: downtrend ? 'declining' : 'stable',
    alerts: [
      ...(veto ? [{ type: 'critical', msg: '安全严重违规，立即处置' }] : []),
      ...(downtrend ? [{ type: 'warning',
        msg: `连续下滑：${series.join('→')}` }] : []),
      ...(norm.cost < 40 ? [{ type: 'warning',
        msg: '成本水位过高' }] : []),
    ],
  };
}
// 呈现：总分+四维雷达图+告警明细；权重可配置但默认安全最高。
```

**评分点**:
- 四维加权且安全/质量权重高于可用性（AI 服务特性认知）。
- 一票否决（安全严重违规直接红）——加权不掩盖硬伤。
- 趋势检测连续 3 点下滑才告警（防单点波动误报）。
- 归一化处理量纲差异；告警明细可执行。
