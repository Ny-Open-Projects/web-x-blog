---
title: [TST-861] AI 测试工程化全景：从「生成用例」到「自治测试」的成熟度分级？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-861：AI 测试工程化全景：从「生成用例」到「自治测试」的成熟度分级？
**答**：
- 结论：AI 测试分五级——L1 辅助生成 → L2 评审修复 → L3 自愈定位 → L4 自主探索 → L5 质量自治，越往上人的角色从「执行」转向「监督」。
- L1-L2：AI 生成用例/补全断言、失败自动归因建议，人始终在环审核（呼应 TST-172/341）。
- L3-L4：Self-healing 自动修复失效定位器、AI Agent 自主探索路径发现未知 bug。
- L5：AI 参与测试策略制定、风险预测、发布决策，人只设目标与护栏。
- 追问钩子：级别越高「幻觉」风险越大，你如何为每级设置 corresponding 的护栏与人工介入点？

```javascript
// AI 测试成熟度自评
const MATURITY = {
  1: '辅助生成用例', 2: '评审与修复建议', 3: '自愈定位器',
  4: '自主探索测试', 5: '质量自治与预测',
};
function maturityLevel(capabilities) {
  if (capabilities.predictQuality && capabilities.autoStrategy) return 5;
  if (capabilities.autonomousExplore) return 4;
  if (capabilities.selfHealing) return 3;
  if (capabilities.failureTriage) return 2;
  if (capabilities.generateTests) return 1;
  return 0;
}
console.log(maturityLevel({ generateTests: true, selfHealing: true,
  autonomousExplore: false }), MATURITY[3]); // 3 自愈定位器
```
