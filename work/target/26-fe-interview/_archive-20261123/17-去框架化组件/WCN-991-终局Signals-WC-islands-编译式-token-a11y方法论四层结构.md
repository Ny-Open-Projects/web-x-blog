---
title: [WCN-991] 终局追问：Signals / WC / islands / 编译式 / token / a11y 怎么串成一套方法论
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-991：终局追问：Signals / WC / islands / 编译式 / token / a11y 怎么串成一套方法论

**答**：
- 结论先行：这些不是零散技术点，而是一条主线——「把框架做的事下沉到平台/编译/标准，只在该交互的地方付运行时成本」，用一个统一框架回答。
- 四层结构：① 标准层（WC/DSD/ElementInternals/token）解决「跨端复用与语义」；② 编译层（模板编译/IR/source map/token 内联）把工作前移；③ 运行时层（Signals 细粒度/合帧/islands 水合）只在交互处付费；④ 治理层（a11y/性能预算/版本灰度/价值度量）保证长期健康。
- 串联逻辑：编译式产出轻量运行时 + 标准组件，islands 决定哪里水合，Signals 负责水合后的细粒度更新，token 保证跨端一致，a11y 与性能是贯穿各层的非功能红线。
- 回答范式：遇到任何需求先问「能否前移到编译/构建？能否用标准？运行时是否只在必要处？」——这是去框架化的第一性原理。
- 追问钩子：面试官问「什么时候不该去框架化」——答：强交互、重状态、团队小且单一框架的场景，框架原生更高效；去框架化的收益随「跨端数 × 组件稳定性 × 规模」增长。

```javascript
// 方法论：四层结构示意
const layers = {
  standard: ['Web Components', 'DSD', 'ElementInternals', 'Design Tokens'],
  compile:  ['模板编译', 'IR 多目标', 'source map', 'token 内联'],
  runtime:  ['Signals 细粒度', 'rAF 合帧', 'islands 水合'],
  governance:['a11y 门禁', '性能预算', '版本灰度', '价值度量'],
};
function answerPrinciple(need) {
  return ['能否前移到编译/构建？', '能否用 Web 标准？', '运行时是否只在交互处付费？']
    .map(q => `${need}: ${q}`);
}
console.log(Object.keys(layers)); // 四层
console.log(answerPrinciple('新组件需求'));
```
