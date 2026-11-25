---
title: [AIC-052] 用 AI 做大规模重构（如 Options API 迁移 Composition API）怎么保证不改坏？安全流程是什么？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-052：用 AI 做大规模重构（如 Options API 迁移 Composition API）怎么保证不改坏？安全流程是什么？
**答**：
- 前提三件套：重构前测试基线是绿的（没有测试的模块先补关键用例）、重构模式写成规则（映射表：data→ref、computed→computed、mixin→composable）、一次只重构一个文件。
- 流程：选文件 → AI 按映射规则改写 → tsc/lint/单测跑增量 → diff 只允许出现「机械变换」不允许顺手改逻辑 → 人工抽查行为敏感点（生命周期顺序、this 指向）。
- 最重要的红线：**禁止 AI 在重构 PR 里夹带行为修改**。发现逻辑变化要么拆 PR 要么还原——重构 diff 必须可机械化验证。
- 批量推进：单文件验证通过后用脚本批跑，失败文件自动回滚并记录，人只处理失败名单。
- 追问钩子：没有测试覆盖的存量重构，先让 AI 生成「特征测试」（characterization test）锁住当前行为再动手。

```javascript
// 重构批处理骨架（每文件验证，失败回滚）
async function batchRefactor(files, rewrite) {
  const failed = [];
  for (const f of files) {
    const before = testSnapshot();
    git.checkoutBranch(`refactor/${f}`);
    const ok = await rewrite(f)
      .then(() => run(['tsc', '--noEmit']))
      .then(() => run(['vitest', 'run', '--related', f]))
      .catch(() => false);
    if (!ok) { git.abort(); failed.push(f); continue; }
    if (hasLogicDiff(git.diff(f))) { git.abort(); failed.push(`${f}: 含非机械 diff`); continue; }
    git.commit(`refactor: ${f}`);
  }
  return { failed };
}
```
