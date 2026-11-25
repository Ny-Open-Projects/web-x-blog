---
title: [ENG-306] 笔试题——实现 browserslist 目标与 RUM 分布校验（兼容性决策）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-306：手写 browserslist 校验

**需求与边界**：
- 需求：对比声明目标（browserslist 解析后的浏览器集合）与 RUM 真实分布——① 目标未覆盖的流量占比（老浏览器被放弃的用户量）；② 覆盖但流量 < 0.1% 的目标（过保护，polyfill 浪费）；③ 输出目标调整建议。
- 边界：① 流量占比精确到浏览器主版本；② 调整建议保守（只动占比 < 0.1% 或 > 1% 的两端）；③ 输出体积影响估算（砍掉某目标省多少 polyfill）。

**答**：
```javascript
function browserslistAudit(targets, rumDistribution, { tail = 0.001, head = 0.01 } = {}) {
  const covered = parseBrowserslist(targets);        // 目标集合（主版本粒度）
  let uncoveredTraffic = 0;
  const waste = [];
  for (const [browser, pct] of rumDistribution) {
    if (!covered.has(browser)) {
      uncoveredTraffic += pct;                       // 被放弃的流量
      if (pct > head) report({ type: 'UNCOVERED_SIGNIFICANT', browser, pct,
        suggest: '评估加入目标或引导升级' });
    } else if (pct < tail) {
      waste.push({ browser, pct, polyfillSaving: estimatePolyfillSaving(browser) });
    }
  }
  return {
    uncoveredTrafficPct: uncoveredTraffic,
    waste,                                            // 过保护目标（polyfill 浪费）
    suggestion: {
      add: rumDistribution.filter(([b, p]) => p > head && !covered.has(b)),
      drop: waste.filter(w => w.polyfillSaving > 20_000),   // 省 >20KB 才建议砍
    },
  };
}
```

**评分点**:
- 双向审计（未覆盖流量 + 过保护浪费）。
- 调整建议保守阈值（<0.1% 砍 / >1% 加，ENG-243 数据驱动）。
- polyfill 节省估算（决策有体积依据）。
- 显著未覆盖流量单独告警（用户体验风险）。
