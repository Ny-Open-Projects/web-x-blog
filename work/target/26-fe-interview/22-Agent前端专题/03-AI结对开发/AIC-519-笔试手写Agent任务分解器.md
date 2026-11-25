---
title: [AIC-519] 笔试：手写 Agent 任务分解器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-519：笔试：手写 Agent 任务分解

**答**：实现 `decomposeTask(task, { maxSteps })`。task: `{ goal: string, hasTests: boolean, files: string[] }`. 规则：1) **步骤生成**：基于 goal 类型生成步骤序列（refactor → read→plan→modify→test→fix；feature → read→design→code→test；bugfix → reproduce→fix→verify）；2) **测试步骤的条件**：hasTests=true → 包含 run-tests 步骤（Agent 的传感器）；hasTests=false → 包含 write-tests-first 步骤（先写测试再写代码 RBL-518）；3) maxSteps 上限（超出 → 需要人类介入——任务过大）；4) 返回 `Array<{ action, tool, description }>`。边界：goal 空；files 空（无法 read——跳过 read 步骤）；maxSteps=0。

```javascript
function decomposeTask(task = { goal: '', hasTests: false, files: [] },
  { maxSteps = 15 } = {}) {
  if (!task.goal) return [];
  const goal = task.goal.toLowerCase();
  let steps: { action: string; tool: string; description: string }[] = [];
  if (task.hasTests) {
    // 有测试：Agent 有传感器
    if (goal.includes('refactor')) {
      steps = [
        { action: 'read', tool: 'read-files', description: 'Read existing code' },
        { action: 'plan', tool: 'llm', description: 'Design refactoring plan' },
        { action: 'modify', tool: 'write-file', description: 'Apply refactoring' },
        { action: 'test', tool: 'run-tests', description: 'Verify refactoring' },
        { action: 'fix', tool: 'write-file', description: 'Fix test failures if any' },
      ];
    } else if (goal.includes('feature') || goal.includes('add')) {
      steps = [
        { action: 'read', tool: 'read-files', description: 'Understand codebase' },
        { action: 'design', tool: 'llm', description: 'Design implementation' },
        { action: 'code', tool: 'write-file', description: 'Implement feature' },
        { action: 'test', tool: 'run-tests', description: 'Verify feature' },
      ];
    } else {
      steps = [
        { action: 'reproduce', tool: 'run-tests', description: 'Reproduce the bug' },
        { action: 'fix', tool: 'write-file', description: 'Fix the bug' },
        { action: 'verify', tool: 'run-tests', description: 'Verify fix' },
      ];
    }
  } else {
    // 无测试：先写测试（Agent 需要传感器）
    steps = [
      { action: 'read', tool: 'read-files', description: 'Understand codebase' },
      { action: 'write-tests', tool: 'write-file', description: 'Write tests first' },
      { action: 'human-review-tests', tool: 'human', description: 'Human reviews tests' },
      { action: 'implement', tool: 'write-file', description: 'Implement against tests' },
      { action: 'test', tool: 'run-tests', description: 'Verify' },
    ];
  }
  if (steps.length > maxSteps)
    steps = steps.slice(0, maxSteps).concat([
      { action: 'need-help', tool: 'human', description: 'Task too large——human needed' } ]);
  return steps;
}

// 自测
// 有测试的 refactor
let r = decomposeTask({ goal: 'refactor auth module', hasTests: true, files: ['auth.ts'] });
console.log(r.length === 5);
console.log(r.some(s => s.tool === 'run-tests'));
console.log(!r.some(s => s.tool === 'human'));

// 无测试 → 先写测试 + human review
r = decomposeTask({ goal: 'add feature', hasTests: false, files: [] });
console.log(r.some(s => s.tool === 'human'));            // 需要 human 审测试
console.log(r.some(s => s.action === 'write-tests'));

// bugfix
r = decomposeTask({ goal: 'fix pagination bug', hasTests: true, files: [] });
console.log(r.some(s => s.action === 'reproduce'));

// maxSteps
r = decomposeTask({ goal: 'refactor auth', hasTests: true, files: ['a'] }, { maxSteps: 3 });
console.log(r.length === 4);                             // 3 步 + need-help
console.log(r.at(-1).tool === 'human');

// 空 goal
console.log(decomposeTask({ goal: '', hasTests: true, files: [] }).length === 0);
```

**评分点**：
- 三种 goal 类型的步骤序列（refactor/feature/bugfix——不同类型的自主执行策略）
- hasTests 的条件分支（有测试 = Agent 自主 / 无测试 = 先写测试 + human review）；maxSteps 熔断
- 边界（空 goal/maxSteps 上限/空 files）；Agent 的传感器 = 测试的理念
- 能说清「Agent 的可靠性与测试覆盖率直接相关：测试是 Agent 的传感器——无测试 = Agent 盲飞」属于加分
