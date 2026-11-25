---
title: [TST-810] 业务迭代速度 vs 测试完备性冲突时，测试架构师如何取舍？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-810：业务迭代速度 vs 测试完备性冲突时，测试架构师如何取舍？
**答**：
- 结论：用「风险分级 + 分层裁剪」替代一刀切——高风险改动不降级，低风险改动只跑核心集，把有限测试预算花在刀刃上。
- 依据变更类型裁剪：文案/样式改动跑视觉快照即可； touching 核心状态机则强制全量单测 + 核心 E2E。
- 用「测试影响分析(TIA)」：根据 git diff 只跑受影响的用例，既快又保持覆盖（呼应智能回归选择）。
- 留安全阀：紧急发布允许绕过非阻塞门禁，但必须 tech-lead 审批且 24h 内补测，避免绕过成为常态。
- 追问钩子：如果「紧急发布」每周都发生，说明门禁设计本身有问题，你如何定位并修正？

```javascript
// 基于变更风险裁减测试范围
function selectTests(changedFiles, riskMap) {
  const touched = changedFiles.map(f => riskMap[f] || 'low');
  if (touched.includes('core')) return ['unit:full', 'e2e:core', 'visual'];
  if (touched.includes('ui')) return ['visual', 'unit:affected'];
  return ['unit:affected']; // 纯低风险改动
}
const riskMap = {
  'src/store/order.ts': 'core',
  'src/components/Button.tsx': 'ui',
  'README.md': 'low',
};
console.log(selectTests(['src/components/Button.tsx'], riskMap)); // [visual, unit:affected]
```
