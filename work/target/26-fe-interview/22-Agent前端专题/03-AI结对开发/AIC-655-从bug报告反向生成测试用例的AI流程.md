---
title: [AIC-655] 线上出 bug 后，怎么让 AI 从 bug 报告反向生成测试？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-655：线上出 bug 后，怎么让 AI 从 bug 报告反向生成测试？

**答**：
- 结论先行：**正确的流程是「先复现成 red 测试，再修 bug 让它 green」——AI 负责把 bug 报告翻译成复现用例，但人必须确认这个用例真的复现了 bug**（AIC-419 先红后绿）。
- 流程四步：1) **结构化 bug 报告**：让 AI 从模糊的「列表偶尔空白」提取出「什么操作 + 什么数据 + 期望 vs 实际」；2) **生成最小复现用例**：AI 写一个恰好触发 bug 的测试（用最小数据集），人运行确认它失败（red）——如果测试直接通过，说明没复现，不能继续；3) **修 bug**：让 AI 修，目标是让 red 变 green 且不破坏其他测试；4) **入库 + 提炼不变量**：这个用例作为回归测试永久入库，并让 AI 从它提炼一条不变量（AIC-647）补充到属性测试。
- 关键陷阱：AI 常写出「改了实现让测试通过」而非「修复逻辑」——它可能为了让测试绿而改断言；必须 review diff 确认改的是实现逻辑。
- 为什么先红后绿重要：如果先写实现再写测试，测试会「迁就」实现（实现什么样测试就断言什么），失去发现 bug 的能力；先 red 保证测试独立于实现、真正捕捉了 bug。
- 追问钩子：为什么「最小复现用例」比「完整场景用例」更好？——因为最小用例把 bug 隔离到最少的触发条件，将来代码变动时它更稳定、更易定位；完整场景用例掺杂太多无关步骤，既慢又脆，还可能在 bug 修好后因无关变更而失败。

```typescript
// 先红后绿的验证骨架
type BugReport = { steps: string[]; expected: string; actual: string; data: any };

function regenerateFromBug(
  bug: BugReport,
  runTest: (caseData: any) => boolean, // 返回 true=通过
): { reproduced: boolean; next: string } {
  // AI 生成最小用例（此处用 bug.data 示意）
  const minimalCase = bug.data;
  const passed = runTest(minimalCase);
  if (passed) {
    return { reproduced: false, next: '测试未复现 bug，需补充触发条件' };
  }
  return { reproduced: true, next: 'red 已确认，可以让 AI 修复实现让测试变 green' };
}

const bug: BugReport = {
  steps: ['搜索', '清空结果'], expected: '显示空态', actual: '白屏',
  data: { query: '', items: [] },
};
console.log(regenerateFromBug(bug, () => false).reproduced); // true —— 成功复现
console.log(regenerateFromBug(bug, () => true).next.includes('未复现')); // true
```
