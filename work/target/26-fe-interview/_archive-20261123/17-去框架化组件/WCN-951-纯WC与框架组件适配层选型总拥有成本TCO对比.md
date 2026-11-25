---
title: [WCN-951] 设计系统选「纯 WC」还是「框架组件 + 多框架适配层」：总拥有成本怎么算
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-951：设计系统选「纯 WC」还是「框架组件 + 多框架适配层」：总拥有成本怎么算

**答**：
- 结论先行：选型本质是 TCO 对比——纯 WC 一次实现多端复用但生态/调试/TS 体验弱；框架组件 + 适配层开发体验好但要维护 N 套适配与版本对齐。
- 成本项拆解：初始实现、每新增一个框架的适配成本、长期维护（bug 修 N 遍 vs 修 1 遍）、招聘培训、调试工具链投入。
- 临界点：当框架数 ≥3 且组件稳定后，纯 WC 的「修一次」收益通常超过适配层维护；框架数 ≤2 且组件高频迭代时，适配层反而更快。
- 折中方案：核心原子层用 WC 保证稳定复用，业务复合层用各框架原生实现并复用 WC 原子——分层选型而非一刀切（设计系统中台常见）。
- 追问钩子：面试官问「适配层会不会漏功能」——答：会，适配层是「最小公分母」，WC 独有的高级特性（slot/ElementInternals）很难穿透，要在协议层约束只暴露可跨端的能力。

```javascript
// TCO 简化模型：比较纯 WC 与框架组件+适配层
function tco({ frameworks, components, changeRate }) {
  const wc = 1 * components + changeRate * components * 1;      // 修一次
  const adapter = components + frameworks * components * 0.4   // N 套适配
                + changeRate * components * frameworks * 0.4;  // 每套都要改
  return { pureWC: Math.round(wc), withAdapters: Math.round(adapter),
    recommend: wc < adapter ? '纯 WC' : '框架组件+适配层' };
}
console.log(tco({ frameworks: 3, components: 50, changeRate: 0.2 }));
// 纯WC 60，适配层 110 → 推荐纯 WC
```
