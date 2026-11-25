---
title: [AIC-958] AI 重构一个上千行的商品列表组件，如何确定「最小安全步长」——一次改多少才不会翻车？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-958：AI 重构一个上千行的商品列表组件，如何确定「最小安全步长」——一次改多少才不会翻车？
**答**：
- 步长由「可回滚性 + 可验证性」决定：每一步的改动量应小到「能在一分钟内 review 完、出错能一键回滚、有测试能验证」——结论：步长不是固定行数，而是由验证能力反推。
- 用「绞杀者模式」逐步替换：每次只迁移一个子模块（如先把价格计算抽成纯函数），旧实现暂时保留并做差分校验，确认一致后再删旧代码。
- 每步都是完整闭环：改一点 → 跑测试/差分 → 提交（小 commit）→ 可独立回滚；小 commit 让问题定位精确到某一步。
- 追问钩子：能提出「如果某一步无法写出验证它的测试，说明步长太大或边界不清，应继续拆分」的候选人，把可测试性当作拆分的判据。

```typescript
// 分步重构：每步一个可验证、可独立回滚的改动
const steps = [
  { id:1, change:'抽离价格计算', verify:'差分对比 computePrice 新旧输出', rollback:'revert commit-1' },
  { id:2, change:'抽离库存展示', verify:'快照对比列表渲染', rollback:'revert commit-2' },
  { id:3, change:'删除旧实现',   verify:'全量回归测试', rollback:'恢复旧文件' },
];
function executeStep(step, verifyFn) {
  if (!verifyFn(step)) throw new Error('步骤'+step.id+'验证失败，立即停止并'+step.rollback);
  return `${step.id} 完成，可独立回滚`;
}
console.log(executeStep(steps[0], () => true));
```
