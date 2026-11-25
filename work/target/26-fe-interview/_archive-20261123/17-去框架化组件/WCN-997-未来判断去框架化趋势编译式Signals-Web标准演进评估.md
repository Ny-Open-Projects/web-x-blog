---
title: [WCN-997] 未来判断：去框架化是不是趋势——编译式 / Signals / Web 标准演进怎么评估
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-997：未来判断：去框架化是不是趋势——编译式 / Signals / Web 标准演进怎么评估

**答**：
- 结论先行：趋势明确但渐进——「编译期做更多、运行时做更少、标准接管更多」是主旋律，但框架不会消失，而是演变为「编译目标 + 薄运行时」。
- 三个信号：① 编译式框架（Solid/Vue Vapor/Svelte runes/Qwik）证明可去掉 VDOM；② TC39 Signals 提案推进让细粒度响应有标准；③ Web 标准补齐（DSD/ElementInternals/Custom State）。
- 驱动力：性能敏感场景（移动端/大促）、跨端复用需求、降低运行时成本——这些是真实业务压力，不是纯技术时髦。
- 阻力：标准落地慢、浏览器兼容、生态与工具链惯性、团队学习成本——所以是「渐进化」而非「颠覆式」。
- 追问钩子：面试官问「作为负责人怎么跟进」——答：以「可验证的小步试点」跟进——在低风险模块验证编译式/标准组件收益，用数据决定是否扩大，不追新追风口。

```javascript
// 趋势信号评估
const signals = [
  { item:'编译式框架', maturity:4, impact:5 },
  { item:'TC39 Signals', maturity:2, impact:4 },
  { item:'Web 标准(DSD等)', maturity:3, impact:4 },
];
function score(s){ return s.maturity * s.impact; }
console.log(signals.map(s=>({ item:s.item, score:score(s) }))
  .sort((a,b)=>b.score-a.score));
// 编译式框架得分最高：当前可落地收益最大
```
