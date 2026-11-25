---
title: [TST-872] 如何让 AI 参与「测试设计」而非只生成代码（基于风险/需求生成策略）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-872：如何让 AI 参与「测试设计」而非只生成代码（基于风险/需求生成策略）？
**答**：
- 结论：让 AI 做「测试设计」要给它「需求 + 风险画像 + 历史缺陷」而非只给函数签名，让它输出测试策略（测什么、优先级、边界）再落代码。
- 输入：需求文档、变更风险热度图（呼应 TST-807）、历史缺陷分布、架构约束。
- 输出：分层测试计划、关键场景清单、边界表、fixture 方案——人评审策略后再让 AI 生成代码。
- 价值：从源头保证「测对的东西」，避免 AI 只针对易生成的 trivial 用例堆量。
- 追问钩子：AI 生成的「测试策略」看起来很全面但抓不住重点，你如何在 prompt 中注入优先级约束？

```javascript
// AI 测试设计的输入结构：需求 + 风险 + 历史
const designInput = {
  requirement: '支持优惠券叠加下单',
  riskHotspots: [{ area: '金额计算', score: 25 }, { area: 'UI 展示', score: 4 }],
  historicalBugs: ['叠加顺序错误导致多扣款', '负数金额未拦截'],
  constraints: ['金额计算是纯函数', '接口需 mock'],
};
// prompt = `基于风险热点和历史缺陷，输出分层测试计划，高分区优先...`
function prioritizeByRisk(design) {
  return [...design.riskHotspots].sort((a, b) => b.score - a.score)
    .map(h => h.area);
}
console.log(prioritizeByRisk(designInput)); // ['金额计算','UI 展示'] —— 引导 AI 聚焦重点
```
